#!/usr/bin/env python3
"""Gera XMLTV para todos os canais da playlist, usando correspondências exatas de ID/nome."""
import argparse
import copy
import html
from datetime import datetime, timedelta, timezone
import re
import unicodedata
import xml.etree.ElementTree as ET
from pathlib import Path

ATTR = re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')

# Correspondências alternativas verificadas por identidade do canal e programação recente.
# Não usar aproximação/fuzzy matching para evitar guias de canais diferentes.
MANUAL_ALIASES = {
    'htsporttv': {'htspor'},
    'lalegultv': {'lalegul'},
    'bbcfirstturkiye': {'bbcfirst'},
}

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

def is_turkish_lang(value):
    """Aceita códigos XMLTV explícitos de turco; idioma ausente é tratado pelas validações de texto."""
    lang = (value or '').strip().replace('_', '-').casefold()
    return not lang or lang == 'tr' or lang == 'tur' or lang.startswith('tr-')

def has_non_turkish_script(value):
    """Detecta sistemas de escrita incompatíveis com a programação turca em alfabeto latino."""
    for char in value or '':
        code = ord(char)
        if (0x3040 <= code <= 0x30FF or 0x3400 <= code <= 0x9FFF or
            0xAC00 <= code <= 0xD7AF or 0x0400 <= code <= 0x052F or
            0x0600 <= code <= 0x06FF or 0x0370 <= code <= 0x03FF):
            return True
    return False

def programme_is_current(programme, now):
    """Descarta EPG expirado ou excessivamente distante (ex.: feeds históricos)."""
    def parse_xmltv(value):
        value = (value or '').strip()
        for fmt in ('%Y%m%d%H%M%S %z', '%Y%m%d%H%M%S',
                    '%Y%m%d%H%M %z', '%Y%m%d%H%M'):
            try:
                parsed = datetime.strptime(value, fmt)
                return parsed.replace(tzinfo=timezone.utc) if parsed.tzinfo is None else parsed.astimezone(timezone.utc)
            except ValueError:
                pass
        return None

    start = parse_xmltv(programme.get('start'))
    stop = parse_xmltv(programme.get('stop'))
    return bool(start and stop and stop > start and
                stop > now - timedelta(hours=6) and
                start < now + timedelta(days=14))


STRICT_LANGUAGE_SOURCES = {
    'teleonline-multilingue.xml',
    'antifriz-multilingue.xml',
    'admuspeh-multilingue.xml',
    'gcdn-multilingue.xml',
}


def programme_is_turkish(programme, strict_language=False):
    # Não publica programas com idioma explicitamente diferente de turco
    # nem títulos/descrições escritos em japonês, chinês, coreano, cirílico,
    # árabe ou grego. Fontes usadas pelo workflow são específicas da Turquia.
    text_nodes = [node for node in programme.iter()
                  if node is not programme and (node.text or '').strip()]
    titles = [node for node in text_nodes if node.tag == 'title']
    descriptions = [node for node in text_nodes if node.tag in ('desc', 'sub-title')]
    if not titles:
        return False
    if strict_language and any(not (node.get('lang') or '').strip().casefold().startswith('tr')
                               for node in titles + descriptions):
        return False
    for node in text_nodes:
        if not is_turkish_lang(node.get('lang')):
            return False
        if has_non_turkish_script(node.text):
            return False
    return True

def playlist_records(path):
    records = []
    id_counts = {}
    for line in Path(path).read_text(encoding='utf-8').splitlines():
        if not line.startswith('#EXTINF:'):
            continue
        meta, _, display = line.partition(',')
        a = attrs(meta)
        display = display.strip()
        name = (a.get('tvg-name') or display).strip()
        names = {clean_name(name), clean_name(display)}
        names.discard('')
        channel_id = a.get('tvg-id') or clean_name(name) + '.local'
        id_counts[channel_id] = id_counts.get(channel_id, 0) + 1
        if id_counts[channel_id] > 1:
            channel_id = f'{channel_id}.duplicate{id_counts[channel_id]}'
        records.append((channel_id, name, names, a.get('tvg-logo', ''), a.get('group-title', '')))
    if not records:
        raise SystemExit('Nenhum canal #EXTINF encontrado na playlist.')
    return records

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--playlist', default='Tv.m3u')
    ap.add_argument('--input', action='append', required=True)
    ap.add_argument('--output', required=True)
    ap.add_argument('--report', help='Arquivo TXT com canais sem programação real correspondente.')
    args = ap.parse_args()

    records = playlist_records(args.playlist)
    source_channels, source_programmes, counts = {}, [], {}
    now = datetime.now(timezone.utc)
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
        strict_language = Path(source_path).name in STRICT_LANGUAGE_SOURCES
        for programme in root.findall('programme'):
            source_key = (source_path, programme.get('channel'))
            if not programme_is_current(programme, now):
                continue
            if not programme_is_turkish(programme, strict_language=strict_language):
                continue
            source_programmes.append((source_key, programme))
            counts[source_key] = counts.get(source_key, 0) + 1

    if not source_channels or not source_programmes:
        raise SystemExit('Fontes XMLTV sem canais/programas; guia anterior preservado.')

    id_index, name_index = {}, {}
    for key, channel in source_channels.items():
        normalized_id = clean_name(key[1])
        if normalized_id:
            id_index.setdefault(normalized_id, []).append(key)
        for item in channel.findall('display-name'):
            normalized = clean_name(item.text or '')
            if normalized:
                name_index.setdefault(normalized, []).append(key)

    output = ET.Element('tv', root_attrs)
    output.set('generator-info-name', 'Playlist Turquia XMLTV - Open-EPG + EPGShare + FreeEPG + fontes adicionais')
    source_to_playlist, matched = {}, set()

    for channel_id, name, aliases, logo, category in records:
        candidates = [k for k in id_index.get(clean_name(channel_id), [])
                      if counts.get(k, 0) > 0]
        if not candidates:
            verified_aliases = aliases | MANUAL_ALIASES.get(clean_name(name), set())
            for alias in verified_aliases:
                candidates.extend(k for k in name_index.get(alias, [])
                                  if counts.get(k, 0) > 0)
        # Nunca associa uma programação por semelhança parcial: só ID/nome normalizado exato.
        source_key = max(set(candidates), key=lambda k: counts.get(k, 0)) if candidates else None

        if source_key:
            source_to_playlist.setdefault(source_key, []).append(channel_id)
            matched.add(channel_id)
            node = copy.deepcopy(source_channels[source_key])
            node.set('id', channel_id)
            # Remove nomes/categorias alternativos identificados como outro idioma.
            for child in list(node):
                if child.tag in ('display-name', 'category') and (
                    not is_turkish_lang(child.get('lang')) or
                    has_non_turkish_script(child.text or '')
                ):
                    node.remove(child)
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
        targets = source_to_playlist.get(source_key, [])
        for target in targets:
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
    unmatched = [(r[0], r[1], r[4]) for r in records if r[0] not in matched]
    if args.report:
        report = Path(args.report)
        report.parent.mkdir(parents=True, exist_ok=True)
        lines = [f'Relatório XMLTV — {destination}', f'Canais na playlist: {len(records)}', f'Canais com programação real: {len(matched)}', f'Canais sem programação correspondente: {len(unmatched)}', f'Programas reais copiados: {copied}', '', 'CANAIS SEM PROGRAMAÇÃO:']
        lines.extend(f'- {name} | ID: {channel_id} | Categoria: {category or "sem categoria"}' for channel_id, name, category in unmatched)
        report.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(f'{destination}: {len(actual)} canais declarados; {len(matched)} com programação; {len(unmatched)} sem correspondência; {copied} programas reais.')

if __name__ == '__main__':
    main()
