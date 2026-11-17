#!/usr/bin/env python3
"""Teste de disponibilidade dos streams do TV principal; nunca altera a playlist."""
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
from datetime import datetime, timezone
import sys, time

playlist = Path(sys.argv[1] if len(sys.argv) > 1 else "Tv.m3u")
report = Path(sys.argv[2] if len(sys.argv) > 2 else "reports/anti-crash/resultado.txt")
lines = playlist.read_text(encoding="utf-8-sig").splitlines()
channels, current = [], None
for line in lines:
    line = line.strip()
    if line.startswith("#EXTINF:"):
        current = line.rsplit(",", 1)[-1].strip()
    elif line and not line.startswith("#") and current:
        channels.append((current, line))
        current = None

def probe(item):
    name, url = item
    if not url.lower().startswith(("http://", "https://")):
        return name, "IGNORADO", "protocolo não HTTP(S)"
    last = ""
    for attempt in range(2):
        try:
            req = Request(url, headers={"User-Agent":"Mozilla/5.0 IPTV-health-check", "Range":"bytes=0-1023"}, method="GET")
            with urlopen(req, timeout=12) as response:
                code = response.status
                ctype = response.headers.get("Content-Type", "")
                if code < 400:
                    return name, "OK", f"HTTP {code}; {ctype or 'tipo não informado'}"
                last = f"HTTP {code}"
        except HTTPError as exc:
            last = f"HTTP {exc.code}"
            if exc.code in (401, 403, 404, 410):
                break
        except (URLError, TimeoutError, OSError) as exc:
            last = f"{type(exc).__name__}: {str(exc)[:140]}"
        if attempt == 0:
            time.sleep(1)
    return name, "FALHA", last or "sem resposta"

results = []
with ThreadPoolExecutor(max_workers=12) as pool:
    futures = [pool.submit(probe, item) for item in channels]
    for future in as_completed(futures):
        results.append(future.result())
results.sort(key=lambda row: row[0].casefold())
ok = sum(status == "OK" for _, status, _ in results)
failed = sum(status == "FALHA" for _, status, _ in results)
ignored = sum(status == "IGNORADO" for _, status, _ in results)
report.parent.mkdir(parents=True, exist_ok=True)
with report.open("w", encoding="utf-8") as out:
    out.write(f"Auditoria anti-crash TV principal | {datetime.now(timezone.utc).isoformat()}\n")
    out.write(f"Total: {len(results)} | OK: {ok} | Falhas: {failed} | Ignorados: {ignored}\n")
    out.write("A verificação é pontual; falha pode ser bloqueio temporário/geográfico ou proteção anti-bot. Nenhum canal foi removido.\n\n")
    for name, status, detail in results:
        out.write(f"[{status}] {name} — {detail}\n")
print(f"TV principal: {len(results)} canais | OK: {ok} | falhas: {failed} | ignorados: {ignored}")
print(f"Relatório: {report}")
# Falhas são reportadas para o workflow, sem alterar nem excluir streams.
if failed:
    raise SystemExit(1)
