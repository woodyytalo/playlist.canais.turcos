#!/usr/bin/env python3
"""Auditoria HTTP/HLS de todos os canais com URL em Tv.m3u.

Não reproduz vídeo, não altera a playlist e não grava URLs com query strings
nos relatórios. Testa manifesto e uma pequena amostra do primeiro segmento.
"""
from __future__ import annotations

import json
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin, urlsplit, urlunsplit
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

PLAYLIST = Path("Tv.m3u")
OUT = Path("reports")
TIMEOUT = 12
MAX_MANIFEST = 1_000_000
SEGMENT_SAMPLE = 64 * 1024
UA = "PlaylistStreamAudit/1.0 (+GitHub Actions)"


def safe_url(url: str) -> str:
    p = urlsplit(url)
    return urlunsplit((p.scheme, p.netloc, p.path, "", ""))


def request(url: str, byte_range: bool = False):
    headers = {"User-Agent": UA, "Accept": "*/*"}
    if byte_range:
        headers["Range"] = f"bytes=0-{SEGMENT_SAMPLE - 1}"
    req = Request(url, headers=headers)
    started = time.monotonic()
    try:
        with urlopen(req, timeout=TIMEOUT) as response:
            body = response.read(MAX_MANIFEST if not byte_range else SEGMENT_SAMPLE)
            return {
                "ok": 200 <= response.status < 300,
                "status": response.status,
                "elapsed_ms": round((time.monotonic() - started) * 1000),
                "content_type": response.headers.get("Content-Type", ""),
                "final_url": safe_url(response.geturl()),
                "body": body,
                "error": "",
            }
    except HTTPError as e:
        return {"ok": False, "status": e.code, "elapsed_ms": round((time.monotonic()-started)*1000),
                "content_type": e.headers.get("Content-Type", ""), "final_url": safe_url(e.geturl()),
                "body": b"", "error": f"HTTP {e.code}"}
    except (URLError, TimeoutError, OSError) as e:
        return {"ok": False, "status": None, "elapsed_ms": round((time.monotonic()-started)*1000),
                "content_type": "", "final_url": safe_url(url), "body": b"",
                "error": str(getattr(e, "reason", e))[:240]}


def parse_channels(text: str):
    lines = text.splitlines()
    found = []
    for i, line in enumerate(lines):
        if not line.startswith("#EXTINF"):
            continue
        name = line.rsplit(",", 1)[-1].strip() if "," in line else "Canal sem nome"
        group = re.search(r'group-title="([^"]*)"', line, re.IGNORECASE)
        category = group.group(1) if group else "Sem categoria"
        url = next((x.strip() for x in lines[i + 1:] if x.strip() and not x.startswith("#")), "")
        if url.startswith(("http://", "https://")):
            found.append({"name": name, "category": category, "url": url})
    return found


def audit(channel):
    url = channel["url"]
    result = {
        "channel": channel["name"], "category": channel.get("category", "Sem categoria"), "url": safe_url(url),
        "scheme": urlsplit(url).scheme.lower(), "manifest": "FAIL",
        "http_status": None, "response_ms": None, "content_type": "",
        "resolution": [], "bandwidth_kbps": [], "segment_sample": "NOT_TESTED",
        "segment_status": None, "segment_ms": None, "error": "",
    }
    first = request(url)
    result["http_status"] = first["status"]
    result["response_ms"] = first["elapsed_ms"]
    result["content_type"] = first["content_type"]
    result["error"] = first["error"]
    if not first["ok"]:
        return result

    body = first["body"]
    text = body.decode("utf-8", errors="replace").lstrip("\ufeff").strip()
    if not text.startswith("#EXTM3U"):
        result["manifest"] = "INVALID"
        result["error"] = "Resposta HTTP positiva, mas o conteúdo não começa com #EXTM3U"
        return result

    result["manifest"] = "OK"
    lines = [x.strip() for x in text.splitlines() if x.strip()]
    variants = []
    for idx, line in enumerate(lines):
        if line.startswith("#EXT-X-STREAM-INF:"):
            attrs = line.split(":", 1)[1]
            bw = re.search(r"(?:AVERAGE-BANDWIDTH|BANDWIDTH)=(\d+)", attrs)
            res = re.search(r"RESOLUTION=(\d+x\d+)", attrs)
            next_uri = next((x for x in lines[idx+1:] if not x.startswith("#")), "")
            if next_uri:
                variants.append((int(bw.group(1)) if bw else 0, res.group(1) if res else "", next_uri))
    media_url = url
    if variants:
        variants.sort(key=lambda x: x[0], reverse=True)
        for bw, res, _ in variants:
            if bw: result["bandwidth_kbps"].append(round(bw / 1000))
            if res: result["resolution"].append(res)
        _, _, uri = variants[0]
        media_url = urljoin(first["final_url"], uri)
        media = request(media_url)
        if not media["ok"]:
            result["segment_sample"] = "MASTER_OK_MEDIA_PLAYLIST_FAIL"
            result["error"] = media["error"] or "Falha ao obter playlist de mídia da variante"
            return result
        media_text = media["body"].decode("utf-8", errors="replace")
        if not media_text.lstrip().startswith("#EXTM3U"):
            result["segment_sample"] = "MASTER_OK_MEDIA_PLAYLIST_INVALID"
            return result
        lines = [x.strip() for x in media_text.splitlines() if x.strip()]

    segment_uri = next((x for x in lines if not x.startswith("#") and
                        re.search(r"\.(?:ts|m4s|mp4|aac|mp3)(?:[?#]|$)", x, re.I)), "")
    if not segment_uri:
        result["segment_sample"] = "NO_SEGMENT_URI_FOUND"
        return result

    seg_url = urljoin(media_url, segment_uri)
    seg = request(seg_url, byte_range=True)
    result["segment_status"] = seg["status"]
    result["segment_ms"] = seg["elapsed_ms"]
    result["segment_sample"] = "OK" if seg["ok"] and len(seg["body"]) > 0 else "FAIL"
    if not seg["ok"]:
        result["error"] = (result["error"] + "; " if result["error"] else "") + (seg["error"] or "Falha no segmento")
    return result


def main():
    if not PLAYLIST.exists():
        print("Tv.m3u não encontrada na raiz do repositório.", file=sys.stderr)
        return 2
    channels = parse_channels(PLAYLIST.read_text(encoding="utf-8", errors="replace"))
    if not channels:
        print('Nenhum canal com URL HTTP/HTTPS encontrado.', file=sys.stderr)
        return 2

    OUT.mkdir(exist_ok=True)
    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=12) as pool:
        results = list(pool.map(audit, channels))
    payload = {"checked_at_utc": datetime.now(timezone.utc).isoformat(),
               "playlist": str(PLAYLIST), "channels_checked": len(results), "results": results}
    (OUT / "stream-audit.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    rows = [
        "# Relatório de auditoria HLS — todos os canais", "",
        f"- Verificado em (UTC): {payload['checked_at_utc']}",
        f"- Canais testados: {len(results)}",
        "- Teste: resposta HTTP, manifesto HLS, playlist de mídia (quando master) e amostra do primeiro segmento.",
        "- Limite: teste pontual; não mede reprodução contínua, buffering real ou qualidade percebida.", "",
        "| Canal | Categoria | Protocolo | HTTP | Manifesto | Resolução declarada | Segmento | Resposta (ms) |",
        "|---|---|---:|---:|---|---|---|---:|",
    ]
    for r in results:
        rows.append(f"| {r['channel'].replace('|', '/')} | {r['category']} | {r['scheme']} | {r['http_status'] or '—'} | {r['manifest']} | {', '.join(r['resolution']) or '—'} | {r['segment_sample']} | {r['response_ms'] if r['response_ms'] is not None else '—'} |")
    rows += ["", "## Detalhes", ""]
    for r in results:
        rows += [f"### {r['channel']}", f"- Categoria: {r['category']}", f"- URL: `{r['url']}`",
                 f"- Tipo: {r['content_type'] or 'não informado'}",
                 f"- Bitrate declarado (kbps): {', '.join(map(str, r['bandwidth_kbps'])) or 'não informado'}",
                 f"- Segmento HTTP: {r['segment_status'] or 'não testado'}",
                 f"- Tempo do segmento (ms): {r['segment_ms'] if r['segment_ms'] is not None else '—'}",
                 f"- Observação: {r['error'] or 'sem erro detectado neste teste'}", ""]
    (OUT / "stream-audit.md").write_text("\n".join(rows), encoding="utf-8")
    ok = sum(r["manifest"] == "OK" and r["segment_sample"] == "OK" for r in results)
    print(f"Auditoria concluída: {len(results)} canais; {ok} com manifesto e amostra de segmento OK.")
    print("Relatórios: reports/stream-audit.md e reports/stream-audit.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
