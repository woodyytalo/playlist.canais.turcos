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


# Padroniza também as logos efetivamente usadas pela playlist principal.
# A referência é assets/logos/017-atv.png: 512x482 pixels.
from pathlib import Path as _Path
from PIL import Image as _Image

_assets = _Path("assets/logos")
_reference = _Image.open(_assets / "017-atv.png")
_target_size = _reference.size
_processed = 0

for _file in sorted(_assets.glob("*.png")):
    with _Image.open(_file) as _source:
        _im = _source.convert("RGBA")
        _im.thumbnail(_target_size, _Image.Resampling.LANCZOS)
        _canvas = _Image.new("RGBA", _target_size, (0, 0, 0, 0))
        _canvas.alpha_composite(_im, ((_target_size[0] - _im.width) // 2, (_target_size[1] - _im.height) // 2))
        _canvas.save(_file, format="PNG", optimize=True)
        _processed += 1

print(f"Padronizadas {_processed} logos em {_target_size[0]}x{_target_size[1]} pixels.")
