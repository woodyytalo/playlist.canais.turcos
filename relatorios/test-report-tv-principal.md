# Relatório de teste — TV principal

**Repositório:** woodyytalo/playlist.canais.turcos  
**Branch:** github/workflows/atualizar-logos.yml  
**Playlist analisada:** `Tv.m3u`  
**Arquivo:** TV principal

## Resultado da inspeção estrutural

| Verificação | Resultado |
|---|---:|
| Entradas de canais (`#EXTINF`) | 206 |
| Entradas com atributo `tvg-logo` | 206 |
| Entradas sem atributo `tvg-logo` | 0 |

## Escopo

Esta inspeção contou as entradas e verificou apenas a presença do atributo `tvg-logo` nas linhas `#EXTINF`.

## Limitações

- A presença de `tvg-logo` não confirma que a imagem PNG/URL abre ou corresponde ao canal.
- Não foi realizado teste de reprodução dos streams.
- Não foi validada a disponibilidade ao vivo, estabilidade, resolução ou desempenho de buffer.
- A existência de um `tvg-id` não garante correspondência de programação XMLTV.

## Próximas verificações recomendadas

1. Validar individualmente os endereços das logos e identificar imagens ausentes ou inválidas.
2. Testar os streams da TV principal e registrar falhas sem misturar links entre canais.
3. Conferir o mapeamento de cada canal com o guia XMLTV.

**Status:** inspeção estrutural concluída; testes de imagem, transmissão e EPG não realizados nesta execução.
