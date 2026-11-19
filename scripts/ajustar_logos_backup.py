#!/usr/bin/env python3
import io
import os
import re
import unicodedata
import urllib.request
from collections import defaultdict, deque
from pathlib import Path

from PIL import Image

ROOT = Path(".")
PLAYLIST = ROOT / "Tv.m3u"
OUTPUT = ROOT / "logos-ajustadas"
OUTPUT.mkdir(exist_ok=True)
BRANCH = os.environ.get("GITHUB_REF_NAME", "github/workflows/atualizar-logos.yml")
RAW_BASE = (
    "https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/"
    + BRANCH + "/logos-ajustadas/"
)
CANVAS_WIDTH = 512
CANVAS_HEIGHT = 165
LOGO_MAX_SIZE = (480, 133)

# URLs identificadas para os três canais sem arquivo correspondente nos catálogos locais.
EXTRA_SOURCES = {
    "luystv": "https://assets.tvcdn.net/e876bf88-411c-4a9c-ad29-e449e651f7ae.png",
    "mukabeletv": "https://assets.tvcdn.net/23b391ac-5edb-4e37-8664-27da64fb0785.png",
    "kanalada": "https://assets.tvcdn.net/5cbdd199-9ed1-4f2d-a106-a6d9c53227c4.png",
}

def norm(value):
    value = unicodedata.normalize("NFKD", value or "")
    value = "".join(ch for ch in value if not unicodedata.combining(ch))
    return re.sub(r"[^a-z0-9]", "", value.lower())

def parse_entries(path):
    if not Path(path).exists():
        return []
    lines = Path(path).read_text(encoding="utf-8", errors="replace").splitlines()
    items = []
    for i, line in enumerate(lines):
        if not line.startswith("#EXTINF") or "," not in line:
            continue
        name = line.rsplit(",", 1)[-1].strip()
        logo = re.search(r'tvg-logo="([^"]*)"', line)
        items.append({"name": name, "key": norm(name), "logo": logo.group(1) if logo else "", "line": i})
    return items

def open_source(source):
    if isinstance(source, Path):
        image = Image.open(source)
    else:
        request = urllib.request.Request(
            source,
            headers={"User-Agent": "Mozilla/5.0 IPTV-logo-normalizer/2.0"},
        )
        with urllib.request.urlopen(request, timeout=30) as response:
            data = response.read(8 * 1024 * 1024 + 1)
        if len(data) > 8 * 1024 * 1024:
            raise ValueError("arquivo de logo excede 8 MB")
        image = Image.open(io.BytesIO(data))
    image.load()
    return image

def normalize_image(image, target):
    image = image.convert("RGBA")
    image.thumbnail(LOGO_MAX_SIZE, Image.Resampling.LANCZOS)
    # Canvas horizontal 512x165; mantém as cores e a transparência da logo original.
    canvas = Image.new("RGBA", (CANVAS_WIDTH, CANVAS_HEIGHT), (0, 0, 0, 0))
    x = (CANVAS_WIDTH - image.width) // 2
    y = (CANVAS_HEIGHT - image.height) // 2
    canvas.alpha_composite(image, (x, y))
    canvas.save(target, "PNG", optimize=True)

def index_local_sources():
    indexed = defaultdict(list)
    roots = [
        ROOT / "logos-tvlogo-turquia",
        ROOT / "logos-turcas-catalogo",
        ROOT / "logos-ajustadas",
    ]
    for source_root in roots:
        if not source_root.exists():
            continue
        for path in sorted(source_root.rglob("*.png")):
            if not path.is_file():
                continue
            stem = path.stem
            stem = re.sub(r"^tvlogos-github-", "", stem, flags=re.I)
            stem = re.sub(r"-tr$", "", stem, flags=re.I)
            key = norm(stem)
            if key:
                indexed[key].append(path)
    return indexed

def index_backup_urls():
    indexed = defaultdict(list)
    for backup in ("Backup.m3u", "Tvt.m3u"):
        for item in parse_entries(backup):
            if item["key"] and item["logo"].startswith(("https://", "http://")):
                indexed[item["key"]].append(item["logo"])
    return indexed

def main():
    if not PLAYLIST.exists():
        raise SystemExit("Tv.m3u não encontrado.")

    lines = PLAYLIST.read_text(encoding="utf-8").splitlines()
    entries = parse_entries(PLAYLIST)
    local_sources = index_local_sources()
    backup_sources = index_backup_urls()

    updated = 0
    reused = 0
    failures = []

    for entry in entries:
        key = entry["key"]
        slug = re.sub(r"[^a-z0-9]+", "-", key).strip("-") or "canal"
        target = OUTPUT / (slug + ".png")

        candidates = []
        # Fontes originais catalogadas têm prioridade sobre cópias de trabalho antigas.
        candidates.extend(local_sources.get(key, []))
        candidates.extend(backup_sources.get(key, []))
        if key in EXTRA_SOURCES:
            candidates.append(EXTRA_SOURCES[key])

        # Remove duplicatas sem alterar a ordem de prioridade.
        unique = []
        seen = set()
        for candidate in candidates:
            marker = str(candidate)
            if marker not in seen and candidate != target:
                seen.add(marker)
                unique.append(candidate)

        if not unique and target.exists():
            unique = [target]

        image_ok = False
        last_error = ""
        for source in unique:
            try:
                image = open_source(source)
                normalize_image(image, target)
                image_ok = True
                if isinstance(source, Path):
                    reused += 1
                break
            except Exception as exc:
                last_error = str(exc)[:180]
                continue

        if not image_ok and target.exists():
            try:
                image = open_source(target)
                normalize_image(image, target)
                image_ok = True
                reused += 1
            except Exception as exc:
                last_error = str(exc)[:180]

        if not image_ok:
            failures.append((entry["name"], last_error or "nenhuma fonte com correspondência exata"))
            continue

        logo_url = RAW_BASE + target.name
        old_line = lines[entry["line"]]
        if re.search(r'tvg-logo="[^"]*"', old_line):
            new_line = re.sub(r'tvg-logo="[^"]*"', 'tvg-logo="' + logo_url + '"', old_line, count=1)
        else:
            head, title = old_line.rsplit(",", 1)
            new_line = head + ' tvg-logo="' + logo_url + '",' + title
        lines[entry["line"]] = new_line
        updated += 1

    if failures:
        print("Canais sem logo correspondente:")
        for name, reason in failures:
            print(f"- {name}: {reason}")
        raise SystemExit(f"Processamento interrompido: {len(failures)} de {len(entries)} canais sem logo. Tv.m3u não foi alterado.")

    PLAYLIST.write_text("\n".join(lines) + "\n", encoding="utf-8")
    dimensions_ok = 0
    for path in OUTPUT.glob("*.png"):
        try:
            with Image.open(path) as image:
                if image.size == (CANVAS_WIDTH, CANVAS_HEIGHT):
                    dimensions_ok += 1
        except Exception:
            pass

    print(f"Logos associadas à TV principal: {updated}/{len(entries)}")
    print(f"PNG 512x165 verificados na pasta de saída: {dimensions_ok}")
    print("Padrão: canvas 512x165 (3,10:1), logo original centralizada, cores e transparência preservadas, sem cortes nem deformação.")

if __name__ == "__main__":
    main()
