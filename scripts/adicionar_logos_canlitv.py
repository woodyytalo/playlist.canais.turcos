from collections import Counter, deque
from io import BytesIO
from pathlib import Path
from urllib.request import Request, urlopen

from PIL import Image

ROOT = Path("logos-turcas-catalogo/TODAS-LOGOS-NA-ORDEM/PNG-512-CENTRALIZADAS")
SOURCES = {
    "015.png": "https://tr.canlitv.watch/channels/aras-tv.webp",
    "046.png": "https://tr.canlitv.watch/channels/erciyes-tv.png",
    "057.png": "https://tr.canlitv.watch/channels/grt-tv-izle.webp",
    "064.png": "https://tr.canlitv.watch/channels/hunat-tv.webp",
    "095.png": "https://tr.canlitv.watch/channels/life-tv.png",
    "130.png": "https://tr.canlitv.watch/channels/ton-tv.webp",
    "171.png": "https://tr.canlitv.watch/channels/ekol-tv-izle.webp",
}


def remove_border_background(image):
    image = image.convert("RGBA")
    pixels = image.load()
    width, height = image.size

    # Detect the most common opaque color around the image border.
    border = []
    for x in range(width):
        border.extend((pixels[x, 0], pixels[x, height - 1]))
    for y in range(height):
        border.extend((pixels[0, y], pixels[width - 1, y]))
    opaque = [p for p in border if p[3] > 0]
    if not opaque:
        return image
    quantized = Counter(tuple((c // 16) * 16 for c in p[:3]) for p in opaque)
    bg = max(quantized, key=quantized.get)

    # Remove only pixels connected to the outer edge and close to its dominant
    # background color; internal dark/light logo details remain intact.
    seen = bytearray(width * height)
    queue = deque()
    for x in range(width):
        queue.append((x, 0))
        queue.append((x, height - 1))
    for y in range(height):
        queue.append((0, y))
        queue.append((width - 1, y))

    while queue:
        x, y = queue.popleft()
        idx = y * width + x
        if seen[idx]:
            continue
        seen[idx] = 1
        r, g, b, a = pixels[x, y]
        if a == 0:
            continue
        if max(abs(r - bg[0]), abs(g - bg[1]), abs(b - bg[2])) <= 38:
            pixels[x, y] = (r, g, b, 0)
            if x: queue.append((x - 1, y))
            if x + 1 < width: queue.append((x + 1, y))
            if y: queue.append((x, y - 1))
            if y + 1 < height: queue.append((x, y + 1))
    return image


def main():
    ROOT.mkdir(parents=True, exist_ok=True)
    for filename, url in SOURCES.items():
        request = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urlopen(request, timeout=30) as response:
            payload = response.read()
        source = Image.open(BytesIO(payload))
        source.load()
        source = remove_border_background(source)
        alpha = source.getchannel("A")
        bbox = alpha.getbbox()
        if not bbox:
            raise RuntimeError(f"Imagem sem conteúdo visível: {filename}")
        source = source.crop(bbox)
        source.thumbnail((460, 460), Image.Resampling.LANCZOS)
        canvas = Image.new("RGBA", (512, 512), (0, 0, 0, 0))
        canvas.alpha_composite(source, ((512 - source.width) // 2, (512 - source.height) // 2))
        canvas.save(ROOT / filename, format="PNG", optimize=True)
        print(f"Atualizada: {ROOT / filename}")


if __name__ == "__main__":
    main()
