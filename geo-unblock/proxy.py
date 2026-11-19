import asyncio
import base64
import hashlib
import hmac
import os
import re
from urllib.parse import urljoin, urlsplit

import aiohttp
from aiohttp import web

PLAYLIST = os.getenv("PLAYLIST_PATH", "/data/Tv.m3u")
SECRET = os.environ["PROXY_SIGNING_KEY"].encode()
PORT = int(os.getenv("PORT", "8080"))
TIMEOUT = aiohttp.ClientTimeout(total=45, connect=15)
SESSION = None

def token_for(url: str) -> str:
    raw = url.encode()
    payload = base64.urlsafe_b64encode(raw).decode().rstrip("=")
    sig = hmac.new(SECRET, payload.encode(), hashlib.sha256).hexdigest()
    return payload + "." + sig

def url_from_token(token: str) -> str:
    try:
        payload, sig = token.rsplit(".", 1)
        expected = hmac.new(SECRET, payload.encode(), hashlib.sha256).hexdigest()
        if not hmac.compare_digest(sig, expected):
            raise ValueError("assinatura inválida")
        raw = base64.urlsafe_b64decode(payload + "=" * (-len(payload) % 4))
        url = raw.decode()
        parts = urlsplit(url)
        if parts.scheme not in ("http", "https") or not parts.hostname:
            raise ValueError("URL inválida")
        if parts.username or parts.password:
            raise ValueError("credenciais embutidas não permitidas")
        return url
    except Exception as exc:
        raise web.HTTPForbidden(text="URL de proxy inválida") from exc

def proxied(url: str) -> str:
    return "/p/" + token_for(url)

def rewrite_manifest(text: str, base_url: str) -> str:
    out = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            out.append(line)
        elif stripped.startswith("#"):
            # Reescreve URIs de chaves, mapas, legendas e outros atributos HLS.
            def replace_uri(match):
                absolute = urljoin(base_url, match.group(2))
                return match.group(1) + proxied(absolute) + match.group(3)
            line = re.sub(r'(URI=")([^"]+)(")', replace_uri, line)
            out.append(line)
        else:
            out.append(proxied(urljoin(base_url, stripped)))
    return "\n".join(out) + "\n"

async def health(_request):
    return web.Response(text="ok\n", content_type="text/plain")

async def playlist(_request):
    try:
        with open(PLAYLIST, "r", encoding="utf-8-sig") as f:
            source = f.read()
    except OSError as exc:
        raise web.HTTPServiceUnavailable(text="Tv.m3u indisponível") from exc

    lines = source.splitlines()
    result = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("http://") or stripped.startswith("https://"):
            result.append(proxied(stripped))
        else:
            result.append(line)
    body = "\n".join(result) + "\n"
    return web.Response(
        text=body,
        content_type="application/vnd.apple.mpegurl",
        headers={"Cache-Control": "no-store", "Access-Control-Allow-Origin": "*"},
    )

async def stream(request):
    url = url_from_token(request.match_info["token"])
    headers = {"User-Agent": "Mozilla/5.0 (compatible; TV-HLS-Proxy/1.0)"}
    if request.headers.get("Range"):
        headers["Range"] = request.headers["Range"]
    try:
        async with SESSION.get(url, headers=headers, allow_redirects=True) as upstream:
            data = await upstream.read()
            if upstream.status >= 400:
                raise web.HTTPBadGateway(text=f"Origem respondeu HTTP {upstream.status}")
            content_type = upstream.headers.get("Content-Type", "application/octet-stream")
            if "mpegurl" in content_type.lower() or data.lstrip().startswith(b"#EXTM3U"):
                try:
                    text = data.decode("utf-8-sig")
                except UnicodeDecodeError:
                    raise web.HTTPBadGateway(text="Manifest HLS não está em UTF-8")
                body = rewrite_manifest(text, str(upstream.url))
                return web.Response(
                    text=body,
                    content_type="application/vnd.apple.mpegurl",
                    headers={"Cache-Control": "no-store", "Access-Control-Allow-Origin": "*"},
                )
            response_headers = {"Access-Control-Allow-Origin": "*"}
            for key in ("Content-Range", "Accept-Ranges"):
                if key in upstream.headers:
                    response_headers[key] = upstream.headers[key]
            return web.Response(
                body=data,
                status=upstream.status,
                content_type=content_type,
                headers=response_headers,
            )
    except web.HTTPException:
        raise
    except (aiohttp.ClientError, asyncio.TimeoutError) as exc:
        raise web.HTTPBadGateway(text="Falha ao buscar o stream de origem") from exc

async def on_startup(app):
    global SESSION
    SESSION = aiohttp.ClientSession(timeout=TIMEOUT)

async def on_cleanup(app):
    if SESSION:
        await SESSION.close()

app = web.Application(client_max_size=2 * 1024 * 1024)
app.router.add_get("/health", health)
app.router.add_get("/tv-principal.m3u", playlist)
app.router.add_get("/p/{token}", stream)
app.on_startup.append(on_startup)
app.on_cleanup.append(on_cleanup)

if __name__ == "__main__":
    web.run_app(app, host="0.0.0.0", port=PORT)
