from io import BytesIO
from pathlib import Path
import subprocess
from PIL import Image, ImageFilter

DELETION_COMMIT = "4575f7d3329e0c734bcbd854ffe0b3ca85afd99b"
SOURCE_COMMIT = "25e5bf2bca185cf86994734605334c369214bede"
PREFIX = "logos-turcas-catalogo/TODAS-LOGOS-NA-ORDEM/PNG-512-CENTRALIZADAS/"
TARGET = Path(PREFIX)

def git_bytes(*args):
    return subprocess.check_output(["git", *args])

deleted = git_bytes("diff-tree", "--no-commit-id", "--name-only", "-r", "--diff-filter=D", DELETION_COMMIT).decode().splitlines()
files = sorted(p for p in deleted if p.startswith(PREFIX) and p.lower().endswith(".png"))
if len(files) != 51:
    raise SystemExit(f"Esperadas 51 PNGs originais; encontradas {len(files)}")

TARGET.mkdir(parents=True, exist_ok=True)
for path in files:
    raw = git_bytes("show", f"{SOURCE_COMMIT}:{path}")
    with Image.open(BytesIO(raw)) as source:
        image = source.convert("RGBA")
    # Preserva a imagem integral; apenas padroniza e aplica nitidez moderada.
    image.thumbnail((460, 460), Image.Resampling.LANCZOS)
    image = image.filter(ImageFilter.UnsharpMask(radius=1.0, percent=125, threshold=3))
    canvas = Image.new("RGBA", (512, 512), (0, 0, 0, 0))
    canvas.alpha_composite(image, ((512-image.width)//2, (512-image.height)//2))
    canvas.save(TARGET / Path(path).name, "PNG", optimize=True)
print(f"Restauradas e padronizadas {len(files)} imagens originais em PNG 512x512.")
