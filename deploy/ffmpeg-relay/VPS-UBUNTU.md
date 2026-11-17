# Instalação em VPS Ubuntu

## Requisitos e limitações

- Ubuntu Server 22.04 ou 24.04 atualizado.
- Acesso SSH com sudo/root.
- Recomenda-se começar com 4 vCPUs, 8 GB RAM e armazenamento SSD; a capacidade real depende dos codecs, resolução e estabilidade das origens. Faça teste de carga antes de aumentar concorrência.
- Rede de saída suficiente para receber os canais e rede de entrada suficiente para servir os espectadores.
- Esta primeira versão limita a 4 canais transcodificados simultaneamente. Não transcodifica os 207 canais todos ao mesmo tempo.
- O script instala o serviço, mas não cria uma VPS, não contrata hospedagem e não configura domínio/HTTPS.

## Instalação automatizada

No Ubuntu, copie o script para a VPS e execute:

    sudo bash install-vps.sh

O instalador:
1. Instala Git, Docker Engine e Docker Compose v2 pelos pacotes do Ubuntu.
2. Baixa a branch do repositório.
3. Copia a playlist Tv.m3u para a área de dados do serviço.
4. Gera um token aleatório privado no arquivo .env (permissão 600).
5. Constrói a imagem e inicia o container.

O compose publica a porta somente em 127.0.0.1:8080. Isso evita expor o serviço diretamente à internet. Para acesso externo, configure um proxy reverso com HTTPS e autenticação/firewall. Não abra a porta 8080 publicamente.

## Comandos úteis

    cd /opt/tv-principal-relay/deploy/ffmpeg-relay
    sudo docker compose ps
    sudo docker compose logs -f --tail=100
    curl http://127.0.0.1:8080/health

Para obter a lista HLS, leia o token localmente sem publicá-lo:

    sudo bash -c 'source .env; curl -fsS "http://127.0.0.1:8080/channels?token=$RELAY_TOKEN"'

## Atualizar playlist

O instalador copia a playlist no primeiro provisionamento. Para atualizar a cópia de trabalho depois de revisar a playlist no GitHub:

    cd /opt/tv-principal-relay
    sudo git pull --ff-only origin "github/workflows/atualizar-logos.yml"
    sudo install -m 0644 Tv.m3u deploy/ffmpeg-relay/data/Tv.m3u

A atualização da playlist não muda a playlist do repositório e não redireciona automaticamente clientes IPTV para o relay.

## Segurança e produção

- Mantenha o arquivo .env privado; contém credencial de acesso.
- Configure HTTPS com proxy reverso (por exemplo, Caddy ou Nginx) antes de acesso externo.
- Não publique o token em prints, listas M3U ou mensagens.
- Monitore CPU, RAM, temperatura, rede e logs.
- O limite de concorrência é deliberadamente conservador. Aumente somente após teste real.
- A taxa configurada é um alvo de encoder, não garantia de 10 Mbps constante nem melhoria da qualidade de uma origem SD.
- Teste um canal por vez no IPTV Pro. Só migre os links após validar estabilidade, latência e consumo.
