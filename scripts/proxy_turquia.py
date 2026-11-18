#!/usr/bin/env python3
"""Valida proxies públicos com saída na Turquia contra Tv.m3u; não altera a playlist."""
import csv, os, re, sys, time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests

PLAYLIST = Path(os.getenv("PLAYLIST_FILE", "Tv.m3u"))
SOURCES = {
    "http": "https://proxyspace.pro/country/tr/http.txt",
    "socks5": "https://proxyspace.pro/country/tr/socks5.txt",
}
IP_CHECK = "https://ipapi.co/json/"
MAX_CANDIDATES = 35
MAX_GOOD = 3
WORKERS = 12

def fetch(url):
    r = requests.get(url, timeout=15)
    r.raise_for_status()
    return r.text

def read_channels():
    rows, name = [], "Canal sem nome"
    for raw in PLAYLIST.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw.strip()
        if line.startswith("#EXTINF"):
            name = line.rsplit(",", 1)[-1].strip() or "Canal sem nome"
        elif line.startswith(("http://", "https://")):
            rows.append((name, line))
            name = "Canal sem nome"
    return rows

def proxy_uri(kind, endpoint):
    scheme = "socks5h" if kind == "socks5" else "http"
    return scheme + "://" + endpoint

def validate_proxy(kind, endpoint):
    uri = proxy_uri(kind, endpoint)
    try:
        start = time.monotonic()
        r = requests.get(IP_CHECK, proxies={"http": uri, "https": uri}, timeout=(5, 10))
        r.raise_for_status()
        data = r.json()
        if str(data.get("country_code", "")).upper() != "TR":
            return None
        return {"kind": kind, "endpoint": endpoint, "uri": uri,
                "ip": data.get("ip", ""), "latency_ms": round((time.monotonic()-start)*1000)}
    except Exception:
        return None

def test_stream(name, url, proxy):
    start = time.monotonic()
    try:
        with requests.get(url, proxies={"http": proxy["uri"], "https": proxy["uri"]},
                          timeout=(8, 12), stream=True,
                          headers={"User-Agent": "Mozilla/5.0 IPTV-Link-Checker/1.0",
                                   "Range": "bytes=0-2047"}) as r:
            sample = next(r.iter_content(2048), b"")
            ok = r.status_code in (200, 206) and bool(sample)
            return {"channel": name, "url": url, "proxy": proxy["endpoint"],
                    "type": proxy["kind"], "status": r.status_code,
                    "latency_ms": round((time.monotonic()-start)*1000),
                    "result": "ACESSÍVEL" if ok else "FALHOU"}
    except Exception as exc:
        return {"channel": name, "url": url, "proxy": proxy["endpoint"],
                "type": proxy["kind"], "status": "", 
                "latency_ms": round((time.monotonic()-start)*1000),
                "result": "FALHOU: " + str(exc)[:140]}

def main():
    if not PLAYLIST.exists():
        print("Playlist não encontrada: " + str(PLAYLIST), file=sys.stderr)
        return 2
    channels = read_channels()
    if not channels:
        print("Nenhum link HTTP(S) encontrado.", file=sys.stderr)
        return 2

    candidates = []
    for kind, source in SOURCES.items():
        try:
            items = [x.strip() for x in fetch(source).splitlines()
                     if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}:\d{1,5}", x.strip())]
            candidates.extend((kind, x) for x in items[:MAX_CANDIDATES])
        except Exception as exc:
            print("Falha ao obter proxies " + kind + ": " + str(exc))

    good = []
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        futures = [pool.submit(validate_proxy, k, e) for k, e in candidates]
        for future in as_completed(futures):
            result = future.result()
            if result:
                good.append(result)
    good.sort(key=lambda x: x["latency_ms"])
    good = good[:MAX_GOOD]

    out = Path("relatorio-proxy-turquia")
    out.mkdir(exist_ok=True)
    with open(out / "proxies-turcos.csv", "w", newline="", encoding="utf-8") as f:
        fields = ["kind", "endpoint", "ip", "latency_ms"]
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows([{k: p[k] for k in fields} for p in good])

    if not good:
        (out / "resultado.md").write_text(
            "# Teste de proxy turco\n\nNenhum proxy passou na validação de IP turco nesta execução.\n",
            encoding="utf-8")
        print("Nenhum proxy turco validado.")
        return 0

    results = []
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        futures = [pool.submit(test_stream, name, url, proxy)
                   for proxy in good for name, url in channels]
        for future in as_completed(futures):
            results.append(future.result())
    results.sort(key=lambda x: (x["channel"].casefold(), x["type"], x["proxy"]))

    fields = ["channel", "url", "proxy", "type", "status", "latency_ms", "result"]
    with open(out / "canais.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(results)

    ok = sum(x["result"] == "ACESSÍVEL" for x in results)
    lines = ["# Relatório — proxies turcos", "",
             "- Canais: **" + str(len(channels)) + "**",
             "- Proxies validados com IP TR: **" + str(len(good)) + "**",
             "- Testes: **" + str(len(results)) + "**",
             "- Respostas acessíveis: **" + str(ok) + "**",
             "- Falhas: **" + str(len(results)-ok) + "**", "",
             "> Teste pontual HTTP/HLS; não confirma reprodução contínua nem autorização do provedor.", "",
             "## Proxies aprovados", ""]
    for p in good:
        lines.append("- " + p["kind"] + " " + p["endpoint"] + " — IP " + p["ip"] +
                     ", " + str(p["latency_ms"]) + " ms")
    lines += ["", "## Canais", "", "| Canal | Proxy | HTTP | Latência | Resultado |",
              "|---|---|---:|---:|---|"]
    for x in results:
        lines.append("| " + x["channel"].replace("|", "/") + " | " + x["proxy"] +
                     " (" + x["type"] + ") | " + str(x["status"]) + " | " +
                     str(x["latency_ms"]) + " ms | " + x["result"] + " |")
    (out / "resultado.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("Concluído: " + str(len(good)) + " proxies turcos; " + str(ok) +
          " respostas acessíveis; " + str(len(results)-ok) + " falhas.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
