#!/usr/bin/env python3
"""Fetch image references from the unified catalog and trace them into SVG files."""
from __future__ import annotations
import csv, hashlib, io, re
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlsplit
import requests
from PIL import Image
from vtracer import convert_image_to_svg_py

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "logos-turcas-catalogo" / "CATALOGO-UNIFICADO.md"
OUT = ROOT / "logos-turcas-catalogo" / "svg"
TMP = ROOT / "artifacts" / "svg-source-images"
OUT.mkdir(parents=True, exist_ok=True)
TMP.mkdir(parents=True, exist_ok=True)

catalog = CATALOG.read_text(encoding="utf-8")
# Include Markdown image embeds (including extensionless CDN URLs) and direct PNG
# references in tables. Exclude ordinary links to pages and non-image documents.
urls = re.findall(r"!\[[^\]]*\]\((https?://[^)\s]+)\)", catalog)
urls += re.findall(r"https?://[^\s|<>\])\"]+\.png(?:\?[^\s|<>\])\"]*)?", catalog)
candidates, seen = [], set()
for url in urls:
    url = url.rstrip(".,;)")
    if url not in seen:
        seen.add(url)
        candidates.append(url)

session = requests.Session()
session.headers.update({"User-Agent": "Mozilla/5.0 (compatible; IPTVLogoVectorizer/1.1)"})
rows = []
for index, url in enumerate(candidates, 1):
    parsed = urlsplit(url)
    basename = Path(parsed.path).stem or f"logo-{index}"
    stem = re.sub(r"[^A-Za-z0-9._-]+", "-", basename).strip("-") or f"logo-{index}"
    digest = hashlib.sha256(url.encode("utf-8")).hexdigest()[:10]
    source_path = TMP / f"{stem}-{digest}.png"
    svg_path = OUT / f"{stem}-{digest}.svg"
    status, detail = "error", ""
    try:
        response = session.get(url, timeout=30)
        response.raise_for_status()
        image = Image.open(io.BytesIO(response.content))
        image.load()
        if image.width < 8 or image.height < 8:
            raise ValueError(f"Imagem muito pequena: {image.size}")
        image.convert("RGBA").save(source_path, format="PNG")
        convert_image_to_svg_py(
            str(source_path), str(svg_path),
            colormode="color", hierarchical="stacked", mode="spline",
            filter_speckle=4, color_precision=6, layer_difference=16,
            corner_threshold=60, length_threshold=4.0,
            max_iterations=10, splice_threshold=45, path_precision=3,
        )
        if not svg_path.exists() or svg_path.stat().st_size < 100:
            raise ValueError("Conversor não produziu SVG válido")

        # Padroniza a área externa em 512x512 sem deformar nem recortar o desenho.
        # O SVG vetorial original fica aninhado e é ajustado por preserveAspectRatio.
        namespace = "http://www.w3.org/2000/svg"
        ET.register_namespace("", namespace)
        original_svg = ET.parse(svg_path).getroot()
        original_svg.set("width", "512")
        original_svg.set("height", "512")
        original_svg.set("preserveAspectRatio", "xMidYMid meet")
        square_svg = ET.Element(
            f"{{{namespace}}}svg",
            {
                "width": "512",
                "height": "512",
                "viewBox": "0 0 512 512",
                "preserveAspectRatio": "xMidYMid meet",
            },
        )
        square_svg.append(original_svg)
        ET.ElementTree(square_svg).write(
            svg_path, encoding="utf-8", xml_declaration=True
        )
        status = "vetorizado"
        detail = f"{image.format} {image.width}x{image.height}"
    except Exception as exc:
        detail = f"{type(exc).__name__}: {exc}"[:400]
        if svg_path.exists():
            svg_path.unlink()
    rows.append({"source_url": url, "svg_file": svg_path.name if status == "vetorizado" else "", "status": status, "details": detail})
    print(f"[{index}/{len(candidates)}] {status}: {url} — {detail}")

with (OUT / "manifest.csv").open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["source_url", "svg_file", "status", "details"])
    writer.writeheader()
    writer.writerows(rows)
success = sum(row["status"] == "vetorizado" for row in rows)
(OUT / "README.md").write_text(
    "# Logos vetorizados em SVG\n\n"
    f"- Referências de imagem únicas processadas: {len(candidates)}\n"
    f"- SVGs gerados: {success}\n"
    f"- Falhas/links inacessíveis: {len(rows)-success}\n\n"
    "Arquivos gerados por vetorização automática (rastreamento de contornos), não por redesenho manual. "
    "Podem existir diferenças em degradês, transparências, letras pequenas e detalhes finos. "
    "Consulte manifest.csv para rastrear cada SVG até sua URL de origem. "
    "Os arquivos originais e a playlist não são alterados.\n",
    encoding="utf-8",
)
print(f"RESUMO: {len(candidates)} referências; {success} SVGs; {len(rows)-success} falhas.")
