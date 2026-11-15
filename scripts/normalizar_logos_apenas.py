#!/usr/bin/env python3
"""Normalize every available TV channel logo to a square black-background PNG."""
import hashlib
import io
import time
import re
import unicodedata
import urllib.parse
import urllib.request
from pathlib import Path

from PIL import Image

# Execução solicitada: reaplicar o padrão PNG 256x256 com fundo preto a todas as entradas.
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
    return re.sub(r"[^a-zA-Z0-9]+", "-", value).strip("-").lower() or "canal"

def http_bytes(url):
    if not url or not url.startswith(("http://", "https://")):
        return None
    for attempt in range(1, 4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 IPTV-LogoBot"})
            with urllib.request.urlopen(req, timeout=25) as response:
                data = response.read(8 * 1024 * 1024 + 1)
            if len(data) <= 8 * 1024 * 1024:
                return data
            print(f"Arquivo acima de 8 MB ignorado: {url}")
            return None
        except Exception as exc:
            print(f"Tentativa {attempt}/3 falhou ({url}): {exc}")
            if attempt < 3:
                time.sleep(attempt * 2)
    return None

def decode_image(data):
    if not data:
        return None
    try:
        return Image.open(io.BytesIO(data)).convert("RGBA")
    except Exception:
        if b"<svg" in data[:4096].lower():
            try:
                import cairosvg
                png = cairosvg.svg2png(bytestring=data, output_width=900)
                return Image.open(io.BytesIO(png)).convert("RGBA")
            except Exception:
                pass
    return None

def fetch_image(url):
    return decode_image(http_bytes(url))

_TV_LOGO_INDEX = None

def normalize_name(value):
    value = unicodedata.normalize("NFKD", value or "").casefold()
    value = "".join(c for c in value if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", "", value)

def http_json(url):
    data = http_bytes(url)
    if not data:
        raise RuntimeError("resposta vazia")
    import json
    return json.loads(data.decode("utf-8"))

def tv_logo_candidate(name):
    global _TV_LOGO_INDEX
    try:
        if _TV_LOGO_INDEX is None:
            tree = http_json("https://api.github.com/repos/tv-logo/tv-logos/git/trees/main?recursive=1")
            _TV_LOGO_INDEX = [
                item["path"] for item in tree.get("tree", [])
                if item.get("type") == "blob"
                and item["path"].lower().endswith((".png", ".jpg", ".jpeg", ".webp", ".svg"))
            ]
        target = normalize_name(name)
        if len(target) < 3:
            return None
        matches = []
        for path in _TV_LOGO_INDEX:
            stem = normalize_name(Path(path).stem)
            if stem in (target, target + "tr", "tr" + target):
                matches.append(path)
        if not matches:
            return None
        matches.sort(key=lambda p: ("/countries/turkey/" not in p.lower(), len(p)))
        return "https://raw.githubusercontent.com/tv-logo/tv-logos/refs/heads/main/" + urllib.parse.quote(matches[0])
    except Exception as exc:
        print(f"Catálogo de logos indisponível para {name}: {exc}")
        return None

def commons_candidate(name):
    try:
        query = urllib.parse.urlencode({
            "action": "query", "generator": "search",
            "gsrsearch": f'filetype:bitmap "{name}" television channel logo',
            "gsrnamespace": 6, "gsrlimit": 12,
            "prop": "imageinfo", "iiprop": "url", "format": "json"
        })
        data = http_json("https://commons.wikimedia.org/w/api.php?" + query)
        target = normalize_name(name)
        ranked = []
        for page in data.get("query", {}).get("pages", {}).values():
            title = page.get("title", "").rsplit(":", 1)[-1]
            stem = normalize_name(re.sub(r"\.[^.]+$", "", title))
            if stem == target or stem.startswith(target) or target in stem:
                info = (page.get("imageinfo") or [{}])[0]
                if info.get("url"):
                    ranked.append((0 if stem == target else 1, info["url"]))
        ranked.sort(key=lambda item: item[0])
        return ranked[0][1] if ranked else None
    except Exception as exc:
        print(f"Busca Wikimedia indisponível para {name}: {exc}")
        return None

def search_online_logo(name):
    for url in (tv_logo_candidate(name), commons_candidate(name)):
        image = fetch_image(url) if url else None
        if image is not None:
            print(f"Logo localizado para {name}: {url}")
            return image
    return None

def save_square_black(source, destination):
    # Ícone quadrado 256x256, fundo preto e logo inteiro sem cortar.
    canvas = Image.new("RGBA", (256, 256), (0, 0, 0, 255))
    source.thumbnail((216, 216), Image.Resampling.LANCZOS)
    x = (256 - source.width) // 2
    y = (256 - source.height) // 2
    canvas.alpha_composite(source, (x, y))

    # Recorta o próprio quadrado preto com cantos arredondados,
    # seguindo o estilo dos ícones de TV8 mostrados pelo usuário.
    from PIL import ImageDraw
    mask = Image.new("L", (256, 256), 0)
    ImageDraw.Draw(mask).rounded_rectangle(
        (0, 0, 255, 255), radius=42, fill=255
    )
    canvas.putalpha(mask)
    canvas.save(destination, format="PNG", optimize=True)

    # Validação pós-gravação: não publica arquivo corrompido ou fora do padrão.
    with Image.open(destination) as check:
        check.load()
        if check.format != "PNG" or check.size != (256, 256) or check.mode != "RGBA":
            raise RuntimeError(f"PNG fora do padrão após gravação: {destination.name}")
        if check.getpixel((0, 0))[3] != 0:
            raise RuntimeError(f"Canto arredondado inválido: {destination.name}")
        if check.getpixel((8, 128))[:3] != (0, 0, 0):
            raise RuntimeError(f"Fundo preto ausente: {destination.name}")

# Reprocessamento solicitado: aplicar novamente o padrão visual do canal TRT Çocuk a todas as logos.
def main():
    if not PLAYLIST.exists():
        raise SystemExit("Tv.m3u8 não encontrado.")
    LOGO_DIR.mkdir(parents=True, exist_ok=True)
    lines = PLAYLIST.read_text(encoding="utf-8").splitlines()
    output = []
    converted = skipped = 0

    for line in lines:
        if not line.startswith("#EXTINF"):
            output.append(line)
            continue

        prefix, comma, display = line.rpartition(",")
        attrs = dict(ATTR.findall(prefix))
        name = attrs.get("tvg-name") or display.strip()
        old_logo = attrs.get("tvg-logo", "")
        identity = attrs.get("tvg-id") or name or display.strip()
        digest = hashlib.sha1(identity.casefold().encode("utf-8")).hexdigest()[:10]
        filename = f"{safe_name(identity)[:54]}-{digest}.png"
        destination = LOGO_DIR / filename

        # Processa também logos que já terminam em .png: o objetivo é padronizar
        # o visual de todos, não apenas converter extensões diferentes.
        source = fetch_image(old_logo)
        if source is None:
            source = search_online_logo(name)

        if source is None:
            skipped += 1
            print(f"FONTE NÃO ENCONTRADA — logo preservada: {name}")
            output.append(line)
            continue

        save_square_black(source, destination)
        new_url = f"{RAW_BASE}/{filename}"
        if re.search(r'\btvg-logo="[^"]*"', prefix):
            prefix = re.sub(r'\btvg-logo="[^"]*"', f'tvg-logo="{new_url}"', prefix, count=1)
        else:
            prefix += f' tvg-logo="{new_url}"'
        output.append(prefix + comma + display)
        converted += 1
        print(f"PNG quadrado 256x256 com fundo preto: {name}")

    PLAYLIST.write_text("\n".join(output) + "\n", encoding="utf-8")
    print(f"FINAL: {converted} logos padronizados; {skipped} sem imagem-fonte confiável e preservados.")

if __name__ == "__main__":
    main()
