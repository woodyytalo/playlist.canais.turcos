#!/usr/bin/env python3
"""Testa alternativas do Backup para os canais com falha na última auditoria.
Não modifica Tv.m3u. Só recomenda URL de backup após resposta HTTP positiva.
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from urllib.parse import urldefrag
import re, time
from datetime import datetime, timezone

TARGETS = [
"24 TV","A Haber","A Para","A Spor","A2","Altas TV","Anadolu TV","Bir TV","CİNE1","CNN Türk","DHA","Ekotürk","ETV Manisa","Güneydoğu TV","İçel TV","Kanal 32","Kanal 33","Kanal Urfa","Kardelen TV","MTürk TV","Natural TV","NOW","Power Dance TV","Sözcü TV","TELE1","TRT 2","TV 1","TV 52","TV100","TV 4","TVNET","TürkHaber","Çay TV","Ülke TV"
]
BLOCKED = ("vavoo.to","europlayiptv.de","185.234.111.229","youtube.com/embed","ythls.kekikakademi.org")
def norm(s):
    s=s.casefold()
    s=s.replace("ı","i").replace("İ","i")
    return re.sub(r"[^a-z0-9]", "", s)
def parse(path):
    raw=Path(path).read_text(encoding="utf-8-sig").splitlines()
    rows=[]; meta=None
    for line in raw:
        line=line.strip()
        if line.startswith("#EXTINF:"): meta=line
        elif line and not line.startswith("#") and meta:
            title=meta.rsplit(",",1)[-1].strip()
            title=re.sub(r"^\d+\s*-\s*","",title)
            rows.append((title,line,meta)); meta=None
    return rows
def probe(item):
    name,url=item; url=urldefrag(url)[0]
    for attempt in range(2):
        try:
            req=Request(url,headers={"User-Agent":"Mozilla/5.0 IPTV-health-check","Range":"bytes=0-65535","Accept":"*/*"})
            with urlopen(req,timeout=14) as r:
                data=r.read(65536)
                if r.status < 400 and data:
                    return name,url,"OK",f"HTTP {r.status}; {len(data)} bytes"
                return name,url,"FALHA",f"HTTP {r.status}; resposta vazia"
        except HTTPError as e:
            detail=f"HTTP {e.code}"
            if e.code in (401,403,404,410): return name,url,"FALHA",detail
        except (URLError,TimeoutError,OSError) as e:
            detail=f"{type(e).__name__}: {str(e)[:120]}"
        if attempt==0: time.sleep(.5)
    return name,url,"FALHA",detail

backup=parse("Backup.m3u")
current=parse("Tv.m3u")
current_urls={norm(n):urldefrag(u)[0] for n,u,_ in current}
tasks=[]; no_candidate=[]
for name in TARGETS:
    key=norm(name)
    candidates=[]
    for title,url,meta in backup:
        if norm(title)!=key: continue
        low=url.lower()
        if any(d in low for d in BLOCKED): continue
        url=urldefrag(url)[0]
        if url==current_urls.get(key): continue
        if url not in [x[1] for x in candidates]: candidates.append((title,url,meta))
    if not candidates:
        no_candidate.append(name)
    for _,url,_ in candidates[:5]: tasks.append((name,url))

results=[]
with ThreadPoolExecutor(max_workers=8) as pool:
    futures=[pool.submit(probe,x) for x in tasks]
    for f in as_completed(futures): results.append(f.result())
results.sort(key=lambda x:(norm(x[0]), x[2]!="OK",x[1]))
success={}
for name,url,status,detail in results:
    if status=="OK" and name not in success: success[name]=(url,detail)
out=Path("reports/anti-crash/alternativas-backup.txt")
out.parent.mkdir(parents=True,exist_ok=True)
with out.open("w",encoding="utf-8") as f:
    f.write(f"Teste de alternativas do Backup | {datetime.now(timezone.utc).isoformat()}\n")
    f.write(f"Alvos: {len(TARGETS)} | URLs alternativas testadas: {len(results)} | canais com ao menos uma alternativa HTTP OK: {len(success)}\n")
    f.write("A resposta HTTP não comprova reprodução contínua; revisar no player antes de considerar resolvido. Tv.m3u não foi alterada.\n\n")
    for name in TARGETS:
        f.write(f"\n[{name}]\n")
        if name in success: f.write(f"RECOMENDADA: {success[name][0]} | {success[name][1]}\n")
        elif name in no_candidate: f.write("SEM ALTERNATIVA COMPATÍVEL NO BACKUP (fontes bloqueadas/duplicadas/ausentes).\n")
        else: f.write("Nenhuma alternativa respondeu HTTP com sucesso.\n")
        for n,url,status,detail in results:
            if n==name: f.write(f"{status} | {url} | {detail}\n")
print(f"Alternativas testadas: {len(results)} | canais com alternativa HTTP OK: {len(success)} | sem candidato no backup: {len(no_candidate)}")
