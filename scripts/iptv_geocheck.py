#!/usr/bin/env python3
"""Check Turkish IPTV playlist endpoints without bypassing regional restrictions."""
from __future__ import annotations
import concurrent.futures
import datetime as dt
import os
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urlparse

PLAYLIST = Path(os.environ.get("PLAYLIST_FILE", "Backup.m3u"))
REPORT = Path(os.environ.get("REPORT_FILE", "reports/iptv-geocheck.md"))
TIMEOUT = float(os.environ.get("CHECK_TIMEOUT", "12"))
WORKERS = int(os.environ.get("CHECK_WORKERS", "16"))
MAX_BODY = 4096
GEO_HINTS = (
    "not available in your country", "not available in your region",
    "geo blocked", "geoblocked", "geographic restriction",
    "country is not supported", "territory restriction",
)

def parse_playlist(path: Path):
    text = path.read_text(encoding="utf-8", errors="replace")
    name = "Canal sem nome"
    entries = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("#EXTINF"):
            tail = line.rsplit(",", 1)
            name = tail[-1].strip() if len(tail) > 1 else "Canal sem nome"
        elif not line.startswith("#") and line.lower().startswith(("http://", "https://")):
            entries.append((name, line))
            name = "Canal sem nome"
    return entries

def check(item):
    name, url = item
    host = urlparse(url).hostname or "host desconhecido"
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "IPTV-GeoCheck/1.0 (+playlist diagnostics)",
            "Range": f"bytes=0-{MAX_BODY - 1}",
            "Accept": "*/*",
            "Connection": "close",
        },
        method="GET",
    )
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as response:
            body = response.read(MAX_BODY).decode("utf-8", errors="ignore").lower()
            status = response.status
            if any(hint in body for hint in GEO_HINTS):
                state = "POSSÍVEL BLOQUEIO REGIONAL"
            elif status in (200, 206, 301, 302, 307, 308):
                state = "ACESSÍVEL NO AMBIENTE DO TESTE"
            else:
                state = f"HTTP {status}"
            return {"name": name, "host": host, "status": status, "state": state}
    except urllib.error.HTTPError as exc:
        if exc.code in (403, 451):
            state = "ACESSO NEGADO — possível restrição regional ou autorização"
        elif exc.code == 404:
            state = "LINK NÃO ENCONTRADO (404)"
        elif exc.code in (401, 407):
            state = f"AUTENTICAÇÃO/PROXY NECESSÁRIO ({exc.code})"
        else:
            state = f"ERRO HTTP {exc.code}"
        return {"name": name, "host": host, "status": exc.code, "state": state}
    except Exception as exc:
        reason = type(exc).__name__
        return {"name": name, "host": host, "status": "-", "state": f"FALHA DE CONEXÃO ({reason})"}

def main():
    if not PLAYLIST.exists():
        raise SystemExit(f"Playlist não encontrada: {PLAYLIST}")
    entries = parse_playlist(PLAYLIST)
    if not entries:
        raise SystemExit("Nenhum link HTTP/HTTPS foi encontrado na playlist.")
    with concurrent.futures.ThreadPoolExecutor(max_workers=WORKERS) as pool:
        results = list(pool.map(check, entries))
    counts = {}
    for row in results:
        counts[row["state"]] = counts.get(row["state"], 0) + 1
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    now = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        "# Relatório IPTV GeoCheck — canais turcos", "",
        f"- Executado em: {now}",
        f"- Playlist analisada: \`{PLAYLIST}\`",
        f"- Entradas testadas: **{len(results)}**",
        f"- URLs únicas: **{len(set(url for _, url in entries))}**", "",
        "## Resumo", "", "| Resultado | Quantidade |", "|---|---:|",
    ]
    for state, count in sorted(counts.items(), key=lambda x: (-x[1], x[0])):
        lines.append(f"| {state} | {count} |")
    lines += ["", "## Detalhamento", "", "| Canal | Host | Resultado | HTTP |", "|---|---|---|---:|"]
    for row in results:
        safe_name = row["name"].replace("|", "\\|")
        lines.append(f"| {safe_name} | \`{row['host']}\` | {row['state']} | {row['status']} |")
    lines += [
        "", "## Observações", "",
        "- HTTP 403/451 indica acesso negado; isso pode ser bloqueio regional, autenticação ou política do servidor.",
        "- Um teste executado no GitHub não confirma disponibilidade a partir do Brasil.",
        "- O bot não usa VPN, proxy para contornar bloqueios, credenciais novas ou técnicas de evasão.",
        "- A playlist original não é modificada. Este relatório é apenas diagnóstico.", "",
    ]
    REPORT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Testados: {len(results)} | Relatório: {REPORT}")
    for state, count in sorted(counts.items(), key=lambda x: (-x[1], x[0])):
        print(f"{count:4}  {state}")

if __name__ == "__main__":
    main()
