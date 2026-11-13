#!/usr/bin/env python3
"""Verifica HLS da TV principal e promove somente variantes HD comprovadas."""
import re
import urllib.request
from urllib.parse import urljoin
from pathlib import Path

PLAYLIST = Path("Tv.m3u8")
REPORT = Path("relatorios/qualidade-hd.md")
TIMEOUT = 12
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; PlaylistQualityCheck/1.0)", "Accept": "*/*"}

def get_text(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=TIMEOUT) as response:
        data = response.read(1_500_000)
        if response.status != 200:
            raise ValueError(f"HTTP {response.status}")
        return data.decode("utf-8", "replace")

def inspect_master(url, depth=0):
    if depth > 2:
        return None
    text = get_text(url)
    if "#EXTM3U" not in text:
        raise ValueError("resposta não é uma playlist HLS")
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    variants = []
    for i, line in enumerate(lines):
        if line.startswith("#EXT-X-STREAM-INF:"):
            match = re.search(r"RESOLUTION=(\d+)x(\d+)", line)
            if match:
                width, height = map(int, match.groups())
                next_uri = next((x for x in lines[i+1:] if not x.startswith("#")), None)
                if next_uri:
                    variants.append((height, width, urljoin(url, next_uri)))
    if variants:
        return max(variants)
    return None

def candidate_urls(url):
    found = []
    patterns = [
        (r"480p", "720p"), (r"360p", "720p"), (r"320p", "720p"),
        (r"480P", "720P"), (r"360P", "720P"), (r"320P", "720P"),
    ]
    for old, new in patterns:
        if re.search(old, url):
            candidate = re.sub(old, new, url)
            if candidate != url and candidate not in found:
                found.append(candidate)
    return found

def resolution_label(height):
    return f"{height}p HD" if height < 1080 else f"{height}p Full HD"

def replace_suffix(extinf, label):
    return re.sub(r"\s*\[(?:\d{3,4}\s*)?(?:SD|HD|Full HD|não confirmado)\]$", f" [{label}]", extinf)

def main():
    lines = PLAYLIST.read_text(encoding="utf-8").splitlines()
    channel_indices = [i for i, line in enumerate(lines) if line.startswith("#EXTINF:")]
    report_rows = []
    changed = 0
    checked = 0

    for pos, idx in enumerate(channel_indices):
        end = channel_indices[pos + 1] if pos + 1 < len(channel_indices) else len(lines)
        url_idx = next((j for j in range(idx + 1, end) if lines[j].strip() and not lines[j].startswith("#")), None)
        if url_idx is None:
            continue
        current_url = lines[url_idx].strip()
        name = lines[idx].split(",", 1)[-1].strip()
        checked += 1
        selected_url = current_url
        variant = None
        status = "sem resolução HD comprovada"

        try:
            variant = inspect_master(current_url)
            if variant and variant[0] >= 720:
                status = f"HD confirmado ({variant[1]}x{variant[0]})"
            elif variant:
                status = f"fonte limitada a {variant[1]}x{variant[0]}"
            else:
                # Só tenta alternativas quando o endereço atual declara explicitamente uma resolução SD.
                for candidate in candidate_urls(current_url):
                    try:
                        candidate_variant = inspect_master(candidate)
                        if candidate_variant and candidate_variant[0] >= 720:
                            variant = candidate_variant
                            selected_url = candidate
                            status = f"alternativa HD confirmada ({variant[1]}x{variant[0]})"
                            break
                    except Exception:
                        continue
        except Exception as exc:
            status = f"não verificado ({type(exc).__name__}: {str(exc)[:90]})"

        if variant and variant[0] >= 720:
            if selected_url != current_url:
                lines[url_idx] = selected_url
                changed += 1
            lines[idx] = replace_suffix(lines[idx], resolution_label(variant[0]))
        report_rows.append((name, status, selected_url if selected_url != current_url else current_url))

    PLAYLIST.write_text("\n".join(lines) + "\n", encoding="utf-8")
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    hd_count = sum(1 for _, status, _ in report_rows if "HD confirmado" in status)
    body = [
        "# Relatório de qualidade — TV principal", "",
        f"- Canais verificados: **{checked}**",
        f"- Canais com HD comprovado: **{hd_count}**",
        f"- Links substituídos por variante HD comprovada: **{changed}**",
        "- Critério: somente playlists HLS que anunciam uma variante com RESOLUTION de 1280x720 ou superior.",
        "- Links sem resolução declarada permanecem inalterados; o relatório não presume HD pelo nome do arquivo.", "",
        "| Canal | Resultado | URL verificada |", "|---|---|---|"
    ]
    for name, status, url in report_rows:
        body.append(f"| {name.replace('|', '/')} | {status.replace('|', '/')} | {url} |")
    REPORT.write_text("\n".join(body) + "\n", encoding="utf-8")
    print(f"Verificados: {checked}; HD comprovados: {hd_count}; links promovidos: {changed}")

if __name__ == "__main__":
    main()
