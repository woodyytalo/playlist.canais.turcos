#!/usr/bin/env python3
"""Gera emblemas 2D padronizados para todos os canais de Tv.m3u, sem alterar a playlist."""
import json
import re
import unicodedata
import zipfile
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

PLAYLIST = Path("Tv.m3u")
OUT = Path("artifacts/logos-todos-canais")
SIZE = 512
RED_DARK = (105, 8, 22)
RED_MID = (174, 15, 34)
RED_LIGHT = (224, 48, 57)
WHITE = (255, 248, 244)
SILVER = (236, 229, 224)

def font(size, bold=True):
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
    ]
    for path in candidates:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()

def slugify(value):
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii").lower()
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return value or "canal"

def monogram(name):
    cleaned = re.sub(r"[^\w\s]", " ", name, flags=re.UNICODE).strip()
    words = cleaned.split()
    if not words:
        return "TV"
    if len(words) == 1:
        token = words[0]
        return token[:3].upper()
    # Preserve channel numbers and short alphanumeric brands such as 4U.
    first = words[0].upper()
    if len(first) <= 3 and any(ch.isdigit() for ch in first):
        return first[:3]
    letters = "".join(w[0] for w in words if w)
    return letters[:3].upper() or "TV"

def wrap_name(draw, name, fnt, max_width):
    words = name.split()
    lines, current = [], ""
    for word in words:
        candidate = (current + " " + word).strip()
        if draw.textbbox((0, 0), candidate, font=fnt)[2] <= max_width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines[:3]

def render(name, output):
    im = Image.new("RGB", (SIZE, SIZE))
    px = im.load()
    # Metallic red brushed finish: smooth red field with restrained horizontal bands.
    for y in range(SIZE):
        vertical = 0.90 + 0.13 * (1 - abs(y - SIZE * 0.43) / (SIZE * 0.72))
        for x in range(SIZE):
            band = 1.0 + 0.045 * (0.5 + 0.5 * __import__("math").sin(y * 0.19))
            edge = 0.92 + 0.08 * (1 - abs(x - SIZE / 2) / (SIZE / 2))
            k = vertical * band * edge
            px[x, y] = tuple(max(0, min(255, int(c * k))) for c in RED_MID)
    d = ImageDraw.Draw(im, "RGBA")
    # Traditional flat plaque framing; no bevel, extrusion, shadow or 3D treatment.
    d.rounded_rectangle((13, 13, 499, 499), radius=30, outline=(255, 224, 220, 220), width=4)
    d.rounded_rectangle((23, 23, 489, 489), radius=24, outline=(75, 0, 12, 180), width=2)
    d.line((38, 74, 474, 74), fill=(255, 225, 220, 105), width=2)
    d.line((38, 438, 474, 438), fill=(70, 0, 12, 130), width=2)
    # Fine horizontal metallic strokes.
    for y in range(92, 425, 9):
        d.line((34, y, 478, y), fill=(255, 210, 205, 12), width=1)

    # Left wordmark, sized to keep long channel names readable.
    max_w = 252
    size = 54
    while size > 25:
        fnt = font(size)
        lines = wrap_name(d, name, fnt, max_w)
        if len(lines) <= 3 and max(d.textbbox((0, 0), line, font=fnt)[2] for line in lines) <= max_w:
            break
        size -= 2
    fnt = font(size)
    lines = wrap_name(d, name, fnt, max_w)
    line_h = size + 13
    total_h = line_h * len(lines)
    y = (SIZE - total_h) // 2
    for line in lines:
        bbox = d.textbbox((0, 0), line, font=fnt, stroke_width=0)
        tw = bbox[2] - bbox[0]
        d.text((42, y), line, font=fnt, fill=WHITE, stroke_width=1, stroke_fill=(75, 0, 12, 180))
        y += line_h

    # Flat traditional medallion with a custom channel monogram.
    d.ellipse((318, 145, 472, 299), fill=(92, 3, 18, 95), outline=(255, 242, 235, 235), width=5)
    d.ellipse((328, 155, 462, 289), outline=(255, 214, 208, 185), width=2)
    mark = monogram(name)
    mark_size = 62 if len(mark) <= 2 else 48
    mf = font(mark_size)
    mb = d.textbbox((0, 0), mark, font=mf)
    mw, mh = mb[2] - mb[0], mb[3] - mb[1]
    d.text((395 - mw / 2, 222 - mh / 2 - mb[1]), mark, font=mf, fill=(255, 255, 255, 255))
    # Small identifying divider.
    d.line((302, 176, 302, 336), fill=(255, 229, 220, 170), width=2)
    d.text((SIZE // 2, 463), "TURKISH CHANNEL COLLECTION", anchor="mm", font=font(13, False), fill=(255, 235, 230, 210))
    im.save(output, "PNG", optimize=True)

def main():
    if not PLAYLIST.exists():
        raise SystemExit("Tv.m3u não foi encontrado na raiz do repositório.")
    names = []
    for line in PLAYLIST.read_text(encoding="utf-8-sig").splitlines():
        if line.startswith("#EXTINF:"):
            match = re.search(r'tvg-name="([^"]+)"', line)
            name = match.group(1).strip() if match else line.rsplit(",", 1)[-1].strip()
            if name and name not in names:
                names.append(name)
    if not names:
        raise SystemExit("Nenhum canal foi encontrado em Tv.m3u.")
    OUT.mkdir(parents=True, exist_ok=True)
    manifest = []
    for index, name in enumerate(names, 1):
        filename = f"{slugify(name)}.png"
        target = OUT / filename
        render(name, target)
        manifest.append({"number": index, "name": name, "file": filename, "size": "512x512", "format": "PNG"})
        print(f"[{index}/{len(names)}] {name} -> {target}")
    (OUT / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    archive = Path("artifacts/logos-todos-canais.zip")
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(OUT.glob("*")):
            zf.write(path, arcname=path.name)
    print(f"Concluído: {len(names)} logos 512x512 PNG em {archive}.")
    print("A playlist Tv.m3u não foi modificada.")

if __name__ == "__main__":
    main()
