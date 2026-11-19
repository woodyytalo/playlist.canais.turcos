#!/usr/bin/env python3
"""Monitor de disponibilidade da TV principal; não modifica a playlist."""
import json, os, re, time, urllib.request, urllib.error
from pathlib import Path

def channels():
    out=[]; cur=None
    for raw in Path("Tv.m3u").read_text(encoding="utf-8",errors="replace").splitlines():
        s=raw.strip()
        if s.startswith("#EXTINF:"):
            cur={"name":s.rsplit(",",1)[-1].strip(),"category":(re.search(r'group-title="([^"]*)"',s) or [None,""])[1],"url":""}
        elif s and not s.startswith("#") and cur:
            cur["url"]=s; out.append(cur); cur=None
    return out

def test(url):
    req=urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0 TVPrincipalMonitor/1.0","Range":"bytes=0-4095"})
    start=time.time()
    try:
        with urllib.request.urlopen(req,timeout=5) as r:
            data=r.read(4096); ms=round((time.time()-start)*1000)
            hls=b"#EXTM3U" in data or "mpegurl" in r.headers.get("Content-Type","").lower()
            return {"status":"OK","http":r.status,"ms":ms,"tipo":"HLS" if hls else "HTTP","detalhe":"Resposta recebida"}
    except urllib.error.HTTPError as e:
        return {"status":"FALHA","http":e.code,"ms":round((time.time()-start)*1000),"tipo":"HTTP","detalhe":str(e.reason)}
    except Exception as e:
        return {"status":"FALHA","http":None,"ms":round((time.time()-start)*1000),"tipo":"rede","detalhe":str(e)[:180]}

def ai_review(rows):
    key=os.getenv("OPENAI_API_KEY")
    if not key: return "IA externa aguardando o segredo OPENAI_API_KEY. Diagnóstico técnico local executado."
    body={"model":"gpt-4.1-mini","temperature":0.2,"messages":[
      {"role":"system","content":"Analise testes de disponibilidade IPTV. Responda em português, classifique falhas e lentidão. Não invente links nem recomende substituir streams sem fonte verificada."},
      {"role":"user","content":json.dumps(rows,ensure_ascii=False)}
    ]}
    req=urllib.request.Request("https://api.openai.com/v1/chat/completions",data=json.dumps(body).encode(),headers={"Authorization":"Bearer "+key,"Content-Type":"application/json"})
    try:
        with urllib.request.urlopen(req,timeout=45) as r: return json.loads(r.read())["choices"][0]["message"]["content"].strip()
    except Exception as e: return "IA indisponível nesta execução: "+str(e)[:160]

def main():
    cs=channels()
    if not cs: raise SystemExit("Nenhum canal encontrado.")
    rows=[]
    for c in cs: rows.append({"canal":c["name"],"categoria":c["category"],"url":c["url"],"teste":test(c["url"])})
    good=sum(x["teste"]["status"]=="OK" for x in rows); bad=len(rows)-good
    slow=sum(x["teste"]["ms"]>=5000 for x in rows)
    review=ai_review(rows)
    Path("relatorios").mkdir(exist_ok=True)
    md=["# Monitor inteligente — TV principal","",f"- Canais testados: **{len(rows)}**",f"- Respostas válidas: **{good}**",f"- Falhas: **{bad}**",f"- Respostas lentas (≥5 s): **{slow}**","","## Análise da IA","",review,"","## Teste por canal","","| Canal | Categoria | Estado | HTTP | Latência | Tipo | Detalhe |","|---|---|---|---:|---:|---|---|"]
    for x in rows:
        t=x["teste"]; md.append(f'| {x["canal"].replace("|","/")} | {x["categoria"].replace("|","/")} | {t["status"]} | {t["http"] or "-"} | {t["ms"]} ms | {t["tipo"]} | {t["detalhe"].replace("|","/")} |')
    md += ["","## Limites e segurança","", "O bot testa respostas HTTP/HLS e registra diagnósticos. Não altera links, não remove canais e não toca em TV 2, Euro ou Backup. HTTP 200 não garante reprodução contínua no aplicativo."]
    Path("relatorios/monitor-tv-principal.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    Path("relatorios/monitor-tv-principal.json").write_text(json.dumps({"total":len(rows),"validos":good,"falhas":bad,"lentos":slow,"canais":rows},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(f"Monitor concluído: {len(rows)} canais; {good} válidos; {bad} falhas; {slow} lentos.")

if __name__=="__main__": main()
