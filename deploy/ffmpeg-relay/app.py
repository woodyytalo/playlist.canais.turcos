import os, re, time, shutil, subprocess, threading
from pathlib import Path
from urllib.parse import quote
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse

PLAYLIST = Path(os.getenv("PLAYLIST_PATH", "/data/Tv.m3u"))
HLS_DIR = Path(os.getenv("HLS_DIR", "/data/hls"))
TOKEN = os.getenv("RELAY_TOKEN", "")
MAX_CONCURRENT = max(1, int(os.getenv("MAX_CONCURRENT", "4")))
VIDEO_BITRATE = os.getenv("VIDEO_BITRATE", "8500k")
MAXRATE = os.getenv("VIDEO_MAXRATE", "9000k")
AUDIO_BITRATE = os.getenv("AUDIO_BITRATE", "192k")
app = FastAPI(title="TV Principal - FFmpeg Relay", version="1.0.0")
processes = {}
lock = threading.RLock()

def channels():
    if not PLAYLIST.exists():
        raise RuntimeError(f"Playlist não encontrada: {PLAYLIST}")
    rows, current = [], None
    for raw in PLAYLIST.read_text(encoding="utf-8-sig").splitlines():
        line = raw.strip()
        if line.startswith("#EXTINF:"):
            current = line.rsplit(",", 1)[-1].strip() or "Canal"
        elif line and not line.startswith("#") and current:
            if line.lower().startswith(("http://", "https://")):
                idx = len(rows) + 1
                slug = re.sub(r"[^a-z0-9]+", "-", current.lower()).strip("-")[:48] or "canal"
                rows.append({"id": f"{idx:03d}-{slug}", "name": current, "source": line})
            current = None
    return rows

def require_token(token):
    if not TOKEN or token != TOKEN:
        raise HTTPException(status_code=403, detail="Token inválido ou não configurado")

def get_channel(channel_id):
    for item in channels():
        if item["id"] == channel_id:
            return item
    raise HTTPException(status_code=404, detail="Canal não encontrado na playlist")

def start_channel(item, token):
    channel_id = item["id"]
    outdir = HLS_DIR / channel_id
    playlist = outdir / "index.m3u8"
    with lock:
        old = processes.get(channel_id)
        if old and old.poll() is None and playlist.exists():
            return
        active = sum(1 for p in processes.values() if p.poll() is None)
        if active >= MAX_CONCURRENT:
            raise HTTPException(status_code=429, detail=f"Limite de {MAX_CONCURRENT} transcodificações simultâneas atingido")
        if old:
            processes.pop(channel_id, None)
        shutil.rmtree(outdir, ignore_errors=True)
        outdir.mkdir(parents=True, exist_ok=True)
        segment_url = f"/hls/{quote(token, safe='')}/{channel_id}/"
        cmd = [
            "ffmpeg", "-hide_banner", "-loglevel", "warning", "-nostdin", "-y",
            "-reconnect", "1", "-reconnect_streamed", "1",
            "-reconnect_at_eof", "1", "-reconnect_delay_max", "5",
            "-i", item["source"],
            "-map", "0:v:0?", "-map", "0:a:0?",
            "-c:v", "libx264", "-preset", "veryfast",
            "-b:v", VIDEO_BITRATE, "-maxrate", MAXRATE, "-bufsize", "18000k",
            "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", AUDIO_BITRATE, "-ac", "2",
            "-f", "hls", "-hls_time", "4", "-hls_list_size", "6",
            "-hls_flags", "delete_segments+append_list+independent_segments",
            "-hls_segment_filename", str(outdir / "seg_%06d.ts"),
            "-hls_base_url", segment_url, str(playlist)
        ]
        log = open(outdir / "ffmpeg.log", "ab")
        try:
            processes[channel_id] = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=log)
        except Exception:
            log.close()
            raise

@app.get("/health")
def health():
    return {"status": "ok", "playlist_exists": PLAYLIST.exists(), "max_concurrent_transcodes": MAX_CONCURRENT}

@app.get("/channels")
def list_channels(token: str):
    require_token(token)
    return [{"id": c["id"], "name": c["name"], "url": f"/hls/{quote(token, safe='')}/{c['id']}/index.m3u8"} for c in channels()]

@app.get("/hls/{token}/{channel_id}/{filename}")
def serve_hls(token: str, channel_id: str, filename: str):
    require_token(token)
    if filename != "index.m3u8" and not re.fullmatch(r"seg_\d{6}\.ts", filename):
        raise HTTPException(status_code=404, detail="Arquivo não encontrado")
    item = get_channel(channel_id)
    path = HLS_DIR / item["id"] / filename
    if filename == "index.m3u8" and not path.exists():
        start_channel(item, token)
        deadline = time.time() + 25
        while time.time() < deadline and not path.exists():
            proc = processes.get(channel_id)
            if proc and proc.poll() is not None:
                raise HTTPException(status_code=502, detail="FFmpeg encerrou; verifique a origem do canal")
            time.sleep(0.25)
    if not path.exists():
        raise HTTPException(status_code=404, detail="Segmento ainda não disponível")
    media = "application/vnd.apple.mpegurl" if filename.endswith(".m3u8") else "video/mp2t"
    return FileResponse(path, media_type=media, headers={"Cache-Control": "no-store"})
