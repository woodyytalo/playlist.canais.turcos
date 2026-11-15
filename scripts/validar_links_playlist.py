#!/usr/bin/env python3
"""Valida que cada canal da TV principal tenha exatamente um link de transmissão."""
from pathlib import Path
import sys

playlist = Path("Tv.m3u8")
if not playlist.is_file():
    raise SystemExit("ERRO: Tv.m3u8 não encontrado.")

lines = playlist.read_text(encoding="utf-8").splitlines()
current = None
errors = []

def finish():
    if current is not None:
        name, urls, line_no = current
        if len(urls) != 1:
            errors.append(f"Linha {line_no} ({name}): esperado 1 link, encontrados {len(urls)}.")

for number, raw in enumerate(lines, start=1):
    line = raw.strip()
    if line.startswith("#EXTINF:"):
        finish()
        current = [line.rsplit(",", 1)[-1].strip() or "sem nome", [], number]
    elif line.startswith(("http://", "https://")):
        if current is None:
            errors.append(f"Linha {number}: link sem entrada #EXTINF correspondente.")
        else:
            current[1].append(line)

finish()
if errors:
    print("FALHA: links da TV principal fora da estrutura individual:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

count = sum(1 for line in lines if line.strip().startswith("#EXTINF:"))
print(f"OK: {count} canais verificados; cada canal possui exatamente um link próprio.")
