# Bot de proxy HLS pela VPN Gate da Turquia

Este modo usa OpenVPN (não WireGuard) e o servidor público turco listado como `vpn849808880.opengw.net`. A listagem consultada informa OpenVPN UDP na porta 1195. Servidores públicos podem mudar de IP, ficar offline ou limitar tráfego; deixe o endpoint definido no perfil `.ovpn` fornecido pelo VPN Gate e valide o país de saída antes de usar.

## O que já está preparado

- `docker-compose.vpngate.yml`: túnel OpenVPN + proxy HLS.
- `proxy.py`: publica `/tv-principal.m3u` e encaminha manifests HLS, segmentos e URIs relacionados pela rede do túnel.
- A playlist original `Tv.m3u` é montada somente para leitura; não é modificada.

## O que falta para ativar

1. Uma VPS Linux ligada continuamente, com Docker Compose e `/dev/net/tun`.
2. Baixar o perfil OpenVPN `.ovpn` do servidor `vpn849808880.opengw.net` no VPN Gate/VPNHub. A página VPNHub exige compartilhar a página para liberar o arquivo; não é necessário publicar o perfil no GitHub.
3. Colocar o arquivo baixado em `geo-unblock/client.ovpn` na VPS. Não faça commit dele.
4. Copiar `.env.vpngate.example` para `.env.vpngate` e gerar uma chave de assinatura:
   `openssl rand -hex 32`
   Cole o resultado em `PROXY_SIGNING_KEY`. Confirme no perfil/provedor as credenciais OpenVPN; VPN Gate normalmente usa usuário e senha `vpn`, mas o perfil/servidor deve ser a referência final.
5. Proteger o arquivo: `chmod 600 .env.vpngate client.ovpn`.
6. Dentro de `geo-unblock`, iniciar:
   `docker compose --env-file .env.vpngate -f docker-compose.vpngate.yml up -d --build`
7. Conferir os logs: `docker compose --env-file .env.vpngate -f docker-compose.vpngate.yml logs -f vpn hls-proxy`.
8. Testar `http://IP-DA-VPS:8080/health` e `http://IP-DA-VPS:8080/tv-principal.m3u`. Antes de trocar a lista no aplicativo, validar o IP de saída como país TR e testar reprodução HLS real.

## Endereço da lista convertida

Depois que a VPS estiver ativa e protegida com HTTPS/autenticação, a lista será publicada em:

`https://SEU-DOMINIO/tv-principal.m3u`

Não use o endereço HTTP público acima em produção. Restrinja a porta 8080 por firewall até configurar TLS e autenticação.

## Limitações

- O serviço é proxy HLS para URLs HTTP/HTTPS; não garante compatibilidade com DASH, DRM, cookies, cabeçalhos proprietários, tokens expirados ou autenticação do provedor.
- A VPS retransmite o vídeo e consome banda de saída. O servidor VPN Gate é público e não oferece garantia de disponibilidade, velocidade ou privacidade; a página de servidores informa política de logs de duas semanas.
- O código não cria um servidor VPN por conta própria. Sem o perfil `.ovpn` válido e a VPS em execução, não há conexão ativa.
- Não contorna DRM, paywalls nem direitos de transmissão.
