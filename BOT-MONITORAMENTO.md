# Bot de monitoramento — modo seguro

O arquivo bot-monitoramento.py lê Tv.m3u sem editar a playlist. Para cada URL HTTP(S),
verifica a resposta HTTP; quando identifica HLS, verifica também o manifesto e
o primeiro segmento ou a primeira variante disponível.

## Execução automática
O workflow .github/workflows/monitorar-canais.yml roda a cada 6 horas (UTC)
e também pode ser iniciado manualmente na aba Actions do GitHub.

## Resultados
Abra a execução mais recente em Actions e baixe o artefato relatorio-canais-N.
Ele contém um relatório Markdown e um CSV detalhado, retidos por 30 dias.

## Limitações
- O resultado representa o acesso a partir do runner do GitHub, não do aparelho ou da rede do usuário.
- Um teste curto não mede estabilidade contínua, bitrate sustentado, qualidade de imagem ou buffering real.
- CDNs podem bloquear IPs de datacenter ou exigir cabeçalhos/cookies; isso pode gerar falso negativo.
- O bot não procura links alternativos, não troca URLs e não grava nas playlists.
- URLs com parâmetros de consulta são omitidas dos relatórios por segurança.

Qualquer correção automática exigirá uma etapa separada, validação da alternativa,
backup e aprovação explícita.
