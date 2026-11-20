#!/usr/bin/env python3
import json, re, urllib.request
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SOURCE="https://tr.canlitv.watch/frekans-bilgileri"
INPUT=ROOT/"dados-satelite"/"ANOTACAO-CANAIS-FREQUENCIAS.md"
OUT=ROOT/"relatorios-satelite"
EXPECTED=211
ROW=re.compile(r"^\|\s*(\d+)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*$")
UNKNOWN={"","—","-","a verificar","n/a","na"}
def clean(s): return s.strip().strip()
def unknown(s): return clean(s).casefold() in UNKNOWN
def main():
    if not INPUT.exists(): raise SystemExit("Arquivo de frequencias nao encontrado")
    entries=[]
    for line in INPUT.read_text(encoding="utf-8").splitlines():
        m=ROW.match(line)
        if not m: continue
        n,name,cat,sat,freq,pol,sr,fec=map(clean,m.groups())
        if n.isdigit() and name:
            entries.append({"number":int(n),"channel":name,"category":cat,"satellite":sat,"frequency_mhz":freq,"polarization":pol,"symbol_rate_ksps":sr,"fec":fec})
    unique={(x["number"],x["channel"]):x for x in entries}
    pending=sorted([x for x in unique.values() if unknown(x["satellite"])],key=lambda x:x["number"])
    sats=Counter(x["satellite"] for x in entries if not unknown(x["satellite"]))
    grouped=defaultdict(list)
    for x in entries: grouped[(x["number"],x["channel"])].append(x)
    multiple=[{"number":k[0],"channel":k[1],"transponders":len(v)} for k,v in grouped.items() if len(v)>1]
    invalid=[]
    for x in entries:
        if unknown(x["satellite"]): continue
        checks=[("frequency_mhz",x["frequency_mhz"].isdigit()),("polarization",x["polarization"].upper() in {"H","V"}),("symbol_rate_ksps",x["symbol_rate_ksps"].isdigit()),("fec",not unknown(x["fec"]))]
        for field,ok in checks:
            if not ok: invalid.append({"channel":x["channel"],"field":field,"value":x[field]})
    req=urllib.request.Request(SOURCE,headers={"User-Agent":"satellite-data-audit/1.0"})
    try:
        with urllib.request.urlopen(req,timeout=15) as r: source={"ok":200<=r.status<400,"http_status":r.status}
    except Exception as e: source={"ok":False,"error":type(e).__name__+": "+str(e)}
    now=datetime.now(timezone.utc).isoformat(timespec="seconds")
    data={"generated_at_utc":now,"source_url":SOURCE,"source_check":source,"summary":{"table_rows":len(entries),"unique_channels":len(unique),"expected_channels":EXPECTED,"pending_verification":len(pending),"channels_with_multiple_transponders":len(multiple),"satellites":dict(sorted(sats.items())),"invalid_confirmed_entries":len(invalid)},"pending_channels":pending,"multiple_transponders":multiple,"invalid_entries":invalid}
    OUT.mkdir(parents=True,exist_ok=True)
    (OUT/"monitoramento-satelite.json").write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    lines=["# Auditoria de frequencias via satelite","",f"- Gerado em UTC: {now}","- Arquivo: dados-satelite/ANOTACAO-CANAIS-FREQUENCIAS.md","- Fonte: "+SOURCE,"- Resposta HTTP da fonte: "+("OK" if source["ok"] else "falha/indisponivel"),"","## Resumo","",f"- Linhas de transponder: **{len(entries)}**",f"- Canais unicos: **{len(unique)}** (esperado: {EXPECTED})",f"- Canais A verificar: **{len(pending)}**",f"- Canais com multiplos transponders: **{len(multiple)}**",f"- Entradas confirmadas com campos invalidos: **{len(invalid)}**","","## Distribuicao por satelite","","| Satelite | Linhas |","|---|---:|"]
    lines += [f"| {k} | {v} |" for k,v in sorted(sats.items())]
    lines += ["","## Canais pendentes","","| Nº | Canal | Categoria |","|---:|---|---|"]
    lines += [f"| {x['number']} | {x['channel']} | {x['category']} |" for x in pending]
    lines += ["","## Limites da auditoria","- Audita a estrutura dos dados e a disponibilidade HTTP da pagina-fonte.","- Nao confirma recepcao de sinal, cobertura, apontamento de antena ou transmissao no ar.","- Nao altera Tv.m3u nem os parametros anotados.",""]
    (OUT/"monitoramento-satelite.md").write_text("\n".join(lines),encoding="utf-8")
    print(json.dumps(data["summary"],ensure_ascii=False))
    return 0 if len(unique)==EXPECTED else 1
if __name__=="__main__": raise SystemExit(main())
