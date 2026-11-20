#!/usr/bin/env python3
"""Replace catalog sources with the exact channel images exposed by CanliTV pages."""
from __future__ import annotations
import csv, re, time, unicodedata
from pathlib import Path
from urllib.parse import urljoin, urlparse
from io import BytesIO
import requests
from bs4 import BeautifulSoup
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
PLAYLIST = ROOT / "Tv.m3u"
CATALOG = ROOT / "logos-turcas-catalogo" / "CATALOGO-UNIFICADO.md"
REPORT = ROOT / "logos-turcas-catalogo" / "canlitv-images-report.csv"
ORIGINALS = ROOT / "logos-turcas-catalogo" / "canlitv-originals"
INDEX = "https://tr.canlitv.watch/frekans-bilgileri"
BASE = "https://tr.canlitv.watch"

def norm(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    value = value.upper().replace("&", " AND ")
    value = re.sub(r"\b(HD|SD|UHD|4K)\b", " ", value)
    value = re.sub(r"\bTV\b$", " ", value)
    return re.sub(r"[^A-Z0-9]+", "", value)

def image_from_detail(session: requests.Session, page_url: str, channel_name: str) -> tuple[str, bytes, str]:
    response = session.get(page_url, timeout=35)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    candidates = []
    for img in soup.find_all("img"):
        src = img.get("src") or img.get("data-src") or img.get("data-lazy-src")
        if src:
            absolute = urljoin(page_url, src)
            if "/channels/" in urlparse(absolute).path.lower():
                candidates.append(absolute)
    for anchor in soup.find_all("a", href=True):
        absolute = urljoin(page_url, anchor["href"])
        path = urlparse(absolute).path.lower()
        if "/channels/" in path and path.endswith((".webp", ".png", ".jpg", ".jpeg")):
            candidates.append(absolute)
    for candidate in dict.fromkeys(candidates):
        try:
            # CanliTV occasionally returns its generic Show TV image as a fallback
            # on unrelated channel pages. Never treat that fallback as a real match.
            filename = Path(urlparse(candidate).path).name.casefold()
            if filename == "show-tv.webp" and norm(channel_name) != norm("Show TV"):
                continue
            image_response = session.get(candidate, timeout=35)
            image_response.raise_for_status()
            image = Image.open(BytesIO(image_response.content))
            image.verify()
            image = Image.open(BytesIO(image_response.content))
            if image.width >= 8 and image.height >= 8:
                return candidate, image_response.content, (image.format or "WEBP").lower()
        except Exception:
            continue
    raise ValueError("Página individual sem imagem própria válida (fallbacks genéricos descartados)")

def main() -> None:
    session = requests.Session()
    session.headers.update({"User-Agent": "Mozilla/5.0 (compatible; PlaylistLogoCollector/1.0)"})
    playlist = PLAYLIST.read_text(encoding="utf-8")
    names = re.findall(r'^#EXTINF:[^\n]*?\btvg-name="([^"]+)"', playlist, re.M)
    if len(names) != 211:
        raise RuntimeError(f"Esperados 211 canais em Tv.m3u; encontrados {len(names)}")

    response = session.get(INDEX, timeout=45)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    channel_pages: dict[str, str] = {}
    for row in soup.find_all("tr"):
        for anchor in row.find_all("a", href=True):
            href = urljoin(BASE, anchor["href"])
            if "/frekans-bilgileri/" not in urlparse(href).path:
                continue
            key = norm(anchor.get_text(" ", strip=True))
            if key:
                channel_pages.setdefault(key, href)

    source_by_channel = {}
    report = []
    used_image_urls = set()
    ORIGINALS.mkdir(parents=True, exist_ok=True)
    for index, name in enumerate(names, 1):
        page = channel_pages.get(norm(name))
        if not page:
            report.append({"number": index, "channel": name, "status": "not_listed", "page_url": "", "image_url": "", "local_file": ""})
            continue
        try:
            image_url, image_bytes, image_format = image_from_detail(session, page, name)
            if image_url in used_image_urls:
                raise ValueError("Imagem repetida em outro canal; possível fallback genérico descartado")
            used_image_urls.add(image_url)
            safe_name = re.sub(r"[^A-Za-z0-9._-]+", "-", unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()).strip("-._") or f"canal-{index:03d}"
            image_path = ORIGINALS / f"{index:03d}-{safe_name}.{image_format}"
            image_path.write_bytes(image_bytes)
            source_by_channel[name.casefold()] = image_url
            report.append({"number": index, "channel": name, "status": "image_found", "page_url": page, "image_url": image_url, "local_file": str(image_path.relative_to(ROOT))})
        except Exception as error:
            report.append({"number": index, "channel": name, "status": "image_unavailable", "page_url": page, "image_url": str(error), "local_file": ""})
        time.sleep(0.15)

    if not source_by_channel:
        raise RuntimeError("Nenhuma imagem de canal foi extraída do CanliTV; catálogo não será alterado.")

    catalog = CATALOG.read_text(encoding="utf-8")
    pattern = re.compile(r"^(\|\s*)(.*?)(\s*\|\s*!\[[^\]]*\]\()([^)]*)(\)\s*\|\s*)$")
    output = []
    replaced = set()
    for line in catalog.splitlines():
        match = pattern.match(line)
        if match and match.group(2).strip().casefold() in source_by_channel:
            channel = match.group(2).strip().casefold()
            line = f"{match.group(1)}{match.group(2)}{match.group(3)}{source_by_channel[channel]}{match.group(5)}"
            replaced.add(channel)
        output.append(line)
    CATALOG.write_text("\n".join(output) + "\n", encoding="utf-8")

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    with REPORT.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["number", "channel", "status", "page_url", "image_url", "local_file"])
        writer.writeheader()
        writer.writerows(report)
    found = sum(row["status"] == "image_found" for row in report)
    unavailable = sum(row["status"] == "image_unavailable" for row in report)
    absent = sum(row["status"] == "not_listed" for row in report)
    print(f"CanliTV: {found}/211 imagens originais próprias baixadas em {ORIGINALS.relative_to(ROOT)}; {unavailable} páginas sem imagem válida; {absent} canais não listados; {len(replaced)} fontes registradas no catálogo.")

if __name__ == "__main__":
    main()
