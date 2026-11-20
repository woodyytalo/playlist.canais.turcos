#!/usr/bin/env python3
"""Prepare every selected unified-catalog logo as a square SVG for the main TV playlist."""
from __future__ import annotations
import csv, hashlib, io, re, shutil, time
import xml.etree.ElementTree as ET
from pathlib import Path
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from PIL import Image
from vtracer import convert_image_to_svg_py

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "logos-turcas-catalogo" / "CATALOGO-UNIFICADO.md"
PLAYLIST = ROOT / "Tv.m3u"
OUT = ROOT / "logos-turcas-catalogo" / "tv-principal-svg"
TMP = ROOT / "artifacts" / "tv-principal-svg"
BRANCH = "github/workflows/atualizar-logos.yml"
RAW_BASE = "https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/" + BRANCH + "/"
SVG_NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", SVG_NS)

def slug(value: str) -> str:
    value = re.sub(r"[^A-Za-z0-9._-]+", "-", value.strip()).strip("-")
    return value or "logo"

def catalog_entries(text: str):
    pattern = re.compile(r"^\|\s*(.*?)\s*\|\s*!\[[^\]]*\]\((https?://[^)\s]+)\)\s*\|$", re.M)
    return [(name.strip(), url.strip()) for name, url in pattern.findall(text)]

def wrap_square(svg_bytes: bytes) -> bytes:
    original = ET.fromstring(svg_bytes)
    if original.tag.split("}")[-1].lower() != "svg":
        raise ValueError("O arquivo vetorial não tem raiz SVG.")
    original.set("width", "512")
    original.set("height", "512")
    original.set("preserveAspectRatio", "xMidYMid meet")
    outer = ET.Element(f"{{{SVG_NS}}}svg", {
        "width": "512", "height": "512", "viewBox": "0 0 512 512",
        "preserveAspectRatio": "xMidYMid meet",
    })
    outer.append(original)
    return ET.tostring(outer, encoding="utf-8", xml_declaration=True)

def convert_source(response, output: Path, temp_png: Path) -> str:
    content = response.content
    content_type = response.headers.get("Content-Type", "").lower()
    looks_svg = ("svg" in content_type or
                 (content.lstrip().startswith(b"<") and b"<svg" in content[:4096].lower()))
    if looks_svg:
        output.write_bytes(wrap_square(content))
        return "SVG original encaixado em canvas 512x512"

    image = Image.open(io.BytesIO(content))
    image.load()
    if image.width < 8 or image.height < 8:
        raise ValueError(f"Imagem muito pequena: {image.size}")
    image.convert("RGBA").save(temp_png, format="PNG")
    traced = output.with_suffix(".traced.svg")
    convert_image_to_svg_py(
        str(temp_png), str(traced), colormode="color", hierarchical="stacked",
        mode="spline", filter_speckle=4, color_precision=6, layer_difference=16,
        corner_threshold=60, length_threshold=4.0, max_iterations=10,
        splice_threshold=45, path_precision=3,
    )
    if not traced.exists() or traced.stat().st_size < 100:
        raise ValueError("O conversor não produziu um SVG válido.")
    output.write_bytes(wrap_square(traced.read_bytes()))
    traced.unlink(missing_ok=True)
    return f"Raster vetorizado ({image.format} {image.width}x{image.height})"

def main() -> None:
    entries = catalog_entries(CATALOG.read_text(encoding="utf-8"))
    if len(entries) != 211:
        raise RuntimeError(f"Esperadas 211 logos no catálogo; encontradas {len(entries)}.")
    if len({name.casefold() for name, _ in entries}) != len(entries):
        raise RuntimeError("O catálogo contém nomes de canal duplicados.")

    playlist_original = PLAYLIST.read_text(encoding="utf-8")
    playlist_names = re.findall(r'^#EXTINF:[^\n]*?\btvg-name="([^"]+)"', playlist_original, re.M)
    if len(playlist_names) != 211:
        raise RuntimeError(f"Esperados 211 canais na playlist; encontrados {len(playlist_names)}.")
    by_name = {name.casefold(): (name, url) for name, url in entries}
    missing = [name for name in playlist_names if name.casefold() not in by_name]
    if missing:
        raise RuntimeError("Canais sem logo correspondente no catálogo: " + ", ".join(missing))

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    TMP.mkdir(parents=True, exist_ok=True)
    session = requests.Session()
    retry = Retry(total=8, connect=5, read=5, status=8, backoff_factor=3,
                  status_forcelist=(429, 500, 502, 503, 504),
                  allowed_methods=frozenset(["GET"]), respect_retry_after_header=True)
    adapter = HTTPAdapter(max_retries=retry, pool_connections=4, pool_maxsize=4)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    session.headers.update({"User-Agent": "TVPrincipalLogoBuilder/1.0 (logo processing; contact: repository maintainer)"})
    output_by_name = {}
    manifest_rows = []

    for index, (channel, url) in enumerate(entries, 1):
        if channel.casefold() == "dost":
            manifest_rows.append({
                "channel": channel, "source_url": url, "svg_file": "",
                "status": "pending", "details": "Logo musical correta não localizada; não usar a marca religiosa Dost TV.",
            })
            print(f"[{index}/{len(entries)}] PENDENTE: {channel} — fonte inequívoca não localizada")
            continue
        digest = hashlib.sha256((channel + "\0" + url).encode("utf-8")).hexdigest()[:10]
        filename = f"{slug(channel)}-{digest}.svg"
        output = OUT / filename
        temp_png = TMP / f"{slug(channel)}-{digest}.png"
        response = session.get(url, timeout=60)
        response.raise_for_status()
        detail = convert_source(response, output, temp_png)
        time.sleep(0.8)
        root = ET.parse(output).getroot()
        if (root.attrib.get("viewBox") != "0 0 512 512" or
            root.attrib.get("width") != "512" or root.attrib.get("height") != "512"):
            raise RuntimeError(f"Canvas inválido para {channel}.")
        output_by_name[channel.casefold()] = filename
        manifest_rows.append({
            "channel": channel, "source_url": url, "svg_file": filename,
            "status": "ok", "details": detail,
        })
        print(f"[{index}/{len(entries)}] OK: {channel} — {detail}")

    def replace_logo(match):
        line = match.group(0)
        name_match = re.search(r'\btvg-name="([^"]+)"', line)
        if not name_match:
            raise RuntimeError("Linha EXTINF sem tvg-name.")
        channel_key = name_match.group(1).casefold()
        if channel_key not in output_by_name:
            return line
        filename = output_by_name[channel_key]
        new_url = RAW_BASE + "logos-turcas-catalogo/tv-principal-svg/" + filename
        return re.sub(r'\btvg-logo="[^"]*"', f'tvg-logo="{new_url}"', line, count=1)

    playlist_updated, count = re.subn(r'^#EXTINF:[^\n]*', replace_logo, playlist_original, flags=re.M)
    if count != 211:
        raise RuntimeError(f"Foram atualizadas {count} linhas EXTINF; esperado 211.")
    mask = lambda value: re.sub(r'\btvg-logo="[^"]*"', 'tvg-logo="__LOGO__"', value)
    if mask(playlist_original) != mask(playlist_updated):
        raise RuntimeError("A validação detectou alteração fora dos atributos tvg-logo.")
    PLAYLIST.write_text(playlist_updated, encoding="utf-8", newline="")

    with (OUT / "manifest.csv").open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["channel", "source_url", "svg_file", "status", "details"])
        writer.writeheader()
        writer.writerows(manifest_rows)
    (OUT / "README.md").write_text(
        "# Logos SVG — TV principal\n\n"
        "- Logos do catálogo unificado: 211\n"
        "- SVGs preparados: 210\n"
        "- Pendência: Dost (logo musical correta não localizada)\n"
        "- Canvas externo: 512 x 512, transparente\n"
        "- Enquadramento: centralizado, xMidYMid meet, sem corte ou deformação\n"
        "- Tv.m3u: somente os valores de tvg-logo foram atualizados\n\n"
        "SVGs que já eram vetoriais foram preservados dentro do canvas quadrado. "
        "Imagens raster foram vetorizadas automaticamente e podem apresentar pequenas diferenças "
        "em degradês, transparências ou detalhes finos. Consulte manifest.csv para rastreabilidade.\n",
        encoding="utf-8",
    )
    print("SUCESSO: 210/211 logos preparadas e aplicadas à Tv.m3u; Dost permaneceu inalterado e pendente.")

if __name__ == "__main__":
    main()
