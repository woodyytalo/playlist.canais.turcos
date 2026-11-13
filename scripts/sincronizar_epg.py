#!/usr/bin/env python3
"""Create XMLTV with an entry for every channel in Tv.m3u8.

Programme data is copied only from source XMLTV files and only after an
unambiguous channel-name match. No programme title or time is fabricated.
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
    return re.sub(r'[^a-z0-9]+', '', value)

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
    ap.add_argument('--input', action='append', required=True)
    ap.add_argument('--output', default='epg/guia-proprio.xml')
    args = ap.parse_args()

    records = playlist_records(args.playlist)
    source_channels = {}
    source_programmes = []
    source_programme_counts = {}
    root_attrs = {}
    for source_path in args.input:
        source = ET.parse(source_path).getroot()
        if source.tag != 'tv':
            raise SystemExit(f'Fonte XMLTV inválida: {source_path}')
        if not root_attrs:
            root_attrs = dict(source.attrib)
        for channel in source.findall('channel'):
            channel_id = channel.get('id')
            if channel_id:
                source_channels[(source_path, channel_id)] = channel
        for programme in source.findall('programme'):
            source_id = programme.get('channel')
            source_programmes.append((source_path, programme))
            source_programme_counts[(source_path, source_id)] = source_programme_counts.get((source_path, source_id), 0) + 1

    if not source_channels or not source_programmes:
        raise SystemExit('As fontes XMLTV não trouxeram canais e programas; guia anterior preservado.')

    # Name index across all sources. When a name exists in multiple sources,
    # use the channel with the greatest number of real programme records.
    name_index = {}
    for (source_path, source_id), channel in source_channels.items():
        for item in channel.findall('display-name'):
            key = clean_name(item.text or '')
            if key:
                name_index.setdefault(key, {})[(source_path, source_id)] = source_programme_counts.get((source_path, source_id), 0)

    output = ET.Element('tv', root_attrs)
    output.set('generator-info-name', 'Playlist Turquia XMLTV sincronizado')
    source_to_playlist = {}
    matched = set()
    for channel_id, name, logo, category in records:
        candidates = name_index.get(clean_name(name), {})
        source_key = None
        if candidates:
            best = max(candidates.values())
            winners = [key for key, count in candidates.items() if count == best]
            if best > 0 and len(winners) == 1:
                source_key = winners[0]
        if source_key:
            source_path, source_id = source_key
            source_to_playlist[source_key] = channel_id
            matched.add(channel_id)
            node = copy.deepcopy(source_channels[source_key])
            node.set('id', channel_id)
        else:
            node = ET.Element('channel', {'id': channel_id})
        names = {n.text for n in node.findall('display-name') if n.text}
        if name not in names:
            ET.SubElement(node, 'display-name').text = name
        if logo.startswith(('http://', 'https://')) and not node.findall('icon'):
            ET.SubElement(node, 'icon', {'src': logo})
        if category and not node.findall('category'):
            ET.SubElement(node, 'category').text = category
        output.append(node)

    copied = 0
    seen_programmes = set()
    for source_path, programme in source_programmes:
        key = (source_path, programme.get('channel'))
        playlist_id = source_to_playlist.get(key)
        if not playlist_id:
            continue
        dedupe = (playlist_id, programme.get('start'), programme.get('stop'),
                  ''.join((x.text or '') for x in programme.findall('title')))
        if dedupe in seen_programmes:
            continue
        seen_programmes.add(dedupe)
        node = copy.deepcopy(programme)
        node.set('channel', playlist_id)
        output.append(node)
        copied += 1

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    ET.ElementTree(output).write(out, encoding='utf-8', xml_declaration=True)
    check = ET.parse(out).getroot()
    expected = {r[0] for r in records}
    actual = {c.get('id') for c in check.findall('channel')}
    if len(check.findall('channel')) != len(records) or actual != expected:
        raise SystemExit('Validação falhou: a saída não contém todos os canais da playlist.')
    valid_ids = actual
    if any(p.get('channel') not in valid_ids for p in check.findall('programme')):
        raise SystemExit('Validação falhou: programa associado a canal inexistente.')
    print(f'Playlist: {len(records)} canais; XMLTV: {len(actual)} canais; '
          f'{len(matched)} com programação encontrada; {len(records)-len(matched)} sem '
          f'correspondência nas fontes; {copied} programas reais copiados.')

if __name__ == '__main__':
    main()
