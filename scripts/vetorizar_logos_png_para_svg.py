#!/usr/bin/env python3
"""Download PNG logo references from the unified catalog and vectorize them to SVG."""
from __future__ import annotations
import csv, hashlib, io, re, zipfile
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit
import requests
from PIL import Image
from vtracer import convert_image_to_svg_py

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "logos-turcas-catalogo" / "CATALOGO-UNIFICADO.md"
OUT = ROOT / "artifacts" / "logos-vetorizados-svg"
OUT.mkdir(parents=True, exist_ok=True)

def clean_url(raw: str) -> str:
    raw = raw.rstrip(".,;)")
    raw = re.sub(r",(?:Public|CC0?|CC BY[^\s|]*)$", "", raw)
    return raw

text = CATALOG.read_text(encoding="utf-8")
raw_urls = re.findall(r"https?://[^\s|<>\])\"]+", text)
candidates = []
seen = set()
for raw in raw_urls:
    url = clean_url(raw)
    path = urlsplit(url).path.lower()
    if not path.endswith(".png"):
        continue
    if "commons.wikimedia.org/wiki/" in url:
        continue
    if url not in seen:
        seen.add(url)
        candidates.append(url)

session = requests.Session()
session.headers.update({"User-Agent": "Mozilla/5.0 (compatible; IPTVLogoVectorizer/1.0)"})
rows = []
for index, url in enumerate(candidates, 1):
    name = Path(urlsplit(url).path).name or f"logo-{index}.png"
    stem = re.sub(r"[^A-Za-z0-9._-]+", "-", Path(name).stem).strip("-") or "logo"
    digest = hashlib.sha256(url.encode("utf-8")).hexdigest()[:10]
    png_path = OUT / "_downloads" / f"{stem}-{digest}.png"
    svg_path = OUT / f"{stem}-{digest}.svg"
    status, detail = "error", ""
    try:
        response = session.get(url, timeout=30)
        response.raise_for_status()
        image = Image.open(io.BytesIO(response.content))
        image.load()
        if image.format != "PNG":
            raise ValueError(f"URL terminou em PNG, mas o conteúdo é {image.format}")
        png_path.parent.mkdir(parents=True, exist_ok=True)
        png_path.write_bytes(response.content)
        convert_image_to_svg_py(
            str(png_path), str(svg_path),
            colormode="color", hierarchical="stacked", mode="spline",
            filter_speckle=4, color_precision=6, layer_difference=16,
            corner_threshold=60, length_threshold=4.0,
            max_iterations=10, splice_threshold=45, path_precision=3,
        )
        if not svg_path.exists() or svg_path.stat().st_size < 100:
            raise ValueError("Conversor não produziu SVG válido")
        status = "vetorizado"
        detail = f"{image.width}x{image.height}"
    except Exception as exc:
        detail = f"{type(exc).__name__}: {exc}"[:500]
        if svg_path.exists():
            svg_path.unlink()
    rows.append({"source_url": url, "svg_file": svg_path.name if status == "vetorizado" else "", "status": status, "details": detail})
    print(f"[{index}/{len(candidates)}] {status}: {name} — {detail}")

with (OUT / "manifest.csv").open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["source_url", "svg_file", "status", "details"])
    writer.writeheader()
    writer.writerows(rows)

success = sum(r["status"] == "vetorizado" for r in rows)
(OUT / "README.md").write_text(
    "# Logos vetorizados em SVG\n\n"
    f"- URLs PNG únicas identificadas no catálogo: {len(candidates)}\n"
    f"- SVGs gerados: {success}\n"
    f"- Falhas/links não convertidos: {len(rows)-success}\n\n"
    "Os SVGs são vetorização automática por rastreamento de contornos. "
    "Podem diferir dos originais, especialmente em logos pequenos, degradês e transparências. "
    "Consulte manifest.csv para a URL de origem e o estado de cada item. "
    "Os PNGs originais foram mantidos apenas na pasta temporária de trabalho e não são alterados.\n",
    encoding="utf-8",
)
zip_path = ROOT / "artifacts" / "logos-vetorizados-svg.zip"
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
    for file in OUT.iterdir():
        if file.is_file():
            z.write(file, arcname=file.name)
print(f"RESUMO: {len(candidates)} candidatos; {success} SVGs; {len(rows)-success} falhas.")
