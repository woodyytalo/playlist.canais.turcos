from collections import Counter, deque
from io import BytesIO
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.parse import urlparse

from PIL import Image, ImageFilter

PREFIX = Path("logos-turcas-catalogo/TODAS-LOGOS-NA-ORDEM/PNG-512-CENTRALIZADAS")

# Apenas arquivos de logo encontrados no próprio Canlı TV.
# Os demais canais desta lista ficam sem PNG para que o catálogo mostre somente o nome.
OFFICIAL_CANLITV = {
    15: ("015-ARAS-TV-d1ed7e4a71.png", "https://tr.canlitv.watch/channels/aras-tv.webp"),
    46: ("046-Erciyes-TV-84ea50b105.png", "https://tr.canlitv.watch/channels/erciyes-tv.png"),
    57: ("057-GRT-Gaziantep-TV-ac1e9bcdac.png", "https://tr.canlitv.watch/channels/grt-tv-izle.webp"),
    64: ("064-Hunat-TV-16147a9bbd.png", "https://tr.canlitv.watch/channels/hunat-tv.webp"),
    95: ("095-Life-TV-b132683ac4.png", "https://tr.canlitv.watch/channels/life-tv.png"),
    130: ("130-Ton-TV-8bb0657442.png", "https://tr.canlitv.watch/channels/ton-tv.webp"),
    171: ("171-Ekol-TV-c67310c229.png", "https://tr.canlitv.watch/channels/ekol-tv-izle.webp"),
}

REVIEWED_POSITIONS = {
    11, 15, 18, 27, 38, 46, 47, 49, 51, 57, 59, 64, 67, 72, 78, 79,
    88, 93, 95, 130, 151, 169, 171, 174, 179, 187, 190, 191, 201, 204, 206,
}


def remove_flat_edge_background(image):
    image = image.convert("RGBA")
    w, h = image.size
    if w < 2 or h < 2:
        return image

    px = image.load()
    border = []
    for x in range(w):
        border.extend((px[x, 0], px[x, h - 1]))
    for y in range(1, h - 1):
        border.extend((px[0, y], px[w - 1, y]))

    opaque = [p[:3] for p in border if p[3] >= 245]
    if not opaque:
        return image

    bg = Counter(opaque).most_common(1)[0][0]
    # Só remove fundo uniforme conectado às bordas; não apaga áreas internas da marca.
    seeds = []
    for x in range(w):
        seeds.extend(((x, 0), (x, h - 1)))
    for y in range(1, h - 1):
        seeds.extend(((0, y), (w - 1, y)))

    seen = bytearray(w * h)
    q = deque()
    for x, y in seeds:
        i = y * w + x
        if seen[i]:
            continue
        seen[i] = 1
        r, g, b, a = px[x, y]
        if a >= 245 and max(abs(r-bg[0]), abs(g-bg[1]), abs(b-bg[2])) <= 32:
            q.append((x, y))

    while q:
        x, y = q.popleft()
        r, g, b, a = px[x, y]
        if a and max(abs(r-bg[0]), abs(g-bg[1]), abs(b-bg[2])) <= 38:
            px[x, y] = (r, g, b, 0)
            for nx, ny in ((x-1,y), (x+1,y), (x,y-1), (x,y+1)):
                if 0 <= nx < w and 0 <= ny < h:
                    i = ny * w + nx
                    if not seen[i]:
                        seen[i] = 1
                        q.append((nx, ny))
    return image


def download_logo(url):
    parsed = urlparse(url)
    if parsed.scheme != "https" or parsed.hostname != "tr.canlitv.watch":
        raise ValueError(f"Fonte não permitida: {url}")
    req = Request(url, headers={"User-Agent": "Mozilla/5.0 (compatible; LogoCatalog/1.0)"})
    with urlopen(req, timeout=30) as response:
        final_host = urlparse(response.geturl()).hostname
        if final_host != "tr.canlitv.watch":
            raise ValueError(f"Redirecionamento para domínio não permitido: {response.geturl()}")
        raw = response.read()
    with Image.open(BytesIO(raw)) as source:
        image = source.convert("RGBA")
    image = remove_flat_edge_background(image)
    bbox = image.getbbox()
    if not bbox:
        raise ValueError(f"Logo vazia: {url}")
    image = image.crop(bbox)
    image.thumbnail((460, 460), Image.Resampling.LANCZOS)
    image = image.filter(ImageFilter.UnsharpMask(radius=0.8, percent=110, threshold=3))
    canvas = Image.new("RGBA", (512, 512), (0, 0, 0, 0))
    canvas.alpha_composite(image, ((512-image.width)//2, (512-image.height)//2))
    return canvas


PREFIX.mkdir(parents=True, exist_ok=True)

# Remove versões antigas (inclusive duplicatas numéricas) somente dos 31 canais auditados.
for path in PREFIX.glob("*.png"):
    try:
        number = int(path.name[:3])
    except ValueError:
        continue
    if number in REVIEWED_POSITIONS:
        path.unlink()

saved = []
for number, (filename, url) in OFFICIAL_CANLITV.items():
    image = download_logo(url)
    image.save(PREFIX / filename, "PNG", optimize=True)
    saved.append(filename)

print(f"Logos oficiais do Canlı TV baixadas e centralizadas: {len(saved)}")
print("Canais sem logo confirmada no Canlı TV: somente nome, sem imagem substituta.")
print("\\n".join(saved))
