#!/usr/bin/env python3
"""Baixa as playlists públicas da IPTV Cat para a Turquia e mescla entradas novas no Backup.m3u."""
from __future__ import annotations
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin
import requests

BASE = "https://iptvcat.net"
PAGES = ["/turkey/mark/tr_m3u", "/turkey/2"]
BACKUP = Path("Backup.m3u")
REPORT = Path("relatorios/iptvcat-turquia-download.md")
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; PlaylistBackupBot/1.0)"}
TIMEOUT = 35

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []
    def handle_starttag(self, tag, attrs):
        if tag.lower() == "a":
            href = dict(attrs).get("href")
            if href:
                self.hrefs.append(href)

def fetch(url):
    r = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
    r.raise_for_status()
    return r.text

def parse_m3u(text):
    lines = [x.strip() for x in text.replace("\r", "").split("\n") if x.strip()]
    entries, pending = [], None
    for line in lines:
        if line.startswith("#EXTINF"):
            pending = line
        elif pending and not line.startswith("#") and re.match(r"^https?://", line):
            entries.append((pending, line))
            pending = None
    return entries

def main():
    session = requests.Session()
    session.headers.update(HEADERS)
    download_urls = []
    page_errors = []
    for path in PAGES:
        page_url = urljoin(BASE, path)
        try:
            response = session.get(page_url, timeout=TIMEOUT)
            response.raise_for_status()
            parser = Links()
            parser.feed(response.text)
            for href in parser.hrefs:
                full = urljoin(page_url, href)
                if "iptvcat.net" in full and ("/my_list/" in full or re.search(r"\.m3u8?(?:$|\?)", full, re.I)):
                    if full not in download_urls:
                        download_urls.append(full)
        except Exception as exc:
            page_errors.append(f"- {page_url}: {exc}")

    downloaded, failed = [], []
    seen_streams = set()
    for url in download_urls:
        try:
            response = session.get(url, timeout=TIMEOUT)
            response.raise_for_status()
            text = response.text
            entries = parse_m3u(text)
            if not entries:
                failed.append((url, "resposta sem entradas M3U reconhecíveis"))
                continue
            for info, stream in entries:
                if stream not in seen_streams:
                    downloaded.append((info, stream))
                    seen_streams.add(stream)
        except Exception as exc:
            failed.append((url, str(exc)))

    if not downloaded:
        details = "\n".join(page_errors + [f"- {u}: {e}" for u, e in failed])
        raise SystemExit("Nenhuma entrada M3U válida foi baixada. Backup preservado.\n" + details)

    original = BACKUP.read_text(encoding="utf-8") if BACKUP.exists() else "#EXTM3U\n"
    existing = {line.strip() for line in original.splitlines() if line.strip().startswith(("http://", "https://"))}
    new_entries = [(info, stream) for info, stream in downloaded if stream not in existing]
    if new_entries:
        with BACKUP.open("a", encoding="utf-8") as f:
            if not original.endswith("\n"):
                f.write("\n")
            for info, stream in new_entries:
                f.write(info + "\n" + stream + "\n")

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    report = [
        "# Relatório — IPTV Cat Turquia",
        "",
        f"- Páginas consultadas: {len(PAGES)}",
        f"- URLs de download encontradas: {len(download_urls)}",
        f"- Entradas M3U válidas baixadas: {len(downloaded)}",
        f"- Entradas novas adicionadas ao Backup.m3u: {len(new_entries)}",
        f"- Streams já existentes ignorados: {len(downloaded) - len(new_entries)}",
        f"- Downloads com falha: {len(failed)}",
        "",
        "## Falhas",
        *( [f"- {u}: {e}" for u, e in failed] or ["Nenhuma falha reportada."] ),
        "",
        "## Páginas",
        *( [f"- {urljoin(BASE, p)}" for p in PAGES] ),
        "",
        "O backup só recebe entradas com pares #EXTINF/URL reconhecidos; se nenhum download válido ocorrer, o arquivo não é alterado.",
    ]
    REPORT.write_text("\n".join(report) + "\n", encoding="utf-8")
    print("\n".join(report[:10]))

if __name__ == "__main__":
    main()
