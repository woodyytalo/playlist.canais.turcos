# Monitoramento das listas IPTV

Este repositório usa três ferramentas complementares no workflow `.github/workflows/iptv-monitoramento.yml`.

## Ferramentas

1. **Dearbulut IPTV Nexus** — consulta externa ao estado agregado dos streams e ao catálogo turco. Os dados são guardados em `reports/dearbulut/` como referência e descoberta; não substituem automaticamente URLs personalizadas da playlist.
   - Projeto: https://github.com/dearbulut/iptv
   - Saúde: https://dearbulut.github.io/iptv/api/v1/health.json
   - Canais turcos: https://dearbulut.github.io/iptv/api/v1/by-country/tr.json

2. **IPTV-org `playlist:test`** — executa teste de conectividade das URLs das listas. O workflow não usa a opção `--fix`; portanto, não remove links nem modifica as playlists originais.
   - Projeto: https://github.com/iptv-org/iptv
   - Documentação: https://github.com/iptv-org/iptv/blob/master/docs/scripts.md

3. **IPTV-CHECK** — testa streams e gera cópias M3U contendo os links que passaram no teste. Essas cópias ficam em `reports/iptv-check/` como resultado para revisão; nunca são copiadas por cima das playlists originais.
   - Projeto: https://github.com/peterpt/IPTV-CHECK

## Listas monitoradas

A TV principal é processada primeiro, seguida por TV2, Euro, TVT e Backup. O workflow roda a cada seis horas e também pode ser iniciado manualmente.

## Segurança

- Nenhuma ferramenta recebe autorização para apagar canais da playlist original.
- Falhas isoladas não provocam substituição automática.
- As listas filtradas são relatórios para revisão, não substituições automáticas.
- Os relatórios ficam disponíveis como artefato do GitHub Actions por 14 dias.

## Observação

Os testes dependem da conectividade do runner do GitHub. Restrições geográficas, cabeçalhos HTTP exigidos por algumas emissoras e bloqueios temporários podem gerar falsos negativos. Confirme canais importantes no aplicativo de IPTV antes de substituir um link.
