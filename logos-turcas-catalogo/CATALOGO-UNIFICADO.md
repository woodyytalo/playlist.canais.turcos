# Catálogo unificado de fontes de logos de canais turcos

Este arquivo reúne o conteúdo dos três arquivos do diretório `logos-turcas-catalogo` em um único documento. Os arquivos originais permanecem preservados.

---

## 1. FONTES-LOGOS-TURCAS.md

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



---

## 2. FONTES.csv

```csv
arquivo_png,url_original,resultado
tvlogos-github-24-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/24-tr.png,OK
tvlogos-github-360-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/360-tr.png,OK
tvlogos-github-4-eylul-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/4-eylul-tr.png,OK
tvlogos-github-a-haber-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/a-haber-tr.png,OK
tvlogos-github-a-news-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/a-news-tr.png,OK
tvlogos-github-a-para-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/a-para-tr.png,OK
tvlogos-github-a-spor-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/a-spor-tr.png,OK
tvlogos-github-a2-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/a2-tr.png,OK
tvlogos-github-ada-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/ada-tv-tr.png,OK
tvlogos-github-agro-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/agro-tv-tr.png,OK
tvlogos-github-akit-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/akit-tv-tr.png,OK
tvlogos-github-aksu-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/aksu-tv-tr.png,OK
tvlogos-github-altas-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/altas-tv-tr.png,OK
tvlogos-github-anadolu-dernek-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/anadolu-dernek-tr.png,OK
tvlogos-github-atv-avrupa-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/atv-avrupa-tr.png,OK
tvlogos-github-atv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/atv-tr.png,OK
tvlogos-github-bahar-turk-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/bahar-turk-tr.png,OK
tvlogos-github-bbn-turk-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/bbn-turk-tr.png,OK
tvlogos-github-bein-box-office-1-hz-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/bein-box-office-1-hz-tr.png,OK
tvlogos-github-bein-box-office-1-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/bein-box-office-1-tr.png,OK
tvlogos-github-bein-box-office-2-hz-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/bein-box-office-2-hz-tr.png,OK
tvlogos-github-bein-box-office-2-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/bein-box-office-2-tr.png,OK
tvlogos-github-bein-box-office-3-hz-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/bein-box-office-3-hz-tr.png,OK
tvlogos-github-bein-box-office-3-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/bein-box-office-3-tr.png,OK
tvlogos-github-bein-gurme-hd-hz-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/bein-gurme-hd-hz-tr.png,OK
tvlogos-github-bein-gurme-hd-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/bein-gurme-hd-tr.png,OK
tvlogos-github-bein-h-and-e-hd-hz-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/bein-h-and-e-hd-hz-tr.png,OK
tvlogos-github-bein-h-and-e-hd-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/bein-h-and-e-hd-tr.png,OK
tvlogos-github-bein-hd-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/bein-hd-tr.png,OK
tvlogos-github-bein-iz-hd-hz-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/bein-iz-hd-hz-tr.png,OK
tvlogos-github-bein-iz-hd-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/bein-iz-hd-tr.png,OK
tvlogos-github-bein-movies-action-2-hd-hz-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/bein-movies-action-2-hd-hz-tr.png,OK
tvlogos-github-bein-movies-action-2-hd-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/bein-movies-action-2-hd-tr.png,OK
tvlogos-github-bein-movies-action-hd-hz-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/bein-movies-action-hd-hz-tr.png,OK
tvlogos-github-bein-movies-action-hd-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/bein-movies-action-hd-tr.png,OK
tvlogos-github-bein-movies-family-hd-hz-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/bein-movies-family-hd-hz-tr.png,OK
tvlogos-github-bein-movies-family-hd-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/bein-movies-family-hd-tr.png,OK
tvlogos-github-bein-movies-premiere-2-hd-hz-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/bein-movies-premiere-2-hd-hz-tr.png,OK
tvlogos-github-bein-movies-premiere-2-hd-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/bein-movies-premiere-2-hd-tr.png,OK
tvlogos-github-bein-movies-premiere-hd-hz-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/bein-movies-premiere-hd-hz-tr.png,OK
tvlogos-github-bein-movies-premiere-hd-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/bein-movies-premiere-hd-tr.png,OK
tvlogos-github-bein-movies-stars-hd-hz-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/bein-movies-stars-hd-hz-tr.png,OK
tvlogos-github-bein-movies-stars-hd-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/bein-movies-stars-hd-tr.png,OK
tvlogos-github-bein-movies-turk-hd-hz-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/bein-movies-turk-hd-hz-tr.png,OK
tvlogos-github-bein-movies-turk-hd-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/bein-movies-turk-hd-tr.png,OK
tvlogos-github-bein-series-comedy-hd-hz-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/bein-series-comedy-hd-hz-tr.png,OK
tvlogos-github-bein-series-comedy-hd-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/bein-series-comedy-hd-tr.png,OK
tvlogos-github-bein-series-drama-hd-hz-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/bein-series-drama-hd-hz-tr.png,OK
tvlogos-github-bein-series-drama-hd-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/bein-series-drama-hd-tr.png,OK
tvlogos-github-bein-series-sci-fi-hd-hz-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/bein-series-sci-fi-hd-hz-tr.png,OK
tvlogos-github-bein-series-sci-fi-hd-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/bein-series-sci-fi-hd-tr.png,OK
tvlogos-github-bein-series-vice-hd-hz-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/bein-series-vice-hd-hz-tr.png,OK
tvlogos-github-bein-series-vice-hd-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/bein-series-vice-hd-tr.png,OK
tvlogos-github-bein-sports-haber-hz-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/bein-sports-haber-hz-tr.png,OK
tvlogos-github-bein-sports-haber-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/bein-sports-haber-tr.png,OK
tvlogos-github-bengu-turk-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/bengu-turk-tr.png,OK
tvlogos-github-berat-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/berat-tv-tr.png,OK
tvlogos-github-beyaz-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/beyaz-tv-tr.png,OK
tvlogos-github-beykent-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/beykent-tv-tr.png,OK
tvlogos-github-bizimev-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/bizimev-tv-tr.png,OK
tvlogos-github-bloomberg-ht-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/bloomberg-ht-tr.png,OK
tvlogos-github-brt-1-hd-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/brt-1-hd-tr.png,OK
tvlogos-github-brt-1-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/brt-1-tr.png,OK
tvlogos-github-brt-2-hd-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/brt-2-hd-tr.png,OK
tvlogos-github-brt-2-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/brt-2-tr.png,OK
tvlogos-github-brt-3-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/brt-3-tr.png,OK
tvlogos-github-brtv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/brtv-tr.png,OK
tvlogos-github-bursaspor-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/bursaspor-tv-tr.png,OK
tvlogos-github-cay-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/cay-tv-tr.png,OK
tvlogos-github-cem-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/cem-tv-tr.png,OK
tvlogos-github-ciftci-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/ciftci-tv-tr.png,OK
tvlogos-github-cnbc-e-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/cnbc-e-tr.png,OK
tvlogos-github-cnn-turk-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/cnn-turk-tr.png,OK
tvlogos-github-cocuk-smart-hd-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/cocuk-smart-hd-tr.png,OK
tvlogos-github-cocuk-smart-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/cocuk-smart-tr.png,OK
tvlogos-github-disney-channel-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/disney-channel-tr.png,OK
tvlogos-github-diyanet-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/diyanet-tv-tr.png,OK
tvlogos-github-diyar-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/diyar-tv-tr.png,OK
tvlogos-github-dizi-smart-max-hd-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/dizi-smart-max-hd-tr.png,OK
tvlogos-github-dizi-smart-max-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/dizi-smart-max-tr.png,OK
tvlogos-github-dizi-smart-premium-hd-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/dizi-smart-premium-hd-tr.png,OK
tvlogos-github-dizi-smart-premium-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/dizi-smart-premium-tr.png,OK
tvlogos-github-dost-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/dost-tv-tr.png,OK
tvlogos-github-dream-turk-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/dream-turk-tr.png,OK
tvlogos-github-drt-denizli-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/drt-denizli-tr.png,OK
tvlogos-github-eba-tv-ilkokul-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/eba-tv-ilkokul-tr.png,OK
tvlogos-github-eba-tv-lise-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/eba-tv-lise-tr.png,OK
tvlogos-github-eba-tv-ortaokul-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/eba-tv-ortaokul-tr.png,OK
tvlogos-github-edessa-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/edessa-tv-tr.png,OK
tvlogos-github-ege-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/ege-tv-tr.png,OK
tvlogos-github-ekin-tv-turk-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/ekin-tv-turk-tr.png,OK
tvlogos-github-ekoturk-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/ekoturk-tr.png,OK
tvlogos-github-es-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/es-tv-tr.png,OK
tvlogos-github-euro-d-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/euro-d-tr.png,OK
tvlogos-github-euro-star-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/euro-star-tr.png,OK
tvlogos-github-fashion-one-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/fashion-one-tv-tr.png,OK
tvlogos-github-fenerbahce-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/fenerbahce-tv-tr.png,OK
tvlogos-github-filmbox-hd-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/filmbox-hd-tr.png,OK
tvlogos-github-filmbox-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/filmbox-tr.png,OK
tvlogos-github-flash-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/flash-tv-tr.png,OK
tvlogos-github-fm-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/fm-tv-tr.png,OK
tvlogos-github-fox-crime-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/fox-crime-tr.png,OK
tvlogos-github-fox-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/fox-tr.png,OK
tvlogos-github-fx-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/fx-tr.png,OK
tvlogos-github-galatasaray-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/galatasaray-tv-tr.png,OK
tvlogos-github-gaziantep-olay-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/gaziantep-olay-tv-tr.png,OK
tvlogos-github-guneydogu-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/guneydogu-tv-tr.png,OK
tvlogos-github-haber-global-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/haber-global-tr.png,OK
tvlogos-github-haberturk-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/haberturk-tr.png,OK
tvlogos-github-halk-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/halk-tv-tr.png,OK
tvlogos-github-hrt-akdeniz-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/hrt-akdeniz-tr.png,OK
tvlogos-github-ht-hayat-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/ht-hayat-tr.png,OK
tvlogos-github-kadirga-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/kadirga-tr.png,OK
tvlogos-github-kanal-15-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/kanal-15-tr.png,OK
tvlogos-github-kanal-16-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/kanal-16-tr.png,OK
tvlogos-github-kanal-23-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/kanal-23-tr.png,OK
tvlogos-github-kanal-26-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/kanal-26-tr.png,OK
tvlogos-github-kanal-33-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/kanal-33-tr.png,OK
tvlogos-github-kanal-42-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/kanal-42-tr.png,OK
tvlogos-github-kanal-58-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/kanal-58-tr.png,OK
tvlogos-github-kanal-7-avrupa-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/kanal-7-avrupa-tr.png,OK
tvlogos-github-kanal-7-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/kanal-7-tr.png,OK
tvlogos-github-kanal-avrupa-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/kanal-avrupa-tr.png,OK
tvlogos-github-kanal-b-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/kanal-b-tr.png,OK
tvlogos-github-kanal-d-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/kanal-d-tr.png,OK
tvlogos-github-kanal-ege-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/kanal-ege-tr.png,OK
tvlogos-github-kanal-firat-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/kanal-firat-tr.png,OK
tvlogos-github-kanal-sim-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/kanal-sim-tr.png,OK
tvlogos-github-kanal-t-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/kanal-t-tr.png,OK
tvlogos-github-kanal-urfa-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/kanal-urfa-tr.png,OK
tvlogos-github-kanal-v-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/kanal-v-tr.png,OK
tvlogos-github-kanal-z-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/kanal-z-tr.png,OK
tvlogos-github-kanal23-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/kanal23-tr.png,OK
tvlogos-github-kanal3-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/kanal3-tr.png,OK
tvlogos-github-kardelen-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/kardelen-tv-tr.png,OK
tvlogos-github-kent-turk-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/kent-turk-tr.png,OK
tvlogos-github-kocaeli-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/kocaeli-tv-tr.png,OK
tvlogos-github-kon-tv-hd-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/kon-tv-hd-tr.png,OK
tvlogos-github-kon-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/kon-tv-tr.png,OK
tvlogos-github-koy-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/koy-tv-tr.png,OK
tvlogos-github-koza-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/koza-tv-tr.png,OK
tvlogos-github-kral-pop-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/kral-pop-tr.png,OK
tvlogos-github-kral-tv-hd-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/kral-tv-hd-tr.png,OK
tvlogos-github-kral-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/kral-tv-tr.png,OK
tvlogos-github-krt-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/krt-tr.png,OK
tvlogos-github-lalegul-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/lalegul-tv-tr.png,OK
tvlogos-github-line-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/line-tv-tr.png,OK
tvlogos-github-manisa-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/manisa-tv-tr.png,OK
tvlogos-github-mavi-karadeniz-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/mavi-karadeniz-tr.png,OK
tvlogos-github-mercan-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/mercan-tv-tr.png,OK
tvlogos-github-milyon-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/milyon-tv-tr.png,OK
tvlogos-github-minika-cocuk-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/minika-cocuk-tr.png,OK
tvlogos-github-minika-go-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/minika-go-tr.png,OK
tvlogos-github-movie-smart-action-hd-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/movie-smart-action-hd-tr.png,OK
tvlogos-github-movie-smart-action-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/movie-smart-action-tr.png,OK
tvlogos-github-movie-smart-classic-hd-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/movie-smart-classic-hd-tr.png,OK
tvlogos-github-movie-smart-classic-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/movie-smart-classic-tr.png,OK
tvlogos-github-movie-smart-family-hd-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/movie-smart-family-hd-tr.png,OK
tvlogos-github-movie-smart-family-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/movie-smart-family-tr.png,OK
tvlogos-github-movie-smart-fest-hd-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/movie-smart-fest-hd-tr.png,OK
tvlogos-github-movie-smart-fest-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/movie-smart-fest-tr.png,OK
tvlogos-github-movie-smart-gold-hd-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/movie-smart-gold-hd-tr.png,OK
tvlogos-github-movie-smart-gold-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/movie-smart-gold-tr.png,OK
tvlogos-github-movie-smart-platin-hd-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/movie-smart-platin-hd-tr.png,OK
tvlogos-github-movie-smart-platin-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/movie-smart-platin-tr.png,OK
tvlogos-github-movie-smart-platin2-hd-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/movie-smart-platin2-hd-tr.png,OK
tvlogos-github-movie-smart-platin2-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/movie-smart-platin2-tr.png,OK
tvlogos-github-movie-smart-premium-hd-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/movie-smart-premium-hd-tr.png,OK
tvlogos-github-movie-smart-premium-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/movie-smart-premium-tr.png,OK
tvlogos-github-movie-smart-premium2-hd-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/movie-smart-premium2-hd-tr.png,OK
tvlogos-github-movie-smart-premium2-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/movie-smart-premium2-tr.png,OK
tvlogos-github-movie-smart-turk-hd-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/movie-smart-turk-hd-tr.png,OK
tvlogos-github-movie-smart-turk-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/movie-smart-turk-tr.png,OK
tvlogos-github-now-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/now-tr.png,OK
tvlogos-github-nr1-ask-hd-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/nr1-ask-hd-tr.png,OK
tvlogos-github-nr1-ask-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/nr1-ask-tr.png,OK
tvlogos-github-nr1-damar-hd-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/nr1-damar-hd-tr.png,OK
tvlogos-github-nr1-damar-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/nr1-damar-tr.png,OK
tvlogos-github-nr1-dance-hd-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/nr1-dance-hd-tr.png,OK
tvlogos-github-nr1-dance-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/nr1-dance-tr.png,OK
tvlogos-github-nr1-hd-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/nr1-hd-tr.png,OK
tvlogos-github-nr1-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/nr1-tr.png,OK
tvlogos-github-nr1-turk-hd-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/nr1-turk-hd-tr.png,OK
tvlogos-github-nr1-turk-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/nr1-turk-tr.png,OK
tvlogos-github-ntv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/ntv-tr.png,OK
tvlogos-github-on4-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/on4-tv-tr.png,OK
tvlogos-github-pamukkale-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/pamukkale-tv-tr.png,OK
tvlogos-github-planet-cocuk-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/planet-cocuk-tr.png,OK
tvlogos-github-planet-pembe-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/planet-pembe-tr.png,OK
tvlogos-github-planet-sinema-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/planet-sinema-tr.png,OK
tvlogos-github-planet-turk-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/planet-turk-tr.png,OK
tvlogos-github-planet-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/planet-tv-tr.png,OK
tvlogos-github-power-tv-hd-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/power-tv-hd-tr.png,OK
tvlogos-github-power-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/power-tv-tr.png,OK
tvlogos-github-powerturk-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/powerturk-tr.png,OK
tvlogos-github-rehber-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/rehber-tv-tr.png,OK
tvlogos-github-rumeli-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/rumeli-tv-tr.png,OK
tvlogos-github-s-sport-2-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/s-sport-2-tr.png,OK
tvlogos-github-s-sport-plus-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/s-sport-plus-tr.png,OK
tvlogos-github-s-sport-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/s-sport-tr.png,OK
tvlogos-github-sat7-turk-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/sat7-turk-tr.png,OK
tvlogos-github-semerkand-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/semerkand-tv-tr.png,OK
tvlogos-github-show-max-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/show-max-tr.png,OK
tvlogos-github-show-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/show-tr.png,OK
tvlogos-github-show-turk-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/show-turk-tr.png,OK
tvlogos-github-sinema-1001-hz-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/sinema-1001-hz-tr.png,OK
tvlogos-github-sinema-1001-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/sinema-1001-tr.png,OK
tvlogos-github-sinema-1002-hz-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/sinema-1002-hz-tr.png,OK
tvlogos-github-sinema-1002-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/sinema-1002-tr.png,OK
tvlogos-github-sinema-aile-hz-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/sinema-aile-hz-tr.png,OK
tvlogos-github-sinema-aile-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/sinema-aile-tr.png,OK
tvlogos-github-sinema-aile2-hz-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/sinema-aile2-hz-tr.png,OK
tvlogos-github-sinema-aile2-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/sinema-aile2-tr.png,OK
tvlogos-github-sinema-aksiyon-hz-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/sinema-aksiyon-hz-tr.png,OK
tvlogos-github-sinema-aksiyon-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/sinema-aksiyon-tr.png,OK
tvlogos-github-sinema-aksiyon2-hz-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/sinema-aksiyon2-hz-tr.png,OK
tvlogos-github-sinema-aksiyon2-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/sinema-aksiyon2-tr.png,OK
tvlogos-github-sinema-komedi-hz-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/sinema-komedi-hz-tr.png,OK
tvlogos-github-sinema-komedi-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/sinema-komedi-tr.png,OK
tvlogos-github-sinema-komedi2-hz-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/sinema-komedi2-hz-tr.png,OK
tvlogos-github-sinema-komedi2-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/sinema-komedi2-tr.png,OK
tvlogos-github-sinema-tv-hz-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/sinema-tv-hz-tr.png,OK
tvlogos-github-sinema-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/sinema-tv-tr.png,OK
tvlogos-github-sinema-tv2-hz-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/sinema-tv2-hz-tr.png,OK
tvlogos-github-sinema-tv2-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/sinema-tv2-tr.png,OK
tvlogos-github-sinema-yerli-hz-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/sinema-yerli-hz-tr.png,OK
tvlogos-github-sinema-yerli-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/sinema-yerli-tr.png,OK
tvlogos-github-sinema-yerli2-hz-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/sinema-yerli2-hz-tr.png,OK
tvlogos-github-sinema-yerli2-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/sinema-yerli2-tr.png,OK
tvlogos-github-spor-smart-hd-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/spor-smart-hd-tr.png,OK
tvlogos-github-sports-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/sports-tv-tr.png,OK
tvlogos-github-star-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/star-tv-tr.png,OK
tvlogos-github-stingray-ambiance-4k-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/stingray-ambiance-4k-tr.png,OK
tvlogos-github-stingray-ambiance-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/stingray-ambiance-tr.png,OK
tvlogos-github-tarim-turk-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/tarim-turk-tr.png,OK
tvlogos-github-tarim-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/tarim-tv-tr.png,OK
tvlogos-github-tatlises-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/tatlises-tv-tr.png,OK
tvlogos-github-tay-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/tay-tv-tr.png,OK
tvlogos-github-tbmm-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/tbmm-tv-tr.png,OK
tvlogos-github-tek-rumeli-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/tek-rumeli-tr.png,OK
tvlogos-github-tele1-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/tele1-tr.png,OK
tvlogos-github-tempo-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/tempo-tv-tr.png,OK
tvlogos-github-teve2-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/teve2-tr.png,OK
tvlogos-github-tgrt-belgesel-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/tgrt-belgesel-tr.png,OK
tvlogos-github-tgrt-eu-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/tgrt-eu-tr.png,OK
tvlogos-github-tgrt-haber-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/tgrt-haber-tr.png,OK
tvlogos-github-tivi6-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/tivi6-tr.png,OK
tvlogos-github-tjk-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/tjk-tv-tr.png,OK
tvlogos-github-tmb-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/tmb-tr.png,OK
tvlogos-github-toprak-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/toprak-tv-tr.png,OK
tvlogos-github-tr-35-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/tr-35-tr.png,OK
tvlogos-github-trt-1-hd-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/trt-1-hd-tr.png,OK
tvlogos-github-trt-1-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/trt-1-tr.png,OK
tvlogos-github-trt-2-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/trt-2-tr.png,OK
tvlogos-github-trt-3-spor-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/trt-3-spor-tr.png,OK
tvlogos-github-trt-3-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/trt-3-tr.png,OK
tvlogos-github-trt-4k-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/trt-4k-tr.png,OK
tvlogos-github-trt-arabi-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/trt-arabi-tr.png,OK
tvlogos-github-trt-avaz-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/trt-avaz-tr.png,OK
tvlogos-github-trt-belgesel-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/trt-belgesel-tr.png,OK
tvlogos-github-trt-cocuk-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/trt-cocuk-tr.png,OK
tvlogos-github-trt-gen--tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/trt-genç-tr.png,FALHA: 'ascii' codec can't encode character '\xe7' in position 51: ordinal not in range(128)
tvlogos-github-trt-haber-hd-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/trt-haber-hd-tr.png,OK
tvlogos-github-trt-haber-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/trt-haber-tr.png,OK
tvlogos-github-trt-kurdi-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/trt-kurdi-tr.png,OK
tvlogos-github-trt-muzik-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/trt-muzik-tr.png,OK
tvlogos-github-trt-spor-2-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/trt-spor-2-tr.png,OK
tvlogos-github-trt-spor-hd-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/trt-spor-hd-tr.png,OK
tvlogos-github-trt-spor-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/trt-spor-tr.png,OK
tvlogos-github-trt-spor-yildiz-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/trt-spor-yildiz-tr.png,OK
tvlogos-github-trt-turk-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/trt-turk-tr.png,OK
tvlogos-github-trt-world-hd-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/trt-world-hd-tr.png,OK
tvlogos-github-trt-world-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/trt-world-tr.png,OK
tvlogos-github-turk-haber-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/turk-haber-tr.png,OK
tvlogos-github-tv-35-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/tv-35-tr.png,OK
tvlogos-github-tv-den-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/tv-den-tr.png,OK
tvlogos-github-tv-kayseri-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/tv-kayseri-tr.png,OK
tvlogos-github-tv1-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/tv1-tr.png,OK
tvlogos-github-tv100-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/tv100-tr.png,OK
tvlogos-github-tv2-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/tv2-tr.png,OK
tvlogos-github-tv264-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/tv264-tr.png,OK
tvlogos-github-tv4-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/tv4-tr.png,OK
tvlogos-github-tv5-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/tv5-tr.png,OK
tvlogos-github-tv52-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/tv52-tr.png,OK
tvlogos-github-tv8-int-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/tv8-int-tr.png,OK
tvlogos-github-tv8-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/tv8-tr.png,OK
tvlogos-github-tv85-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/tv85-tr.png,OK
tvlogos-github-tvnet-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/tvnet-tr.png,OK
tvlogos-github-ucankus-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/ucankus-tr.png,OK
tvlogos-github-ulke-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/ulke-tv-tr.png,OK
tvlogos-github-ulusal-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/ulusal-tv-tr.png,OK
tvlogos-github-uzay-haber-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/uzay-haber-tr.png,OK
tvlogos-github-uzay-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/uzay-tv-tr.png,OK
tvlogos-github-vatan-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/vatan-tv-tr.png,OK
tvlogos-github-vav-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/vav-tv-tr.png,OK
tvlogos-github-vizyon-58-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/vizyon-58-tr.png,OK
tvlogos-github-vizyon-turk-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/vizyon-turk-tr.png,OK
tvlogos-github-yaban-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/yaban-tr.png,OK
tvlogos-github-yildiz-en-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/yildiz-en-tv-tr.png,OK
tvlogos-github-yol-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/yol-tv-tr.png,OK
tvlogos-github-zarok-tv-tr.png,https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/zarok-tv-tr.png,OK
```

---

## 3. FONTES-ADICIONAIS.csv

```csv
fonte,canal_ou_arquivo,png_256,url_original,licenca,credito,resultado
Wikimedia Commons,Aatv.jpg,,https://upload.wikimedia.org/wikipedia/commons/8/81/Aatv.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC BY-SA 4.0,"<a href=""//commons.wikimedia.org/w/index.php?title=User:Nesetkilic&action=edit&redlink=1"" class=""new"" title=""User:Nesetkilic (page does not exist)"">Nesetkilic</a>",FALHA: HTTP Error 429: Too many requests. Please contact the Wikimedia SRE team at noc@wikimedia.org and refer to this message. (daab851)
Wikimedia Commons,Ahaber Logo.png,logos-turcas-catalogo/fontes-adicionais/wikimedia-commons/ahaber-logo-png-2.png,https://upload.wikimedia.org/wikipedia/commons/7/7c/Ahaber_Logo.png?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,Turkuvaz Yeni Asır Televizyon Prodüksiyon A.Ş.,OK
Wikimedia Commons,Air Box TV Logo.jpg,,https://upload.wikimedia.org/wikipedia/commons/4/4d/Air_Box_TV_Logo.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,Mega Dating,FALHA: HTTP Error 429: Too many requests. Please contact the Wikimedia SRE team at noc@wikimedia.org and refer to this message. (daab851)
Wikimedia Commons,ATV Logo 2.png,,https://upload.wikimedia.org/wikipedia/commons/0/03/ATV_Logo_2.png?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC BY-SA 4.0,"<a href=""//commons.wikimedia.org/w/index.php?title=User:Christian_Winge_Andersen&action=edit&redlink=1"" class=""new"" title=""User:Christian Winge Andersen (page does not exist)"">Christian Winge Andersen</a>",FALHA: HTTP Error 429: Too many requests. Please contact the Wikimedia SRE team at noc@wikimedia.org and refer to this message. (daab851)
Wikimedia Commons,Bengütürk TV.png,logos-turcas-catalogo/fontes-adicionais/wikimedia-commons/beng-t-rk-tv-png-2.png,https://upload.wikimedia.org/wikipedia/commons/2/2f/Beng%C3%BCt%C3%BCrk_TV.png?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC BY-SA 4.0,Bengütürk TV,OK
Wikimedia Commons,Beykent TV logo.png,,https://upload.wikimedia.org/wikipedia/commons/f/fc/Beykent_TV_logo.png?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,Beykent Üniversitesi,FALHA: HTTP Error 429: Too many requests. Please contact the Wikimedia SRE team at noc@wikimedia.org and refer to this message. (daab851)
Wikimedia Commons,Cem TV logo.png,,https://upload.wikimedia.org/wikipedia/commons/2/2f/Cem_TV_logo.png?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,Cem TV,FALHA: HTTP Error 429: Too many requests. Please contact the Wikimedia SRE team at noc@wikimedia.org and refer to this message. (daab851)
Wikimedia Commons,Cine5 logo.png,logos-turcas-catalogo/fontes-adicionais/wikimedia-commons/cine5-logo-png-2.png,https://upload.wikimedia.org/wikipedia/commons/d/d3/Cine5_logo.png?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC BY-SA 4.0,Can Ergen,OK
Wikimedia Commons,Csahaber-lo1go-1-.png,,https://upload.wikimedia.org/wikipedia/commons/5/52/Csahaber-lo1go-1-.png?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC BY-SA 4.0,"<a href=""//commons.wikimedia.org/w/index.php?title=User:Elmasuyu&action=edit&redlink=1"" class=""new"" title=""User:Elmasuyu (page does not exist)"">Elmasuyu</a>",FALHA: HTTP Error 429: Too many requests. Please contact the Wikimedia SRE team at noc@wikimedia.org and refer to this message. (daab851)
Wikimedia Commons,D Max.jpg,,https://upload.wikimedia.org/wikipedia/commons/3/39/D_Max.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC BY-SA 4.0,"<a href=""//commons.wikimedia.org/wiki/User:Totaltv_(bulgaria)_bg"" title=""User:Totaltv (bulgaria) bg"">D Max</a>",FALHA: HTTP Error 429: Too many requests. Please contact the Wikimedia SRE team at noc@wikimedia.org and refer to this message. (daab851)
Wikimedia Commons,D Sinemax.jpg,,https://upload.wikimedia.org/wikipedia/commons/5/5d/D_Sinemax.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC BY-SA 4.0,"<a href=""//commons.wikimedia.org/wiki/User:Viasat_Sport"" title=""User:Viasat Sport"">D Sinemax Europe</a>",FALHA: HTTP Error 429: Too many requests. Please contact the Wikimedia SRE team at noc@wikimedia.org and refer to this message. (daab851)
Wikimedia Commons,E2 (2006-2011).png,,https://upload.wikimedia.org/wikipedia/commons/c/c5/E2_%282006-2011%29.png?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC BY-SA 4.0,"<a href=""//commons.wikimedia.org/w/index.php?title=User:Sabah_Gazetecilik&action=edit&redlink=1"" class=""new"" title=""User:Sabah Gazetecilik (page does not exist)"">Sabah Gazetecilik</a>",FALHA: HTTP Error 429: Too many requests. Please contact the Wikimedia SRE team at noc@wikimedia.org and refer to this message. (daab851)
Wikimedia Commons,E2 logo (Turkish tv channel).png,,https://upload.wikimedia.org/wikipedia/commons/a/a1/E2_logo_%28Turkish_tv_channel%29.png?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,,FALHA: HTTP Error 429: Too many requests. Please contact the Wikimedia SRE team at noc@wikimedia.org and refer to this message. (daab851)
Wikimedia Commons,Ege TV Logo.webp,,https://upload.wikimedia.org/wikipedia/commons/5/5f/Ege_TV_Logo.webp?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC BY-SA 4.0,"<a href=""//commons.wikimedia.org/w/index.php?title=User:ErenAyd%C4%B1nTR&action=edit&redlink=1"" class=""new"" title=""User:ErenAydınTR (page does not exist)"">ErenAydınTR</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,Eko TV.webp,,https://upload.wikimedia.org/wikipedia/commons/3/37/Eko_TV.webp?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,"<a href=""//commons.wikimedia.org/w/index.php?title=User:YusufReyis_38&action=edit&redlink=1"" class=""new"" title=""User:YusufReyis 38 (page does not exist)"">YusufReyis 38</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,Ekol TV Kanalının Logosu.png,,https://upload.wikimedia.org/wikipedia/commons/6/62/Ekol_TV_Kanal%C4%B1n%C4%B1n_Logosu.png?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC BY-SA 4.0,"<a href=""//commons.wikimedia.org/w/index.php?title=User:Televizyon_Delisi&action=edit&redlink=1"" class=""new"" title=""User:Televizyon Delisi (page does not exist)"">Televizyon Delisi</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,Euro D v2.png,,https://upload.wikimedia.org/wikipedia/commons/4/46/Euro_D_v2.png?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC0,Kanal D,FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,FarklıTV.jpg,,https://upload.wikimedia.org/wikipedia/commons/3/34/Farkl%C4%B1TV.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC BY-SA 4.0,"<a href=""//commons.wikimedia.org/w/index.php?title=User:Gvnali123&action=edit&redlink=1"" class=""new"" title=""User:Gvnali123 (page does not exist)"">Gvnali123</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,Flash haber tv 2025.png,logos-turcas-catalogo/fontes-adicionais/wikimedia-commons/flash-haber-tv-2025-png-2.png,https://upload.wikimedia.org/wikipedia/commons/2/23/Flash_haber_tv_2025.png?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,Flash haber tv,OK
Wikimedia Commons,Flash-tv-yeni-logo.jpg,,https://upload.wikimedia.org/wikipedia/commons/0/02/Flash-tv-yeni-logo.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC BY-SA 4.0,"<a href=""//commons.wikimedia.org/w/index.php?title=User:Muhsinsahin2009&action=edit&redlink=1"" class=""new"" title=""User:Muhsinsahin2009 (page does not exist)"">Muhsinsahin2009</a>",FALHA: HTTP Error 429: Too many requests (76af2b0)
Wikimedia Commons,Former logo of Max Smart (2010-2011).png,,https://upload.wikimedia.org/wikipedia/commons/7/72/Former_logo_of_Max_Smart_%282010-2011%29.png?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,"<a href=""//commons.wikimedia.org/wiki/User:Rapsar"" class=""mw-redirect"" title=""User:Rapsar"">Rapsar</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,Fox Life Turkey.png,,https://upload.wikimedia.org/wikipedia/commons/6/6a/Fox_Life_Turkey.png?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC BY-SA 4.0,"<a href=""//commons.wikimedia.org/w/index.php?title=User:Yunusemrelfc&action=edit&redlink=1"" class=""new"" title=""User:Yunusemrelfc (page does not exist)"">Yunusemrelfc</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,FoxTürk.jpg,,https://upload.wikimedia.org/wikipedia/commons/b/b4/FoxT%C3%BCrk.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,Fox,FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,Gala TV.png,,https://upload.wikimedia.org/wikipedia/commons/9/90/Gala_TV.png?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC BY-SA 4.0,"<a href=""//commons.wikimedia.org/wiki/User:D_Spor_(European_TV_channel)"" title=""User:D Spor (European TV channel)"">Gala (TV kanalı)</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,Gala-TV-logo.png,,https://upload.wikimedia.org/wikipedia/commons/f/fb/Gala-TV-logo.png?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC BY-SA 4.0,"<a href=""//commons.wikimedia.org/w/index.php?title=User:TurnerBG&action=edit&redlink=1"" class=""new"" title=""User:TurnerBG (page does not exist)"">Gala TV</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,GEM Group Logo.jpg,,https://upload.wikimedia.org/wikipedia/commons/2/2a/GEM_Group_Logo.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC BY-SA 4.0,"<a href=""//commons.wikimedia.org/w/index.php?title=User:Mohsen-gem&action=edit&redlink=1"" class=""new"" title=""User:Mohsen-gem (page does not exist)"">GEM GROUP</a>",FALHA: HTTP Error 429: Too many requests (76af2b0)
Wikimedia Commons,Gemtv.png,,https://upload.wikimedia.org/wikipedia/commons/5/5f/Gemtv.png?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC BY-SA 4.0,GEM TV,FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,Grt-tv-tr.png,,https://upload.wikimedia.org/wikipedia/commons/f/fd/Grt-tv-tr.png?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC0,"<a href=""//commons.wikimedia.org/w/index.php?title=User:Eneskr27&action=edit&redlink=1"" class=""new"" title=""User:Eneskr27 (page does not exist)"">Eneskr27</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,Gurmeler Televizyon-Logo.png,,https://upload.wikimedia.org/wikipedia/commons/0/05/Gurmeler_Televizyon-Logo.png?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC0,"<a href=""//commons.wikimedia.org/w/index.php?title=User:Annesi_o%C4%9Flu&action=edit&redlink=1"" class=""new"" title=""User:Annesi oğlu (page does not exist)"">Annesi oğlu</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,Habertürktv.jpg,,https://upload.wikimedia.org/wikipedia/commons/5/58/Habert%C3%BCrktv.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC BY-SA 4.0,"<a href=""//commons.wikimedia.org/w/index.php?title=User:Bobby_baccalieri&action=edit&redlink=1"" class=""new"" title=""User:Bobby baccalieri (page does not exist)"">Bobby baccalieri</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,Hdkaradenizlogo.png,,https://upload.wikimedia.org/wikipedia/commons/f/f7/Hdkaradenizlogo.png?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC0,"<a href=""//commons.wikimedia.org/w/index.php?title=User:Nht.etb&action=edit&redlink=1"" class=""new"" title=""User:Nht.etb (page does not exist)"">Nht.etb</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,Hdkaradenizlogo.webp,,https://upload.wikimedia.org/wikipedia/commons/a/aa/Hdkaradenizlogo.webp?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC0,"<a href=""//commons.wikimedia.org/w/index.php?title=User:Nht.etb&action=edit&redlink=1"" class=""new"" title=""User:Nht.etb (page does not exist)"">Nht.etb</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,HDTV Logo.png,,https://upload.wikimedia.org/wikipedia/commons/0/0c/HDTV_Logo.png?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC BY-SA 4.0,"<a href=""//commons.wikimedia.org/w/index.php?title=Template:Dxerty&action=edit&redlink=1"" class=""new"" title=""Template:Dxerty (page does not exist)"">Template:Dxerty</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,Kanal 1 logo.png,,https://upload.wikimedia.org/wikipedia/commons/8/83/Kanal_1_logo.png?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC BY-SA 4.0,"<a href=""//commons.wikimedia.org/w/index.php?title=User:Yusuf_48797&action=edit&redlink=1"" class=""new"" title=""User:Yusuf 48797 (page does not exist)"">Yusuf 48797</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,Kanal 1 logosu.png,,https://upload.wikimedia.org/wikipedia/commons/d/d9/Kanal_1_logosu.png?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC BY-SA 4.0,"<a href=""//commons.wikimedia.org/w/index.php?title=User:KanalFortza&action=edit&redlink=1"" class=""new"" title=""User:KanalFortza (page does not exist)"">KanalFortza</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,Kanaltürk logosu.png,,https://upload.wikimedia.org/wikipedia/commons/2/24/Kanalt%C3%BCrk_logosu.png?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC BY-SA 4.0,"<a href=""//commons.wikimedia.org/w/index.php?title=User:GroupmediaF&action=edit&redlink=1"" class=""new"" title=""User:GroupmediaF (page does not exist)"">GroupmediaF</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,KaramelTVLogo.png,,https://upload.wikimedia.org/wikipedia/commons/e/ec/KaramelTVLogo.png?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC BY-SA 4.0,Karamel Tv,FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,Karamursel.jpg,,https://upload.wikimedia.org/wikipedia/commons/2/22/Karamursel.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC BY-SA 4.0,"<a href=""//commons.wikimedia.org/w/index.php?title=User:Ercanbuber&action=edit&redlink=1"" class=""new"" title=""User:Ercanbuber (page does not exist)"">Ercanbuber</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,Kral TV logo.png,,https://upload.wikimedia.org/wikipedia/commons/2/2f/Kral_TV_logo.png?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC BY-SA 4.0,,FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,KRT Logo 2023.webp,,https://upload.wikimedia.org/wikipedia/commons/c/c4/KRT_Logo_2023.webp?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,KRT TV,FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,Logo of Maxi TV.png,,https://upload.wikimedia.org/wikipedia/commons/3/39/Logo_of_Maxi_TV.png?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,"<a href=""//commons.wikimedia.org/wiki/User:Rapsar"" class=""mw-redirect"" title=""User:Rapsar"">Rapsar</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,Logo of Medical Channel.jpg,,https://upload.wikimedia.org/wikipedia/commons/c/c9/Logo_of_Medical_Channel.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,"<a href=""//commons.wikimedia.org/wiki/User:Rapsar"" class=""mw-redirect"" title=""User:Rapsar"">Rapsar</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,Logo of Meltem TV.gif,,https://upload.wikimedia.org/wikipedia/commons/9/94/Logo_of_Meltem_TV.gif?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,"<a href=""//commons.wikimedia.org/wiki/User:Rapsar"" class=""mw-redirect"" title=""User:Rapsar"">Rapsar</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,Medya-2.jpg,,https://upload.wikimedia.org/wikipedia/commons/e/e7/Medya-2.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC BY-SA 4.0,"<a href=""//commons.wikimedia.org/w/index.php?title=User:Kanalworldtv&action=edit&redlink=1"" class=""new"" title=""User:Kanalworldtv (page does not exist)"">Kanalworldtv</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,Minika go new.webp,,https://upload.wikimedia.org/wikipedia/commons/f/f2/Minika_go_new.webp?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC BY 4.0,"<a href=""//commons.wikimedia.org/wiki/User:Yi%C4%9FitZone"" title=""User:YiğitZone"">YiğitZone</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,Music Box TR.png,,https://upload.wikimedia.org/wikipedia/commons/0/0a/Music_Box_TR.png?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC BY 4.0,"<a href=""//commons.wikimedia.org/w/index.php?title=User:FortzaMusic&action=edit&redlink=1"" class=""new"" title=""User:FortzaMusic (page does not exist)"">FortzaMusic</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,MusicBoxHD.png,,https://upload.wikimedia.org/wikipedia/commons/7/7a/MusicBoxHD.png?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC BY-SA 4.0,"<a href=""//commons.wikimedia.org/w/index.php?title=User:FortzaMedia&action=edit&redlink=1"" class=""new"" title=""User:FortzaMedia (page does not exist)"">FortzaMedia</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,National Geographic Türkiye logo.png,,https://upload.wikimedia.org/wikipedia/commons/d/d0/National_Geographic_T%C3%BCrkiye_logo.png?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,National Geographic Society,FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,Nr1-HD.png,,https://upload.wikimedia.org/wikipedia/commons/c/c3/Nr1-HD.png?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC BY-SA 4.0,"<a href=""//commons.wikimedia.org/w/index.php?title=User:FortzaNR1&action=edit&redlink=1"" class=""new"" title=""User:FortzaNR1 (page does not exist)"">FortzaNR1</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,O-TV-preview.png,,https://upload.wikimedia.org/wikipedia/commons/2/28/O-TV-preview.png?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC BY-SA 4.0,"<a href=""//commons.wikimedia.org/w/index.php?title=User:TurnerBG&action=edit&redlink=1"" class=""new"" title=""User:TurnerBG (page does not exist)"">Телеканал O-TV</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,OTV-music logosu.png,,https://upload.wikimedia.org/wikipedia/commons/2/24/OTV-music_logosu.png?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC BY-SA 4.0,"<a href=""//commons.wikimedia.org/w/index.php?title=User:FortzaMedia&action=edit&redlink=1"" class=""new"" title=""User:FortzaMedia (page does not exist)"">FortzaMedia</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,OTVmusic logo.png,,https://upload.wikimedia.org/wikipedia/commons/f/f5/OTVmusic_logo.png?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC BY-SA 4.0,"<a href=""//commons.wikimedia.org/w/index.php?title=User:FortzaMedia&action=edit&redlink=1"" class=""new"" title=""User:FortzaMedia (page does not exist)"">FortzaMedia</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,OTVmusicHD.png,,https://upload.wikimedia.org/wikipedia/commons/b/be/OTVmusicHD.png?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC BY-SA 4.0,"<a href=""//commons.wikimedia.org/w/index.php?title=User:FortzaMedia&action=edit&redlink=1"" class=""new"" title=""User:FortzaMedia (page does not exist)"">FortzaMedia</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,OTVMusicHD.png,,https://upload.wikimedia.org/wikipedia/commons/a/a9/OTVMusicHD.png?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC BY-SA 4.0,"<a href=""//commons.wikimedia.org/w/index.php?title=User:FortzaMedia&action=edit&redlink=1"" class=""new"" title=""User:FortzaMedia (page does not exist)"">FortzaMedia</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,Pop TV logo.jpg,,https://upload.wikimedia.org/wikipedia/commons/d/de/Pop_TV_logo.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC BY-SA 4.0,,FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,Puhutv.png,,https://upload.wikimedia.org/wikipedia/commons/c/ca/Puhutv.png?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC BY-SA 4.0,"<a href=""//commons.wikimedia.org/w/index.php?title=User:Yunusemrelfc&action=edit&redlink=1"" class=""new"" title=""User:Yunusemrelfc (page does not exist)"">Yunusemrelfc</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,Receptv logo.webp,,https://upload.wikimedia.org/wikipedia/commons/f/fe/Receptv_logo.webp?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,RecepTV,FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,Sony Çocuk.jpg,,https://upload.wikimedia.org/wikipedia/commons/c/c1/Sony_%C3%87ocuk.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC BY-SA 4.0,"<a href=""//commons.wikimedia.org/w/index.php?title=User:Yunusemrelfc&action=edit&redlink=1"" class=""new"" title=""User:Yunusemrelfc (page does not exist)"">Yunusemrelfc</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,Star TV Icon Logo 2001.svg,,https://upload.wikimedia.org/wikipedia/commons/a/ab/Star_TV_Icon_Logo_2001.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC BY-SA 4.0,"<a href=""//commons.wikimedia.org/wiki/User:Estradadarwin10"" title=""User:Estradadarwin10"">Estradadarwin10</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,Star TV Logo 2011.svg,,https://upload.wikimedia.org/wikipedia/commons/5/50/Star_TV_Logo_2011.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC BY-SA 4.0,"<a href=""//commons.wikimedia.org/wiki/User:Estradadarwin10"" title=""User:Estradadarwin10"">Estradadarwin10</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,Trt 1 logolarından.png,,https://upload.wikimedia.org/wikipedia/commons/3/3e/Trt_1_logolar%C4%B1ndan.png?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC BY-SA 4.0,"<a href=""//commons.wikimedia.org/wiki/User:Patateskafa325"" title=""User:Patateskafa325"">Patateskafa325</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,Trt11997-1998.png,,https://upload.wikimedia.org/wikipedia/commons/a/ac/Trt11997-1998.png?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC BY-SA 4.0,"<a href=""//commons.wikimedia.org/wiki/User:Patateskafa325"" title=""User:Patateskafa325"">Patateskafa325</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,TRT1logo1992-1993.png,,https://upload.wikimedia.org/wikipedia/commons/9/92/TRT1logo1992-1993.png?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC BY-SA 4.0,"<a href=""//commons.wikimedia.org/wiki/User:Patateskafa325"" title=""User:Patateskafa325"">Patateskafa325</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,ÇRT LOGO.png,,https://upload.wikimedia.org/wikipedia/commons/8/89/%C3%87RT_LOGO.png?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC BY-SA 4.0,"<a href=""//commons.wikimedia.org/w/index.php?title=User:Mehmethcoskun&action=edit&redlink=1"" class=""new"" title=""User:Mehmethcoskun (page does not exist)"">Mehmethcoskun</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,Atv logo 2010.svg,,https://upload.wikimedia.org/wikipedia/commons/4/45/Atv_logo_2010.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,atv,FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,Bloomberg HT logo.svg,,https://upload.wikimedia.org/wikipedia/commons/8/89/Bloomberg_HT_logo.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,Ciner Yayın Holding,FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,CNN Türk 201x logo.svg,,https://upload.wikimedia.org/wikipedia/commons/f/f0/CNN_T%C3%BCrk_201x_logo.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,"Unknown author<span style=""display: none;"">Unknown author</span>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,CNN Türk logo.svg,,https://upload.wikimedia.org/wikipedia/commons/5/59/CNN_T%C3%BCrk_logo.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,"<a href=""https://en.wikipedia.org/wiki/Turner_Broadcasting_System_Europe"" class=""extiw"" title=""en:Turner Broadcasting System Europe"">Turner Broadcasting System Europe</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,Diyanet TV logo.svg,,https://upload.wikimedia.org/wikipedia/commons/4/43/Diyanet_TV_logo.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,T.C. Diyanet İşleri Başkanlığı,FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,Haber Global logo.svg,,https://upload.wikimedia.org/wikipedia/commons/d/d0/Haber_Global_logo.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,Haber Global,FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,Habertürk logo.svg,,https://upload.wikimedia.org/wikipedia/commons/7/77/Habert%C3%BCrk_logo.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,Ciner Media Group,FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,Habertürk TV logo.svg,,https://upload.wikimedia.org/wikipedia/commons/f/f2/Habert%C3%BCrk_TV_logo.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,Ciner Yayın Holding,FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,Logo of TRT 1 (2009-2012).svg,,https://upload.wikimedia.org/wikipedia/commons/5/57/Logo_of_TRT_1_%282009-2012%29.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,,FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,Logo Star TV (1992-2002).svg,,https://upload.wikimedia.org/wikipedia/commons/b/ba/Logo_Star_TV_%281992-2002%29.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,"Unknown author<span style=""display: none;"">Unknown author</span>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,Logo Star TV (2002-2011).svg,,https://upload.wikimedia.org/wikipedia/commons/f/f4/Logo_Star_TV_%282002-2011%29.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,"Unknown author<span style=""display: none;"">Unknown author</span>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,Logo Star TV (2011-2017).svg,,https://upload.wikimedia.org/wikipedia/commons/a/ae/Logo_Star_TV_%282011-2017%29.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,Star TV,FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,Logo-ShowTV-2002.svg,,https://upload.wikimedia.org/wikipedia/commons/f/f0/Logo-ShowTV-2002.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,"Unknown author<span style=""display: none;"">Unknown author</span>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,NOW TV (Turkey) wordmark-red.svg,,https://upload.wikimedia.org/wikipedia/commons/d/db/NOW_TV_%28Turkey%29_wordmark-red.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,"<a href=""https://en.wikipedia.org/wiki/The_Walt_Disney_Company"" class=""extiw"" title=""wikipedia:The Walt Disney Company"">Disney Enterprises, Inc.</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,Nr1 logo vector.svg,,https://upload.wikimedia.org/wikipedia/commons/b/bf/Nr1_logo_vector.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,"<a href=""//commons.wikimedia.org/wiki/User:Andrikkos"" title=""User:Andrikkos"">Andrikkos</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,NTV (Turkey) logo.svg,,https://upload.wikimedia.org/wikipedia/commons/0/0c/NTV_%28Turkey%29_logo.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,NTV,FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,NTV logo (1996-2008).svg,,https://upload.wikimedia.org/wikipedia/commons/4/41/NTV_logo_%281996-2008%29.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,"<a href=""//commons.wikimedia.org/w/index.php?title=%C3%89tienne_Robial&action=edit&redlink=1"" class=""new"" title=""Étienne Robial (page does not exist)"">Étienne Robial</a> - <a rel=""nofollow"" class=""external text"" href=""http://on-off-productions.com/"">on-off-productions</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,Show MAX logo.svg,,https://upload.wikimedia.org/wikipedia/commons/3/31/Show_MAX_logo.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,Ciner Holding,FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,Show Turk logo.svg,,https://upload.wikimedia.org/wikipedia/commons/f/fd/Show_Turk_logo.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,Ciner Holding,FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,Show TV logo.svg,,https://upload.wikimedia.org/wikipedia/commons/c/cb/Show_TV_logo.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,Ciner Holding,FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,TBMM TV logo.svg,,https://upload.wikimedia.org/wikipedia/commons/c/c5/TBMM_TV_logo.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,"<a href=""//commons.wikimedia.org/w/index.php?title=User:Jelican9&action=edit&redlink=1"" class=""new"" title=""User:Jelican9 (page does not exist)"">Jelican9</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,TRT 1 logo (1989-1991).svg,,https://upload.wikimedia.org/wikipedia/commons/a/aa/TRT_1_logo_%281989-1991%29.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC0,"<a href=""//commons.wikimedia.org/w/index.php?title=User:Jelican9&action=edit&redlink=1"" class=""new"" title=""User:Jelican9 (page does not exist)"">Jelican9</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,TRT 1 logo (1998-2001).svg,,https://upload.wikimedia.org/wikipedia/commons/a/a0/TRT_1_logo_%281998-2001%29.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,TRT,FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,TRT 1 logo (2001-2005).svg,,https://upload.wikimedia.org/wikipedia/commons/9/9d/TRT_1_logo_%282001-2005%29.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,"<a href=""//commons.wikimedia.org/w/index.php?title=User:Jelican9&action=edit&redlink=1"" class=""new"" title=""User:Jelican9 (page does not exist)"">Jelican9</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,TRT 1 logo (2020-2021).svg,,https://upload.wikimedia.org/wikipedia/commons/3/31/TRT_1_logo_%282020-2021%29.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,TRT,FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,TRT 1 logo (2021-).svg,,https://upload.wikimedia.org/wikipedia/commons/8/85/TRT_1_logo_%282021-%29.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,"<a href=""//commons.wikimedia.org/wiki/User:SA%C4%B0T71"" title=""User:SAİT71"">SAİT71</a><br><div style=""display:table;width:;vertical-align:middle;direction:ltr;float:left;line-height:22px;height:24px;font-size:.96em;margin:0px;padding:2px 4px 2px 6px;color:inherit;background:var(--background-color-neutral-subtle,#f8f9fa);border:1px solid var(--border-color-base,#a2a9b1);border-collapse:separate;border-spacing:0px;background:var(--background-color-error-subtle, #ffe9e5); border:1px solid var(--border-color-destructive, #f54739);""><span typeof=""mw:File""><a href=""//commons.wikimedia.org/wiki/File:Inkscape-ws.svg"" class=""mw-file-description""><img src=""https://thumb.wikimedia.org/wikipedia/commons/thumb/3/34/Inkscape-ws.svg/40px-Inkscape-ws.svg.png?utm_source=commons.wikimedia.org&utm_campaign=parser&utm_content=thumbnail"" decoding=""async"" loading=""lazy"" width=""22"" height=""22"" class=""mw-file-element"" srcset=""https://thumb.wikimedia.org/wikipedia/commons/thumb/3/34/Inkscape-ws.svg/60px-Inkscape-ws.svg.png?utm_source=commons.wikimedia.org&utm_campaign=parser&utm_content=thumbnail 2x"" data-file-width=""390"" data-file-height=""390""></a></span> This <i>W3C-unspecified</i> <a href=""https://en.wikipedia.org/wiki/Vector_images"" class=""extiw"" title=""w:Vector images"">vector image</a> was created with <a href=""https://en.wikipedia.org/wiki/Inkscape"" class=""extiw"" title=""w:Inkscape"">Inkscape</a> .</div>",FALHA: HTTP Error 429: Too many requests (76af2b0)
Wikimedia Commons,TRT 2 logo (1998-2001).svg,,https://upload.wikimedia.org/wikipedia/commons/1/1f/TRT_2_logo_%281998-2001%29.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC0,"<a href=""//commons.wikimedia.org/w/index.php?title=User:Jelican9&action=edit&redlink=1"" class=""new"" title=""User:Jelican9 (page does not exist)"">Jelican9</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,TRT 2 logo (2001-2005).svg,,https://upload.wikimedia.org/wikipedia/commons/9/9d/TRT_2_logo_%282001-2005%29.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,"<a href=""//commons.wikimedia.org/w/index.php?title=User:Jelican9&action=edit&redlink=1"" class=""new"" title=""User:Jelican9 (page does not exist)"">Jelican9</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,TRT 2 logo (TV2).svg,,https://upload.wikimedia.org/wikipedia/commons/f/ff/TRT_2_logo_%28TV2%29.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC0,"<a href=""//commons.wikimedia.org/w/index.php?title=User:Jelican9&action=edit&redlink=1"" class=""new"" title=""User:Jelican9 (page does not exist)"">Jelican9</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,TRT 2 logo.svg,,https://upload.wikimedia.org/wikipedia/commons/1/19/TRT_2_logo.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,Türkiye Radyo ve Televizyon Kurumu,FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,TRT 3 logo (1989-1993).svg,,https://upload.wikimedia.org/wikipedia/commons/e/e1/TRT_3_logo_%281989-1993%29.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC0,"<a href=""//commons.wikimedia.org/w/index.php?title=User:Jelican9&action=edit&redlink=1"" class=""new"" title=""User:Jelican9 (page does not exist)"">Jelican9</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,TRT 3 logo (1998-2001).svg,,https://upload.wikimedia.org/wikipedia/commons/9/9f/TRT_3_logo_%281998-2001%29.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC0,"<a href=""//commons.wikimedia.org/w/index.php?title=User:Jelican9&action=edit&redlink=1"" class=""new"" title=""User:Jelican9 (page does not exist)"">Jelican9</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,TRT 3 logo (2001-2005).svg,,https://upload.wikimedia.org/wikipedia/commons/2/2f/TRT_3_logo_%282001-2005%29.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,"<a href=""//commons.wikimedia.org/w/index.php?title=User:Jelican9&action=edit&redlink=1"" class=""new"" title=""User:Jelican9 (page does not exist)"">Jelican9</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,TRT 3 logo (2021).svg,,https://upload.wikimedia.org/wikipedia/commons/a/af/TRT_3_logo_%282021%29.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,Türkiye Radyo ve Televizyon Kurumu,FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,TRT 3 logo.svg,,https://upload.wikimedia.org/wikipedia/commons/2/24/TRT_3_logo.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,"<a href=""//commons.wikimedia.org/w/index.php?title=User:Jelican9&action=edit&redlink=1"" class=""new"" title=""User:Jelican9 (page does not exist)"">Jelican9</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,TRT 3 Spor logo (2022).svg,,https://upload.wikimedia.org/wikipedia/commons/3/35/TRT_3_Spor_logo_%282022%29.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,"<a href=""//commons.wikimedia.org/w/index.php?title=User:Jelican9&action=edit&redlink=1"" class=""new"" title=""User:Jelican9 (page does not exist)"">Jelican9</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,TRT 4 logo (1993-1998).svg,,https://upload.wikimedia.org/wikipedia/commons/0/03/TRT_4_logo_%281993-1998%29.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC0,"<a href=""//commons.wikimedia.org/w/index.php?title=User:Jelican9&action=edit&redlink=1"" class=""new"" title=""User:Jelican9 (page does not exist)"">Jelican9</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,TRT 4 logo (1998-2001).svg,,https://upload.wikimedia.org/wikipedia/commons/3/3a/TRT_4_logo_%281998-2001%29.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC0,"<a href=""//commons.wikimedia.org/w/index.php?title=User:Jelican9&action=edit&redlink=1"" class=""new"" title=""User:Jelican9 (page does not exist)"">Jelican9</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,TRT 4 logo (2001-2005).svg,,https://upload.wikimedia.org/wikipedia/commons/9/96/TRT_4_logo_%282001-2005%29.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,"<a href=""//commons.wikimedia.org/w/index.php?title=User:Jelican9&action=edit&redlink=1"" class=""new"" title=""User:Jelican9 (page does not exist)"">Jelican9</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,TRT 4K logo.svg,,https://upload.wikimedia.org/wikipedia/commons/0/07/TRT_4K_logo.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC0,"<a href=""//commons.wikimedia.org/w/index.php?title=User:Jelican9&action=edit&redlink=1"" class=""new"" title=""User:Jelican9 (page does not exist)"">Jelican9</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,TRT 4K.svg,,https://upload.wikimedia.org/wikipedia/commons/6/69/TRT_4K.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,Türkiye Radyo ve Televizyon Kurumu,FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,TRT 5 logo (1990-1992).svg,,https://upload.wikimedia.org/wikipedia/commons/8/87/TRT_5_logo_%281990-1992%29.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC0,"<a href=""//commons.wikimedia.org/w/index.php?title=User:Jelican9&action=edit&redlink=1"" class=""new"" title=""User:Jelican9 (page does not exist)"">Jelican9</a>",FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,TRT Arabi logo.svg,,https://upload.wikimedia.org/wikipedia/commons/b/b1/TRT_Arabi_logo.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,Türkiye Radyo ve Televizyon Kurumu,FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,TRT Avaz logo.svg,,https://upload.wikimedia.org/wikipedia/commons/5/54/TRT_Avaz_logo.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,TRT,FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,TRT Belgesel logo (2019-).svg,,https://upload.wikimedia.org/wikipedia/commons/0/09/TRT_Belgesel_logo_%282019-%29.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,TRT,FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,TRT Belgesel logosu (2019-).svg,,https://upload.wikimedia.org/wikipedia/commons/7/75/TRT_Belgesel_logosu_%282019-%29.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,TRT,FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,TRT Dinle logo.svg,,https://upload.wikimedia.org/wikipedia/commons/1/10/TRT_Dinle_logo.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,Türkiye Radyo ve Televizyon Kurumu,FALHA: HTTP Error 429: Too Many Requests. Please contact noc@wikimedia.org
Wikimedia Commons,TRT EBA TV Anaokulu logo.svg,,https://upload.wikimedia.org/wikipedia/commons/6/6a/TRT_EBA_TV_Anaokulu_logo.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,"<a href=""//commons.wikimedia.org/w/index.php?title=User:Jelican9&action=edit&redlink=1"" class=""new"" title=""User:Jelican9 (page does not exist)"">Jelican9</a>",FALHA: HTTP Error 429: Too Many Requests. Please contact noc@wikimedia.org
Wikimedia Commons,TRT EBA TV Lise logo.svg,,https://upload.wikimedia.org/wikipedia/commons/0/0e/TRT_EBA_TV_Lise_logo.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,TRT,FALHA: HTTP Error 429: Too Many Requests. Please contact noc@wikimedia.org
Wikimedia Commons,TRT EBA TV logo.svg,,https://upload.wikimedia.org/wikipedia/commons/b/b8/TRT_EBA_TV_logo.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,TRT,FALHA: HTTP Error 429: Too Many Requests. Please contact noc@wikimedia.org
Wikimedia Commons,TRT EBA TV logos.svg,,https://upload.wikimedia.org/wikipedia/commons/6/69/TRT_EBA_TV_logos.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,"<p>TRT logo: <span typeof=""mw:File""><a href=""//commons.wikimedia.org/wiki/File:TRT_logo_(2018-).svg"" class=""mw-file-description""><img src=""https://thumb.wikimedia.org/wikipedia/commons/thumb/6/6d/TRT_logo_%282018-%29.svg/40px-TRT_logo_%282018-%29.svg.png?utm_source=commons.wikimedia.org&utm_campaign=parser&utm_content=thumbnail"" decoding=""async"" loading=""lazy"" width=""25"" height=""9"" class=""mw-file-element"" srcset=""https://thumb.wikimedia.org/wikipedia/commons/thumb/6/6d/TRT_logo_%282018-%29.svg/60px-TRT_logo_%282018-%29.svg.png?utm_source=commons.wikimedia.org&utm_campaign=parser&utm_content=thumbnail 2x"" data-file-width=""512"" data-file-height=""181""></a></span>
</p>
EBA logo: <a rel=""nofollow"" class=""external free"" href=""https://www.eba.gov.tr/"">https://www.eba.gov.tr/</a>",FALHA: HTTP Error 429: Too Many Requests. Please contact noc@wikimedia.org
Wikimedia Commons,TRT EBA TV Ortaokul logo.svg,,https://upload.wikimedia.org/wikipedia/commons/4/41/TRT_EBA_TV_Ortaokul_logo.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,TRT,FALHA: HTTP Error 429: Too Many Requests. Please contact noc@wikimedia.org
Wikimedia Commons,TRT EBA TV İlkokul logo.svg,,https://upload.wikimedia.org/wikipedia/commons/9/98/TRT_EBA_TV_%C4%B0lkokul_logo.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,TRT,FALHA: HTTP Error 429: Too Many Requests. Please contact noc@wikimedia.org
Wikimedia Commons,TRT GAP logo.svg,,https://upload.wikimedia.org/wikipedia/commons/b/bd/TRT_GAP_logo.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,"<a href=""//commons.wikimedia.org/w/index.php?title=User:Jelican9&action=edit&redlink=1"" class=""new"" title=""User:Jelican9 (page does not exist)"">Jelican9</a>",FALHA: HTTP Error 429: Too Many Requests. Please contact noc@wikimedia.org
Wikimedia Commons,TRT Haber Eylül 2020 Logo.svg,,https://upload.wikimedia.org/wikipedia/commons/7/72/TRT_Haber_Eyl%C3%BCl_2020_Logo.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,"<a href=""//commons.wikimedia.org/w/index.php?title=User:Xephix&action=edit&redlink=1"" class=""new"" title=""User:Xephix (page does not exist)"">Xephix</a>",FALHA: HTTP Error 429: Too Many Requests. Please contact noc@wikimedia.org
Wikimedia Commons,TRT Haber logo (2013-2020).svg,,https://upload.wikimedia.org/wikipedia/commons/8/89/TRT_Haber_logo_%282013-2020%29.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC0,"<a href=""//commons.wikimedia.org/w/index.php?title=User:Jelican9&action=edit&redlink=1"" class=""new"" title=""User:Jelican9 (page does not exist)"">Jelican9</a>",FALHA: HTTP Error 429: Too Many Requests. Please contact noc@wikimedia.org
Wikimedia Commons,TRT int logo (1990-1992).svg,,https://upload.wikimedia.org/wikipedia/commons/6/69/TRT_int_logo_%281990-1992%29.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,TRT,FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,TRT int logo (2001-2005).svg,,https://upload.wikimedia.org/wikipedia/commons/0/00/TRT_int_logo_%282001-2005%29.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,TRT,FALHA: HTTP Error 429: Too Many Requests. Please contact noc@wikimedia.org
Wikimedia Commons,TRT Kurdî logo.svg,,https://upload.wikimedia.org/wikipedia/commons/7/79/TRT_Kurd%C3%AE_logo.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,Türkiye Radyo ve Televizyon Kurumu,FALHA: HTTP Error 429: Too Many Requests. Please contact noc@wikimedia.org
Wikimedia Commons,TRT Müzik logo.svg,,https://upload.wikimedia.org/wikipedia/commons/f/f2/TRT_M%C3%BCzik_logo.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,TRT,FALHA: HTTP Error 429: Too Many Requests. Please contact noc@wikimedia.org
Wikimedia Commons,TRT Müzik.svg,,https://upload.wikimedia.org/wikipedia/commons/4/47/TRT_M%C3%BCzik.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,TRT,FALHA: HTTP Error 429: Too Many Requests. Please contact noc@wikimedia.org
Wikimedia Commons,TRT Spor 2 logo (2019-2021).svg,,https://upload.wikimedia.org/wikipedia/commons/1/1a/TRT_Spor_2_logo_%282019-2021%29.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,"<a href=""//commons.wikimedia.org/w/index.php?title=User:Jelican9&action=edit&redlink=1"" class=""new"" title=""User:Jelican9 (page does not exist)"">Jelican9</a>",FALHA: HTTP Error 429: Too Many Requests. Please contact noc@wikimedia.org
Wikimedia Commons,TRT Spor logo (2021).svg,,https://upload.wikimedia.org/wikipedia/commons/8/8f/TRT_Spor_logo_%282021%29.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,Türkiye Radyo ve Televizyon Kurumu,FALHA: HTTP Error 429: Too Many Requests. Please contact noc@wikimedia.org
Wikimedia Commons,TRT Spor logo (2022).svg,,https://upload.wikimedia.org/wikipedia/commons/9/92/TRT_Spor_logo_%282022%29.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,"<a href=""//commons.wikimedia.org/w/index.php?title=User:XIIF&action=edit&redlink=1"" class=""new"" title=""User:XIIF (page does not exist)"">XIIF</a>",FALHA: HTTP Error 429: Too Many Requests. Please contact noc@wikimedia.org
Wikimedia Commons,TRT Spor logo.svg,,https://upload.wikimedia.org/wikipedia/commons/d/d4/TRT_Spor_logo.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,"<a href=""//commons.wikimedia.org/w/index.php?title=User:Jelican9&action=edit&redlink=1"" class=""new"" title=""User:Jelican9 (page does not exist)"">Jelican9</a>",FALHA: HTTP Error 429: Too Many Requests. Please contact noc@wikimedia.org
Wikimedia Commons,TRT Spor Yıldız Logo.svg,,https://upload.wikimedia.org/wikipedia/commons/c/ce/TRT_Spor_Y%C4%B1ld%C4%B1z_Logo.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,"<a href=""//commons.wikimedia.org/wiki/User:Furkan"" title=""User:Furkan"">Furkan</a>",FALHA: HTTP Error 429: Too Many Requests. Please contact noc@wikimedia.org
Wikimedia Commons,TRT Türk logo (2001-2005).svg,,https://upload.wikimedia.org/wikipedia/commons/b/b5/TRT_T%C3%BCrk_logo_%282001-2005%29.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,TRT,FALHA: HTTP Error 429: Too Many Requests. Please contact noc@wikimedia.org
Wikimedia Commons,TRT Türk logo (2015-2021).svg,,https://upload.wikimedia.org/wikipedia/commons/0/0a/TRT_T%C3%BCrk_logo_%282015-2021%29.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,TRT,FALHA: HTTP Error 429: Too many requests - please contact noc@wikimedia.org to discuss a less disruptive approach or instead use thumbnail images in sizes listed on https://w.wiki/GHai. (0c640b1)
Wikimedia Commons,TRT Türk logo.svg,,https://upload.wikimedia.org/wikipedia/commons/d/d2/TRT_T%C3%BCrk_logo.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,Türkiye Radyo ve Televizyon Kurumu,FALHA: HTTP Error 429: Too Many Requests. Please contact noc@wikimedia.org
Wikimedia Commons,TRT World logo.svg,,https://upload.wikimedia.org/wikipedia/commons/6/6e/TRT_World_logo.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,"<a href=""https://en.wikipedia.org/wiki/TRT_World"" class=""extiw"" title=""en:TRT World"">TRT World</a>",FALHA: HTTP Error 429: Too Many Requests. Please contact noc@wikimedia.org
Wikimedia Commons,TRT World.svg,,https://upload.wikimedia.org/wikipedia/commons/2/27/TRT_World.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,TRT,FALHA: HTTP Error 429: Too Many Requests. Please contact noc@wikimedia.org
Wikimedia Commons,TRT Çocuk logo (2021).svg,,https://upload.wikimedia.org/wikipedia/commons/1/1a/TRT_%C3%87ocuk_logo_%282021%29.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,Türkiye Radyo ve Televizyon Kurumu,FALHA: HTTP Error 429: Too Many Requests. Please contact noc@wikimedia.org
Wikimedia Commons,TRT1 logo (2012-2021).svg,,https://upload.wikimedia.org/wikipedia/commons/4/4b/TRT1_logo_%282012-2021%29.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,CC0,"<a href=""//commons.wikimedia.org/w/index.php?title=User:Jelican9&action=edit&redlink=1"" class=""new"" title=""User:Jelican9 (page does not exist)"">Jelican9</a>",FALHA: HTTP Error 429: Too Many Requests. Please contact noc@wikimedia.org
Wikimedia Commons,TRT3 Spor logo.svg,,https://upload.wikimedia.org/wikipedia/commons/5/54/TRT3_Spor_logo.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,Türkiye Radyo ve Televizyon Kurumu,FALHA: HTTP Error 429: Too Many Requests. Please contact noc@wikimedia.org
Wikimedia Commons,Tvnet logo (2022).svg,,https://upload.wikimedia.org/wikipedia/commons/5/5a/Tvnet_logo_%282022%29.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,Albayrak Medya,FALHA: HTTP Error 429: Too Many Requests. Please contact noc@wikimedia.org
Wikimedia Commons,Tvnet logo.svg,,https://upload.wikimedia.org/wikipedia/commons/9/97/Tvnet_logo.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,Tvnet,FALHA: HTTP Error 429: Too Many Requests. Please contact noc@wikimedia.org
Wikimedia Commons,Ülke TV logo.svg,,https://upload.wikimedia.org/wikipedia/commons/2/28/%C3%9Clke_TV_logo.svg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original,Public domain,Ülke TV,FALHA: HTTP Error 429: Too Many Requests. Please contact noc@wikimedia.org
TRT oficial,TRT Turk,logos-turcas-catalogo/fontes-adicionais/trt-oficial/trt-turk.png,https://www.trt.net.tr/logos/Televizyon.zip,TRT - pacote oficial,TRT Kurumsal,OK
TRT oficial,__MACOSX/Televizyon/._TRT Turk.png,,https://www.trt.net.tr/logos/Televizyon.zip,TRT - pacote oficial,TRT Kurumsal,FALHA: cannot identify image file <_io.BytesIO object at 0x752fdbc4afc0>
TRT oficial,TRT World,logos-turcas-catalogo/fontes-adicionais/trt-oficial/trt-world.png,https://www.trt.net.tr/logos/Televizyon.zip,TRT - pacote oficial,TRT Kurumsal,OK
TRT oficial,__MACOSX/Televizyon/._TRT World.png,,https://www.trt.net.tr/logos/Televizyon.zip,TRT - pacote oficial,TRT Kurumsal,FALHA: cannot identify image file <_io.BytesIO object at 0x752fdb34c360>
TRT oficial,TRT Muzik,logos-turcas-catalogo/fontes-adicionais/trt-oficial/trt-muzik.png,https://www.trt.net.tr/logos/Televizyon.zip,TRT - pacote oficial,TRT Kurumsal,OK
TRT oficial,__MACOSX/Televizyon/._TRT Muzik.png,,https://www.trt.net.tr/logos/Televizyon.zip,TRT - pacote oficial,TRT Kurumsal,FALHA: cannot identify image file <_io.BytesIO object at 0x752fdb34c360>
TRT oficial,TRT Cocuk,logos-turcas-catalogo/fontes-adicionais/trt-oficial/trt-cocuk.png,https://www.trt.net.tr/logos/Televizyon.zip,TRT - pacote oficial,TRT Kurumsal,OK
TRT oficial,__MACOSX/Televizyon/._TRT Cocuk.png,,https://www.trt.net.tr/logos/Televizyon.zip,TRT - pacote oficial,TRT Kurumsal,FALHA: cannot identify image file <_io.BytesIO object at 0x752fdb34c360>
TRT oficial,TRT Genc,logos-turcas-catalogo/fontes-adicionais/trt-oficial/trt-genc.png,https://www.trt.net.tr/logos/Televizyon.zip,TRT - pacote oficial,TRT Kurumsal,OK
TRT oficial,__MACOSX/Televizyon/._TRT Genc.png,,https://www.trt.net.tr/logos/Televizyon.zip,TRT - pacote oficial,TRT Kurumsal,FALHA: cannot identify image file <_io.BytesIO object at 0x752fdb34c360>
TRT oficial,TRT Belgesel,logos-turcas-catalogo/fontes-adicionais/trt-oficial/trt-belgesel.png,https://www.trt.net.tr/logos/Televizyon.zip,TRT - pacote oficial,TRT Kurumsal,OK
TRT oficial,__MACOSX/Televizyon/._TRT Belgesel.png,,https://www.trt.net.tr/logos/Televizyon.zip,TRT - pacote oficial,TRT Kurumsal,FALHA: cannot identify image file <_io.BytesIO object at 0x752fdb34c360>
TRT oficial,TRT Arabi,logos-turcas-catalogo/fontes-adicionais/trt-oficial/trt-arabi.png,https://www.trt.net.tr/logos/Televizyon.zip,TRT - pacote oficial,TRT Kurumsal,OK
TRT oficial,__MACOSX/Televizyon/._TRT Arabi.png,,https://www.trt.net.tr/logos/Televizyon.zip,TRT - pacote oficial,TRT Kurumsal,FALHA: cannot identify image file <_io.BytesIO object at 0x752fdb34c360>
TRT oficial,TRT 3,logos-turcas-catalogo/fontes-adicionais/trt-oficial/trt-3.png,https://www.trt.net.tr/logos/Televizyon.zip,TRT - pacote oficial,TRT Kurumsal,OK
TRT oficial,__MACOSX/Televizyon/._TRT 3.png,,https://www.trt.net.tr/logos/Televizyon.zip,TRT - pacote oficial,TRT Kurumsal,FALHA: cannot identify image file <_io.BytesIO object at 0x752fdb34c5e0>
TRT oficial,TRT 2,logos-turcas-catalogo/fontes-adicionais/trt-oficial/trt-2.png,https://www.trt.net.tr/logos/Televizyon.zip,TRT - pacote oficial,TRT Kurumsal,OK
TRT oficial,__MACOSX/Televizyon/._TRT 2.png,,https://www.trt.net.tr/logos/Televizyon.zip,TRT - pacote oficial,TRT Kurumsal,FALHA: cannot identify image file <_io.BytesIO object at 0x752fdb34c5e0>
TRT oficial,TRT Haber,logos-turcas-catalogo/fontes-adicionais/trt-oficial/trt-haber.png,https://www.trt.net.tr/logos/Televizyon.zip,TRT - pacote oficial,TRT Kurumsal,OK
TRT oficial,__MACOSX/Televizyon/._TRT Haber.png,,https://www.trt.net.tr/logos/Televizyon.zip,TRT - pacote oficial,TRT Kurumsal,FALHA: cannot identify image file <_io.BytesIO object at 0x752fdb34c5e0>
TRT oficial,TRT-eba-tek-kanal-logo,logos-turcas-catalogo/fontes-adicionais/trt-oficial/trt-eba-tek-kanal-logo.png,https://www.trt.net.tr/logos/Televizyon.zip,TRT - pacote oficial,TRT Kurumsal,OK
TRT oficial,__MACOSX/Televizyon/._TRT-eba-tek-kanal-logo.png,,https://www.trt.net.tr/logos/Televizyon.zip,TRT - pacote oficial,TRT Kurumsal,FALHA: cannot identify image file <_io.BytesIO object at 0x752fdb34c450>
TRT oficial,TRT Kurdi,logos-turcas-catalogo/fontes-adicionais/trt-oficial/trt-kurdi.png,https://www.trt.net.tr/logos/Televizyon.zip,TRT - pacote oficial,TRT Kurumsal,OK
TRT oficial,__MACOSX/Televizyon/._TRT Kurdi.png,,https://www.trt.net.tr/logos/Televizyon.zip,TRT - pacote oficial,TRT Kurumsal,FALHA: cannot identify image file <_io.BytesIO object at 0x752fdb34c5e0>
TRT oficial,TRT 1,logos-turcas-catalogo/fontes-adicionais/trt-oficial/trt-1.png,https://www.trt.net.tr/logos/Televizyon.zip,TRT - pacote oficial,TRT Kurumsal,OK
TRT oficial,__MACOSX/Televizyon/._TRT 1.png,,https://www.trt.net.tr/logos/Televizyon.zip,TRT - pacote oficial,TRT Kurumsal,FALHA: cannot identify image file <_io.BytesIO object at 0x752fdb34c5e0>
TRT oficial,TRT4K,logos-turcas-catalogo/fontes-adicionais/trt-oficial/trt4k.png,https://www.trt.net.tr/logos/Televizyon.zip,TRT - pacote oficial,TRT Kurumsal,OK
TRT oficial,__MACOSX/Televizyon/._TRT4K.png,,https://www.trt.net.tr/logos/Televizyon.zip,TRT - pacote oficial,TRT Kurumsal,FALHA: cannot identify image file <_io.BytesIO object at 0x752fdb34c5e0>
TRT oficial,TRT Avaz,logos-turcas-catalogo/fontes-adicionais/trt-oficial/trt-avaz.png,https://www.trt.net.tr/logos/Televizyon.zip,TRT - pacote oficial,TRT Kurumsal,OK
TRT oficial,__MACOSX/Televizyon/._TRT Avaz.png,,https://www.trt.net.tr/logos/Televizyon.zip,TRT - pacote oficial,TRT Kurumsal,FALHA: cannot identify image file <_io.BytesIO object at 0x752fdb34c5e0>
TRT oficial,TRT Spor,logos-turcas-catalogo/fontes-adicionais/trt-oficial/trt-spor.png,https://www.trt.net.tr/logos/Televizyon.zip,TRT - pacote oficial,TRT Kurumsal,OK
TRT oficial,__MACOSX/Televizyon/._TRT Spor.png,,https://www.trt.net.tr/logos/Televizyon.zip,TRT - pacote oficial,TRT Kurumsal,FALHA: cannot identify image file <_io.BytesIO object at 0x752fdb34c5e0>
TRT oficial,TRT Spor Y─▒ld─▒z,logos-turcas-catalogo/fontes-adicionais/trt-oficial/trt-spor-y-ld-z.png,https://www.trt.net.tr/logos/Televizyon.zip,TRT - pacote oficial,TRT Kurumsal,OK
TRT oficial,__MACOSX/Televizyon/._TRT Spor Y─▒ld─▒z.png,,https://www.trt.net.tr/logos/Televizyon.zip,TRT - pacote oficial,TRT Kurumsal,FALHA: cannot identify image file <_io.BytesIO object at 0x752fdb34c590>
TRT oficial,TRT Diyanet Cocuk,logos-turcas-catalogo/fontes-adicionais/trt-oficial/trt-diyanet-cocuk.png,https://www.trt.net.tr/logos/Televizyon.zip,TRT - pacote oficial,TRT Kurumsal,OK
TRT oficial,__MACOSX/Televizyon/._TRT Diyanet Cocuk.png,,https://www.trt.net.tr/logos/Televizyon.zip,TRT - pacote oficial,TRT Kurumsal,FALHA: cannot identify image file <_io.BytesIO object at 0x752fdb34c590>
GunesTV,Catálogo Turkey,,https://raw.githubusercontent.com/Oktay2617/gunestv/main/channels_turkey.json,,,FALHA: Expecting value: line 923 column 24 (char 39906)
```


---

# Fontes adicionais pesquisadas — atualização de 19/11/2026

Esta seção acrescenta pontos de consulta e validação encontrados em nova pesquisa. Os links abaixo são fontes para localizar, comparar ou confirmar logos; sua inclusão **não significa** que todos os arquivos tenham sido baixados, validados ou autorizados para redistribuição.

## 1. Wikimedia Commons — categorias específicas e subcategorias

- Categoria geral de logos de canais turcos: https://commons.wikimedia.org/wiki/Category:Logos_of_television_channels_in_Turkey
  - Índice com 64 arquivos e 28 subcategorias na consulta realizada.
  - Subcategorias úteis: ATV, beIN, BluTV, CNN Türk, Digiturk, Haber Global, Halk TV, Kanal 7, NTV, S Sport, Show TV, Star TV, TGRT, TRT, TVnet e Türksat Kablo.
- Categoria de logos vetoriais SVG: https://commons.wikimedia.org/wiki/Category:SVG_logos_of_television_channels_in_Turkey
  - Índice com 77 arquivos SVG na consulta realizada; inclui versões de Bloomberg HT, CNN Türk, Diyanet TV, Haber Global, Habertürk, NOW, NTV, Show TV e diversos canais TRT.
- Categoria complementar de televisão turca: https://commons.wikimedia.org/wiki/Category:Television_logos_of_Turkey
- Categoria de emissoras turcas: https://commons.wikimedia.org/wiki/Category:Television_channels_from_Turkey
- Categoria específica NTV: https://commons.wikimedia.org/wiki/Category:NTV_logos
- Categoria específica Show TV: https://commons.wikimedia.org/wiki/Category:Show_TV_logos

**Orientação:** priorizar SVG quando houver versão atual; verificar a data/versão, autoria e licença na página de cada arquivo. O índice também contém logos históricos, portanto não assumir que a primeira imagem encontrada seja a identidade visual vigente.

## 2. TRT — pacote oficial de logos

- Página institucional: https://www.trt.net.tr/kurumsal/logolar
- Pacote de logos de televisão indicado pela página institucional: https://www.trt.net.tr/logos/Televizyon.zip

A página institucional disponibiliza seção de canais de televisão e opção de baixar o conjunto. Usar como referência primária para canais TRT; conferir individualmente os arquivos e descartar entradas auxiliares de sistema que possam existir dentro do ZIP.

## 3. TheSportsDB — possível fonte complementar de imagens

- Discussão sobre canais de TV da Turquia e atualização de imagens: https://www.thesportsdb.com/forum_topic.php?t=6415

A discussão aponta que há imagens associadas a canais turcos na base, mas também alerta para logos antigos, canais encerrados e imagens com recorte/transparência inadequados. Tratar como fonte secundária de descoberta, não como autoridade para confirmar a logo atual.

## 4. RTÜK — validação de identidade e alterações oficiais

- Regulamento sobre logo e indicativo de emissoras: https://www.rtuk.gov.tr/by-law-on-administrative-and-financial-conditions-with-which-media-service-providers-and--platform-and-infrastructure-operators-are-required-to-comply/4049/en
- Exemplo de decisão oficial sobre alteração de logo de canal: https://www.rtuk.gov.tr/UstKurulKarar/Detay/17176
- Guia oficial para solicitação de alteração de logo: https://www.rtuk.gov.tr/Media/FM/Icerik/Klavuzlar%2C%20Form%20ve%20Beyan%20%C3%96rnekleri/logo-degisikligi-basvuru-kilavuzu.pdf

O RTÜK é útil para confirmar que houve alteração oficial de identidade e para evitar associar uma logo antiga a um canal atual. As decisões e os documentos regulatórios são fontes de validação, não necessariamente repositórios de arquivos gráficos.

## Critérios para incorporar logos ao acervo

1. Confirmar que o canal existe na playlist e identificar o nome/variante exatos.
2. Preferir página oficial da emissora ou pacote institucional; em seguida, SVG com licença explícita; por último, fontes secundárias.
3. Conferir se a imagem é atual, se corresponde à versão SD/HD/ internacional correta e se não é logo de programa, plataforma ou canal encerrado.
4. Registrar URL original, nome do arquivo, data de consulta, autoria e licença/condições de uso.
5. Só depois converter e padronizar a cópia local; preservar o arquivo de origem quando a licença permitir.
6. Não substituir automaticamente logos na playlist: manter a playlist intacta até revisão e aprovação.


---

# Galeria de imagens de referência — Wikimedia Commons

As imagens abaixo foram incorporadas como pré-visualizações diretamente neste catálogo. Cada imagem aponta para o arquivo hospedado no Wikimedia Commons; abra a página de origem para conferir autoria, licença, histórico e resolução antes de reutilizar ou redistribuir. São referências visuais e não uma confirmação automática de que todas representam a identidade atualmente em uso.

| Canal | Pré-visualização | Página de origem |
|---|---|---|
| ATV | ![Logo ATV](https://commons.wikimedia.org/wiki/Special:FilePath/Atv%20logo%202010.svg) | https://commons.wikimedia.org/wiki/File:Atv_logo_2010.svg |
| Bloomberg HT | ![Logo Bloomberg HT](https://commons.wikimedia.org/wiki/Special:FilePath/Bloomberg%20HT%20logo.svg) | https://commons.wikimedia.org/wiki/File:Bloomberg_HT_logo.svg |
| CNN Türk | ![Logo CNN Türk](https://commons.wikimedia.org/wiki/Special:FilePath/CNN%20T%C3%BCrk%20logo.svg) | https://commons.wikimedia.org/wiki/File:CNN_T%C3%BCrk_logo.svg |
| Diyanet TV | ![Logo Diyanet TV](https://commons.wikimedia.org/wiki/Special:FilePath/Diyanet%20TV%20logo.svg) | https://commons.wikimedia.org/wiki/Category:SVG_logos_of_television_channels_in_Turkey |
| Habertürk TV | ![Logo Habertürk TV](https://commons.wikimedia.org/wiki/Special:FilePath/Habert%C3%BCrk%20TV%20logo.svg) | https://commons.wikimedia.org/wiki/Category:SVG_logos_of_television_channels_in_Turkey |
| NTV | ![Logo NTV](https://commons.wikimedia.org/wiki/Special:FilePath/NTV%20(Turkey)%20logo.svg) | https://commons.wikimedia.org/wiki/File:NTV_%28Turkey%29_logo.svg |
| Show TV | ![Logo Show TV](https://commons.wikimedia.org/wiki/Special:FilePath/Show%20TV%20logo.svg) | https://commons.wikimedia.org/wiki/Category:SVG_logos_of_television_channels_in_Turkey |
| TRT 1 | ![Logo TRT 1](https://commons.wikimedia.org/wiki/Special:FilePath/TRT%201%20logo%20(2021-).svg) | https://commons.wikimedia.org/wiki/Category:SVG_logos_of_television_channels_in_Turkey |

**Notas de uso:** algumas categorias incluem versões históricas. A logo ATV listada, por exemplo, é identificada como versão de 2010. Compare com o site oficial e com o sinal atual do canal antes de selecionar a imagem definitiva. As pré-visualizações são links externos, não cópias dos arquivos dentro do repositório.


---

# Fontes adicionais — canais de música já presentes na Tv.m3u

Pesquisa complementar de fontes para logos de canais de música que já constam na playlist. Esta seção não propõe adicionar canais novos e não altera os campos `tvg-logo` da playlist. As imagens externas abaixo são referências/candidatas: confirmar identidade, versão vigente e licença antes de copiar para o repositório.

## Candidatas com correspondência identificada

| Canal | Fonte de logo / referência | Observações |
|---|---|---|
| Med Müzik (Med Muzîk) | PNG: https://i.imgur.com/gtUFmCD.png · Identificação do canal: https://iptv-org.github.io/channels/tr/MedMuzik | A página do iptv-org identifica Med Muzik como canal da Turquia, idioma curdo, categoria Music e site http://medmuzik.tv/. A fonte é útil para confirmar a identidade; verificar se a imagem continua atual e se o canal está ativo antes de adotar. |
| NR1 Fashion One | PNG: https://i.ibb.co/HV0x9JZ/fashion-one.png · Lista M3U de referência: https://github.com/maotuon/iptv-listesi/blob/main/iptv.m3u | A lista associa a imagem ao nome NR1 FASHION ONE. Atenção: há registro do RTÜK de alteração de logo/nome relacionado a “FASHION ONE TELEVİZYON” para “NR1 TÜRK”; tratar esta imagem como candidata possivelmente histórica e confirmar a identidade atual. |
| TopPop / Toppop TV | PNG: http://assets.tvcdn.net/4a8468ec-c134-4db1-93ef-699f15e1522b.png · Lista M3U de referência: https://github.com/hhdblog/TR/blob/main/tv_radyo.m3u | A lista apresenta uma imagem específica para Toppop TV. Confirmar que corresponde exatamente à entrada TopPop da playlist, pois outras listas encontradas reutilizam uma imagem genérica/placeholder. |
| Power TV | Logo: https://blutv-images.mncdn.com/q/t/i/bluv2/100/750x750/5dc2c155866ac331e0feb22b · Lista de referência: https://github.com/tecobaba/m3link/blob/main/ulusal.m3u | Fonte encontrada em lista que também relaciona canais do grupo Power. Candidata para a entrada Power TV; confirmar versão e direitos de reutilização. |
| KN Music TV | Site: https://www.knmusictv.com/ · PNG oficial indicado: https://www.knmusictv.com/wp-content/uploads/2026/01/LOGO2112.png | Há logo no site da emissora, mas a identificação consultada aponta para canal do Azerbaijão, não da Turquia. Só associar à entrada da playlist depois de confirmar que é a mesma emissora/sinal. |
| 30A Music | PNG em lista de referência: https://i.imgur.com/gNWg9tl.png · Site da emissora: https://30a.media/television/ | A emissora identificada é dos Estados Unidos, não turca. Manter apenas como possível logo da entrada internacional 30A Music se o stream da playlist corresponder a essa emissora. |

## Correspondências que exigem cautela — não usar como logo turca sem confirmação

- **Retro Music Television:** foi encontrada uma versão SVG em https://www.tvchannellists.com/w/File:Retro_Music_Television.svg e uma imagem no Wikimedia Commons em https://commons.wikimedia.org/wiki/File:Retro_Music_TV_logo.png. As referências identificam a emissora como canal de música da República Tcheca, não da Turquia. Não associar automaticamente à entrada da playlist.
- **KN Music TV:** embora exista logo no site oficial, a emissora identificada é azeri. A presença de um stream em infraestrutura de distribuição turca não prova que o canal seja turco.
- **NR1 Fashion One:** a imagem encontrada pode ser antiga em razão do histórico regulatório de alteração de identidade. Confirmar com o sinal atual e fontes oficiais antes de adotar.

## Outras listas consultadas — fontes secundárias de descoberta

Estas listas podem ajudar a cruzar nomes e URLs, mas não devem ser tratadas como autoridades de identidade, atualidade ou licença:

- https://github.com/Roblabs-Teknoloji/iptv
- https://github.com/hayatiptv
- https://github.com/maotuon/iptv-listesi
- https://github.com/tecobaba/m3link
- https://github.com/hhdblog/TR
- https://github.com/maviing/tr
- https://github.com/gkhncksn/m3u8_lists

**Procedimento recomendado:** conferir o canal diretamente no sinal e no site oficial; comparar nome, país e identidade visual; registrar licença e autoria da imagem; só então armazenar uma cópia local. Nenhuma dessas referências foi aplicada à playlist nesta atualização.


---

# Fontes PNG — canais locais e regionais da Tv.m3u

Atualização de 19/11/2026. Esta seção reúne todos os links PNG diretos apresentados na pesquisa de canais locais e regionais. São referências externas para os canais já existentes na playlist; não adiciona emissoras e não altera os campos `tvg-logo` de `Tv.m3u`.

**Critério de uso:** os links são candidatos de imagem. Antes de copiar qualquer arquivo para o repositório ou substituir uma logo, conferir se o PNG abre, se representa o canal correto, se a identidade visual é atual e se há permissão/licença de reutilização. A inclusão neste catálogo não significa que todos os arquivos foram validados individualmente.

## Links PNG diretos por canal

| Canal existente / referência | PNG direto | Observação |
|---|---|---|
| Aksu TV | https://i.imgur.com/mgDCKiy.png | Correspondência em lista M3U de referência. |
| Alanya Posta TV | https://i.imgur.com/a3w9eFe.png | Correspondência em lista M3U de referência. |
| Altaş TV | https://i.imgur.com/XaJ7fp6.png | Correspondência em lista M3U de referência. |
| ARAS TV | https://i.imgur.com/JsDCyWG.png | Correspondência em lista M3U de referência. |
| ATV Alanya | https://i.imgur.com/bUwarR0.png | Correspondência em lista M3U de referência. |
| BRTV Karabük | https://i.imgur.com/U3qlEAp.png | Candidata da pesquisa anterior; confirmar associação exata. |
| Çay TV | https://i.imgur.com/ndupxwu.png | Correspondência em lista M3U de referência. |
| Deniz Postası TV | https://i.imgur.com/Mm8hdfx.png | Correspondência em lista M3U de referência. |
| Edessa TV | https://i.imgur.com/rhU6j9I.png | Correspondência em lista M3U de referência. |
| ER TV Malatya | https://i.imgur.com/VDGEPrD.png | Correspondência em lista M3U de referência para ER TV. |
| Erzurum Web TV | https://i.imgur.com/HF7N4Li.png | Correspondência em lista M3U de referência. |
| ES TV | https://i.imgur.com/epAEBrp.png | Candidata da pesquisa anterior; confirmar associação exata. |
| ETV Manisa | https://i.ibb.co/QKXtdkz/sOd3INg.png | Correspondência em lista M3U de referência. |
| Sun RTV | https://i.imgur.com/64tph9N.png | Correspondência em lista M3U de referência. |
| Anadolu Net TV | https://www.anadolunettv.com/d/r/logo.png | URL PNG indicada como fonte da emissora; verificar correspondência com a entrada “Anadolu TV” da playlist. |
| Bir TV | https://birtv.tv/assets/upload/637f83951df60.png | PNG indicado no site da emissora e em lista M3U. |

## Diretórios e fontes adicionais de descoberta

- TVLogo.org — diretório de logos de canais turcos: https://www.tvlogo.org/turkey/
- Repositório de listas M3U com logos diretas: https://github.com/Roblabs-Teknoloji/iptv
- Lista turca de referência: https://github.com/baycuman-hub/turk-tv
- Gist público com logos e streams de canais turcos: https://gist.github.com/lThrone/8fae0a913039b4676872f6abd30a2b37

## Evidência de correspondência em listas M3U

As listas consultadas confirmam diretamente várias associações nome/PNG/stream, incluindo Aksu TV, Alanya Posta TV, Altaş TV, ATV Alanya, Çay TV, Deniz Postası TV, ETV Manisa, Sun RTV, ARAS TV, Edessa TV, ER TV e Erzurum Web TV. Referências:
- https://github.com/Roblabs-Teknoloji/iptv/blob/master/index.m3u
- https://gist.github.com/lThrone/8fae0a913039b4676872f6abd30a2b37
- https://github.com/stardustbro/StarDustyList/blob/main/clean_playlist.m3u

**Limitação da pesquisa:** os PNGs de BRTV Karabük e ES TV foram preservados porque foram apresentados na pesquisa anterior, mas não tiveram confirmação independente equivalente nas listas consultadas nesta atualização. Anadolu Net TV também deve ser comparada com a entrada “Anadolu TV” antes de qualquer adoção. A URL da Bir TV aparece como PNG de emissora e em lista de referência.

Nenhum arquivo de imagem foi baixado para o repositório nesta etapa. Este catálogo armazena os endereços e as observações para posterior validação; a playlist permanece intacta.


---

# Complemento de fontes PNG — demais canais locais e regionais da Tv.m3u

Pesquisa complementar de 19/11/2026. Esta seção acrescenta fontes PNG diretas para outros canais que já aparecem na categoria `REGIONAIS` da playlist. Os links são extraídos de listas M3U públicas e/ou páginas de emissoras. Não representam validação de licença, nem confirmação visual independente de cada arquivo. Não alterar a playlist automaticamente.

## PNGs diretos encontrados

| Canal na Tv.m3u | PNG direto | Fonte / observação |
|---|---|---|
| Hunat TV | https://i.imgur.com/NrxHGnb.png | Lista M3U turca; nome e stream coincidem. |
| İçel TV | https://i.imgur.com/CGwImKv.png | Lista M3U turca; nome e stream coincidem. |
| Kanal 12 | https://i.imgur.com/51xCkXG.png | Lista M3U turca; nome e stream coincidem. |
| Kanal 15 | https://i.imgur.com/wb1Cdc9.png | Lista M3U turca; nome e stream coincidem. |
| Kanal 23 | https://i.imgur.com/3br8RCq.png | Duas listas de referência associam a imagem ao canal. |
| Kanal 26 Eskişehir | https://i.imgur.com/Mr7XPii.png | Lista M3U; confirmar que corresponde à entrada “Kanal 26 Eskişehir”. |
| Kanal 33 | https://i.imgur.com/5WYaoFZ.png | Lista M3U turca; nome e stream coincidem. |
| Kanal 34 | https://i.imgur.com/SIaI6Sj.png | Lista M3U turca; confirmar se é a mesma emissora local da playlist. |
| Kanal 58 | https://i.imgur.com/Rgc66sv.png | Lista M3U turca; nome e stream coincidem. |
| Kanal V | https://i.imgur.com/7RNjTno.png | Lista M3U turca; nome e stream coincidem. |
| Kardelen TV | https://www.tvlogo.org/turkey/kardelen-tv-tr.png | Diretório de logos da Turquia; confirmar URL e identidade visual atual. |
| Kent Türk TV | https://i.imgur.com/FQKPjsm.png | Lista M3U turca; nome semelhante e stream de Kent Türk. |
| Kocaeli TV | https://i.imgur.com/LeTP4zq.png | Lista M3U turca; nome e stream coincidem. |
| Konya Olay TV | https://www.konyaolaytv.com/upload/tema/20230307__5154687762.jpg | Fonte no domínio da emissora; imagem é JPG, não PNG. Mantida como referência, não como PNG validado. |
| Mercan TV | https://i.imgur.com/3CWV8bS.png | Lista M3U turca; nome e stream coincidem. |
| MTürk TV | https://i.imgur.com/xj1gvrq.png | Lista M3U turca; nome e stream coincidem. |
| Tempo TV | https://i.imgur.com/tZpx32y.png | Lista M3U turca; nome e stream coincidem. |
| TV 1 | https://i.imgur.com/8CtrYVb.png | Lista M3U turca; nome e stream coincidem. |
| TV 264 | https://i.imgur.com/tudXdOZ.png | Listas M3U independentes associam a imagem ao canal. |
| TV 41 | https://i.imgur.com/6T472LM.png | Listas M3U independentes associam a imagem ao canal. |
| TV 42 | https://www.tv42.com.tr/logo.png | PNG no domínio oficial da emissora. |
| TV 52 | https://i.imgur.com/k4R5CzO.png | Listas M3U e referência institucional para TV52. |
| TV Den | https://i.imgur.com/Uhg95Ze.png | Lista M3U turca; nome e stream coincidem. |
| Urfanatik TV | https://i.imgur.com/8KO0uxn.png | Lista M3U usa o nome “Urfa Natik TV”, com o mesmo stream da entrada Urfanatik TV; confirmar grafia/identidade. |
| Van 65 TV | https://van65tv.com/assets/images/logo/logo.png | PNG no domínio da própria emissora. |

## Referências consultadas

- Lista de canais turcos com imagens diretas e streams: https://github.com/baycuman-hub/turk-tv/blob/main/Turk-Kanallari.m3u
- Outra lista M3U com logos de Kanal 23, 26, 32, 33, 53, 56, 58 e Kanal Fırat: https://github.com/erdodo/iptv/blob/main/tv.m3u8
- Lista de referência com logos de ETV Kayseri, Hunat TV, İçel TV e outros canais locais: https://gist.github.com/akan1970/ba2a378e5552a1feabca4c9c8a73b075
- Diretório de logos de canais turcos: https://www.tvlogo.org/turkey/
- Catálogo de canais locais: https://tr.canlitv.watch/kanallar/yerel

## Canais da categoria REGIONAIS ainda sem PNG direto confirmado nesta rodada

Aksu TV, Alanya Posta TV, Altaş TV, ARAS TV, ATV Alanya, BRTV Karabük, Çay TV, Deniz Postası TV, Dim TV, Edessa TV, ER TV Malatya, Erciyes TV, Erzurum Web TV, ES TV, ETV, Ezgi TV, FRT TV, GRT Gaziantep TV, Güneydoğu TV, İzmir Time 35 TV, K+ Kayseri, Kanal 19, Kanal 32, Kanal B, Kanal Fırat, Kayhan TV, Konya KTV, Mekameleen TV, Tivi 6, Natural TV, Sun RTV, TBMM TV, Vuslat TV, YOL TV, Kanal Ada, Kanal Urfa, Trabzon Büyükşehir Belediyesi TV, MK TV e outros que exigem conferência individual. Alguns desses canais já possuem fontes registradas em seções anteriores deste catálogo; esta lista indica apenas que não foi acrescentado um novo PNG direto confirmado nesta rodada.

**Atenção à classificação:** Mekameleen TV e TBMM TV não são necessariamente canais locais comerciais; a presença em `group-title="REGIONAIS"` da playlist não comprova que sejam emissoras regionais. Confirmar a natureza de cada emissora antes de padronizar ou mover categorias.

Nenhum PNG foi baixado para o repositório nesta atualização. Foram acrescentados apenas URLs e notas de validação. `Tv.m3u` permanece intacta.


---

# Inventário completo dos canais REGIONAIS da Tv.m3u — 68 entradas

Esta tabela inclui **todos os 68 canais** identificados na categoria `group-title="REGIONAIS"` da versão da playlist consultada em 19/11/2026. O objetivo é manter um controle único: quais já têm referências de logo registradas neste catálogo e quais ainda precisam de pesquisa. “Fonte registrada” não significa que o arquivo foi baixado, que a URL foi testada agora ou que a imagem foi aprovada para uso.

| Canal na playlist | Situação das fontes neste catálogo |
|---|---|
| Aksu TV | Fonte PNG registrada na seção anterior |
| Alanya Posta TV | Fonte PNG registrada na seção anterior |
| Altas TV | Fonte PNG registrada como Altaş TV |
| Anadolu TV | Candidata Anadolu Net TV; identidade ainda precisa ser comparada |
| ARAS TV | Fonte PNG registrada na seção anterior |
| ATV Alanya | Fonte PNG registrada na seção anterior |
| BRTV Karabük | Fonte candidata registrada; confirmação independente pendente |
| Çay TV | Fonte PNG registrada na seção anterior |
| Deniz Postası TV | Fonte PNG registrada na seção anterior |
| Dim TV | Sem novo PNG direto registrado |
| Edessa TV | Fonte PNG registrada na seção anterior |
| ER TV Malatya | Fonte PNG registrada na seção anterior |
| Erciyes TV | Sem novo PNG direto registrado |
| Erzurum Web TV | Fonte PNG registrada na seção anterior |
| ES TV | Fonte candidata registrada; confirmação independente pendente |
| ETV | Sem novo PNG direto registrado; não confundir com ETV Manisa |
| Ezgi TV | Sem novo PNG direto registrado |
| FRT TV | Sem novo PNG direto registrado |
| GRT Gaziantep TV | Sem novo PNG direto registrado |
| Güneydoğu TV | Sem novo PNG direto registrado |
| Hunat TV | PNG direto acrescentado na atualização complementar |
| İçel TV | PNG direto acrescentado na atualização complementar |
| Kardelen TV | Fonte de diretório registrada na atualização complementar; validar arquivo |
| İzmir Time 35 TV | Sem novo PNG direto registrado |
| K+ Kayseri | Sem novo PNG direto registrado |
| Kanal 12 | PNG direto acrescentado na atualização complementar |
| Kanal 15 | PNG direto acrescentado na atualização complementar |
| Kanal 19 | Sem novo PNG direto registrado |
| Kanal 23 | PNG direto acrescentado na atualização complementar |
| Kanal 26 Eskişehir | PNG direto acrescentado na atualização complementar; confirmar correspondência |
| Kanal 3 | Sem novo PNG direto registrado |
| Kanal 32 | Sem novo PNG direto registrado nesta rodada |
| Kanal 33 | PNG direto acrescentado na atualização complementar |
| Kanal 34 | PNG direto acrescentado na atualização complementar; confirmar emissora |
| Kanal 53 | Sem novo PNG direto registrado |
| Kanal 58 | PNG direto acrescentado na atualização complementar |
| Kanal B | Sem novo PNG direto registrado |
| Kanal Fırat | Sem novo PNG direto registrado |
| Kanal V | PNG direto acrescentado na atualização complementar |
| Kay TV | Sem novo PNG direto registrado |
| Kayhan TV | Sem novo PNG direto registrado |
| Kent Türk TV | PNG direto acrescentado na atualização complementar |
| Kocaeli TV | PNG direto acrescentado na atualização complementar |
| Konya KTV | Sem novo PNG direto registrado |
| Konya Olay TV | Referência de imagem JPG registrada; não é PNG |
| Mekameleen TV | Sem novo PNG direto registrado; classificar identidade/categoria |
| Mercan TV | PNG direto acrescentado na atualização complementar |
| MTürk TV | PNG direto acrescentado na atualização complementar |
| Tempo TV | PNG direto acrescentado na atualização complementar |
| Tivi 6 | Sem novo PNG direto registrado |
| Ton TV | Sem novo PNG direto registrado |
| TV 1 | PNG direto acrescentado na atualização complementar |
| TV 264 | PNG direto acrescentado na atualização complementar |
| TV 41 | PNG direto acrescentado na atualização complementar |
| TV 52 | PNG direto acrescentado na atualização complementar |
| TV DEN | PNG direto acrescentado na atualização complementar |
| Vuslat TV | Sem novo PNG direto registrado |
| Natural TV | Sem novo PNG direto registrado |
| Sun RTV | Fonte PNG registrada na seção anterior |
| TBMM TV | Sem novo PNG direto registrado; emissora institucional, não regional comercial |
| Van 65 TV | PNG direto no domínio da emissora acrescentado na atualização complementar |
| YOL TV | Sem novo PNG direto registrado |
| Kanal Ada | Sem URL de logo registrada; entrada sem tvg-logo na playlist |
| Kanal Urfa | Sem novo PNG direto registrado |
| Trabzon Buyuksehir Belediyesi TV | Sem novo PNG direto registrado |
| Urfanatik TV | PNG direto acrescentado; confirmar grafia/identidade |
| ETV Manisa | Fonte PNG registrada na seção anterior |
| MK TV | Sem novo PNG direto registrado |

**Resultado do inventário:** 68 de 68 canais estão agora listados nominalmente neste arquivo. Os canais sem fonte direta continuam explicitamente marcados como pendentes, em vez de receberem URLs inventadas ou logos de emissoras homônimas. Os links PNG candidatos das seções anteriores e complementares permanecem sujeitos a validação visual, disponibilidade e correspondência de identidade. A playlist não foi modificada.


# Logos originais de canais de música — referências visuais pesquisadas em 20/11/2026

Esta seção registra as referências visuais identificadas para canais de música já presentes na playlist `Tv.m3u`. Os links são fontes externas; nenhum arquivo de imagem foi baixado para o repositório nesta atualização e nenhuma entrada da playlist foi alterada.

| Canal da playlist | Referência direta da imagem | Fonte / observação | Situação |
|---|---|---|---|
| Dream Türk | https://blutv-images.mncdn.com/q/t/i/bluv2/100/750x750/5dc2c085866ac31da06187cd | Imagem CDN associada ao canal; também aparece em listas M3U de referência | Candidata; validar versão atual |
| PowerTürk TV | https://blutv-images.mncdn.com/q/t/i/bluv2/100/750x750/5dc2c125866ac31da06187d6 | Imagem CDN associada ao canal; também aparece em listas M3U de referência | Candidata; validar versão atual |
| Kral Pop | http://assets.tvcdn.net/61431fea-4103-46a3-9f8c-aad1504b9776.png | Imagem usada em lista M3U de referência para Kral Pop TV | Candidata; validar versão atual |
| TRT Müzik | https://cdn-i.pr.trt.com.tr/trttv/w750/h750/q100/12382043.png | Imagem servida no domínio CDN da TRT; portal institucional de logos: https://www.trt.net.tr/kurumsal/logolar | Referência institucional; conferir correspondência com a identidade visual vigente |
| Kral TV (histórico) | https://commons.wikimedia.org/wiki/File:Kral_TV_logo.png | Wikimedia Commons; referência histórica, não confundir com Kral Pop | Apenas referência histórica; não usar como logo atual de Kral Pop |

## Fontes de confirmação e contexto

- Lista M3U de referência com Dream Türk, PowerTürk TV, Kral Pop TV e Number One TV: https://github.com/hhdblog/TR/blob/main/tv_radyo.m3u
- Lista M3U de referência com Dream Türk, PowerTürk TV e TRT Müzik: https://github.com/tecobaba/m3link/blob/main/ulusal.m3u
- Outra lista M3U de referência com Dream Türk, PowerTürk TV, TRT Müzik e canais NR1: https://github.com/officialmmt/lists/blob/main/bos.m3u
- Página de canais de música que identifica TRT Müzik, Dream Türk, Kral Pop TV, Number1 TV e PowerTürk TV: https://televizyon.com.tr/kanallar
- Portal oficial de logos da TRT: https://www.trt.net.tr/kurumsal/logolar
- Categoria de logos de canais turcos no Wikimedia Commons: https://commons.wikimedia.org/wiki/Category:Logos_of_television_channels_in_Turkey

**Critérios:** uma imagem encontrada em lista M3U ou CDN de terceiros é tratada como referência/candidata, não como confirmação automática de que seja o logo oficial e atual. A imagem histórica de Kral TV foi separada de Kral Pop para evitar associação incorreta. Antes de aplicar qualquer logo à playlist, verificar visualmente a identidade, atualidade, transparência, resolução e licença/condições de reutilização.


# Galeria visual — quatro logos originais de canais de música

As quatro imagens abaixo foram incorporadas como referências visuais externas para consulta. Elas não foram baixadas nem armazenadas como arquivos locais neste commit.

### Dream Türk
![Referência visual da logo Dream Türk](https://blutv-images.mncdn.com/q/t/i/bluv2/100/750x750/5dc2c085866ac31da06187cd)

Fonte da imagem: CDN associada ao canal. Validar se corresponde à identidade visual atual.

### PowerTürk TV
![Referência visual da logo PowerTürk TV](https://blutv-images.mncdn.com/q/t/i/bluv2/100/750x750/5dc2c125866ac31da06187d6)

Fonte da imagem: CDN associada ao canal. Validar se corresponde à identidade visual atual.

### Kral Pop
![Referência visual da logo Kral Pop](http://assets.tvcdn.net/61431fea-4103-46a3-9f8c-aad1504b9776.png)

Fonte da imagem: CDN de imagens de TV, referenciada em lista M3U para Kral Pop TV. Confirmar a versão vigente.

### TRT Müzik
![Referência visual da logo TRT Müzik](https://cdn-i.pr.trt.com.tr/trttv/w750/h750/q100/12382043.png)

Fonte da imagem: domínio CDN da TRT. Conferir correspondência com o pacote institucional de logos em https://www.trt.net.tr/kurumsal/logolar.

**Nota de validação:** estas imagens são referências de trabalho, não uma aprovação definitiva de uso. Verificar identidade, atualidade, resolução e condições de reutilização antes de substituir qualquer logo na playlist. Nenhuma playlist foi alterada.


# Inventário complementar — canais de música da Tv.m3u (fontes candidatas e pendências)

Esta seção registra os 24 canais da categoria `MÚSICA` que ainda não estavam contemplados na galeria de quatro logos originais (Dream Türk, PowerTürk TV, Kral Pop e TRT Müzik). As URLs abaixo são referências de pesquisa: não se afirma que todos os arquivos foram baixados, que permanecem ativos ou que representam a identidade visual atual. Não usar estas imagens para substituir logos na playlist sem validação visual e confirmação da emissora.

## Fontes de imagem candidatas localizadas

| Canal na Tv.m3u | Referência de imagem ou fonte | Observação |
|---|---|---|
| NR1 Aşk | https://www.tvlogo.org/turkey/nr1-ask-tr.png | Candidato do diretório TVLogo; validar versão e identidade. |
| NR1 Damar | https://www.tvlogo.org/turkey/nr1-damar-tr.png | Candidato do diretório TVLogo; validar versão e identidade. |
| NR1 Dance | https://www.tvlogo.org/turkey/nr1-dance-tr.png | Candidato do diretório TVLogo; validar versão e identidade. |
| Number 1 TV | https://www.tvlogo.org/turkey/nr1-tr.png | Candidato do diretório TVLogo; conferir se corresponde à variante exata da playlist. |
| NR1 Fashion One | https://i.ibb.co/HV0x9JZ/fashion-one.png | Referência PNG encontrada em lista M3U; pode ser antiga. |
| Med Müzik | https://i.imgur.com/gtUFmCD.png | PNG candidato; referência de canal turco de música curda. Confirmar atualidade. |
| Power Dance TV | https://cdn.powergroup.com.tr/image/500x500/powerapp/channels/v3/logo_40.png | CDN do Power Group; candidato associado ao canal. |
| Power Love TV | https://cdn.powergroup.com.tr/image/500x500/powerapp/channels/v3/logo_2559.png | CDN do Power Group; candidato associado ao canal. |
| PowerTürk Taptaze | https://cdn.powergroup.com.tr/image/500x500/powerapp/channels/v3/logo_2534.png | CDN do Power Group; candidato associado à marca/canal. |
| Power TV (720p) | https://i.ibb.co/JrXDQJy/power-tv.png | Referência PNG encontrada em lista M3U; validar correspondência com a entrada da playlist. |
| TopPop | https://assets.tvcdn.net/4a8468ec-c134-4db1-93ef-699f15e1522b.png | CDN de imagens de TV; candidato, identidade atual a confirmar. |
| Now 70 s | https://epg.ovh/logo/NOW+70s.png | Diretório de logos EPG; confirmar que corresponde à entrada da playlist. |
| Now 80 s | https://epg.ovh/logo/NOW+80s.png | Diretório de logos EPG; confirmar que corresponde à entrada da playlist. |
| NOW ROCK | https://epg.ovh/logo/NOW+ROCK.png | Diretório de logos EPG; confirmar que corresponde à entrada da playlist. |
| KN Music TV | https://www.knmusictv.com/wp-content/uploads/2026/01/LOGO2112.png | Site do canal; emissora do Azerbaijão, não turca. Manter separada das identidades turcas. |
| Retro Music Television | https://www.tvchannellists.com/w/File:Retro_Music_Television.svg | Referência SVG; canal tcheco, não turco. Página de arquivo, não URL PNG direta. |
| 30A Music | https://30a.media/television/ | Página institucional da emissora; emissora norte-americana. Não foi identificada URL direta de PNG nesta pesquisa. |
| TMB TV | https://www.tvlogo.org/turkey/tmb-tr.png | PNG candidato atribuído ao TMB TV; confirmar no site da emissora antes de aprovar. |

## Canais sem logo original inequívoca ou com identidade divergente

| Canal na Tv.m3u | Resultado da pesquisa | Próxima validação necessária |
|---|---|---|
| 1Mus | A correspondência encontrada para “1MUS COM” é russa e não comprova relação com a entrada da playlist. | Identificar emissora, país e site oficial antes de associar qualquer logo. |
| Play TV | Não foi localizada correspondência inequívoca com um canal musical turco. | Obter nome empresarial, site ou identificador de transmissão. |
| Dost | Foi localizada uma imagem de Dost TV (https://www.tvlogo.org/turkey/dost-tv-tr.png), mas a emissora identificada é religiosa, não um canal musical. Não associar automaticamente. | Confirmar se a entrada “Dost” da playlist é realmente Dost TV ou outra emissora. |
| Company TV | A correspondência localizada é uma emissora musical italiana; não há evidência de que seja a entrada da playlist. | Confirmar país, operador e identidade da entrada. |
| Güçlü TV | Foi localizada uma referência institucional à Türkü Yayıncılık (https://turkuyayincilik.net/), mas não foi confirmada uma URL de logo isolada e atual. | Solicitar/identificar o arquivo oficial da emissora e confirmar que corresponde à entrada. |
| IQ Channel | A correspondência encontrada é um antigo canal musical da Costa Rica, sem vínculo comprovado com a entrada da playlist. | Identificar a emissora correta antes de usar essa imagem. |

## Critérios de aprovação

1. Priorizar arquivo publicado no site/CDN oficial da própria emissora ou em pacote institucional de logos.
2. Conferir visualmente o nome, símbolo, país e variante do canal contra a entrada exata em `Tv.m3u`.
3. Marcar como “candidato” qualquer arquivo vindo de diretório de terceiros, lista M3U, agregador ou CDN sem confirmação oficial.
4. Não reutilizar logos de canais homônimos de outros países (por exemplo, KN Music TV, Retro Music Television, Company TV ou IQ Channel) como se fossem turcos.
5. Não alterar `Tv.m3u`, `TV2.m3u`, `Euro.m3u` ou `Backup.m3u` durante esta etapa de pesquisa.

**Estado:** referências catalogadas para pesquisa; nenhuma logo foi aprovada para substituição e nenhuma playlist foi modificada.


# Fontes oficiais adicionais — canais musicais e identidades institucionais (20/11/2026)

Esta seção separa **fontes primárias/publicadas pelos próprios grupos ou emissoras** de referências secundárias. Uma página institucional confirma a identidade e a existência do canal, mas não significa, por si só, que tenha sido localizado um arquivo de logo atual, direto e reutilizável. As fontes abaixo foram acrescentadas para orientar a validação dos canais pendentes da categoria `MÚSICA` e de marcas musicais já presentes em `Tv.m3u`.

## Fontes primárias confirmadas

| Canal/marca relacionada à playlist | Fonte institucional | O que confirma | Situação para uso de logo |
|---|---|---|---|
| PowerTürk TV | https://www.powerapp.com.tr/tvs/power-tvs/ | Página oficial PowerApp lista PowerTürk TV entre os canais de televisão do grupo. | Fonte oficial de identidade; conferir/obter a imagem atual diretamente da página ou do CDN oficial antes de aplicar. |
| Power TV | https://www.powerapp.com.tr/tvs/power-tvs/ | Página oficial PowerApp lista Power TV. | Fonte oficial de identidade; a referência PNG de terceiros já catalogada continua sendo apenas candidata. |
| Power Dance TV | https://www.powerapp.com.tr/tvs/power-tvs/powerdancetv/ | Página oficial individual do canal e presença na lista de TVs PowerApp. | Fonte oficial de identidade; usar a arte servida pelo site oficial após validação visual. |
| Power Love TV | https://www.powerapp.com.tr/tvs/power-tvs/ | Página oficial PowerApp lista Power Love TV. | Fonte oficial de identidade; conferir a imagem atual no site/CDN oficial. |
| PowerTürk Taptaze TV | https://www.powerapp.com.tr/tvs/power-tvs/ | Página oficial PowerApp lista PowerTürk Taptaze TV. | Fonte oficial de identidade; conferir a imagem atual no site/CDN oficial. |
| NR1 / Number 1 TV, Number1 Aşk, Number1 Dance e Fashion One | https://www.numberone.com.tr/tv/ | Página oficial Number1 lista páginas/transmissões para Nr1 TV, Nr1 Türk, Number1 Aşk, Number1 Dance e Fashionone TV. | Fonte primária para confirmar as marcas. A página não foi tratada como confirmação de arquivo de logo PNG direto. |
| Güçlü TV | https://turkuyayincilik.net/ | Site institucional da Türkü Yayıncılık identifica Güçlü TV e apresenta dados de transmissão. | Fonte oficial de identidade; não foi localizado nesta consulta um arquivo de logo direto e inequívoco. Confirmar situação de licença/transmissão antes de aprovar a marca para a entrada atual da playlist. |
| TRT Müzik | https://www.trt.net.tr/kurumsal/logolar ; https://www.trt.net.tr/logos/Televizyon.zip | Portal institucional de logos e pacote de logos da TRT. | Fonte oficial prioritária; comparar o arquivo do pacote com a imagem atualmente usada. |
| Dream Türk | https://www.dreamturk.com.tr/ | Site oficial associado à marca Dream Türk; a página institucional/expediente do grupo confirma a identidade editorial. | Fonte primária de identidade; o CDN de imagem já listado no catálogo permanece referência até validar a versão atual. |
| 30A Music | https://30a.media/television/ | Site da própria 30A Media apresenta a operação de televisão 30A. | Fonte oficial da emissora norte-americana, mas não comprova que seja a identidade correta da entrada “30A Music” da playlist turca. Não aplicar sem confirmar essa correspondência. |

## Canais pendentes sem fonte oficial inequívoca localizada

| Entrada em Tv.m3u | Resultado desta rodada |
|---|---|
| 1Mus | Não foi encontrada página institucional oficial que vincule inequivocamente a marca à entrada e ao stream da playlist. As duas imagens de listas externas permanecem candidatas, não oficiais. |
| Play TV | Não foi identificada emissora/site oficial que corresponda de forma inequívoca ao canal e ao stream da playlist. |
| Dost | O resultado “Dost TV” encontrado em diretórios refere-se a uma emissora religiosa; não comprova identidade com a entrada musical “Dost”. Não reutilizar essa logo. |
| Company TV | Não foi localizada fonte oficial que associe a entrada da playlist a uma emissora musical turca. Não usar a emissora italiana homônima. |
| IQ Channel | Não foi localizada fonte institucional correspondente à entrada da playlist; resultados homônimos estrangeiros não são prova de identidade. |
| TopPop | Há referências em playlists de terceiros e dados de stream, mas não foi identificada página institucional oficial que confirme a marca e forneça logo. |
| Retro Music Television | A referência visual encontrada é de uma emissora tcheca; não é fonte oficial para a entrada da playlist. |

## Referências regulatórias e diretórios secundários — não são fontes de arquivos oficiais

- RTÜK — https://www.rtuk.gov.tr/ : usar para conferir titularidade, licença, nome jurídico e situação regulatória de serviços de mídia; documentos regulatórios não substituem um pacote oficial de identidade visual.
- Televizyon.com.tr — https://televizyon.com.tr/kanallar/muzik : diretório secundário útil para cruzar nomes e grupos de canais musicais; não tratar como fonte oficial de logos.
- TVLogo.org — https://www.tvlogo.org/turkey/ : repositório de terceiros; pode fornecer PNGs candidatos, mas não transforma os arquivos em logos oficiais.
- Playlists M3U públicas: fontes de descoberta e comparação de metadados, nunca prova isolada de titularidade ou oficialidade de uma imagem.

## Regras de classificação adotadas

1. **Oficial/primária:** domínio da emissora ou do grupo responsável, portal institucional ou pacote de identidade visual publicado pelo titular.
2. **Secundária:** diretório de logos, agregador de canais, CDN sem vínculo institucional demonstrado ou playlist de terceiros.
3. **Identidade não confirmada:** nome semelhante, canal de outro país, stream sem dados institucionais ou marca homônima.
4. Uma fonte oficial de identidade não autoriza automaticamente baixar, redistribuir ou converter a imagem; verificar termos de uso, licença e condições de reutilização.
5. Nenhuma logo foi aprovada ou aplicada nesta atualização. Nenhuma playlist foi modificada; esta alteração limita-se ao catálogo unificado.


---

# Logos pesquisadas no Google — LUYS TV e MUKABELE TV

Imagens localizadas por pesquisa de imagens e cruzamento com fontes públicas. As duas referências ficam registradas como imagens externas no catálogo; não foram baixadas nem armazenadas como arquivos binários neste commit.

## LUYS TV

![Logo LUYS TV](https://pbs.twimg.com/profile_images/1476179658643226628/8FjXUjD6.jpg)

- Imagem direta: https://pbs.twimg.com/profile_images/1476179658643226628/8FjXUjD6.jpg
- Perfil associado à emissora: https://x.com/luystv
- Site institucional: https://luysmedya.com/
- Confirmação regulatória: RTÜK, reunião 2021/34, decisão 7, aprovou a alteração do logotipo de “LUYS 1” para “LUYS TV”: https://www.rtuk.gov.tr/UstKurulKarar/Detay/17061
- Classificação: imagem associada ao perfil da emissora; referência visual identificada. A decisão do RTÜK confirma o nome da marca, não necessariamente a atualidade desta imagem específica.

## MUKABELE TV

![Logo MUKABELE TV](https://assets.tvcdn.net/23b391ac-5edb-4e37-8664-27da64fb0785.png)

- Imagem direta: https://assets.tvcdn.net/23b391ac-5edb-4e37-8664-27da64fb0785.png
- Referência em playlist pública com a entrada “MUKABELE TV” e identificador “MUKABELE TV.tr”: https://github.com/erdodo/iptv/blob/main/tv.m3u8
- Referência adicional com a mesma imagem e nome do canal: https://github.com/tecobaba/m3link/blob/main/ulusal.m3u
- Stream listado junto à entrada em uma das referências: https://stream.tvcdn.net/dini/mukabele-tv.m3u8
- Classificação: imagem associada de forma consistente ao serviço/canal “Mukabele TV” em listas públicas de canais; não foi localizada confirmação institucional independente do titular da marca.

## Nota de procedência

As imagens acima foram localizadas por pesquisa pública na web (incluindo resultados de imagens e páginas indexadas). A inclusão registra as referências visuais e suas fontes para consulta; não declara que os arquivos sejam licenciados para redistribuição nem que tenham sido baixados para o repositório. Antes de converter ou redistribuir localmente, verificar direitos e condições de uso. Esta atualização altera somente o catálogo unificado, não as playlists.


---

# Galeria completa de logos — canais da Tv.m3u

Inventário visual gerado a partir das entradas da playlist `Tv.m3u` na branch `github/workflows/atualizar-logos.yml`. Cada miniatura usa exatamente o endereço `tvg-logo` já declarado na playlist; nenhuma URL foi inventada e nenhuma playlist foi modificada. As imagens são carregadas dos seus endereços de origem (incluindo arquivos hospedados neste repositório), não duplicadas como arquivos binários dentro deste catálogo.

**Cobertura:** 211 entradas de canais; 210 entradas com URL de logo na playlist; 1 entrada sem `tvg-logo` cadastrado (Kanal Ada, cuja identidade visual existe, mas cuja URL direta ainda não foi confirmada).

## NOTÍCIAS (31)

| Canal | Logo |
|---|---|
| 24 TV | ![Logo 24 TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/24-tr-6c8ffebcb1.svg) |
| Lider Haber | ![Logo Lider Haber ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/liderhaber.png) |
| A Haber | ![Logo A Haber ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/a-haber-tr-afc99b5484.svg) |
| A Para | ![Logo A Para ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/a-para-tr-554f2e296a.svg) |
| AS TV | ![Logo AS TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/astv.png) |
| Bengü Türk | ![Logo Bengü Türk ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/bengu-turk-tr-df28759989.svg) |
| Bloomberg HT | ![Logo Bloomberg HT ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/bloomberg-ht-tr-5043c40214.svg) |
| Bloomberg HT 2 | ![Logo Bloomberg HT 2 ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/bloomberght2.png) |
| CNBC e | ![Logo CNBC e ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/cnbc-e-tr-07bac24fc2.svg) |
| CNN Türk | ![Logo CNN Türk ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/cnn-turk-tr-4b24f7fc71.svg) |
| DHA | ![Logo DHA ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/dha.png) |
| Ekotürk | ![Logo Ekotürk ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/ekoturk-tr-f24a44f2a2.svg) |
| Flash Haber TV | ![Logo Flash Haber TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/flashhabertv.png) |
| Haber Global | ![Logo Haber Global ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/haber-global-tr-84b7531601.svg) |
| Haber61 TV | ![Logo Haber61 TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/haber61tv.png) |
| Habertürk | ![Logo Habertürk ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/haberturk-tr-216bd975f1.svg) |
| Halk TV | ![Logo Halk TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/halk-tv-tr-eb19ced815.svg) |
| İlke TV | ![Logo İlke TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/ilketv.png) |
| Life TV | ![Logo Life TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/lifetv.png) |
| NTV | ![Logo NTV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/ntv-tr-db227ac5f3.svg) |
| TELE1 | ![Logo TELE1 ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/tele1-tr-23e3dde442.svg) |
| TGRT Haber | ![Logo TGRT Haber ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/tgrt-haber-tr-909feb71b1.svg) |
| TRT Haber | ![Logo TRT Haber ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/trt-haber-tr-71c1281f72.svg) |
| TürkHaber | ![Logo TürkHaber ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/turk-haber-tr-a295fd4816.svg) |
| TV100 | ![Logo TV100 ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/tv100-tr-c1bb2dda9f.svg) |
| TV5 | ![Logo TV5 ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/tv5-tr-8d4e094d6e.svg) |
| TVNET | ![Logo TVNET ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/tvnet-tr-eabc386abb.svg) |
| Ülke TV | ![Logo Ülke TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/ulke-tv-tr-85b432a94c.svg) |
| Sözcü TV | ![Logo Sözcü TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/sozcutv.png) |
| Ekol TV | ![Logo Ekol TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/ekoltv.png) |
| GZT | ![Logo GZT ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/gzt.png) |

## ENTRETENIMENTO (19)

| Canal | Logo |
|---|---|
| 360 TV | ![Logo 360 TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/360-tr-94cc53e4c2.svg) |
| 4U TV | ![Logo 4U TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/4utv.png) |
| A2 | ![Logo A2 ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/a2-tr-73490be5f4.svg) |
| ATV | ![Logo ATV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/atv-tr-0ff6d6098d.svg) |
| Beyaz TV | ![Logo Beyaz TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/beyaz-tv-tr-db1ed61595.svg) |
| Bi Kanal | ![Logo Bi Kanal ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/bikanal.png) |
| Bir TV | ![Logo Bir TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/birtv.png) |
| EURO D | ![Logo EURO D ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/euro-d-tr-dec2cd5c7b.svg) |
| Kanal 7 Avrupa | ![Logo Kanal 7 Avrupa ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/kanal-7-avrupa-tr-652c0937af.svg) |
| Kanal D | ![Logo Kanal D ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/kanal-d-tr-b170d0acaf.svg) |
| Kanal D Drama | ![Logo Kanal D Drama ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/kanalddrama.png) |
| NOW | ![Logo NOW ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/now-tr-c1ea46eafb.svg) |
| Show Max | ![Logo Show Max ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/show-max-tr-376e98d883.svg) |
| Show TV | ![Logo Show TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/showtv.png) |
| Star TV | ![Logo Star TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/star-tv-tr-8c39b00aae.svg) |
| teve2 | ![Logo teve2 ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/teve2-tr-4dfc4fc940.svg) |
| TRT 1 | ![Logo TRT 1 ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/trt-1-tr-770d4f54e5.svg) |
| TV8 | ![Logo TV8 ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/tv8-tr-3fc55e9fc0.svg) |
| Euro Star TV | ![Logo Euro Star TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/eurostartv.png) |

## ESPORTES (7)

| Canal | Logo |
|---|---|
| A Spor | ![Logo A Spor ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/a-spor-tr-a909d55490.svg) |
| FB TV | ![Logo FB TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/fbtv.png) |
| HT Spor TV | ![Logo HT Spor TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/htsportv.png) |
| TAY TV | ![Logo TAY TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/tay-tv-tr-b8a6ca1c6a.svg) |
| TJK TV | ![Logo TJK TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/tjk-tv-tr-cc00aa14d4.svg) |
| Ekol Sports | ![Logo Ekol Sports ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/ekolsports.png) |
| beIN Sports 1 Turk | ![Logo beIN Sports 1 Turk ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/beinsports1turk.png) |

## REGIONAIS (68)

| Canal | Logo |
|---|---|
| Aksu TV | ![Logo Aksu TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/aksu-tv-tr-41a97bb2ae.svg) |
| Alanya Posta TV | ![Logo Alanya Posta TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/alanyapostatv.png) |
| Altas TV | ![Logo Altas TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/altas-tv-tr-2c1a3838b8.svg) |
| Anadolu TV | ![Logo Anadolu TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/anadolutv.png) |
| ARAS TV | ![Logo ARAS TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/arastv.png) |
| ATV Alanya | ![Logo ATV Alanya ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/atvalanya.png) |
| BRTV Karabük | ![Logo BRTV Karabük ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/brtv-tr-e91e9891f3.svg) |
| Çay TV | ![Logo Çay TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/cay-tv-tr-ea28c9051f.svg) |
| Deniz Postası TV | ![Logo Deniz Postası TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/denizpostastv.png) |
| Dim TV | ![Logo Dim TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/dimtv.png) |
| Edessa TV | ![Logo Edessa TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/edessa-tv-tr-d97485b114.svg) |
| ER TV Malatya | ![Logo ER TV Malatya ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/ertvmalatya.png) |
| Erciyes TV | ![Logo Erciyes TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/erciyestv.png) |
| Erzurum Web TV | ![Logo Erzurum Web TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/erzurumwebtv.png) |
| ES TV | ![Logo ES TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/es-tv-tr-603faff734.svg) |
| ETV | ![Logo ETV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/etv.png) |
| Ezgi TV | ![Logo Ezgi TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/ezgitv.png) |
| FRT TV | ![Logo FRT TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/frttv.png) |
| GRT Gaziantep TV | ![Logo GRT Gaziantep TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/grtgazianteptv.png) |
| Güneydoğu TV | ![Logo Güneydoğu TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/guneydogu-tv-tr-9e4e4c2bb3.svg) |
| Hunat TV | ![Logo Hunat TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/hunattv.png) |
| İçel TV | ![Logo İçel TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/iceltv.png) |
| Kardelen TV | ![Logo Kardelen TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/kardelen-tv-tr-96e6f44d3c.svg) |
| İzmir Time 35 TV | ![Logo İzmir Time 35 TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/izmirtime35tv.png) |
| K+ Kayseri | ![Logo K+ Kayseri ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/kkayseri.png) |
| Kanal 12 | ![Logo Kanal 12 ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/kanal12.png) |
| Kanal 15 | ![Logo Kanal 15 ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/kanal-15-tr-34ab83c63c.svg) |
| Kanal 19 | ![Logo Kanal 19 ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/kanal19.png) |
| Kanal 23 | ![Logo Kanal 23 ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/kanal-23-tr-2c993cfc8d.svg) |
| Kanal 26 Eskişehir | ![Logo Kanal 26 Eskişehir ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/kanal26eskisehir.png) |
| Kanal 3 | ![Logo Kanal 3 ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/kanal3-tr-5954d469cb.svg) |
| Kanal 32 | ![Logo Kanal 32 ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/kanal32.png) |
| Kanal 33 | ![Logo Kanal 33 ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/kanal-33-tr-1cb420e0fb.svg) |
| Kanal 34 | ![Logo Kanal 34 ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/kanal34.png) |
| Kanal 53 | ![Logo Kanal 53 ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/kanal53.png) |
| Kanal 58 | ![Logo Kanal 58 ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/kanal-58-tr-ff0d629d70.svg) |
| Kanal B | ![Logo Kanal B ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/kanal-b-tr-fc20656db8.svg) |
| Kanal Fırat | ![Logo Kanal Fırat ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/kanalfrat.png) |
| Kanal V | ![Logo Kanal V ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/kanal-v-tr-266a073b4c.svg) |
| Kay TV | ![Logo Kay TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/kaytv.png) |
| Kayhan TV | ![Logo Kayhan TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/kayhantv.png) |
| Kent Türk TV | ![Logo Kent Türk TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/kentturktv.png) |
| Kocaeli TV | ![Logo Kocaeli TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/kocaeli-tv-tr-701a7249cc.svg) |
| Konya KTV | ![Logo Konya KTV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/konyaktv.png) |
| Konya Olay TV | ![Logo Konya Olay TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/konyaolaytv.png) |
| Mekameleen TV | ![Logo Mekameleen TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/mekameleentv.png) |
| Mercan TV | ![Logo Mercan TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/mercan-tv-tr-657f4262fa.svg) |
| MTürk TV | ![Logo MTürk TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/mturktv.png) |
| Tempo TV | ![Logo Tempo TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/tempo-tv-tr-f7eb709e2b.svg) |
| Tivi 6 | ![Logo Tivi 6 ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/tivi6-tr-a26898c5d8.svg) |
| Ton TV | ![Logo Ton TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/tontv.png) |
| TV 1 | ![Logo TV 1 ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/tv1-tr-6e1cc90803.svg) |
| TV 264 | ![Logo TV 264 ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/tv264-tr-a197381feb.svg) |
| TV 41 | ![Logo TV 41 ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/tv41.png) |
| TV 52 | ![Logo TV 52 ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/tv52-tr-cfffa086e3.svg) |
| TV DEN | ![Logo TV DEN ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/tv-den-tr-a265989388.svg) |
| Vuslat TV | ![Logo Vuslat TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/vuslattv.png) |
| Natural TV | ![Logo Natural TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/naturaltv.png) |
| Sun RTV | ![Logo Sun RTV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/sunrtv.png) |
| TBMM TV | ![Logo TBMM TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/tbmm-tv-tr-9d1f406b88.svg) |
| Van 65 TV | ![Logo Van 65 TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/van65tv.png) |
| YOL TV | ![Logo YOL TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/yol-tv-tr-a747116203.svg) |
| Kanal Ada | ![Logo Kanal Ada](https://assets.tvcdn.net/5cbdd199-9ed1-4f2d-a106-a6d9c53227c4.png) |
| Kanal Urfa | ![Logo Kanal Urfa ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/kanal-urfa-tr-0831c8c3c9.svg) |
| Trabzon Buyuksehir Belediyesi TV | ![Logo Trabzon Buyuksehir Belediyesi TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/trabzonbuyuksehirbelediyesitv.png) |
| Urfanatik TV | ![Logo Urfanatik TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/urfanatiktv.png) |
| ETV Manisa | ![Logo ETV Manisa ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/etvmanisa.png) |
| MK TV | ![Logo MK TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/mktv.png) |

## RELIGIOSOS (15)

| Canal | Logo |
|---|---|
| Al Zahra TV Turkic | ![Logo Al Zahra TV Turkic ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/alzahratvturkic.png) |
| Diyanet TV | ![Logo Diyanet TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/diyanet-tv-tr-781c463071.svg) |
| Diyar TV | ![Logo Diyar TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/diyar-tv-tr-7522d5d784.svg) |
| Dost TV | ![Logo Dost TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/dost-tv-tr-19fe83f8ba.svg) |
| Lalegül TV | ![Logo Lalegül TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/lalegul-tv-tr-bf073564f5.svg) |
| Meltem TV | ![Logo Meltem TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/meltemtv.png) |
| MUKABELE TV | ![Logo MUKABELE TV ](https://assets.tvcdn.net/23b391ac-5edb-4e37-8664-27da64fb0785.png) |
| Rehber TV | ![Logo Rehber TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/rehber-tv-tr-13433fc4a3.svg) |
| Sat7 Türk | ![Logo Sat7 Türk ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/sat7-turk-tr-5046f8f42f.svg) |
| Semerkand TV | ![Logo Semerkand TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/semerkand-tv-tr-2709228c81.svg) |
| Sercem TV | ![Logo Sercem TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/sercemtv.png) |
| Vav TV | ![Logo Vav TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/vav-tv-tr-2a9fd4d80a.svg) |
| MADINAH TV | ![Logo MADINAH TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/madinahtv.png) |
| ABN TURKEY | ![Logo ABN TURKEY ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/abnturkey.png) |
| Makkah TV | ![Logo Makkah TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/makkahtv.png) |

## INTERNACIONAIS (13)

| Canal | Logo |
|---|---|
| Almahriah TV | ![Logo Almahriah TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/almahriahtv.png) |
| Elsharq TV | ![Logo Elsharq TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/elsharqtv.png) |
| Kanal Avrupa | ![Logo Kanal Avrupa ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/kanal-avrupa-tr-6994284255.svg) |
| Syria TV | ![Logo Syria TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/syriatv.png) |
| Balkan Türk | ![Logo Balkan Türk ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/balkanturk.png) |
| Thaqalayn TV | ![Logo Thaqalayn TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/thaqalayntv.png) |
| RTG International | ![Logo RTG International ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/rtginternational.png) |
| MC EU TV | ![Logo MC EU TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/mceutv.png) |
| Persiana Türkiye | ![Logo Persiana Türkiye ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/persianaturkiye.png) |
| INTV Australia | ![Logo INTV Australia ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/intvaustralia.png) |
| İSVİÇRE TV | ![Logo İSVİÇRE TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/isvicretv.png) |
| JÎN TV | ![Logo JÎN TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/jintv.png) |
| 4U Family (persa) | ![Logo 4U Family (persa) ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/4ufamilypersa.png) |

## INFANTIS (9)

| Canal | Logo |
|---|---|
| Cartoon Network Türkiye | ![Logo Cartoon Network Türkiye ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/cartoonnetworkturkiye.png) |
| Minika Çocuk | ![Logo Minika Çocuk ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/minika-cocuk-tr-3210746295.svg) |
| Minika GO | ![Logo Minika GO ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/minika-go-tr-f1ffe0aa8e.svg) |
| Spacetoon Türkiye | ![Logo Spacetoon Türkiye ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/spacetoonturkiye.png) |
| TRT Çocuk | ![Logo TRT Çocuk ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/trt-cocuk-tr-43225604c7.svg) |
| TRT Diyanet Çocuk | ![Logo TRT Diyanet Çocuk ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/trtdiyanetcocuk.png) |
| Zarok TV Kurmanji | ![Logo Zarok TV Kurmanji ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/zaroktvkurmanji.png) |
| Zarok TV Sorani | ![Logo Zarok TV Sorani ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/zaroktvsorani.png) |
| BabyFirst TV | ![Logo BabyFirst TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/babyfirsttv.png) |

## FILMES E SÉRIES (6)

| Canal | Logo |
|---|---|
| CİNE1 | ![Logo CİNE1 ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/cine1.png) |
| Grand Cinema | ![Logo Grand Cinema ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/grandcinema.png) |
| Tabii | ![Logo Tabii ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/tabii.png) |
| BBC First Türkiye | ![Logo BBC First Türkiye ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/bbcfirstturkiye.png) |
| Arzu Film | ![Logo Arzu Film ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/arzufilm.png) |
| Dizi TV | ![Logo Dizi TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/dizitv.png) |

## CULTURA/EDUCAÇÃO (4)

| Canal | Logo |
|---|---|
| Çiftçi TV | ![Logo Çiftçi TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/ciftci-tv-tr-ac1e5d4e6e.svg) |
| Luys TV | ![Logo Luys TV ](https://assets.tvcdn.net/e876bf88-411c-4a9c-ad29-e449e651f7ae.png) |
| TRT EBA Ortaokul | ![Logo TRT EBA Ortaokul ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/trtebaortaokul.png) |
| TV Karadeniz | ![Logo TV Karadeniz ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/tvkaradeniz.png) |

## MÚSICA (28)

| Canal | Logo |
|---|---|
| 1Mus | ![Logo 1Mus ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/1mus.png) |
| 30A Music | ![Logo 30A Music ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/gNWg9tl-950f250b00.svg) |
| Dream Türk | ![Logo Dream Türk ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/dream-turk-tr-e6563818a6.svg) |
| TMB TV | ![Logo TMB TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/tmb-tr-7d943cd91a.svg) |
| Med Müzik | ![Logo Med Müzik ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/gtUFmCD-16b5c1691d.svg) |
| Play TV | ![Logo Play TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/playtv.png) |
| NR1 Aşk | ![Logo NR1 Aşk ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/nr1-ask-tr-e4ccc540f4.svg) |
| NR1 Damar | ![Logo NR1 Damar ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/nr1-damar-tr-7db83aa170.svg) |
| NR1 Dance | ![Logo NR1 Dance ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/nr1-dance-tr-a671de54fb.svg) |
| Number 1 TV | ![Logo Number 1 TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/nr1-tr-4bdfbc1994.svg) |
| Power Dance TV | ![Logo Power Dance TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/logo_40-c210f3f043.svg) |
| Power Love TV | ![Logo Power Love TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/logo_2559-7d3e7ab543.svg) |
| PowerTürk Taptaze | ![Logo PowerTürk Taptaze ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/logo_2534-9630fe0103.svg) |
| TRT Müzik | ![Logo TRT Müzik ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/trt-muzik-tr-74b356c37f.svg) |
| Kral Pop | ![Logo Kral Pop ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/kral-pop-tr-f8a6e4ca20.svg) |
| NR1 Fashion One | ![Logo NR1 Fashion One ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/fashion-one-da3b8e871a.svg) |
| PowerTürk TV | ![Logo PowerTürk TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/powerturk-tr-d394635d8d.svg) |
| KN Music TV | ![Logo KN Music TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/LOGO2112-24686be8ce.svg) |
| Dost | ![Logo Dost ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/dost.png) |
| Company TV | ![Logo Company TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/companytv.png) |
| Güçlü TV | ![Logo Güçlü TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/guclutv.png) |
| Now 70 s | ![Logo Now 70 s ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/NOW-70s-7b89fcaeac.svg) |
| Now 80 s | ![Logo Now 80 s ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/NOW-80s-c66cb1d53d.svg) |
| NOW ROCK | ![Logo NOW ROCK ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/NOW-ROCK-730c1ac459.svg) |
| IQ Channel | ![Logo IQ Channel ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/iqchannel.png) |
| TopPop | ![Logo TopPop ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/toppop.png) |
| Retro Music Television | ![Logo Retro Music Television ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/retromusictelevision.png) |
| Power TV (720p) | ![Logo Power TV (720p) ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/power-tv-69f69ef8fe.svg) |

## ESTILO DE VIDA (3)

| Canal | Logo |
|---|---|
| Fashion One | ![Logo Fashion One ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/fashion-one-tv-tr-2a744d42ce.svg) |
| TV4 | ![Logo TV4 ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/tv4-tr-ea5eb885c8.svg) |
| MOR TV | ![Logo MOR TV ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/mortv.png) |

## TRT (6)

| Canal | Logo |
|---|---|
| TRT Arabi | ![Logo TRT Arabi ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/trt-arabi-tr-114c5303c8.svg) |
| TRT Avaz | ![Logo TRT Avaz ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/trt-avaz-tr-75ce0bdca3.svg) |
| TRT Genç | ![Logo TRT Genç ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/trtgenc.png) |
| TRT Kurdî | ![Logo TRT Kurdî ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/trt-kurdi-tr-617f440f3b.svg) |
| TRT Türk | ![Logo TRT Türk ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/trt-turk-tr-7ba89a0beb.svg) |
| TRT World | ![Logo TRT World ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-turcas-catalogo/svg/trt-world-tr-54ed154eef.svg) |

## DOCUMENTÁRIOS (2)

| Canal | Logo |
|---|---|
| TLC | ![Logo TLC ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/tlc.png) |
| Love Nature | ![Logo Love Nature ](https://raw.githubusercontent.com/woodyytalo/playlist.canais.turcos/github/workflows/atualizar-logos.yml/logos-ajustadas/lovenature.png) |

## Pendências

- **Kanal Ada** — a entrada atual de `Tv.m3u` continua sem atributo `tvg-logo`. A logo foi incluída na galeria a partir do endereço `https://assets.tvcdn.net/5cbdd199-9ed1-4f2d-a106-a6d9c53227c4.png`, associado ao canal Kanal Ada em uma playlist pública de referência que também identifica o fluxo `stream.tvcdn.net/yerel/kanal-ada.m3u8`. Fonte de conferência: https://github.com/erdodo/iptv/blob/main/tv.m3u8. A referência visual foi adicionada ao catálogo; a playlist principal não foi alterada.
