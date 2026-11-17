#!/usr/bin/env python3
import os, re, io, unicodedata, urllib.request
from pathlib import Path
from collections import deque
from PIL import Image

ROOT = Path(".")
PLAYLIST = ROOT / "Tv.m3u"
BACKUPS = ["Backup.m3u", "Tvt.m3u", "TV2.m3u", "Euro.m3u"]
OUT = ROOT / "logos-ajustadas"
OUT.mkdir(exist_ok=True)
RAW_BASE = "https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/" + os.environ.get("GITHUB_REF_NAME", "github/workflows/atualizar-logos.yml") + "/logos-ajustadas/"

def norm(value):
    value = re.sub(r"^\\s*\\d+\\s*-\\s*", "", value or "")
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

def remove_white_edge_background(image):
    image = image.convert("RGBA")
    w, h = image.size
    px = image.load()
    def near_white(p):
        r, g, b, a = p
        return a > 0 and min(r, g, b) >= 235 and max(r, g, b) - min(r, g, b) <= 22
    corners = [px[0,0], px[w-1,0], px[0,h-1], px[w-1,h-1]]
    if not all(near_white(p) for p in corners):
        return image
    seen = bytearray(w*h)
    q = deque()
    def add(x, y):
        k = y*w+x
        if not seen[k] and near_white(px[x,y]):
            seen[k] = 1
            q.append((x,y))
    for x in range(w):
        add(x,0); add(x,h-1)
    for y in range(h):
        add(0,y); add(w-1,y)
    while q:
        x,y=q.popleft()
        px[x,y]=(px[x,y][0],px[x,y][1],px[x,y][2],0)
        if x: add(x-1,y)
        if x+1<w: add(x+1,y)
        if y: add(x,y-1)
        if y+1<h: add(x,y+1)
    return image

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
downloaded = 0
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
                with urllib.request.urlopen(req, timeout=25) as response:
                    data = response.read(8 * 1024 * 1024 + 1)
                if len(data) > 8 * 1024 * 1024:
                    continue
                image = Image.open(io.BytesIO(data))
                image.load()
                image = remove_white_edge_background(image)
                image.thumbnail((560, 360), Image.Resampling.LANCZOS)
                canvas = Image.new("RGBA", (600, 400), (0, 0, 0, 255))
                canvas.alpha_composite(image, ((600-image.width)//2, (400-image.height)//2))
                canvas.convert("RGB").save(target, "PNG", optimize=True)
                downloaded += 1
                break
            except Exception as exc:
                print("Fonte ignorada:", entry["name"], url, str(exc)[:180])
                continue
    if target.exists():
        logo_url = RAW_BASE + target.name
        old_line = lines[entry["line"]]
        if re.search(r'tvg-logo="[^"]*"', old_line):
            new_line = re.sub(r'tvg-logo="[^"]*"', 'tvg-logo="' + logo_url + '"', old_line, count=1)
        else:
            head, title = old_line.rsplit(",", 1)
            new_line = head + ' tvg-logo="' + logo_url + '",' + title
        lines[entry["line"]] = new_line
        changed += 1

PLAYLIST.write_text("\n".join(lines) + "\n", encoding="utf-8")
print("Logos novas processadas:", downloaded)
print("Canais atualizados na TV principal:", changed)
print("PNG existentes na pasta:", len(list(OUT.glob("*.png"))))
print("Canais sem correspondência no backup:", sum(1 for e in main if not e["logo"] and not sources.get(e["key"])))
