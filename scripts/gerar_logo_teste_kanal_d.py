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
    "Create an original, professional square 1:1 Turkish television channel logo concept "
    "for KANAL D. This is a test asset only, not an instruction to modify any playlist. "
    "Composition: exact wordmark 'KANAL D' on the LEFT and a distinctive custom geometric "
    "D-shaped emblem on the RIGHT. The emblem is a bold sculptural rounded D with a vivid "
    "electric-blue outer form and clean white inner negative space. Deep navy lettering, "
    "blue emblem, clean light neutral background, subtle dimensional depth, crisp edges, "
    "premium broadcast identity, balanced spacing, highly legible. No extra text, no watermark, "
    "no mockup, no border. Original concept; do not reproduce an existing designer's artwork."
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
