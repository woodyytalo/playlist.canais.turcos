#!/usr/bin/env python3
"""Build XMLTV guides for every playlist channel using exact ID/name matches only."""
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
    value = re.sub(r'^\\s*(?:TR|TURKEY|TURKIYE)\\s*[:|/-]\\s*', '', value or '', flags=re.I)
    value = re.sub(r'\\s*(?:HD|SD|FHD|UHD|4K)\\s*$', '', value, flags=re.I)
    value = re.sub(r'\\s*\\[(?:360|480)\\s*SD\\]\\s*$', '', value, flags=re.I)
    value = re.sub(r'^\\s*\\d+\\s*-\\s*', '', value)
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
        name = re.sub(r'^\\s*\\d+\\s*-\\s*', '', name)
        name = re.sub(r'\\s*\\[(?:360|480)\\s*SD\\]\\s*$', '', name, flags=re.I).strip()
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
    ap.add_argument('--output', required=True)
    args = ap.parse_args()

    records = playlist_records(args.playlist)
    source_channels, source_programmes, counts = {}, [], {}
    root_attrs = {}
    for source_path in args.input:
        root = ET.parse(source_path).getroot()
        if root.tag != 'tv':
            raise SystemExit(f'Fonte XMLTV inválida: {source_path}')
        if not root_attrs:
            root_attrs = dict(root.attrib)
        for channel in root.findall('channel'):
            sid = channel.get('id')
            if sid:
                key = (source_path, sid)
                source_channels[key] = channel
        for programme in root.findall('programme'):
            key = (source_path, programme.get('channel'))
            source_programmes.append((key, programme))
            counts[key] = counts.get(key, 0) + 1

    if not source_channels or not source_programmes:
        raise SystemExit('Fontes XMLTV sem canais/programas; guia anterior preservado.')

    id_index, name_index = {}, {}
    for key, channel in source_channels.items():
        sid = clean_name(key[1])
        if sid:
            id_index.setdefault(sid, []).append(key)
        for item in channel.findall('display-name'):
            name = clean_name(item.text or '')
            if name:
                name_index.setdefault(name, []).append(key)

    output = ET.Element('tv', root_attrs)
    output.set('generator-info-name', 'Playlist Turquia XMLTV - Open-EPG + fonte principal')
    source_to_playlist, used = {}, set()
    matched = set()

    for channel_id, name, logo, category in records:
        # Prefer an exact normalized tvg-id; only then use an exact display-name.
        candidates = [k for k in id_index.get(clean_name(channel_id), [])
                      if counts.get(k, 0) > 0 and k not in used]
        if not candidates:
            candidates = [k for k in name_index.get(clean_name(name), [])
                          if counts.get(k, 0) > 0 and k not in used]
        source_key = max(candidates, key=lambda k: counts.get(k, 0)) if candidates else None

        if source_key:
            used.add(source_key)
            source_to_playlist[source_key] = channel_id
            matched.add(channel_id)
            node = copy.deepcopy(source_channels[source_key])
            node.set('id', channel_id)
        else:
            node = ET.Element('channel', {'id': channel_id})

        existing = {x.text for x in node.findall('display-name') if x.text}
        if name not in existing:
            ET.SubElement(node, 'display-name').text = name
        if logo.startswith(('http://', 'https://')) and not node.findall('icon'):
            ET.SubElement(node, 'icon', {'src': logo})
        if category and not node.findall('category'):
            ET.SubElement(node, 'category').text = category
        output.append(node)

    copied, seen = 0, set()
    for source_key, programme in source_programmes:
        target = source_to_playlist.get(source_key)
        if not target:
            continue
        dedupe = (target, programme.get('start'), programme.get('stop'),
                  ''.join(x.text or '' for x in programme.findall('title')))
        if dedupe in seen:
            continue
        seen.add(dedupe)
        node = copy.deepcopy(programme)
        node.set('channel', target)
        output.append(node)
        copied += 1

    if copied == 0:
        raise SystemExit('Nenhum programa real associado; saída não publicada.')
    destination = Path(args.output)
    destination.parent.mkdir(parents=True, exist_ok=True)
    ET.ElementTree(output).write(destination, encoding='utf-8', xml_declaration=True)

    check = ET.parse(destination).getroot()
    expected = {r[0] for r in records}
    actual = {c.get('id') for c in check.findall('channel')}
    if len(check.findall('channel')) != len(records) or actual != expected:
        raise SystemExit('Validação falhou: saída não contém todos os canais.')
    if any(p.get('channel') not in actual for p in check.findall('programme')):
        raise SystemExit('Programa aponta para canal inexistente.')
    print(f'{destination}: {len(actual)} canais declarados; {len(matched)} com programação; {len(records)-len(matched)} sem correspondência; {copied} programas reais.')

if __name__ == '__main__':
    main()
