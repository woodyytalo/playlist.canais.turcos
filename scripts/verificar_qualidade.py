#!/usr/bin/env python3
"""Measure the actual video resolution of each entry in Tv.m3u8."""
import concurrent.futures
import csv
import datetime as dt
import json
import os
import re
import subprocess
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

PLAYLIST = Path(os.getenv("PLAYLIST", "Tv.m3u8"))
OUT = Path("relatorio-qualidade")
TIMEOUT = int(os.getenv("PROBE_TIMEOUT", "22"))
WORKERS = int(os.getenv("PROBE_WORKERS", "6"))
UA = "Mozilla/5.0 (compatible; IPTVQualityChecker/1.0)"

def parse_playlist(path):
    text = path.read_text(encoding="utf-8-sig", errors="replace")
    rows, pending = [], None
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("#EXTINF"):
            pending = line.split(",", 1)[-1].strip() or "Canal sem nome"
        elif line and not line.startswith("#") and pending is not None:
            rows.append({"name": pending, "url": line})
            pending = None
    return rows

def fetch_text(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=12) as response:
        return response.read(1_500_000).decode("utf-8", errors="replace")

def best_variant(url):
    """If URL is a master HLS playlist, choose its highest declared resolution."""
    try:
        body = fetch_text(url)
        if "#EXT-X-STREAM-INF" not in body:
            return url, None
        variants = []
        lines = body.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("#EXT-X-STREAM-INF:"):
                attrs = line.split(":", 1)[1]
                res = re.search(r"(?:^|,)RESOLUTION=(\d+)x(\d+)", attrs)
                bandwidth = re.search(r"(?:^|,)BANDWIDTH=(\d+)", attrs)
                next_uri = next((x.strip() for x in lines[i+1:] if x.strip() and not x.strip().startswith("#")), None)
                if next_uri:
                    w, h = (int(res.group(1)), int(res.group(2))) if res else (0, 0)
                    variants.append((w*h, int(bandwidth.group(1)) if bandwidth else 0,
                                     urllib.parse.urljoin(url, next_uri), f"{w}x{h}" if w and h else ""))
        if variants:
            variants.sort(reverse=True)
            chosen = variants[0]
            return chosen[2], chosen[3] or None
        return url, None
    except Exception:
        return url, None

def probe(item):
    name, original = item["name"], item["url"]
    target, declared = best_variant(original)
    cmd = [
        "ffprobe", "-v", "error", "-user_agent", UA,
        "-rw_timeout", str(TIMEOUT * 1_000_000),
        "-select_streams", "v:0",
        "-show_entries", "stream=codec_name,width,height",
        "-of", "json", target
    ]
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=TIMEOUT + 5)
        if p.returncode != 0:
            msg = (p.stderr or "ffprobe não conseguiu abrir o stream").strip().splitlines()[-1][:240]
            return result(name, original, "Não verificado", "", "", msg, declared)
        data = json.loads(p.stdout or "{}")
        streams = data.get("streams", [])
        if not streams or not streams[0].get("width") or not streams[0].get("height"):
            return result(name, original, "Sem vídeo detectável", "", "", "Manifesto acessível, mas sem resolução de vídeo", declared)
        s = streams[0]
        w, h = int(s["width"]), int(s["height"])
        if h >= 1080:
            status = "Full HD" if h == 1080 else "Acima de Full HD"
        elif h >= 720:
            status = "HD"
        else:
            status = "SD"
        return result(name, original, status, f"{w}x{h}", s.get("codec_name", ""), "OK", declared)
    except subprocess.TimeoutExpired:
        return result(name, original, "Não verificado", "", "", f"Tempo limite ({TIMEOUT}s)", declared)
    except Exception as exc:
        return result(name, original, "Não verificado", "", "", str(exc)[:240], declared)

def result(name, url, status, resolution, codec, detail, declared):
    host = urllib.parse.urlparse(url).netloc
    return {"canal": name, "classificacao": status, "resolucao": resolution,
            "codec": codec, "host": host, "resultado": detail,
            "resolucao_declarada_no_master": declared or ""}

def main():
    if not PLAYLIST.exists():
        raise SystemExit(f"Playlist não encontrada: {PLAYLIST}")
    entries = parse_playlist(PLAYLIST)
    OUT.mkdir(parents=True, exist_ok=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=WORKERS) as pool:
        # executor.map preserves playlist order, even when channel names repeat.
        ordered = list(pool.map(probe, entries))
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    csv_path = OUT / "TV-principal.csv"
    json_path = OUT / "TV-principal.json"
    md_path = OUT / "TV-principal.md"
    fields = list(ordered[0].keys()) if ordered else ["canal", "classificacao", "resolucao", "codec", "host", "resultado", "resolucao_declarada_no_master"]
    with csv_path.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fields); writer.writeheader(); writer.writerows(ordered)
    json_path.write_text(json.dumps({"verificado_em": stamp, "total": len(ordered), "canais": ordered}, ensure_ascii=False, indent=2), encoding="utf-8")
    counts = {}
    for row in ordered:
        counts[row["classificacao"]] = counts.get(row["classificacao"], 0) + 1
    lines = [f"# Verificação de qualidade — TV principal", "", f"Verificado em: **{stamp}**", "", f"Total de entradas: **{len(ordered)}**", "", "## Resumo", ""]
    for label in ["Acima de Full HD", "Full HD", "HD", "SD", "Sem vídeo detectável", "Não verificado"]:
        lines.append(f"- {label}: **{counts.get(label, 0)}**")
    lines += ["", "> A classificação usa a resolução de vídeo que o FFprobe conseguiu ler no momento da execução. Falhas temporárias, bloqueio geográfico, autenticação, formatos incompatíveis e indisponibilidade podem resultar em 'Não verificado'. Nenhum link da playlist é alterado.", "", "## Resultado por canal", "", "| Canal | Classificação | Resolução | Codec | Resultado |", "|---|---|---:|---|---|"]
    for r in ordered:
        safe = lambda x: str(x).replace("|", "\\|").replace("\n", " ")
        lines.append(f"| {safe(r['canal'])} | {safe(r['classificacao'])} | {safe(r['resolucao'])} | {safe(r['codec'])} | {safe(r['resultado'])} |")
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Verificadas {len(ordered)} entradas. " + ", ".join(f"{k}: {v}" for k,v in sorted(counts.items())))
    print(f"Relatórios: {csv_path}, {json_path}, {md_path}")

if __name__ == "__main__":
    main()
