#!/usr/bin/env python3
"""Extrai logos das outras playlists para os canais da Tv.m3u, preservando a ordem."""
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.parse import urlparse
import csv, io, re, unicodedata, time
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "logos-turcas-catalogo" / "LOGOS-EXTRAIDAS-DAS-PLAYLISTS"
PLAYLISTS = ["Backup.m3u", "Euro.m3u", "IPTV-Cat.m3u", "TV2.m3u", "Tvt.m3u"]
PRIORITY = {"IPTV-Cat.m3u": 0, "Backup.m3u": 1, "Tvt.m3u": 2, "Euro.m3u": 3, "TV2.m3u": 4}
ALIASES = {
    "360 TV": ["360"], "4U TV": ["4U"], "Bloomberg HT 2": ["Bloomberg HT"],
    "BRTV Karabük": ["BRTV"], "Cartoon Network Türkiye": ["Cartoon Network"],
    "ER TV Malatya": ["ERTV", "Er TV"], "Ezgi TV": ["Ezgi TV"],
    "FRT TV": ["FRT"], "GRT Gaziantep TV": ["GRT TV", "GRT Gaziantep"],
    "Kanal 26 Eskişehir": ["Kanal 26"], "Konya KTV": ["KTV"],
    "Mekameleen TV": ["Mekameleen"], "Power Dance TV": ["Power Dance"],
    "Power Love TV": ["Power Love"], "Spacetoon Türkiye": ["Spacetoon"],
    "TV Karadeniz": ["Karadeniz TV", "TV Karadeniz"],
    "Zarok TV Kurmanji": ["Zarok TV"], "Zarok TV Sorani": ["Zarok TV"],
    "Syria TV": ["Syria TV"], "Balkan Türk": ["Balkan Turk"],
    "RTG International": ["RTG"], "Arzu Film": ["Arzu Film"],
    "MC EU TV": ["MC EU"], "BabyFirst TV": ["BabyFirst", "Baby First"],
    "Company TV": ["Company TV"], "INTV Australia": ["INTV"],
    "IQ Channel": ["IQ Channel"], "MK TV": ["MK TV"],
    "Retro Music Television": ["Retro Music"],
}
def norm(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"\([^)]*\)|\[[^]]*\]", " ", s)
    s = re.sub(r"\b(1080p|720p|576p|480p|360p|hd|fhd|uhd|sd|hevc|4k)\b", " ", s)
    return re.sub(r"[^a-z0-9]", "", s)

def parse(path):
    entries=[]
    lines=path.read_text(encoding="utf-8-sig", errors="replace").splitlines()
    for line in lines:
        if not line.startswith("#EXTINF"):
            continue
        name=line.rsplit(",",1)[-1].strip()
        match=re.search(r'tvg-logo\s*=\s*"([^"]+)"', line, re.I)
        logo=match.group(1).strip() if match else ""
        if logo.startswith(("http://","https://")):
            entries.append((name,logo,path.name))
    return entries

def safe_name(s):
    s=unicodedata.normalize("NFKD",s).encode("ascii","ignore").decode()
    s=re.sub(r"[^A-Za-z0-9]+","-",s).strip("-")
    return s[:70] or "canal"

def fetch_image(url):
    req=Request(url,headers={"User-Agent":"Mozilla/5.0 (compatible; PlaylistLogoCollector/1.0)"})
    with urlopen(req,timeout=25) as r:
        data=r.read(12*1024*1024)
        ctype=r.headers.get("Content-Type","").lower()
    if "svg" in ctype or data.lstrip().startswith(b"<svg") or b"<svg" in data[:1000]:
        try:
            import cairosvg
            data=cairosvg.svg2png(bytestring=data,output_width=1024,output_height=1024)
        except Exception as e:
            raise ValueError("SVG conversion failed: "+str(e))
    im=Image.open(io.BytesIO(data)).convert("RGBA")
    # Trim only genuinely transparent margins; do not erase colored/black logo backgrounds.
    alpha=im.getchannel("A")
    bbox=alpha.getbbox()
    if bbox:
        im=im.crop(bbox)
    im.thumbnail((460,460),Image.Resampling.LANCZOS)
    canvas=Image.new("RGBA",(512,512),(0,0,0,0))
    canvas.alpha_composite(im,((512-im.width)//2,(512-im.height)//2))
    out=io.BytesIO()
    canvas.save(out,format="PNG",optimize=True)
    return out.getvalue()

def main():
    main_file=ROOT/"Tv.m3u"
    if not main_file.exists():
        raise SystemExit("Tv.m3u não encontrada")
    channels=[(line.rsplit(",",1)[-1].strip()) for line in main_file.read_text(encoding="utf-8-sig",errors="replace").splitlines() if line.startswith("#EXTINF")]
    entries=[]
    for filename in PLAYLISTS:
        p=ROOT/filename
        if p.exists():
            entries.extend(parse(p))
    by_name={}
    for name,url,source in entries:
        by_name.setdefault(norm(name),[]).append((url,source,name))
    OUT.mkdir(parents=True,exist_ok=True)
    for p in OUT.glob("*.png"): p.unlink()
    rows=[]
    downloaded=0
    for index,channel in enumerate(channels,1):
        keys=[norm(channel)]+[norm(x) for x in ALIASES.get(channel,[])]
        candidates=[]
        seen=set()
        for key in keys:
            for item in by_name.get(key,[]):
                if item[0] not in seen:
                    candidates.append(item); seen.add(item[0])
        candidates.sort(key=lambda x:(PRIORITY.get(x[1],99), x[1], x[2]))
        status="SEM LOGO CORRESPONDENTE"
        used_url=source=matched_name=""
        for url,src,srcname in candidates:
            try:
                content=fetch_image(url)
                filename=f"{index:03d}-{safe_name(channel)}.png"
                (OUT/filename).write_bytes(content)
                status="OK"
                used_url,source,matched_name=url,src,srcname
                downloaded+=1
                break
            except Exception as exc:
                print(f"Falha {channel} [{srcname}] {url}: {exc}")
                time.sleep(.15)
        rows.append([f"{index:03d}",channel,status,source,matched_name,used_url])
    with (OUT/"INDICE.csv").open("w",newline="",encoding="utf-8-sig") as f:
        w=csv.writer(f); w.writerow(["ordem","canal_Tv.m3u","status","lista_origem","nome_encontrado","url_logo"]); w.writerows(rows)
    missing=[r[1] for r in rows if r[2]!="OK"]
    (OUT/"LEIA-ME.txt").write_text(
        f"Logos extraídas das outras listas M3U para os canais de Tv.m3u.\\n"
        f"Ordem original preservada. PNG 512x512, com margens transparentes quando disponíveis.\\n"
        f"Logos baixadas: {downloaded}/{len(channels)}.\\n"
        f"Não foi removido fundo opaco para evitar danificar a arte original.\\n"
        f"Canais sem logo correspondente ou cujo download/conversão falhou: {len(missing)}.\\n"
        + "\\n".join(missing) + "\\n",encoding="utf-8")
    print(f"Resultado: {downloaded}/{len(channels)} logos; {len(missing)} pendentes.")
if __name__=="__main__": main()
