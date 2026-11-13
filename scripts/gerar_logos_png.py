#!/usr/bin/env python3
"""Create local PNG artwork for playlist entries whose logo is absent or not PNG.

Existing remote artwork is downloaded and converted where possible. If no usable
image exists, a clean text-based channel tile is generated on a black background.
The script never invents an official brand mark.
"""
import hashlib
import io
import re
import unicodedata
import urllib.request
from pathlib import Path
from urllib.parse import unquote

from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parents[1]
PLAYLIST = ROOT / "Tv.m3u8"
LOGO_DIR = ROOT / "assets" / "logos"
REPO = "woodyytalo/playlist.canais.turcos"
BRANCH = "github/workflows/atualizar-logos.yml"
RAW_BASE = f"https://raw.githubusercontent.com/{REPO}/{BRANCH}/assets/logos"

ATTR = re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')

def safe_name(value):
    value = unicodedata.normalize("NFKD", value or "")
    value = "".join(c for c in value if not unicodedata.combining(c))
    value = re.sub(r"[^a-zA-Z0-9]+", "-", value).strip("-").lower()
    return value or "canal"

def font(size, bold=True):
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold
        else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf",
    ]
    for candidate in candidates:
        try:
            return ImageFont.truetype(candidate, size)
        except OSError:
            pass
    return ImageFont.load_default()

def fetch_image(url):
    if not url or not url.startswith(("http://", "https://")):
        return None
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 IPTV-LogoBot"})
        with urllib.request.urlopen(req, timeout=18) as response:
            data = response.read(8 * 1024 * 1024 + 1)
        if len(data) > 8 * 1024 * 1024:
            return None
        try:
            return Image.open(io.BytesIO(data)).convert("RGBA")
        except Exception:
            # SVG sources are converted only when CairoSVG can parse them.
            if b"<svg" in data[:4096].lower():
                try:
                    import cairosvg
                    png = cairosvg.svg2png(bytestring=data, output_width=900)
                    return Image.open(io.BytesIO(png)).convert("RGBA")
                except Exception:
                    return None
            return None
    except Exception as exc:
        print(f"Imagem indisponível ({url}): {exc}")
        return None

def generated_tile(name, destination):
    canvas = Image.new("RGBA", (480, 270), (0, 0, 0, 255))
    draw = ImageDraw.Draw(canvas)
    draw.rounded_rectangle((12, 12, 468, 258), radius=24, outline=(75, 75, 75, 255), width=3)
    label = re.sub(r"\s+", " ", name).strip()
    f = font(48)
    while f.size > 22 and draw.textbbox((0, 0), label, font=f)[2] > 410:
        f = font(f.size - 2)
    bounds = draw.textbbox((0, 0), label, font=f)
    x = (480 - (bounds[2] - bounds[0])) / 2
    y = 112 - (bounds[3] - bounds[1]) / 2
    draw.text((x, y), label, font=f, fill=(245, 245, 245, 255), stroke_width=1, stroke_fill=(35, 35, 35, 255))
    sub = font(20, False)
    sub_text = "CANAL DE TV"
    sb = draw.textbbox((0, 0), sub_text, font=sub)
    draw.text(((480 - (sb[2] - sb[0])) / 2, 205), sub_text, font=sub, fill=(155, 155, 155, 255))
    canvas.convert("RGB").save(destination, format="PNG", optimize=True)

def save_png(source, destination):
    background = Image.new("RGBA", (480, 270), (0, 0, 0, 255))
    source.thumbnail((440, 230), Image.Resampling.LANCZOS)
    x = (480 - source.width) // 2
    y = (270 - source.height) // 2
    if source.mode == "RGBA":
        background.alpha_composite(source, (x, y))
    else:
        background.paste(source, (x, y))
    background.convert("RGB").save(destination, format="PNG", optimize=True)

def main():
    if not PLAYLIST.exists():
        raise SystemExit("Tv.m3u8 não encontrado.")
    LOGO_DIR.mkdir(parents=True, exist_ok=True)
    lines = PLAYLIST.read_text(encoding="utf-8").splitlines()
    output = []
    current = 0
    converted = generated = unchanged = 0

    for line in lines:
        if not line.startswith("#EXTINF"):
            output.append(line)
            continue

        display = line.rsplit(",", 1)[-1].strip()
        attrs = dict(ATTR.findall(line.split(",", 1)[0]))
        name = attrs.get("tvg-name") or display
        raw_logo = attrs.get("tvg-logo", "")
        # Already a repository PNG: leave it untouched.
        if raw_logo.startswith(RAW_BASE + "/") and raw_logo.lower().endswith(".png"):
            output.append(line)
            unchanged += 1
            continue
        if raw_logo.lower().endswith(".png") and raw_logo.startswith(("http://", "https://")):
            output.append(line)
            unchanged += 1
            continue

        identity = attrs.get("tvg-id") or name
        digest = hashlib.sha1(identity.casefold().encode("utf-8")).hexdigest()[:10]
        filename = f"{safe_name(identity)[:54]}-{digest}.png"
        destination = LOGO_DIR / filename

        source = fetch_image(raw_logo)
        if source is not None:
            save_png(source, destination)
            converted += 1
            print(f"Convertido para PNG: {name}")
        else:
            generated_tile(name, destination)
            generated += 1
            print(f"PNG de identificação criado: {name}")

        new_url = f"{RAW_BASE}/{filename}"
        prefix, comma, tail = line.partition(",")
        # Recover a tvg-id swallowed by an earlier malformed data-URI attribute.
        broken_id = re.search(r'\btvg-id="([^"]+)"', raw_logo)
        if broken_id and not re.search(r'\btvg-id="[^"]+"', prefix):
            prefix = prefix.replace('tvg-logo="' + raw_logo + '"', f'tvg-id="{broken_id.group(1)}"')
        if re.search(r'\btvg-logo="[^"]*"', prefix):
            prefix = re.sub(r'\btvg-logo="[^"]*"', f'tvg-logo="{new_url}"', prefix, count=1)
        else:
            prefix = re.sub(r'(\s+group-title=)', f' tvg-logo="{new_url}"\\1', prefix, count=1)
            if 'tvg-logo="' not in prefix:
                prefix += f' tvg-logo="{new_url}"'
        output.append(prefix + comma + tail)

    PLAYLIST.write_text("\n".join(output) + "\n", encoding="utf-8")
    print(f"Resultado: {converted} logos convertidos; {generated} PNGs gerados; {unchanged} PNGs existentes preservados.")

if __name__ == "__main__":
    main()
