from pathlib import Path
from PIL import Image
import cairosvg, io

source = Path("logos-turcas-catalogo/TODAS-LOGOS-NA-ORDEM")
target = source / "PNG-512-CENTRALIZADAS"
target.mkdir(parents=True, exist_ok=True)

files = sorted(source.glob("[0-9][0-9][0-9]-*.svg"))
if len(files) != 211:
    raise SystemExit(f"Esperadas 211 logos SVG; encontradas {len(files)}")

for svg in files:
    rendered = cairosvg.svg2png(url=str(svg), output_width=1536, output_height=1536)
    im = Image.open(io.BytesIO(rendered)).convert("RGBA")
    alpha = im.getchannel("A")
    bbox = alpha.getbbox()
    if not bbox:
        print(f"AVISO: SVG sem arte visível; gerando quadro transparente: {svg.name}")
        Image.new("RGBA", (512, 512), (0, 0, 0, 0)).save(target / (svg.stem + ".png"), optimize=True)
        continue
    im = im.crop(bbox)
    im.thumbnail((460, 460), Image.Resampling.LANCZOS)
    canvas = Image.new("RGBA", (512, 512), (0, 0, 0, 0))
    canvas.alpha_composite(im, ((512-im.width)//2, (512-im.height)//2))
    canvas.save(target / (svg.stem + ".png"), optimize=True)

print(f"Geradas {len(files)} imagens PNG de 512x512, centralizadas.")


# Diagnostico: logos cujo conteudo visivel e um retangulo predominantemente preto.
for png in sorted(target.glob("*.png")):
    im = Image.open(png).convert("RGBA")
    alpha = im.getchannel("A")
    bbox = alpha.getbbox()
    if not bbox:
        continue
    crop = im.crop(bbox)
    pixels = list(crop.getdata())
    visible = [(r, g, b) for r, g, b, a in pixels if a > 16]
    if not visible:
        continue
    black = sum(1 for r, g, b in visible if max(r, g, b) < 28)
    occupancy = len(visible) / (crop.width * crop.height)
    black_ratio = black / len(visible)
    aspect = max(crop.width, crop.height) / max(1, min(crop.width, crop.height))
    if black_ratio >= 0.92 and occupancy >= 0.72 and aspect >= 1.25:
        print(f"RETANGULO PRETO SUSPEITO: {png.name} | preto={black_ratio:.1%} | ocupacao={occupancy:.1%} | proporcao={aspect:.2f}")
