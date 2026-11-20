#!/usr/bin/env python3
"""Ajusta margens de PNGs sem alterar orientação, proporção ou desenho da marca."""
from collections import deque
from pathlib import Path
from PIL import Image

ROOT = Path("logos-ajustadas")
MAX_SIDE = 512
BLACK_LIMIT = 18


def remove_black_background_connected_to_edges(image: Image.Image) -> bool:
    """Remove somente preto conectado às bordas quando os quatro cantos são pretos."""
    width, height = image.size
    pixels = image.load()
    corners = [pixels[0, 0], pixels[width - 1, 0],
               pixels[0, height - 1], pixels[width - 1, height - 1]]
    if not all(a > 240 and max(r, g, b) <= BLACK_LIMIT
               for r, g, b, a in corners):
        return False

    seen = bytearray(width * height)
    queue = deque()

    def is_background(x, y):
        r, g, b, a = pixels[x, y]
        return a > 0 and max(r, g, b) <= BLACK_LIMIT

    def add(x, y):
        index = y * width + x
        if not seen[index] and is_background(x, y):
            seen[index] = 1
            queue.append((x, y))

    for x in range(width):
        add(x, 0)
        add(x, height - 1)
    for y in range(height):
        add(0, y)
        add(width - 1, y)

    removed = False
    while queue:
        x, y = queue.popleft()
        pixels[x, y] = (0, 0, 0, 0)
        removed = True
        for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
            if 0 <= nx < width and 0 <= ny < height:
                add(nx, ny)
    return removed


def process(path: Path) -> bool:
    try:
        image = Image.open(path).convert("RGBA")
    except Exception as exc:
        print(f"SKIP {path}: {exc}")
        return False

    original_size = image.size
    background_removed = remove_black_background_connected_to_edges(image)

    # Recorta exclusivamente el espaço transparente; não usa canvas quadrado.
    bbox = image.getchannel("A").getbbox()
    if not bbox:
        print(f"SKIP {path}: sem conteúdo visível")
        return False

    cropped = image.crop(bbox)
    width, height = cropped.size

    # Amplia ou reduz mantendo rigorosamente a proporção original do conteúdo.
    scale = MAX_SIDE / max(width, height)
    new_size = (max(1, round(width * scale)), max(1, round(height * scale)))
    if new_size != cropped.size:
        cropped = cropped.resize(new_size, Image.Resampling.LANCZOS)

    # O arquivo final mantém a proporção da logo; nenhuma rotação ou moldura.
    cropped.save(path, format="PNG", optimize=True)
    changed = background_removed or bbox != (0, 0, original_size[0], original_size[1]) or new_size != original_size
    if changed:
        print(f"FIXED {path}: {original_size} -> {cropped.size}; proporção preservada")
    else:
        print(f"OK {path}: sem alteração necessária")
    return changed


def main():
    if not ROOT.exists():
        raise SystemExit("Pasta logos-ajustadas não encontrada")
    files = sorted(ROOT.glob("*.png"))
    changed = sum(process(path) for path in files)
    print(f"TOTAL_ARQUIVOS={len(files)}")
    print(f"TOTAL_AJUSTADOS={changed}")


if __name__ == "__main__":
    main()
