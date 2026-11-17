#!/usr/bin/env python3
"""Auditoria de resposta HTTP dos streams e sugestão heurística de buffer.
Não altera URLs nem parâmetros da playlist. A medição do manifesto não equivale
a um teste de reprodução/decodificação dentro do IPTV Pro.
"""
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

def profile(status, latency, rate):
    # Heurística baseada somente na resposta HTTP inicial do endereço HLS.
    if status != "OK":
        return "5000 ms (investigar fonte)", "FALHA HTTP; não aplicar automaticamente"
    if latency <= 1.5 and rate >= 64:
        return "1000 ms (resposta rápida)", "baixo atraso HTTP observado"
    if latency <= 4.0 and rate >= 16:
        return "2000 ms (resposta intermediária)", "resposta HTTP moderada"
    return "3000 ms (resposta lenta)", "resposta HTTP lenta/transferência reduzida"

def probe(item):
    name, url = item
    if not url.lower().startswith(("http://", "https://")):
        return name, "IGNORADO", "protocolo não HTTP(S)", None, None, "não definido", "protocolo não testado"
    last = ""
    for attempt in range(2):
        started = time.monotonic()
        try:
            req = Request(url, headers={
                "User-Agent": "Mozilla/5.0 IPTV-health-check",
                "Range": "bytes=0-65535",
                "Accept": "*/*",
            }, method="GET")
            with urlopen(req, timeout=12) as response:
                code = response.status
                ctype = response.headers.get("Content-Type", "")
                first_byte = time.monotonic() - started
                payload = response.read(65536)
                elapsed = max(time.monotonic() - started, 0.001)
                rate = len(payload) / elapsed / 1024
                if code < 400:
                    recommended, reason = profile("OK", first_byte, rate)
                    return name, "OK", f"HTTP {code}; {ctype or 'tipo não informado'}", first_byte, rate, recommended, reason
                last = f"HTTP {code}"
        except HTTPError as exc:
            last = f"HTTP {exc.code}"
            if exc.code in (401, 403, 404, 410):
                break
        except (URLError, TimeoutError, OSError) as exc:
            last = f"{type(exc).__name__}: {str(exc)[:140]}"
        if attempt == 0:
            time.sleep(1)
    recommended, reason = profile("FALHA", None, None)
    return name, "FALHA", last or "sem resposta", None, None, recommended, reason

results = []
with ThreadPoolExecutor(max_workers=8) as pool:
    futures = [pool.submit(probe, item) for item in channels]
    for future in as_completed(futures):
        results.append(future.result())
results.sort(key=lambda row: row[0].casefold())
ok = sum(row[1] == "OK" for row in results)
failed = sum(row[1] == "FALHA" for row in results)
ignored = sum(row[1] == "IGNORADO" for row in results)
report.parent.mkdir(parents=True, exist_ok=True)
with report.open("w", encoding="utf-8") as out:
    out.write(f"Auditoria de rede TV principal | {datetime.now(timezone.utc).isoformat()}\n")
    out.write(f"Total: {len(results)} | HTTP OK: {ok} | Falhas: {failed} | Ignorados: {ignored}\n")
    out.write("PERFIS SUGERIDOS (heurística de resposta HTTP; não são aplicados à playlist).\n")
    out.write("A medição do manifesto HLS não testa decodificação, continuidade do vídeo, Wi-Fi ou desempenho real do IPTV Pro.\n")
    out.write("O parâmetro #EXTVLCOPT:network-caching pode ser ignorado por players que não usam VLC.\n")
    out.write("Não remova canais nem altere URLs com base apenas neste relatório.\n\n")
    out.write("Canal | Estado | Primeiro byte | Taxa de leitura | Perfil sugerido | Detalhe\n")
    for name, status, detail, latency, rate, recommended, reason in results:
        lat = f"{latency:.2f}s" if latency is not None else "—"
        spd = f"{rate:.1f} KiB/s" if rate is not None else "—"
        out.write(f"{name} | {status} | {lat} | {spd} | {recommended} | {detail}; {reason}\n")
print(f"TV principal: {len(results)} canais | HTTP OK: {ok} | falhas: {failed} | ignorados: {ignored}")
print(f"Relatório com perfil sugerido por canal: {report}")
if failed:
    print("Atenção: falhas HTTP pontuais não provam que o canal esteja permanentemente fora do ar.")
