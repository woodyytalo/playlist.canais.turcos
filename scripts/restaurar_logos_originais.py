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
restored = 0
removed_black = 0
for path in files:
    raw = git_bytes("show", f"{SOURCE_COMMIT}:{path}")
    with Image.open(BytesIO(raw)) as source:
        image = source.convert("RGBA")
    # Não inclui arquivos que sejam apenas um retângulo preto, sem desenho recuperável.
    visible = [pixel for pixel in image.getdata() if pixel[3] > 0]
    if not visible or all(max(pixel[:3]) <= 8 for pixel in visible):
        (TARGET / Path(path).name).unlink(missing_ok=True)
        removed_black += 1
        continue
    # Preserva a imagem integral; apenas padroniza e aplica nitidez moderada.
    image.thumbnail((460, 460), Image.Resampling.LANCZOS)
    image = image.filter(ImageFilter.UnsharpMask(radius=1.0, percent=125, threshold=3))
    canvas = Image.new("RGBA", (512, 512), (0, 0, 0, 0))
    canvas.alpha_composite(image, ((512-image.width)//2, (512-image.height)//2))
    canvas.save(TARGET / Path(path).name, "PNG", optimize=True)
    restored += 1
print(f"Restauradas e padronizadas {restored} imagens; descartados {removed_black} arquivos que eram apenas retângulos pretos.")
