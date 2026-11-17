#!/usr/bin/env bash
set -Eeuo pipefail

REPO_URL="https://github.com/woodyytalo/playlist.canais.turcos.git"
BRANCH="github/workflows/atualizar-logos.yml"
INSTALL_DIR="/opt/tv-principal-relay"
SOURCE_DIR="$INSTALL_DIR/deploy/ffmpeg-relay"

if [[ "$(id -u)" -ne 0 ]]; then
  echo "Execute como root: sudo bash install-vps.sh"
  exit 1
fi

if ! grep -qiE 'ubuntu' /etc/os-release; then
  echo "Este instalador foi preparado para Ubuntu Server. Em outra distribuição, siga o VPS-UBUNTU.md manualmente."
  exit 1
fi

export DEBIAN_FRONTEND=noninteractive
apt-get update
apt-get install -y git docker.io docker-compose-v2 openssl
systemctl enable --now docker

if ! docker compose version >/dev/null 2>&1; then
  echo "Docker Compose v2 não foi instalado. Verifique os pacotes da sua versão do Ubuntu."
  exit 1
fi

if [[ -d "$INSTALL_DIR/.git" ]]; then
  git -C "$INSTALL_DIR" fetch origin "$BRANCH"
  git -C "$INSTALL_DIR" checkout "$BRANCH"
  git -C "$INSTALL_DIR" pull --ff-only origin "$BRANCH"
else
  git clone --single-branch --branch "$BRANCH" "$REPO_URL" "$INSTALL_DIR"
fi

if [[ ! -s "$INSTALL_DIR/Tv.m3u" ]]; then
  echo "Tv.m3u não foi encontrado no checkout. Nada será iniciado."
  exit 1
fi

mkdir -p "$SOURCE_DIR/data"
install -m 0644 "$INSTALL_DIR/Tv.m3u" "$SOURCE_DIR/data/Tv.m3u"
cd "$SOURCE_DIR"

if [[ ! -f .env ]]; then
  TOKEN="$(openssl rand -hex 32)"
  umask 077
  printf 'RELAY_TOKEN=%s\nMAX_CONCURRENT=4\nVIDEO_BITRATE=8500k\nVIDEO_MAXRATE=9000k\nAUDIO_BITRATE=192k\n' "$TOKEN" > .env
  chmod 600 .env
  echo "Token privado criado em $SOURCE_DIR/.env (não compartilhe esse arquivo)."
else
  chmod 600 .env
  echo "Arquivo .env existente preservado."
fi

docker compose up -d --build
echo
echo "Instalação concluída. O serviço está vinculado somente a 127.0.0.1:8080."
echo "Verificação local: curl http://127.0.0.1:8080/health"
echo "Para consultar canais, use o token guardado em $SOURCE_DIR/.env."
echo "Configure HTTPS e proxy reverso antes de disponibilizar o serviço externamente."
