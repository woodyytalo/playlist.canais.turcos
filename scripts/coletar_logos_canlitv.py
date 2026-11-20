#!/usr/bin/env python3
"""Replace catalog sources with the exact channel images exposed by CanliTV pages."""
from __future__ import annotations
import csv, re, time, unicodedata
from pathlib import Path
from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO

ROOT = Path(__file__).resolve().parents[1]
PLAYLIST = ROOT / "Tv.m3u"
CATALOG = ROOT / "logos-turcas-catalogo" / "CATALOGO-UNIFICADO.md"
REPORT = ROOT / "logos-turcas-catalogo" / "canlitv-images-report.csv"
INDEX = "https://tr.canlitv.watch/frekans-bilgileri"
BASE = "https://tr.canlitv.watch"

def norm(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    value = value.upper().replace("&", " AND ")
    value = re.sub(r"\b(HD|SD|UHD|4K)\b", " ", value)
    value = re.sub(r"\bTV\b$", " ", value)
    value = re.sub(r"[^A-Z0-9]+", "", value)
    return value

def image_from_detail(session: requests.Session, page_url: str) -> str:
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
            image_response = session.get(candidate, timeout=35)
            image_response.raise_for_status()
            image = Image.open(BytesIO(image_response.content))
            image.verify()
            if image.width >= 8 and image.height >= 8:
                return candidate
        except Exception:
            continue
    raise ValueError("Página individual sem imagem de canal válida")

def main() -> None:
    session = requests.Session()
    session.headers.update({"User-Agent": "Mozilla/5.0 (compatible; PlaylistLogoCollector/1.0)"})
    playlist = PLAYLIST.read_text(encoding="utf-8")
    names = re.findall(r'^#EXTINF:[^\\n]*?\\btvg-name="([^"]+)"', playlist, re.M)
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
            label = anchor.get_text(" ", strip=True)
            key = norm(label)
            if key:
                channel_pages.setdefault(key, href)

    catalog = CATALOG.read_text(encoding="utf-8")
    source_by_channel = {}
    report = []
    for index, name in enumerate(names, 1):
        key = norm(name)
        page = channel_pages.get(key)
        if not page:
            report.append({"number": index, "channel": name, "status": "not_listed", "page_url": "", "image_url": ""})
            continue
        try:
            image_url = image_from_detail(session, page)
            source_by_channel[name.casefold()] = image_url
            report.append({"number": index, "channel": name, "status": "image_found", "page_url": page, "image_url": image_url})
        except Exception as error:
            report.append({"number": index, "channel": name, "status": "image_unavailable", "page_url": page, "image_url": str(error)})
        time.sleep(0.15)

    if not source_by_channel:
        raise RuntimeError("Nenhuma imagem de canal foi extraída do CanliTV; catálogo não será alterado.")

    updated = []
    pattern = re.compile(r"^(\\|\\s*)(.*?)(\\s*\\|\\s*!\\[[^\\]]*\\]\\()([^)]*)(\\)\\s*\\|\\s*)$")
    for line in catalog.splitlines():
        match = pattern.match(line)
        if match:
            channel = match.group(2).strip().casefold()
            if channel in source_by_channel:
                url = source_by_channel[channel]
                line = f"{match.group(1)}{match.group(2)}{match.group(3)}{url}{match.group(5)}"
                updated.append(channel)
        # Keep every non-matching catalog line unchanged.
        if not match:
            pass
    # Apply replacements by exact channel row without changing table order or other sections.
    lines = catalog.splitlines()
    output = []
    for line in lines:
        match = pattern.match(line)
        if match and match.group(2).strip().casefold() in source_by_channel:
            channel = match.group(2).strip().casefold()
            line = f"{match.group(1)}{match.group(2)}{match.group(3)}{source_by_channel[channel]}{match.group(5)}"
        output.append(line)
    CATALOG.write_text("\\n".join(output) + "\\n", encoding="utf-8")

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    with REPORT.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["number", "channel", "status", "page_url", "image_url"])
        writer.writeheader()
        writer.writerows(report)
    found = sum(row["status"] == "image_found" for row in report)
    unavailable = sum(row["status"] == "image_unavailable" for row in report)
    absent = sum(row["status"] == "not_listed" for row in report)
    print(f"CanliTV: {found}/211 imagens encontradas; {unavailable} páginas sem imagem válida; {absent} canais não listados.")
    if found == 0:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
