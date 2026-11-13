#!/usr/bin/env python3
"""Build an XMLTV file for every channel in Tv.m3u8 using real source schedules."""
import argparse
import copy
import difflib
import html
import re
import unicodedata
import xml.etree.ElementTree as ET
from pathlib import Path

ATTR = re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')

def attrs(line):
    return {k: html.unescape(v) for k, v in ATTR.findall(line)}

def clean_name(value):
    value = re.sub(r'^\s*(?:TR|TURKEY|TURKIYE)\s*[:|/-]\s*', '', value or '', flags=re.I)
    value = re.sub(r'\s*(?:HD|SD|FHD|UHD|4K)\s*$', '', value, flags=re.I)
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
    ap.add_argument('--output', default='epg/guia-cyberwire.xml')
    args = ap.parse_args()

    records = playlist_records(args.playlist)
    source_channels = {}
    source_programmes = []
    programme_counts = {}
    root_attrs = {}

    for source_path in args.input:
        source = ET.parse(source_path).getroot()
        if source.tag != 'tv':
            raise SystemExit(f'Fonte XMLTV inválida: {source_path}')
        if not root_attrs:
            root_attrs = dict(source.attrib)
        for channel in source.findall('channel'):
            source_id = channel.get('id')
            if source_id:
                key = (source_path, source_id)
                source_channels[key] = channel
        for programme in source.findall('programme'):
            source_id = programme.get('channel')
            source_programmes.append((source_path, programme))
            key = (source_path, source_id)
            programme_counts[key] = programme_counts.get(key, 0) + 1

    if not source_channels or not source_programmes:
        raise SystemExit('As fontes XMLTV não trouxeram canais e programas; guia anterior preservado.')

    name_index = {}
    source_names = []
    for key, channel in source_channels.items():
        names = {clean_name(key[1])}
        names.update(clean_name(item.text or '') for item in channel.findall('display-name'))
        names.discard('')
        source_names.append((key, names, programme_counts.get(key, 0)))
        for name in names:
            name_index.setdefault(name, {})[key] = programme_counts.get(key, 0)

    output = ET.Element('tv', root_attrs)
    output.set('generator-info-name', 'Playlist Turquia XMLTV + Cyber-Wire')
    source_to_playlist = {}
    matched = set()
    used_source_keys = set()

    for channel_id, name, logo, category in records:
        keys = [clean_name(channel_id), clean_name(name)]
        candidates = {}
        for candidate in keys:
            candidates.update(name_index.get(candidate, {}))
        source_key = None
        eligible = [(key, count) for key, count in candidates.items()
                    if count > 0 and key not in used_source_keys]
        if eligible:
            best_count = max(count for _, count in eligible)
            winners = [key for key, count in eligible if count == best_count]
            if len(winners) == 1:
                source_key = winners[0]

        if source_key is None:
            target = clean_name(name)
            ranked = []
            for candidate_key, candidate_names, count in source_names:
                if count <= 0 or candidate_key in used_source_keys:
                    continue
                score = max((difflib.SequenceMatcher(None, target, candidate).ratio()
                             for candidate in candidate_names), default=0)
                if score >= 0.84:
                    ranked.append((score, count, candidate_key))
            ranked.sort(reverse=True)
            if ranked and (len(ranked) == 1 or ranked[0][0] - ranked[1][0] >= 0.06):
                source_key = ranked[0][2]

        if source_key:
            used_source_keys.add(source_key)
            source_to_playlist[source_key] = channel_id
            matched.add(channel_id)
            node = copy.deepcopy(source_channels[source_key])
            node.set('id', channel_id)
        else:
            node = ET.Element('channel', {'id': channel_id})

        existing_names = {item.text for item in node.findall('display-name') if item.text}
        if name not in existing_names:
            ET.SubElement(node, 'display-name').text = name
        if logo.startswith(('http://', 'https://')) and not node.findall('icon'):
            ET.SubElement(node, 'icon', {'src': logo})
        if category and not node.findall('category'):
            ET.SubElement(node, 'category').text = category
        output.append(node)

    copied = 0
    seen = set()
    for source_path, programme in source_programmes:
        source_key = (source_path, programme.get('channel'))
        playlist_id = source_to_playlist.get(source_key)
        if not playlist_id:
            continue
        dedupe = (playlist_id, programme.get('start'), programme.get('stop'),
                  ''.join(item.text or '' for item in programme.findall('title')))
        if dedupe in seen:
            continue
        seen.add(dedupe)
        node = copy.deepcopy(programme)
        node.set('channel', playlist_id)
        output.append(node)
        copied += 1

    destination = Path(args.output)
    destination.parent.mkdir(parents=True, exist_ok=True)
    ET.ElementTree(output).write(destination, encoding='utf-8', xml_declaration=True)

    check = ET.parse(destination).getroot()
    expected = {record[0] for record in records}
    actual = {channel.get('id') for channel in check.findall('channel')}
    if len(check.findall('channel')) != len(records) or actual != expected:
        raise SystemExit('Validação falhou: a saída não contém todos os canais da playlist.')
    if any(programme.get('channel') not in actual for programme in check.findall('programme')):
        raise SystemExit('Validação falhou: programa associado a canal inexistente.')

    print(f'Playlist: {len(records)} canais; XMLTV: {len(actual)} canais; '
          f'{len(matched)} com programação encontrada; {len(records) - len(matched)} sem '
          f'correspondência nas fontes; {copied} programas reais copiados.')

if __name__ == '__main__':
    main()
