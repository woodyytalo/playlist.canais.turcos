#!/usr/bin/env python3
"""Validação preventiva da playlist TV principal. Não remove nem altera canais."""
from pathlib import Path
from urllib.parse import urlsplit
import re
import sys

path = Path(sys.argv[1] if len(sys.argv) > 1 else "Tv.m3u")
if not path.is_file():
    raise SystemExit(f"ERRO: arquivo não encontrado: {path}")
lines = path.read_text(encoding="utf-8-sig").splitlines()
errors = []
warnings = []
if not lines or not lines[0].lstrip().startswith("#EXTM3U"):
    errors.append("cabeçalho #EXTM3U ausente na primeira linha")

channels = 0
seen_names = {}
i = 0
while i < len(lines):
    line = lines[i].strip()
    if not line or line.startswith("#") and not line.startswith("#EXTINF:"):
        i += 1
        continue
    if line.startswith("#EXTINF:"):
        channels += 1
        if line.count('"') % 2:
            errors.append(f"linha {i+1}: aspas não fechadas em EXTINF")
        if "," not in line or not line.rsplit(",", 1)[1].strip():
            errors.append(f"linha {i+1}: nome do canal vazio ou EXTINF inválido")
        name = line.rsplit(",", 1)[-1].strip() if "," in line else f"linha {i+1}"
        key = re.sub(r"\\s+", " ", name.casefold())
        seen_names.setdefault(key, []).append(i+1)
        logo = re.search(r'tvg-logo="([^"]*)"', line)
        if logo and logo.group(1):
            parsed_logo = urlsplit(logo.group(1))
            if parsed_logo.scheme not in ("http", "https") or not parsed_logo.netloc:
                errors.append(f"linha {i+1}: URL de logo inválida")
        j = i + 1
        while j < len(lines) and (not lines[j].strip() or lines[j].strip().startswith("#EXTVLCOPT:")):
            j += 1
        if j >= len(lines) or lines[j].strip().startswith("#"):
            errors.append(f"linha {i+1}: canal {name!r} sem URL de transmissão")
            i += 1
            continue
        stream = lines[j].strip()
        parsed = urlsplit(stream)
        if parsed.scheme.lower() not in ("http", "https", "rtmp", "rtmps", "rtsp", "udp", "rtp") or not parsed.netloc:
            errors.append(f"linha {j+1}: URL de transmissão inválida para {name!r}")
        i = j + 1
        continue
    if line.startswith(("http://", "https://", "rtmp://", "rtmps://", "rtsp://", "udp://", "rtp://")):
        errors.append(f"linha {i+1}: URL órfã, sem EXTINF correspondente")
    elif not line.startswith("#"):
        errors.append(f"linha {i+1}: conteúdo inesperado")
    i += 1

if channels == 0:
    errors.append("nenhum canal encontrado")
for name, positions in seen_names.items():
    if len(positions) > 1:
        warnings.append(f"nome repetido {name!r} nas linhas {positions} (mantido; não removido)")

print(f"Playlist: {path} | canais: {channels} | linhas: {len(lines)}")
for warning in warnings:
    print("AVISO:", warning)
if errors:
    for error in errors:
        print("ERRO:", error)
    raise SystemExit(f"Validação reprovada: {len(errors)} erro(s). Publicação bloqueada.")
print("Validação aprovada: estrutura M3U e URLs sintaticamente válidas.")
