#!/usr/bin/env python3
import os, re, io, unicodedata, urllib.request
from pathlib import Path
from PIL import Image, ImageOps

ROOT = Path(".")
PLAYLIST = ROOT / "Tv.m3u"
BACKUPS = ["Backup.m3u", "Tvt.m3u", "TV2.m3u", "Euro.m3u"]
OUT = ROOT / "logos-ajustadas"
OUT.mkdir(exist_ok=True)
RAW_BASE = "https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/" + os.environ.get("GITHUB_REF_NAME", "github/workflows/atualizar-logos.yml") + "/logos-ajustadas/"

def norm(value):
    value = re.sub(r"^\s*\d+\s*-\s*", "", value or "")
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]", "", value.lower())

def parse(path):
    lines = Path(path).read_text(encoding="utf-8", errors="replace").splitlines()
    items = []
    for i, line in enumerate(lines):
        if not line.startswith("#EXTINF"):
            continue
        name = line.rsplit(",", 1)[-1].strip()
        logo = re.search(r'tvg-logo="([^"]*)"', line)
        items.append({"name": name, "key": norm(name), "logo": logo.group(1) if logo else "", "line": i})
    return lines, items

def usable(url):
    if not url.startswith(("https://", "http://")):
        return False
    bad = ("Tryerel.png", "thumbnails/", "png-clipart", "data:image", "social-share-logo")
    return not any(x.lower() in url.lower() for x in bad)

sources = {}
for filename in BACKUPS:
    if not Path(filename).exists():
        continue
    _, entries = parse(filename)
    for entry in entries:
        if entry["key"] and usable(entry["logo"]):
            sources.setdefault(entry["key"], []).append(entry["logo"])

lines, main = parse(PLAYLIST)
changed = 0
downloaded = []
for entry in main:
    if entry["logo"]:
        continue
    candidates = list(dict.fromkeys(sources.get(entry["key"], [])))
    if not candidates:
        continue
    slug = re.sub(r"[^a-z0-9]+", "-", entry["key"]).strip("-") or "channel"
    target = OUT / (slug + ".png")
    if not target.exists():
        for url in candidates:
            try:
                req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 IPTV-logo-prep/1.0"})
                with urllib.request.urlopen(req, timeout=20) as response:
                    data = response.read(8 * 1024 * 1024 + 1)
                if len(data) > 8 * 1024 * 1024:
                    continue
                image = Image.open(io.BytesIO(data))
                image.load()
                image = image.convert("RGBA")
                image.thumbnail((560, 360), Image.Resampling.LANCZOS)
                canvas = Image.new("RGBA", (600, 400), (0, 0, 0, 255))
                canvas.alpha_composite(image, ((600-image.width)//2, (400-image.height)//2))
                canvas.convert("RGB").save(target, "PNG", optimize=True)
                downloaded.append(entry["name"])
                break
            except Exception:
                continue
    if target.exists():
        lines[entry["line"]] = re.sub(r'tvg-logo="[^"]*"', 'tvg-logo="' + RAW_BASE + target.name + '"', lines[entry["line"]])
        changed += 1

PLAYLIST.write_text("\n".join(lines) + "\n", encoding="utf-8")
print("Logos processadas:", len(downloaded))
print("Entradas da playlist atualizadas:", changed)
print("PNG disponíveis:", len(list(OUT.glob("*.png"))))
