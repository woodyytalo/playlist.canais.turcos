#!/usr/bin/env python3
"""Busca logos de emissoras na Wikimedia Commons e cria PNG quadrado 512x512."""
import hashlib, re, time
from pathlib import Path
from urllib.parse import quote
import requests
from PIL import Image

ROOT = Path(".")
PLAYLIST = ROOT / "Tv.m3u"
OUT = ROOT / "assets" / "logos"
RAW_BASE = "https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/assets/logos"
API = "https://commons.wikimedia.org/w/api.php"
SESSION = requests.Session()
SESSION.headers.update({"User-Agent": "PlaylistTurquiaLogoBot/1.0 (GitHub Actions)"})

def words(value):
    return re.findall(r"[a-z0-9]+", value.casefold())

def find_logo(name):
    params = {"action":"query","format":"json","generator":"search",
              "gsrsearch":f'"{name}" logo',"gsrnamespace":6,"gsrlimit":12,
              "prop":"imageinfo","iiprop":"url|size|extmetadata","iiurlwidth":1200}
    try:
        data = SESSION.get(API, params=params, timeout=25).json()
    except Exception as exc:
        print(f"Busca falhou para {name}: {exc}")
        return None
    target = set(words(name))
    candidates = []
    for page in ((data.get("query") or {}).get("pages") or {}).values():
        title = page.get("title", "")
        info = (page.get("imageinfo") or [{}])[0]
        if not info.get("thumburl") and not info.get("url"):
            continue
        title_words = set(words(title.replace("File:", "")))
        overlap = len(target & title_words) / max(1, len(target))
        logo_hint = any(x in title.casefold() for x in ("logo","logotype","wordmark","channel"))
        if overlap >= 0.65 and logo_hint:
            candidates.append((overlap + 0.18, info, title))
    if not candidates:
        return None
    candidates.sort(key=lambda x: x[0], reverse=True)
    return candidates[0][1], candidates[0][2]

def make_square(url, destination):
    from io import BytesIO
    response = SESSION.get(url, timeout=35)
    response.raise_for_status()
    image = Image.open(BytesIO(response.content)).convert("RGBA")
    image.thumbnail((440, 440), Image.Resampling.LANCZOS)
    canvas = Image.new("RGBA", (512, 512), (0, 0, 0, 255))
    canvas.alpha_composite(image, ((512-image.width)//2, (512-image.height)//2))
    canvas.convert("RGB").save(destination, "PNG", optimize=True)

def main():
    if not PLAYLIST.exists():
        raise SystemExit("Tv.m3u não encontrado; nenhuma playlist foi alterada.")
    OUT.mkdir(parents=True, exist_ok=True)
    lines = PLAYLIST.read_text(encoding="utf-8-sig").splitlines()
    changed = found = missed = 0
    attributions = []
    for i, line in enumerate(lines):
        if not line.startswith("#EXTINF:") or "," not in line:
            continue
        display = line.rsplit(",", 1)[1].strip()
        if not display:
            continue
        result = find_logo(display)
        if not result:
            missed += 1
            print(f"SEM LOGO CONFIRMADA: {display}")
            continue
        info, commons_title = result
        source = info.get("thumburl") or info.get("url")
        if not source:
            missed += 1
            continue
        key = hashlib.sha1(display.casefold().encode()).hexdigest()[:10]
        filename = (re.sub(r"[^a-z0-9]+", "-", display.casefold()).strip("-")[:45] or "canal") + f"-{key}.png"
        try:
            make_square(source, OUT / filename)
        except Exception as exc:
            missed += 1
            print(f"FALHA AO BAIXAR {display}: {exc}")
            continue
        logo_url = f"{RAW_BASE}/{quote(filename)}"
        if re.search(r'\btvg-logo="[^"]*"', line, re.I):
            new_line = re.sub(r'\btvg-logo="[^"]*"', f'tvg-logo="{logo_url}"', line, count=1, flags=re.I)
        else:
            new_line = line.replace("#EXTINF:", f'#EXTINF: tvg-logo="{logo_url}"', 1)
        if new_line != line:
            lines[i] = new_line
            changed += 1
        found += 1
        meta = info.get("extmetadata") or {}
        artist = re.sub("<[^>]+>", "", (meta.get("Artist") or {}).get("value", ""))
        license_name = re.sub("<[^>]+>", "", (meta.get("LicenseShortName") or {}).get("value", ""))
        attributions.append(f"{display} | {commons_title} | {artist} | {license_name} | {info.get('descriptionurl','')}")
        print(f"LOGO PREPARADA: {display}")
        time.sleep(0.4)
    if changed:
        PLAYLIST.write_text("\n".join(lines) + "\n", encoding="utf-8")
    if attributions:
        attr = OUT / "ATRIBUICOES.txt"
        previous = attr.read_text(encoding="utf-8") if attr.exists() else ""
        known = set(previous.splitlines())
        with attr.open("a", encoding="utf-8") as f:
            for item in attributions:
                if item not in known:
                    f.write(item + "\n")
    print(f"Resumo: {found} logos encontradas; {missed} sem correspondência segura; {changed} entradas atualizadas.")
    print("Formato aplicado: PNG 512x512, fundo preto, logo proporcional e centralizada.")

if __name__ == "__main__":
    main()
