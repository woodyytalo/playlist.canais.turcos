#!/usr/bin/env python3
"""Sincroniza os canais da playlist com um XMLTV de programação existente.

Cria metadados <channel> para todos os tvg-id da playlist que ainda não
existam no XMLTV. Não cria <programme> nem inventa horários.
"""
import argparse
import html
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlparse

ATTR = re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')

def attrs(line):
    return {k: html.unescape(v) for k, v in ATTR.findall(line)}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--playlist", default="Tv.m3u8")
    ap.add_argument("--input", default="epg-source.xml")
    ap.add_argument("--output", default="epg/epg-pw.xml")
    args = ap.parse_args()

    playlist = Path(args.playlist).read_text(encoding="utf-8")
    records = []
    for line in playlist.splitlines():
        if not line.startswith("#EXTINF:"):
            continue
        meta, _, display = line.partition(",")
        a = attrs(meta)
        name = a.get("tvg-name") or re.sub(r"^\s*\d+\s*-\s*", "", display)
        name = re.sub(r"\s*\[(?:360|480)\s*SD\]\s*$", "", name).strip()
        channel_id = a.get("tvg-id")
        if not channel_id:
            slug = re.sub(r"[^a-z0-9]+", "", name.lower())
            channel_id = slug + ".local"
        records.append((channel_id, name, a.get("tvg-logo", ""), a.get("group-title", "")))

    if not records:
        raise SystemExit("Nenhum canal #EXTINF encontrado na playlist.")
    ids = [r[0] for r in records]
    if len(ids) != len(set(ids)):
        raise SystemExit("Há tvg-id duplicado na playlist; sincronização cancelada.")

    root = ET.parse(args.input).getroot()
    if root.tag != "tv":
        raise SystemExit("A fonte não é um XMLTV válido.")
    if not root.findall("programme"):
        raise SystemExit("A fonte XMLTV não contém programas; arquivo anterior preservado.")

    existing = {node.get("id") for node in root.findall("channel")}
    added = 0
    for channel_id, name, logo, category in records:
        if channel_id in existing:
            continue
        node = ET.SubElement(root, "channel", {"id": channel_id})
        ET.SubElement(node, "display-name").text = name
        if logo.startswith(("https://", "http://")):
            ET.SubElement(node, "icon", {"src": logo})
        if category:
            ET.SubElement(node, "display-name", {"lang": "pt"}).text = category
        existing.add(channel_id)
        added += 1

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    ET.ElementTree(root).write(out, encoding="utf-8", xml_declaration=True)
    check = ET.parse(out).getroot()
    if len(check.findall("channel")) < len(records) or not check.findall("programme"):
        raise SystemExit("Validação do XMLTV falhou.")
    print(f"Playlist: {len(records)} canais; XMLTV: {len(check.findall('channel'))} canais e {len(check.findall('programme'))} programas; {added} metadados adicionados. Nenhum horário foi inventado.")

if __name__ == "__main__":
    main()
