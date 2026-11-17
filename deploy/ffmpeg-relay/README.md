# Relay FFmpeg — TV principal

Base de implantação em VPS. O serviço lê a playlist original em modo somente leitura e cria saída HLS transcodificada sob demanda. Não altera Tv.m3u, links de origem, logos, nomes ou categorias.

## Taxa de vídeo

Padrão: vídeo alvo 8.500 kbit/s, pico 9.000 kbit/s e áudio AAC 192 kbit/s. A soma fica próxima da meta de 10 Mbps, mas não é uma garantia de taxa constante: depende da origem, da complexidade do vídeo e do encoder. A resolução original é preservada; uma origem SD não ganha qualidade real ao ser codificada em 10 Mbps.

## Recursos e limites

- HLS com segmentos de 4 segundos e lista móvel de 6 segmentos.
- Reconexão FFmpeg para falhas de rede.
- Limite inicial de 4 transcodificações simultâneas (MAX_CONCURRENT=4).
- Isso não transcodifica os 207 canais ao mesmo tempo. Para isso, dimensione CPU/GPU, RAM, rede e armazenamento, faça testes de carga e aumente o limite gradualmente.
- Teste HTTP e saída HLS não garantem reprodução sem travamentos em todo aparelho.

## Instalação em VPS Linux com Docker Compose

1. Copie esta pasta para a VPS.
2. Copie Tv.m3u para uma pasta data/ ao lado do docker-compose.yml.
3. Defina um token longo e aleatório na variável RELAY_TOKEN.
4. Inicie com docker compose up -d --build.
5. Consulte /health e depois /channels?token=SEU_TOKEN.
6. Teste as URLs HLS retornadas em um cliente IPTV antes de migrar qualquer canal.

Exemplo de docker-compose.yml:

    services:
      tv-relay:
        build: .
        container_name: tv-principal-ffmpeg
        restart: unless-stopped
        environment:
          RELAY_TOKEN: "SUBSTITUA_POR_UM_TOKEN_LONGO_E_ALEATORIO"
          MAX_CONCURRENT: "4"
          VIDEO_BITRATE: "8500k"
          VIDEO_MAXRATE: "9000k"
          AUDIO_BITRATE: "192k"
        ports:
          - "8080:8080"
        volumes:
          - ./data:/data

PLAYLIST_PATH usa /data/Tv.m3u por padrão. Proteja a porta com firewall e HTTPS/reverse proxy antes de expor o serviço à internet. Não publique o token.

## Antes de migrar os links

O serviço não substitui automaticamente os endereços da playlist principal. Primeiro é necessário instalar em uma VPS, testar alguns canais, medir consumo e confirmar compatibilidade com IPTV Pro. Só depois disso deve ser feita qualquer migração dos links.
