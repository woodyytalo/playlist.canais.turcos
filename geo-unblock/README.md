# Gateway VPN + publicação da TV principal

Este diretório publica o arquivo integral `Tv.m3u` por meio do gateway Nginx. A configuração não mantém mais rotas individuais para GZT, Power TV, 4U Family ou beIN Sports 1 Turk: a fonte da playlist é o arquivo principal do repositório.

## Requisitos

- VPS/servidor Linux com Docker Compose.
- Provedor VPN que forneça configuração WireGuard e permita saída na Turquia, caso seja necessário usar saída turca.
- Autorização para acessar os streams.

O GitHub Actions não hospeda um proxy permanente. O serviço precisa rodar em uma VPS. As credenciais VPN ficam no servidor, nunca no repositório.

## Instalação

1. Copie/clonar o repositório para a VPS.
2. Entre em `geo-unblock`.
3. Copie `.env.example` para `.env` e preencha os dados WireGuard do seu provedor.
4. Proteja o arquivo: `chmod 600 .env`. Não envie `.env` ao GitHub.
5. Inicie com `docker compose up -d`.
6. Confira os logs: `docker compose logs -f vpn hls-proxy`.
7. Teste `http://IP-DA-VPS:8080/health`.
8. Abra `http://IP-DA-VPS:8080/tv-principal.m3u` no player IPTV.

## Fonte da playlist

O Docker monta `../Tv.m3u` diretamente em Nginx como `/tv-principal.m3u`. Assim, a integração publica a TV principal completa, mantendo nomes, categorias, logos e links individuais do arquivo original. Para refletir alterações futuras, atualize o repositório na VPS e recrie/reinicie o serviço se necessário.

## Limitação importante

Esta configuração serve a playlist integral, mas **não transforma automaticamente os links de cada canal em links do proxy**. Os endereços dentro de `Tv.m3u` continuam sendo os originais; portanto, a publicação da lista não garante desbloqueio geográfico por canal. Para retransmitir os streams pela VPN, é necessário um proxy HLS com roteamento e reescrita de manifests/segmentos compatível com cada provedor. Não substitua os links originais por endereços locais antes de implementar e testar essa camada.

Uma resposta HTTP 200 em `/health` confirma apenas que o Nginx responde, não que os canais reproduzem. Restrinja a porta 8080 por firewall e use HTTPS/autenticação antes de expor o gateway externamente.

## Segurança

- Use credenciais WireGuard próprias e canais cujo acesso/retransmissão você esteja autorizado a utilizar.
- Não publique chaves WireGuard, tokens ou arquivos `.env`.
- A VPN não contorna DRM, autenticação, paywalls ou outras restrições de acesso.
