#!/usr/bin/env python3
"""Diagnóstico somente leitura de streams HLS em uma playlist M3U."""
import csv
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlsplit, urlunsplit
from urllib.request import Request, urlopen

PLAYLIST = Path("Tv.m3u")
REPORT_DIR = Path("relatorios-monitoramento")
TIMEOUT = 15
MAX_BYTES = 1024 * 1024
USER_AGENT = "PlaylistMonitor/1.0 (GitHub Actions; read-only health check)"


def safe_url(url):
    p = urlsplit(url)
    host = p.hostname or ""
    if p.port:
        host += f":{p.port}"
    return urlunsplit((p.scheme, host, p.path, "", ""))


def fetch(url):
    req = Request(url, headers={"User-Agent": USER_AGENT, "Range": f"bytes=0-{MAX_BYTES-1}"})
    with urlopen(req, timeout=TIMEOUT) as response:
        return response.status, response.headers.get("Content-Type", ""), response.read(MAX_BYTES)


def first_hls_media(url, body):
    lines = [x.strip() for x in body.decode("utf-8", errors="replace").splitlines() if x.strip()]
    if not any(x.startswith("#EXTM3U") for x in lines[:3]):
        return None
    for i, line in enumerate(lines):
        if line.startswith("#EXT-X-STREAM-INF"):
            for candidate in lines[i + 1:]:
                if not candidate.startswith("#"):
                    return urljoin(url, candidate)
    for line in lines:
        if not line.startswith("#"):
            return urljoin(url, line)
    return None


def check(url):
    start = time.monotonic()
    try:
        status, content_type, body = fetch(url)
        elapsed = (time.monotonic() - start) * 1000
        if not 200 <= status < 400:
            return "FALHA_HTTP", f"HTTP {status}", status, elapsed, ""
        is_hls = ".m3u8" in url.lower() or "mpegurl" in content_type.lower() or body.lstrip().startswith(b"#EXTM3U")
        if is_hls:
            media = first_hls_media(url, body)
            if not media:
                return "ALERTA_HLS", "Manifesto HLS sem variante/segmento identificável", status, elapsed, ""
            seg_start = time.monotonic()
            seg_status, _, _ = fetch(media)
            elapsed += (time.monotonic() - seg_start) * 1000
            if 200 <= seg_status < 400:
                return "OK", f"Manifesto e primeiro segmento acessíveis (HTTP {seg_status})", status, elapsed, safe_url(media)
            return "FALHA_SEGMENTO", f"Primeiro segmento HTTP {seg_status}", status, elapsed, safe_url(media)
        return "OK", f"Endpoint respondeu HTTP {status}; formato não identificado como HLS", status, elapsed, ""
    except HTTPError as e:
        return "FALHA_HTTP", f"HTTP {e.code}", e.code, (time.monotonic() - start) * 1000, ""
    except (URLError, TimeoutError, OSError, ValueError) as e:
        reason = getattr(e, "reason", None) or str(e)
        return "ERRO_CONEXAO", str(reason)[:220], None, (time.monotonic() - start) * 1000, ""


def parse_playlist(path):
    current = None
    for raw in path.read_text(encoding="utf-8-sig", errors="replace").splitlines():
        line = raw.strip()
        if line.startswith("#EXTINF:"):
            current = line.rsplit(",", 1)[-1].strip() if "," in line else "Canal sem nome"
        elif line and not line.startswith("#") and current:
            if line.startswith(("http://", "https://")):
                yield current, line
            current = None


def main():
    if not PLAYLIST.exists():
        raise SystemExit("Tv.m3u não encontrada na raiz do repositório.")
    REPORT_DIR.mkdir(exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    entries = list(parse_playlist(PLAYLIST))
    rows = []
    for index, (channel, url) in enumerate(entries, 1):
        status, detail, code, latency, media = check(url)
        rows.append({
            "numero": index, "canal": channel, "status": status, "detalhe": detail,
            "http": code if code is not None else "", "latencia_ms": round(latency),
            "url": safe_url(url), "segmento_testado": media,
            "verificado_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        })
        print(f"[{index}/{len(entries)}] {channel}: {status} ({round(latency)} ms)")
        time.sleep(0.15)

    csv_path = REPORT_DIR / f"canais-{stamp}.csv"
    fields = ["numero", "canal", "status", "detalhe", "http", "latencia_ms", "url", "segmento_testado", "verificado_utc"]
    with csv_path.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    counts = {}
    for row in rows:
        counts[row["status"]] = counts.get(row["status"], 0) + 1
    md_path = REPORT_DIR / f"relatorio-{stamp}.md"
    with md_path.open("w", encoding="utf-8") as f:
        f.write(f"# Monitoramento de canais — {stamp} UTC\n\n")
        f.write(f"- Playlist analisada: Tv.m3u (somente leitura)\n- URLs testadas: **{len(rows)}**\n")
        f.write("- Teste: resposta HTTP; para HLS, manifesto e primeiro segmento/variante identificável.\n")
        f.write("- Mede acessibilidade no runner do GitHub, não qualidade de imagem, bitrate sustentado ou funcionamento no aparelho.\n")
        f.write("- Nenhuma URL ou playlist foi alterada.\n\n## Resumo\n\n")
        for key, value in sorted(counts.items()):
            f.write(f"- **{key}:** {value}\n")
        f.write("\n## Resultados que precisam de atenção\n\n")
        attention = [r for r in rows if r["status"] != "OK"]
        if not attention:
            f.write("Nenhuma falha detectada nesta execução.\n")
        else:
            f.write("| Canal | Estado | Detalhe | Latência |\n|---|---|---|---:|\n")
            for r in attention:
                detail = r["detalhe"].replace("|", "\\|")
                f.write(f"| {r['canal']} | {r['status']} | {detail} | {r['latencia_ms']} ms |\n")
        f.write("\nO CSV anexo contém os resultados completos; parâmetros de consulta das URLs foram omitidos.\n")
    print("Relatórios gerados:", csv_path, md_path, "Resumo:", counts)


if __name__ == "__main__":
    main()
