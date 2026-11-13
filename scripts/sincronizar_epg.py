#!/usr/bin/env python3
"""Build an XMLTV whose channel IDs match every entry in Tv.m3u8.

All playlist channels are emitted as <channel> records. Real <programme>
records are copied only when the source has an unambiguous name match.
No schedules or times are fabricated.
"""
import argparse
import copy
import html
import re
import unicodedata
import xml.etree.ElementTree as ET
from pathlib import Path

ATTR = re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')

def attrs(line):
    return {k: html.unescape(v) for k, v in ATTR.findall(line)}

def clean_name(value):
    value = re.sub(r'^\s*TR\s*:\s*', '', value or '', flags=re.I)
    value = re.sub(r'\s*\[(?:360|480)\s*SD\]\s*$', '', value, flags=re.I)
    value = re.sub(r'^\s*\d+\s*-\s*', '', value)
    value = unicodedata.normalize('NFKD', value)
    value = ''.join(c for c in value if not unicodedata.combining(c))
    value = value.casefold().replace('&', ' and ')
    value = re.sub(r'[^a-z0-9]+', '', value)
    return value

def playlist_records(path):
    records = []
    for line in Path(path).read_text(encoding='utf-8').splitlines():
        if not line.startswith('#EXTINF:'):
            continue
        meta, _, display = line.partition(',')
        a = attrs(meta)
        name = (a.get('tvg-name') or display).strip()
        name = re.sub(r'^\s*\d+\s*-\s*', '', name)
        name = re.sub(r'\s*\[(?:360|480)\s*SD\]\s*$', '', name, flags=re.I).strip()
        channel_id = a.get('tvg-id') or clean_name(name) + '.local'
        records.append((channel_id, name, a.get('tvg-logo', ''), a.get('group-title', '')))
    if not records:
        raise SystemExit('Nenhum canal #EXTINF encontrado na playlist.')
    ids = [r[0] for r in records]
    if len(ids) != len(set(ids)):
        raise SystemExit('Há tvg-id duplicado na playlist; sincronização cancelada.')
    return records

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--playlist', default='Tv.m3u8')
    ap.add_argument('--input', default='epg-source.xml')
    ap.add_argument('--output', default='epg/guia-proprio.xml')
    args = ap.parse_args()

    records = playlist_records(args.playlist)
    source = ET.parse(args.input).getroot()
    if source.tag != 'tv':
        raise SystemExit('A fonte não é um XMLTV válido.')

    source_channels = source.findall('channel')
    source_programmes = source.findall('programme')
    if not source_channels:
        raise SystemExit('A fonte XMLTV não contém canais; arquivo anterior preservado.')

    # Index every source display-name. Only unique normalized names are eligible.
    name_index = {}
    for channel in source_channels:
        names = [n.text for n in channel.findall('display-name') if n.text]
        for name in names:
            key = clean_name(name)
            if key:
                name_index.setdefault(key, set()).add(channel.get('id'))

    source_by_id = {c.get('id'): c for c in source_channels if c.get('id')}
    source_to_playlist = {}
    matched_playlist_ids = set()
    output = ET.Element('tv', dict(source.attrib))
    output.set('generator-info-name', 'Playlist Turquia XMLTV sincronizado')

    # Emit a channel node for every playlist entry, including channels without
    # guide data, so no tvg-id is absent from the XMLTV document.
    for channel_id, name, logo, category in records:
        candidates = name_index.get(clean_name(name), set())
        source_id = next(iter(candidates)) if len(candidates) == 1 else None
        if source_id:
            source_to_playlist[source_id] = channel_id
            matched_playlist_ids.add(channel_id)
            node = copy.deepcopy(source_by_id[source_id])
            node.set('id', channel_id)
        else:
            node = ET.Element('channel', {'id': channel_id})
        existing_names = {n.text for n in node.findall('display-name') if n.text}
        if name not in existing_names:
            ET.SubElement(node, 'display-name').text = name
        if logo.startswith(('http://', 'https://')) and not node.findall('icon'):
            ET.SubElement(node, 'icon', {'src': logo})
        if category and not node.findall('category'):
            ET.SubElement(node, 'category').text = category
        output.append(node)

    copied_programmes = 0
    for programme in source_programmes:
        source_id = programme.get('channel')
        playlist_id = source_to_playlist.get(source_id)
        if not playlist_id:
            continue
        node = copy.deepcopy(programme)
        node.set('channel', playlist_id)
        output.append(node)
        copied_programmes += 1

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    ET.ElementTree(output).write(out, encoding='utf-8', xml_declaration=True)

    # Re-open and validate exact playlist coverage and programme references.
    check = ET.parse(out).getroot()
    output_ids = [c.get('id') for c in check.findall('channel')]
    expected_ids = [r[0] for r in records]
    if len(output_ids) != len(expected_ids) or set(output_ids) != set(expected_ids):
        raise SystemExit('Validação falhou: nem todos os canais da playlist estão no XMLTV.')
    valid_ids = set(output_ids)
    bad_refs = [p.get('channel') for p in check.findall('programme') if p.get('channel') not in valid_ids]
    if bad_refs:
        raise SystemExit('Validação falhou: há programas apontando para canais inexistentes.')
    print(f'Playlist: {len(records)} canais; XMLTV: {len(output_ids)} canais; '
          f'{len(matched_playlist_ids)} canais com correspondência na fonte; '
          f'{len(records)-len(matched_playlist_ids)} sem programação correspondente; '
          f'{copied_programmes} programas reais copiados. Nenhum horário foi inventado.')

if __name__ == '__main__':
    main()
