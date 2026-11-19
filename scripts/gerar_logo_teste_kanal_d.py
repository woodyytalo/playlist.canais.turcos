#!/usr/bin/env python3
"""Gera uma logo de teste da Kanal D e salva fora da playlist."""
import base64
import json
import os
import urllib.request
from pathlib import Path

API_KEY = os.environ.get("OPENAI_API_KEY")
if not API_KEY:
    raise SystemExit("Falta configurar OPENAI_API_KEY em Settings > Secrets and variables > Actions.")

prompt = (
    "Create an original, standalone custom emblem for a Turkish television channel, "
    "based on the personalized RIGHT-HAND symbol from a Kanal D-style logo concept. "
    "Show ONLY the emblem: no channel name, no letters, no wordmark, no typography, "
    "and no other symbols. The emblem is a distinctive sculptural geometric D form, "
    "with a vivid electric-blue outer shape and a clean white inner negative space. "
    "Give it a premium three-dimensional broadcast-identity finish inspired by "
    "high-end television channel ident design: polished dimensional surfaces, "
    "controlled highlights, subtle depth, precise contours, and balanced proportions. "
    "Centered alone on a clean light neutral background, square 1:1 composition, "
    "crisp and highly legible at small sizes. Original design; do not reproduce "
    "an existing designer's artwork, mockup, watermark, border, or extra text."
)
payload = {
    "model": "gpt-image-1.5",
    "prompt": prompt,
    "size": "1024x1024",
    "quality": "high",
    "output_format": "png"
}
req = urllib.request.Request(
    "https://api.openai.com/v1/images/generations",
    data=json.dumps(payload).encode("utf-8"),
    headers={"Authorization": "Bearer " + API_KEY, "Content-Type": "application/json"},
    method="POST"
)
try:
    with urllib.request.urlopen(req, timeout=240) as response:
        result = json.loads(response.read().decode("utf-8"))
except Exception as exc:
    detail = getattr(exc, "read", lambda: b"")()
    if detail:
        try:
            detail = json.loads(detail.decode("utf-8"))
        except Exception:
            detail = detail.decode("utf-8", "replace")[:1200]
    raise SystemExit(f"Falha na geração da imagem: {exc}. Detalhes: {detail}")

items = result.get("data") or []
if not items or not items[0].get("b64_json"):
    raise SystemExit("A API não retornou a imagem em base64.")
out = Path("artifacts/logo-teste-kanal-d.png")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_bytes(base64.b64decode(items[0]["b64_json"]))
print(f"Imagem de teste salva em {out} ({out.stat().st_size} bytes).")
print("Nenhuma playlist foi lida, alterada ou atualizada.")
