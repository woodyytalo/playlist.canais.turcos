#!/usr/bin/env python3
"""Auditoria resiliente dos links HTTP(S) da TV principal.

Repete cada teste antes de classificar uma falha, destaca HTTP 404 e gera
relatório para GitHub Actions. Nunca altera Tv.m3u nem remove canais.
"""
from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit, urlunsplit
from urllib.request import Request, urlopen
import re
import sys
import time

PLAYLIST = Path(sys.argv[1] if len(sys.argv) > 1 else "Tv.m3u")
REPORT = Path(sys.argv[2] if len(sys.argv) > 2 else "reports/anti-crash/resultado.txt")
TIMEOUT = 20
ATTEMPTS = 5
SAMPLE_BYTES = 65536
USER_AGENT = "Mozilla/5.0 (compatible; TVPlaylistLinkAudit/2.0)"


def safe_url(url: str) -> str:
    """Remove query/fragment e credenciais do relatório."""
    p = urlsplit(url)
    host = p.hostname or ""
    if p.port:
        host = f"{host}:{p.port}"
    return urlunsplit((p.scheme, host, p.path, "", ""))


def parse_channels(text: str):
    channels = []
    name = None
    for raw in text.splitlines():
        line = raw.strip()
        if line.startswith("#EXTINF:"):
            name = line.rsplit(",", 1)[-1].strip() if "," in line else "Canal sem nome"
        elif line and not line.startswith("#") and name:
            if line.lower().startswith(("http://", "https://")):
                channels.append((name, line))
            name = None
    return channels


def classify(status: int | None, error: str, body_size: int) -> str:
    if status == 404:
        return "HTTP_404"
    if status == 410:
        return "HTTP_410"
    if status in (401, 403):
        return "HTTP_BLOQUEADO"
    if status is not None and status >= 500:
        return "HTTP_SERVIDOR"
    if status is not None and status >= 400:
        return "HTTP_ERRO"
    if status is None:
        return "FALHA_REDE"
    if body_size == 0:
        return "RESPOSTA_VAZIA"
    return "OK"


def probe(item):
    name, url = item
    last = None
    for attempt in range(1, ATTEMPTS + 1):
        started = time.monotonic()
        try:
            req = Request(url, headers={
                "User-Agent": USER_AGENT,
                "Accept": "*/*",
                "Range": f"bytes=0-{SAMPLE_BYTES - 1}",
            })
            with urlopen(req, timeout=TIMEOUT) as response:
                body = response.read(SAMPLE_BYTES)
                status = response.status
                final_url = safe_url(response.geturl())
                content_type = response.headers.get("Content-Type", "")
                elapsed = round((time.monotonic() - started) * 1000)
                category = classify(status, "", len(body))
                last = {
                    "name": name, "url": safe_url(url), "final_url": final_url,
                    "category": category, "status": status, "attempts": attempt,
                    "elapsed_ms": elapsed, "bytes": len(body),
                    "content_type": content_type, "detail": "",
                }
                if category == "OK":
                    return last
                last["detail"] = "Resposta HTTP sem conteúdo."
        except HTTPError as exc:
            last = {
                "name": name, "url": safe_url(url), "final_url": safe_url(exc.geturl()),
                "category": classify(exc.code, "", 0), "status": exc.code,
                "attempts": attempt, "elapsed_ms": round((time.monotonic() - started) * 1000),
                "bytes": 0, "content_type": exc.headers.get("Content-Type", ""),
                "detail": f"HTTP {exc.code}",
            }
        except (URLError, TimeoutError, OSError) as exc:
            reason = getattr(exc, "reason", exc)
            last = {
                "name": name, "url": safe_url(url), "final_url": safe_url(url),
                "category": "FALHA_REDE", "status": None, "attempts": attempt,
                "elapsed_ms": round((time.monotonic() - started) * 1000),
                "bytes": 0, "content_type": "",
                "detail": f"{type(exc).__name__}: {str(reason)[:180]}",
            }

        # Repetir também 404: CDNs e proxies podem responder incorretamente
        # durante uma oscilação. Só classificar após as três tentativas.
        if attempt < ATTEMPTS:
            time.sleep(attempt)

    return last


def main() -> int:
    if not PLAYLIST.is_file():
        print(f"ERRO: playlist não encontrada: {PLAYLIST}", file=sys.stderr)
        return 2

    channels = parse_channels(PLAYLIST.read_text(encoding="utf-8-sig", errors="replace"))
    if not channels:
        print("ERRO: nenhum link HTTP(S) encontrado na playlist.", file=sys.stderr)
        return 2

    results = []
    with ThreadPoolExecutor(max_workers=5) as pool:
        futures = [pool.submit(probe, channel) for channel in channels]
        for future in as_completed(futures):
            results.append(future.result())
    results.sort(key=lambda row: row["name"].casefold())

    counts = {}
    for row in results:
        counts[row["category"]] = counts.get(row["category"], 0) + 1

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    with REPORT.open("w", encoding="utf-8") as out:
        out.write("# Auditoria de links — TV principal\n")
        out.write(f"Verificado em UTC: {datetime.now(timezone.utc).isoformat()}\n")
        out.write(f"Playlist: {PLAYLIST} | Canais HTTP(S): {len(results)}\n")
        out.write(f"Tentativas por endereço: até {ATTEMPTS} | Timeout por tentativa: {TIMEOUT}s\n")
        out.write("A auditoria é somente leitura: não modifica Tv.m3u e não remove canais.\n")
        out.write("HTTP 404 só é confirmado após repetir a requisição três vezes.\n\n")
        out.write("## Resumo\n")
        for category in ("OK", "HTTP_404", "HTTP_410", "HTTP_BLOQUEADO",
                         "HTTP_SERVIDOR", "HTTP_ERRO", "FALHA_REDE", "RESPOSTA_VAZIA"):
            out.write(f"- {category}: {counts.get(category, 0)}\n")
        out.write("\n## Resultado por canal\n")
        out.write("| Canal | Estado | HTTP | Tentativas | Tempo final (ms) | Detalhe |\n")
        out.write("|---|---|---:|---:|---:|---|\n")
        for row in results:
            detail = (row["detail"] or row["content_type"] or "—").replace("|", "/")
            out.write(f"| {row['name'].replace('|', '/')} | {row['category']} | "
                      f"{row['status'] or '—'} | {row['attempts']} | "
                      f"{row['elapsed_ms']} | {detail} |\n")
        for row in results:
            if row["category"] != "OK":
                out.write(f"\n### {row['name']} — {row['category']}\n")
                out.write(f"- URL testada: {row['url']}\n")
                out.write(f"- URL final após redirecionamentos: {row['final_url']}\n")
                out.write(f"- HTTP: {row['status'] or 'sem resposta'}; tentativas: {row['attempts']}\n")
                out.write(f"- Detalhe: {row['detail'] or 'verificar a origem do stream'}\n")

    print(f"Auditoria concluída: {len(results)} canais.")
    print(" | ".join(f"{key}: {counts.get(key, 0)}" for key in
                    ("OK", "HTTP_404", "HTTP_410", "HTTP_BLOQUEADO",
                     "HTTP_SERVIDOR", "HTTP_ERRO", "FALHA_REDE", "RESPOSTA_VAZIA")))
    print(f"Relatório: {REPORT}")
    print("Nenhum canal foi removido ou alterado.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
