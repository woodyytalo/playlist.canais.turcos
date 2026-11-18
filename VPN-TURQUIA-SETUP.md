# Configurar a VPN da Turquia no GitHub Actions

O workflow `.github/workflows/vpn-turquia.yml` conecta um runner temporário do GitHub Actions a um perfil WireGuard e testa os links HTTP/HTTPS de `Tv.m3u` pelo túnel.

## 1. Obter um perfil WireGuard turco

1. Gere/baixe um perfil WireGuard em um provedor que ofereça servidor na Turquia.
2. Confirme no painel do provedor que o perfil é para Turquia (TR/Istambul).
3. O perfil precisa ser de túnel completo IPv4: em `[Peer]`, `AllowedIPs` deve incluir `0.0.0.0/0`.
4. Não publique o arquivo `.conf` no repositório nem em Issues.

O workflow não fornece VPN nem credenciais. Perfis gratuitos podem expirar, ter limites ou deixar de funcionar.

## 2. Cadastrar o segredo

No repositório, abra **Settings → Secrets and variables → Actions → New repository secret**.

- **Name:** `TURKEY_WG_CONF`
- **Secret:** cole o conteúdo completo do arquivo WireGuard, incluindo as seções `[Interface]` e `[Peer]`.

Salve. Não coloque a configuração em arquivos públicos, commits, variáveis comuns ou mensagens de log.

## 3. Executar

Abra **Actions → VPN Turquia - testar TV principal → Run workflow**.

O workflow também executa automaticamente a cada 12 horas e quando `Tv.m3u` ou o próprio workflow é alterado.

## 4. Consultar o resultado

Na execução, confira:
- se a rota de saída está usando a interface WireGuard;
- se o país do IP público foi identificado como `TR`;
- o resultado HTTP de cada URL da playlist.

Baixe o artefato **relatorio-vpn-turquia** para obter os relatórios CSV e Markdown. Os artefatos ficam disponíveis por 14 dias.

## Limitações importantes

- O runner do GitHub é temporário: a VPN é desligada ao final da execução.
- Isso verifica os links a partir de um IP turco; não transforma a playlist em um proxy contínuo e não retransmite vídeo para o aplicativo IPTV.
- Um status HTTP 2xx/3xx confirma apenas que o servidor respondeu ao teste; não garante reprodução, áudio, estabilidade ou compatibilidade HLS.
- O workflow não altera `Tv.m3u` nem substitui links.
