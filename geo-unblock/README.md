# Gateway híbrido VPN + proxy HLS (Turquia)

Este diretório prepara um gateway: WireGuard encaminha a saída de rede por um endpoint VPN turco e Nginx publica rotas HLS fixas para os canais configurados.

## Requisitos

- VPS/servidor Linux com Docker Compose e acesso público (ou acesso pela rede local).
- Provedor VPN que forneça configuração WireGuard e permita saída na Turquia.
- Autorização para acessar e retransmitir os streams. O gateway não contorna autenticação, DRM, tokens, paywalls ou controles de acesso do provedor.

O GitHub Actions não hospeda um proxy permanente: runners são temporários. Este serviço deve rodar em uma VPS. O repositório guarda apenas os arquivos de implantação; as credenciais ficam no servidor.

## Instalação

1. Copie este diretório para uma VPS.
2. Copie `.env.example` para `.env` e preencha os dados WireGuard do provedor.
3. Proteja o arquivo: `chmod 600 .env`. Não envie o arquivo `.env ao GitHub.
4. Inicie: `docker compose up -d`.
5. Confira o túnel e os logs: `docker compose logs -f vpn hls-proxy`.
6. Teste `http://IP-DA-VPS:8080/health`. Restrinja a porta 8080 por firewall à sua rede/IP; não exponha publicamente sem autenticação ou uma camada segura.

## Rotas preparadas

- `/gzt/playlist.m3u8`
- `/power-tv/playlist.m3u8`
- `/4u-family/stream.m3u8`
- `/bein-sports-1-turk/index.m3u8`

As rotas são exemplos de proxy reverso para os quatro endereços atualmente adicionados à TV principal. A compatibilidade depende de como cada origem entrega playlists, segmentos, redirecionamentos e tokens. Uma resposta HTTP 200 não comprova reprodução; teste cada canal em um player.

## Integração com a playlist

Depois de instalar e testar o gateway, substitua na TV principal apenas as URLs dos canais que funcionarem pelo endereço correspondente, por exemplo:

`http://IP-DA-VPS:8080/gzt/playlist.m3u8`

Não troque os links da playlist por endereços locais fictícios antes de o servidor estar ativo. As URLs atuais da TV principal permanecem inalteradas nesta etapa.

## Segurança e limitações

- Use apenas credenciais VPN próprias e canais cujo acesso/retransmissão você esteja autorizado a utilizar.
- Não publique chaves WireGuard, tokens ou arquivos `.env`.
- A VPN só altera a rota de saída do servidor; não garante que a plataforma aceite o acesso.
- Se o fornecedor exigir cookies, cabeçalhos, token dinâmico ou DRM, esta configuração simples não será suficiente.
- Use HTTPS e autenticação antes de permitir acesso externo ao gateway.
