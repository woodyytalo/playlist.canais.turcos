#!/usr/bin/env python3
"""Substitui cartões genéricos por logos reais identificadas para canais da Tv.m3u."""
from io import BytesIO
from pathlib import Path
from urllib.request import Request, urlopen
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "logos-turcas-catalogo" / "TODAS-LOGOS-NA-ORDEM" / "PNG-512-CENTRALIZADAS"

# Fontes identificadas para os canais correspondentes; nenhuma arte é criada.
LOGOS = {
    "014-Anadolu-TV-fc2e70f890.png": "https://canlitv.com/kanal/logo/13394.jpg",
    "184-MADINAH-TV-7d10e449b9.png": "https://aloula.faulio.com/storage/mediagallery/33/92/fullhd_879e557011826f507a045b4e0b4c3b57ba93edae.png",
    "202-IQ-Channel-8da53c150e.png": "https://i.imgur.com/hwuaomt.png",
}

def download(url):
    req = Request(url, headers={"User-Agent": "Mozilla/5.0 (compatible; ChannelLogoUpdater/1.0)"})
    with urlopen(req, timeout=30) as response:
        data = response.read(12 * 1024 * 1024)
    image = Image.open(BytesIO(data)).convert("RGBA")
    image.load()
    return image

def normalize(image):
    # Remove somente margens totalmente transparentes; mantém fundos opacos originais.
    bbox = image.getchannel("A").getbbox()
    if bbox:
        image = image.crop(bbox)
    image.thumbnail((460, 460), Image.Resampling.LANCZOS)
    canvas = Image.new("RGBA", (512, 512), (0, 0, 0, 0))
    canvas.alpha_composite(image, ((512 - image.width) // 2, (512 - image.height) // 2))
    return canvas

def main():
    if not TARGET.is_dir():
        raise SystemExit(f"Pasta de logos não encontrada: {TARGET}")
    for filename, url in LOGOS.items():
        path = TARGET / filename
        if not path.is_file():
            raise SystemExit(f"Arquivo de destino não encontrado: {path}")
        image = normalize(download(url))
        image.save(path, format="PNG", optimize=True)
        print(f"Logo original atualizada: {filename} <- {url}")

if __name__ == "__main__":
    main()
