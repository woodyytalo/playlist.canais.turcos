#!/usr/bin/env python3
"""Aplica na Tv.m3u somente logos existentes no catálogo local ou obtidas do Backup.m3u."""
from __future__ import annotations
import io, re, time, unicodedata
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.parse import quote, urlsplit
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
PLAYLIST = ROOT / "Tv.m3u"
BACKUP = ROOT / "Backup.m3u"
LOGOS = ROOT / "logos-turcas-catalogo" / "LOGOS-EXTRAIDAS-DAS-PLAYLISTS"
BRANCH = "github/workflows/atualizar-logos.yml"
RAW = f"https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/{BRANCH}/"

ALIASES = {
    "24 TV": ["24"], "360 TV": ["360"], "4U TV": ["4U"],
    "Bloomberg HT 2": ["Bloomberg HT"], "BRTV Karabük": ["BRTV"],
    "Cartoon Network Türkiye": ["Cartoon Network"],
    "ER TV Malatya": ["ERTV", "Er TV"], "FRT TV": ["FRT"],
    "GRT Gaziantep TV": ["GRT TV", "GRT Gaziantep"],
    "Kanal 26 Eskişehir": ["Kanal 26"], "Konya KTV": ["KTV"],
    "Mekameleen TV": ["Mekameleen"], "Power Dance TV": ["Power Dance"],
    "Power Love TV": ["Power Love"], "Spacetoon Türkiye": ["Spacetoon"],
    "TV Karadeniz": ["Karadeniz TV", "Karadeniz"],
    "Zarok TV Kurmanji": ["Zarok TV"], "Zarok TV Sorani": ["Zarok TV"],
    "Syria TV": ["Syria TV"], "Balkan Türk": ["Balkan Turk"],
    "RTG International": ["RTG", "RTG int."], "Arzu Film": ["Arzu Film"],
    "MC EU TV": ["MC EU"], "BabyFirst TV": ["BabyFirst", "Baby First"],
    "Company TV": ["Company TV"], "INTV Australia": ["INTV"],
    "IQ Channel": ["IQ Channel"], "MK TV": ["MK TV"],
    "Retro Music Television": ["Retro Music"], "Dim TV": ["DIM TV"],
    "Kardelen TV": ["KARDELEN TV"], "Kanal 32": ["KANAL 32"],
    "Kent Türk TV": ["Kent Turk", "KENT TÜRK"], "Luys TV": ["LUYS TV"],
    "Sat7 Türk": ["SAT 7 TÜRK"], "Vuslat TV": ["Malatya Vuslat TV", "VUSLAT TV"],
    "beIN Sports 1 Turk": ["BEINSPORTS 1 HD", "BEIN SPORTS 1 HD"],
    "Al Zahra TV Turkic": ["Al Zahra TV", "Alzahra TV"],
    "Euro Star TV": ["Euro Star", "Eurostar"],
    "İzmir Time 35 TV": ["Izmir Time 35", "İzmir Time 35"],
}

def norm(value: str) -> str:
    value = unicodedata.normalize("NFKD", value or "")
    value = "".join(c for c in value if not unicodedata.combining(c)).lower()
    value = re.sub(r"\\([^)]*\\)|\\[[^]]*\\]", " ", value)
    value = re.sub(r"\\b(2160p|1440p|1080p|900p|720p|576p|540p|480p|360p|uhd|fhd|4k|hd|sd)\\b", " ", value)
    return re.sub(r"[^a-z0-9]", "", value)

def parse_playlist(path: Path):
    entries, meta = [], None
    for line in path.read_text(encoding="utf-8-sig", errors="replace").splitlines():
        if line.lstrip().startswith("#EXTINF"):
            meta = line
        elif meta and line.strip() and not line.lstrip().startswith("#"):
            attrs = {k.lower(): v for k, v in re.findall(r'([\\w-]+)\\s*=\\s*"([^"]*)"', meta)}
            display = meta.split(",", 1)[1].strip() if "," in meta else ""
            name = attrs.get("tvg-name") or display
            entries.append({
                "name": name,
                "logo": attrs.get("tvg-logo", "").strip(),
                "id": attrs.get("tvg-id", "").strip(),
                "meta": meta,
                "url": line.strip(),
            })
            meta = None
    return entries

def local_files_by_backup_index():
    found = {}
    for path in LOGOS.iterdir():
        m = re.match(r"^\\d{4} - (\\d{4})\\.(png|jpe?g|webp|svg)$", path.name, re.I)
        if m:
            found.setdefault(int(m.group(1)), []).append(path)
    for index in found:
        found[index].sort(key=lambda p: (p.suffix.lower() != ".png", p.name))
    return found

def download_from_backup(url: str, target: Path):
    if not url.startswith(("http://", "https://")):
        raise ValueError("URL ausente")
    request = Request(url, headers={"User-Agent": "Mozilla/5.0 (compatible; BackupLogoImporter/1.0)", "Accept": "image/*,*/*;q=0.8"})
    with urlopen(request, timeout=35) as response:
        data = response.read(12 * 1024 * 1024 + 1)
        mime = response.headers.get("Content-Type", "").split(";", 1)[0].lower()
    if len(data) > 12 * 1024 * 1024 or not data or mime == "text/html":
        raise ValueError("A resposta não é uma imagem válida")
    if mime == "image/svg+xml" or data.lstrip().startswith(b"<svg") or b"<svg" in data[:1000]:
        import cairosvg
        data = cairosvg.svg2png(bytestring=data, output_width=1024, output_height=1024)
    with Image.open(io.BytesIO(data)) as source:
        image = source.convert("RGBA")
    if image.width < 8 or image.height < 8:
        raise ValueError("Imagem pequena ou inválida")
    bbox = image.getchannel("A").getbbox()
    if bbox:
        image = image.crop(bbox)
    image.thumbnail((460, 460), Image.Resampling.LANCZOS)
    canvas = Image.new("RGBA", (512, 512), (0, 0, 0, 0))
    canvas.alpha_composite(image, ((512-image.width)//2, (512-image.height)//2))
    target.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(target, "PNG", optimize=True)

def main():
    if not PLAYLIST.is_file() or not BACKUP.is_file() or not LOGOS.is_dir():
        raise SystemExit("Tv.m3u, Backup.m3u ou pasta de logos não encontrada.")
    main_entries = parse_playlist(PLAYLIST)
    backup_entries = parse_playlist(BACKUP)
    if len(main_entries) != 213:
        raise SystemExit(f"Esperados 213 canais na Tv.m3u; encontrados {len(main_entries)}.")
    local_by_index = local_files_by_backup_index()
    backup_by_name = {}
    for index, entry in enumerate(backup_entries, 1):
        backup_by_name.setdefault(norm(entry["name"]), []).append((index, entry))

    replacements, missing, added = {}, [], []
    for channel_index, channel in enumerate(main_entries, 1):
        names = [channel["name"]] + ALIASES.get(channel["name"], [])
        keys = list(dict.fromkeys(norm(x) for x in names if norm(x)))
        candidates = []
        seen = set()
        # Nome exato vem primeiro; aliases explícitos vêm depois.
        for key in keys:
            for backup_index, entry in backup_by_name.get(key, []):
                marker = (backup_index, entry["logo"])
                if marker not in seen:
                    candidates.append((backup_index, entry))
                    seen.add(marker)

        selected = None
        # Primeiro, usar a imagem já guardada na pasta e associada à posição exata do Backup.
        for backup_index, entry in candidates:
            existing = local_by_index.get(backup_index, [])
            if existing:
                selected = existing[0]
                break

        # Se não existir cópia local, baixar somente a URL que consta no Backup.m3u.
        if selected is None:
            for backup_index, entry in candidates:
                url = entry["logo"]
                if not url.startswith(("http://", "https://")):
                    continue
                suffix = Path(urlsplit(url).path).suffix.lower()
                target = LOGOS / f"backup-tv-{channel_index:03d}-{re.sub(r'[^a-z0-9]+','-',norm(channel['name']))[:45]}.png"
                try:
                    if not target.is_file():
                        download_from_backup(url, target)
                    selected = target
                    added.append(channel["name"])
                    break
                except Exception as exc:
                    print(f"FALHA {channel['name']} usando entrada {backup_index} do Backup: {exc}")
                    time.sleep(0.2)

        if selected is None:
            missing.append(channel["name"])
        else:
            relative = selected.relative_to(ROOT).as_posix()
            replacements[channel_index] = RAW + quote(relative, safe="/-._")

    original_lines = PLAYLIST.read_text(encoding="utf-8-sig").splitlines()
    updated_lines = []
    ext_index = 0
    for line in original_lines:
        if line.startswith("#EXTINF:"):
            ext_index += 1
            logo = replacements.get(ext_index)
            if logo:
                if re.search(r'\\btvg-logo\\s*=', line, re.I):
                    line = re.sub(r'\\btvg-logo\\s*=\\s*"[^"]*"', f'tvg-logo="{logo}"', line, count=1, flags=re.I)
                else:
                    line = re.sub(r",", f' tvg-logo="{logo}",', line, count=1)
        updated_lines.append(line)
    if ext_index != 213:
        raise SystemExit(f"Validação falhou: {ext_index} entradas EXTINF.")
    # A única diferença permitida nas linhas EXTINF são os valores tvg-logo.
    def mask(text):
        return re.sub(r'\\btvg-logo\\s*=\\s*"[^"]*"', 'tvg-logo="__LOGO__"', text, flags=re.I)
    old_ext = [x for x in original_lines if x.startswith("#EXTINF:")]
    new_ext = [x for x in updated_lines if x.startswith("#EXTINF:")]
    if len(old_ext) != len(new_ext) or any(mask(a) != mask(b) for a, b in zip(old_ext, new_ext)):
        raise SystemExit("Validação detectou alteração em nome, categoria, ID ou metadados.")
    PLAYLIST.write_text("\\n".join(updated_lines) + "\\n", encoding="utf-8")
    print(f"Logos aplicadas: {len(replacements)}/213")
    print(f"Novas imagens baixadas exclusivamente do Backup.m3u: {len(added)}")
    print(f"Sem correspondência no Backup: {len(missing)}")
    if missing:
        print("PENDENTES: " + " | ".join(missing))

if __name__ == "__main__":
    main()
