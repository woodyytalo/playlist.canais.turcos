# Proxy HLS da TV principal com saída VPN na Turquia

Este serviço converte os endereços HTTP(S) da playlist em rotas do proxy e retransmite manifests HLS, segmentos e recursos HLS (por exemplo, chaves e mapas) pela rede do contêiner VPN.

## Requisitos

- VPS Linux ligada continuamente, com Docker Compose e suporte a `/dev/net/tun`.
- Provedor WireGuard com endpoint e saída de internet na Turquia.
- Autorização para acessar e retransmitir os streams.
- Domínio e HTTPS recomendados antes de disponibilizar a playlist publicamente.

O GitHub Actions não é um servidor de streaming permanente. As chaves VPN e a chave de assinatura devem existir somente no arquivo `.env` da VPS, nunca no repositório ou nesta conversa.

## Configuração na VPS

1. Clone o repositório e entre em `geo-unblock`.
2. Copie `.env.example` para `.env`.
3. Preencha os campos WireGuard com o perfil fornecido pelo seu provedor. Use o endpoint localizado na Turquia e confirme que a rota é full-tunnel.
4. Gere uma chave aleatória longa para `PROXY_SIGNING_KEY` (pelo menos 32 bytes).
5. Proteja o arquivo: `chmod 600 .env`.
6. Inicie: `docker compose up -d --build`.
7. Confira: `docker compose logs -f vpn hls-proxy`.
8. Teste `http://IP-DA-VPS:8080/health` e depois `http://IP-DA-VPS:8080/tv-principal.m3u`.

## Como funciona

- `/tv-principal.m3u` publica a TV principal com cada URL de stream encaminhada para uma rota assinada do proxy.
- `/p/{token}` busca o recurso de origem pela conexão de rede do contêiner VPN.
- Manifests HLS são reescritos para que variantes, segmentos e URIs HLS relacionados também passem pelo proxy.
- Nomes, categorias, logos e metadados da playlist são preservados.

## Limitações e segurança

- Esta implementação é voltada a HLS sobre HTTP(S). DASH, DRM, autenticação proprietária, cookies específicos, tokens que expiram, restrições de referer/origin e protocolos não HLS podem exigir adaptações por provedor.
- Alguns provedores entregam segmentos em domínios CDN diferentes ou exigem cabeçalhos especiais. Teste canal por canal antes de trocar a playlist usada no aplicativo.
- A VPN não contorna DRM, autenticação, paywalls ou direitos de transmissão.
- O proxy encaminha dados e consome banda da VPS. Dimensione CPU, memória e tráfego conforme o número de espectadores.
- Não exponha a porta diretamente à internet sem HTTPS, autenticação e firewall. Restrinja o acesso à playlist e ao proxy.
- O token assinado impede que a rota seja usada como um proxy aberto arbitrário; mantenha `PROXY_SIGNING_KEY` secreta.
- Um HTTP 200 em `/health` confirma somente que o processo responde. É necessário testar a reprodução real de cada canal.

**Importante:** o repositório recebe apenas o código. A ativação real depende da VPS, do perfil WireGuard turco e dos testes de reprodução. Não altere o link de playlist do aplicativo antes desses testes.
