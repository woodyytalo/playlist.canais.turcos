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
        raise RuntimeError(f"Logo sem pixels visíveis: {svg.name}")
    im = im.crop(bbox)
    im.thumbnail((460, 460), Image.Resampling.LANCZOS)
    canvas = Image.new("RGBA", (512, 512), (0, 0, 0, 0))
    canvas.alpha_composite(im, ((512-im.width)//2, (512-im.height)//2))
    canvas.save(target / (svg.stem + ".png"), optimize=True)

print(f"Geradas {len(files)} imagens PNG de 512x512, centralizadas.")
