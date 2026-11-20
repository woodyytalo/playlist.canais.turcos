# Fontes de logos de canais turcos

Este documento reúne as fontes identificadas para localizar, conferir e obter logos de canais da Turquia. As fontes estão separadas por tipo para evitar que catálogos de operadoras sejam tratados como arquivos de imagens em lote.

## 1. Repositórios e catálogos de imagens

| Fonte | Endereço | Tipo | Uso |
|---|---|---|---|
| TVLogo.org — Turquia | https://www.tvlogo.org/turkey/ | Diretório de imagens PNG | Fonte direta de arquivos de logos; conferir a versão e o canal antes de usar. |
| tv-logo/tv-logos — Turkey | https://github.com/tv-logo/tv-logos/tree/main/countries/turkey | Repositório GitHub | Fonte direta de imagens; já contemplada pela rotina de catálogo do projeto. |
| Wikimedia Commons — logos de canais turcos | https://commons.wikimedia.org/wiki/Category:Logos_of_television_channels_in_Turkey | Biblioteca de mídia | Imagens com metadados de autoria/licença; verificar cada arquivo. |
| Wikimedia Commons — logos SVG | https://commons.wikimedia.org/wiki/Category:SVG_logos_of_television_channels_in_Turkey | Biblioteca de vetores | Logos vetoriais que podem ser convertidas para PNG. |
| Wikimedia Commons — televisão da Turquia | https://commons.wikimedia.org/wiki/Category:Television_logos_of_Turkey | Categoria geral | Fonte complementar para encontrar logos e referências históricas. |
| GunesTV | https://github.com/Oktay2617/gunestv | Dataset GitHub com dados de canais e URLs de logos | Usar somente entradas identificadas como Turkey e conferir cada imagem. |
| discevisita/iptv | https://github.com/discevisita/iptv | Playlist IPTV com metadados tvg-logo | Fonte de referência para localizar URLs de logos; não é um arquivo dedicado de imagens. |

## 2. Fontes oficiais e pacotes de identidade visual

| Fonte | Endereço | Tipo | Uso |
|---|---|---|---|
| TRT Kurumsal — Logolar | https://www.trt.net.tr/corporate/logos | Página oficial de logos | Fonte oficial para canais TRT; a automação do projeto já consulta o pacote de televisão. |
| Pacote oficial de logos de televisão TRT | https://www.trt.net.tr/logos/Televizyon.zip | Arquivo ZIP | Download direto disponibilizado pela TRT; já contemplado pela rotina de catálogo. |
| D-Smart | https://www.dsmart.com.tr/ | Catálogo de operadora | Referência para conferir nomes, marcas e identidade de canais. Não foi confirmado como arquivo público de logos em lote. |
| Digiturk | https://www.digiturk.com.tr/ | Catálogo de operadora | Referência para conferir nomes, marcas e identidade de canais. Não foi confirmado como arquivo público de logos em lote. |
| Tivibu | https://www.tivibu.com.tr/ | Catálogo de operadora | Referência para conferir nomes, marcas e identidade de canais. Não foi confirmado como arquivo público de logos em lote. |

## 3. Fontes adicionais identificadas

| Fonte | Endereço | Tipo | Uso e observações |
|---|---|---|---|
| msvsee/IPTV — Turkey Turkish | https://github.com/msvsee/IPTV/blob/main/turkey_turkish.m3u | Playlist M3U com metadados tvg-logo | Fonte de descoberta para nomes de canais e URLs de logos. Validar cada URL individualmente; não importar a playlist como catálogo de imagens. |
| baycuman-hub/turk-tv | https://github.com/baycuman-hub/turk-tv/blob/main/Turk-Kanallari.m3u.m3u | Playlist M3U com metadados tvg-logo | Fonte complementar de descoberta e cruzamento de canais/logos. Validar atualidade, correspondência e URL de cada imagem. |
| yasserstudio/tv-logos | https://github.com/yasserstudio/tv-logos | Repositório GitHub de logos por país | Repositório arquivado (somente leitura, conforme consulta realizada). Conferir se há arquivos da Turquia que acrescentem cobertura além de tv-logo/tv-logos antes de importar. |
| Wikimedia Commons — NTV logos | https://commons.wikimedia.org/wiki/Category:NTV_logos | Categoria especializada de mídia | Inclui versões atuais e históricas; selecionar somente a versão atual correspondente ao canal NTV. |

## 4. Regras para incorporar imagens ao catálogo

1. Confirmar que a logo pertence exatamente ao canal da entrada da playlist.
2. Preferir a versão atual e oficial; não substituir logo atual por variante histórica.
3. Registrar a URL original, fonte, crédito e licença quando disponíveis.
4. Converter somente imagens correspondentes e verificadas para PNG quadrado de 256 x 256 px.
5. Manter fundo preto uniforme, logo centralizada, cores preservadas e sem deformação.
6. Não alterar os links de transmissão, categorias ou a playlist TV principal durante a coleta de logos.
7. Catálogos de operadoras e playlists de terceiros são fontes de conferência; não devem ser raspados automaticamente como se fossem repositórios de imagens sem verificar permissões, estabilidade e URLs diretas.

## 5. Estado da integração

- **Já contempladas na automação do catálogo:** tv-logo/tv-logos, Wikimedia Commons, TRT oficial e GunesTV.
- **Registradas como fontes adicionais de consulta:** TVLogo.org, Wikimedia geral, dataset discevisita/iptv, D-Smart, Digiturk, Tivibu, msvsee/IPTV, baycuman-hub/turk-tv, yasserstudio/tv-logos e categoria NTV do Wikimedia Commons.
- O registro neste documento não significa que todas as imagens dessas fontes já foram baixadas, convertidas ou associadas aos canais.
- Playlists M3U são fontes para descobrir nomes e metadados tvg-logo; não são arquivos PNG nem garantem que os endereços estejam ativos ou que a imagem seja oficial.
- A playlist TV principal e os arquivos de transmissão não são modificados por este catálogo de fontes.

