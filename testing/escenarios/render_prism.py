#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render genérico de Escenarios PRISM v1.0 (YAML canonico v1.0 estricto -> HTML dinamico).
Uso:
    python render_prism.py <NOMBRE_SIN_EXT> [directorio_assets]
Ej:
    python render_prism.py PRISM-2026-010-neurodatos-soberania-digital
Genera <NOMBRE>.html en el mismo directorio del YAML.
"""
import sys
import yaml, html, re, pathlib, urllib.parse

ROOT = pathlib.Path(__file__).resolve().parent
if len(sys.argv) < 2:
    print("Uso: python render_prism.py <NOMBRE_YAML_SIN_EXT> [carpeta_assets]")
    sys.exit(1)
BASE = sys.argv[1]
YAML_PATH = ROOT / f"{BASE}.yaml"
OUT = ROOT / f"{BASE}.html"
ASSETS = sys.argv[2] if len(sys.argv) > 2 else "assets"

# ---- Glosario (siglas paises + instituciones) — cargado al inicio para usar en todo el render ----
GLOSSARY = ROOT.parent.parent / "metodologia" / "glosario.md"
GLOS = {}; FLAGS = {}
if GLOSSARY.exists():
    txt = GLOSSARY.read_text(encoding="utf-8")
    mode = None
    for line in txt.splitlines():
        if line.startswith("## Países"): mode="country"; continue
        if line.startswith("## Instituciones"): mode="inst"; continue
        if line.startswith("## Uso"): mode=None; continue
        if mode and line.strip() and (":" in line):
            code, d = line.split(":",1)
            code=code.strip(); d=d.strip()
            if mode=="country":
                # d = "India 🇮🇳" -> separar nombre y emoji
                parts = d.split()
                emoji = parts[-1] if parts and len(parts[-1]) <= 4 else ""
                name = " ".join(parts[:-1]) if emoji else d
                FLAGS[code]=(emoji, name)
            elif mode=="inst": GLOS[code]=d
def gloss(text):
    """Resalta siglas: paises con bandera+codigo (nombre solo en tooltip), instituciones con popover.
    Limpia duplicados: si el texto ya trae 'India 🇮🇳 IN', lo deja como '🇮🇳 IN'."""
    if not text: return ""
    t=str(text)
    # Paises: consumir (nombre opcional)(emoji opcional)CODIGO
    for code,(emoji,name) in sorted(FLAGS.items(), key=lambda x:-len(x[0])):
        pat = rf'(?:[A-Za-zÀ-ÿ\.\s]+?)?\s*(?:[\U0001F1E6-\U0001F1FF]{2})?\s*{re.escape(code)}\b'
        t = re.sub(pat,
                   lambda m: f'<span class="flag" title="{esc(name)}">{esc(emoji)} {esc(code)}</span>',
                   t, flags=re.UNICODE)
    for code,d in sorted(GLOS.items(), key=lambda x:-len(x[0])):
        if re.search(rf'(?<![A-Za-z]){re.escape(code)}(?![A-Za-z])', t):
            t=t.replace(code, f'<span class="acr" tabindex="0">{esc(code)}<span class="acr-pop">{esc(d)}</span></span>')
    return t

def esc(s):
    return html.escape(str(s)) if s is not None else ""
def num(v):
    try: return float(v)
    except: return 0.0

doc = yaml.safe_load(YAML_PATH.read_text(encoding="utf-8"))
e = doc["escenario"]; m = doc.get("metadatos", {})
ref = doc.get("referencias", []); chg = doc.get("cambios", [])

# ---- Citas: clasificar por TIPO (paper/company/lab/search/news/law) con color + icono ----
# Categorias de fuente (Opción B): badge con icono + color, popover en hover.
CITES_ASSETS = "assets/cites"

# Mapa de dominios/keywords -> (tipo, icono, color, etiqueta)
SOURCE_TYPES = {
    "paper":   ("cite-paper.png",   "#4aa3ff", "Paper revisado por pares"),
    "company": ("cite-company.png", "#36d399", "Web de empresa"),
    "lab":     ("cite-lab.png",     "#a78bfa", "Laboratorio / institución"),
    "law":     ("cite-law.png",     "#2dd4bf", "Ley / legislación"),
    "news":    ("cite-news.png",    "#ff5230", "Artículo / noticia"),
    "search":  ("cite-search.png",  "#9aa0aa", "Búsqueda (verificación)"),
}

# Detección por palabras clave
PAPER_KW   = ["nature","science","cell","arxiv","doi.org","wiley","springer",".pdf",
              "encephalography","neural decoding","brain-computer","ieee","plos","frontiers"]
COMPANY_KW = {"neuralink":"neuralink.com","synchron":"synchron.com","precision":"precisionneuro.io",
              "risc zero":"risczero.com","meta":"ai.meta.com","apple":"apple.com","zama":"zama.ai",
              "fda":"fda.gov","openai":"openai.com","google":"blog.google"}
LAW_KW     = ["ley","law","chile","españa","espana","colorado","eu ","unión europea","union europea",
              "ai act","ai act","gdpr","constitución","constitucion","decreto","código","codigo","estatuto"]
LAB_KW     = ["mit","stanford","harvard","max planck","yale","university","universidad","instituto",
              "national","laboratorio","lab ","center","centro","nsf","nih","conicet","csic"]

def detect_type(referencia, namehint=""):
    s = (str(referencia) + " " + str(namehint)).lower()
    for k in PAPER_KW:
        if k in s: return "paper"
    for k, dom in COMPANY_KW.items():
        if k in s: return "company"
    for k in LAW_KW:
        if k in s: return "law"
    for k in LAB_KW:
        if k in s: return "lab"
    if any(x in s for x in ["news","articulo","artículo","noticia","reuters","bbc","the verge","wired","mit tech"]):
        return "news"
    return "search"

def cite_url(referencia, namehint=""):
    """Devuelve URL real de la fuente."""
    s = str(referencia or "").lower()
    for r in ref:
        auth = r.get("autores","") or ""
        sur = (auth.replace(","," ").split() or [""])[0]
        if len(sur) > 3 and sur.lower() in s and r.get("doi_url"):
            return r["doi_url"]
    for k,v in COMPANY_KW.items():
        if k in s or k in (namehint or "").lower():
            return "https://"+v if not v.startswith("http") else v
    q = urllib.parse.quote((str(referencia) or namehint)[:80])
    return f"https://www.google.com/search?q={q}"

def cite(referencia, namehint=""):
    """Marca de cita con popover clasificado por tipo (Opción B). El doble control
    de validez de URL se hace en un paso separado (report_url_check) para no
    acoplar el render a la red."""
    tipo = detect_type(referencia, namehint)
    icon, color, label = SOURCE_TYPES[tipo]
    url = cite_url(referencia, namehint)
    domain = url.split("//")[-1].split("/")[0]
    title = str(referencia) or str(namehint)
    return (f'<span class="cite-wrap" tabindex="0">'
            f'<a class="cite-badge" style="--c:{color}" href="{esc(url)}" target="_blank" rel="noopener"><img src="{CITES_ASSETS}/{icon}" alt="{esc(tipo)}">Fuente ↗</a>'
            f'<span class="cite-pop" style="--c:{color}">'
            f'<img class="cite-pop-icon" src="{CITES_ASSETS}/{icon}" alt="">'
            f'<b class="cite-pop-type">{esc(label)}</b>'
            f'<span class="cite-pop-title">{esc(title[:90])}</span>'
            f'<span class="cite-pop-domain">{esc(domain)}</span>'
            f'<span class="cite-pop-hint">Clic para abrir la fuente ↗</span>'
            f'</span></span>')

POP = [
    ("Matrix (1999)", "Jacking-in neural a una realidad simulada via puerto en la nuca.", "Entrada neural directa a un mundo sintetico.", "pop-jacking.png", "https://es.wikipedia.org/wiki/The_Matrix"),
    ("Inception (2010)", "Invasion de capas de sueno compartidas y arquitectura imposible.", "Sonar dentro de un sueno; el cerebro como terreno editable.", "pop-dreams.png", "https://es.wikipedia.org/wiki/Inception"),
    ("Black Mirror: Crocodile (2017)", "Extraccion de memoria visual grabada por dispositivo neural.", "El recuerdo como evidencia extraible y auditable.", "pop-memory-extract.png", "https://es.wikipedia.org/wiki/Black_Mirror"),
    ("Altered Carbon (2018)", "Stack cortical que almacena la conciencia como datos.", "La identidad como archivo transferible.", "pop-cortical-stack.png", "https://es.wikipedia.org/wiki/Altered_Carbon"),
    ("Eternal Sunshine (2004)", "Borrado quirurgico de memorias especificas.", "La voluntad sobre el contenido mental.", "pop-memory-erase.png", "https://es.wikipedia.org/wiki/Eternal_Sunshine_of_the_Spotless_Mind"),
    ("Ghost in the Shell (1995)", "Cibercerebro hackeable y capas mentales aumentadas.", "La frontera mente-codigo y su ataque.", "pop-cyberbrain.png", "https://es.wikipedia.org/wiki/Ghost_in_the_Shell"),
]

# ---- Plausibilidad ----
pl = e.get("plausibilidad", {}); pt = num(pl.get("puntuacion_total",0))
dims = pl.get("dimensiones", {})
dim_rows = "".join(f'<div class="dim"><span>{esc(k.replace("_"," ").title())}</span><div class="bar"><i style="width:{num(v)}%"></i></div><b>{num(v):.0f}</b></div>' for k,v in dims.items())
pl_metodologia = esc(pl.get("metodologia_calculo","")).replace(chr(10)," ")
IMG = e.get("imagenes", {}) or {}

# ---- Impactos ----
imp = e.get("impactos", {})
imp_order = ["economico","politico","ambiental","social","filosofico","sobre_la_conciencia"]
imp_fig = f'<figure class="fig reveal"><img loading="lazy" src="{ASSETS}/{esc(IMG["impacto"])}" alt="{esc(e.get("titulo","")[0:32])}"><figcaption>{esc(e.get("titulo",""))}</figcaption></figure>' if IMG.get("impacto") else ""
narr_fig = f'<figure class="narr-fig reveal"><img loading="lazy" src="{ASSETS}/{esc(IMG["narrativa"])}" alt="{esc(e.get("titulo","")[0:32])}"><figcaption>{esc(e.get("titulo",""))}</figcaption></figure>' if IMG.get("narrativa") else ""
imp_html = ""
for k in imp_order:
    v = imp.get(k)
    if not v: continue
    mag = esc(v.get("magnitud","")); desc = gloss(v.get("descripcion","")); extra=""
    if k=="filosofico" and v.get("preguntas_que_abre"):
        extra="<ul>"+"".join(f"<li>{esc(p)}</li>" for p in v["preguntas_que_abre"])+"</ul>"
    if k=="sobre_la_conciencia" and v.get("implicaciones"):
        extra="<ul>"+"".join(f"<li>{esc(p)}</li>" for p in v["implicaciones"])+"</ul>"
    if v.get("sectores_afectados"):
        extra+='<div class="tags">'+"".join(f"<span>{esc(s)}</span>" for s in v["sectores_afectados"])+"</div>"
    fig = imp_fig if k=="economico" else ""
    imp_html+=f'<div class="impact-card reveal"><div class="imp-head"><h4>{esc(k.replace("_"," ").title())}</h4><span class="mag mag-{esc(mag)}">{esc(mag)}</span></div><p>{desc}</p>{extra}</div>{fig}'

# ---- Riesgos / Oportunidades / Señales / Actores / Lineas ----
risk_html="".join(f'<div class="risk reveal"><div class="risk-top"><b>{esc(r.get("riesgo",""))}</b><span class="pill pill-{esc(r.get("categoria",""))}">{esc(r.get("categoria",""))}</span></div><div class="risk-meta">Prob: <b>{esc(r.get("probabilidad",""))}</b> · Impacto: <b>{esc(r.get("impacto",""))}</b> · Mitigabilidad: <b>{esc(r.get("mitigabilidad",""))}</b></div><p>{esc("; ".join(r.get("mitigaciones_posibles",[])))}</p></div>' for r in e.get("riesgos",[]))
opp_html="".join(f'<div class="opp reveal"><b>{esc(o.get("oportunidad",""))}</b><span class="mag mag-{esc(o.get("magnitud",""))}">{esc(o.get("magnitud",""))}</span><p>Ventana: {esc(o.get("ventana_temporal",""))}</p><div class="tags">{"".join(f"<span>{esc(a)}</span>" for a in o.get("actores_que_pueden_capturarla",[]))}</div></div>' for o in e.get("oportunidades",[]))
sig_html="".join(f'<div class="sig reveal"><div class="sig-id">{esc(s.get("id",""))}</div><div class="sig-body"><p class="sig-t">{esc(s.get("senal",""))}</p><div class="sig-meta">Umbral: {esc(s.get("umbral_de_activacion",""))} · Estado: <b class="st-{esc(s.get("estado_actual",""))}">{esc(s.get("estado_actual",""))}</b> · Relevancia: {num(s.get("relevancia_para_escenario",0)):.0f}</div></div></div>' for s in e.get("senales_tempranas",[]))
act_html="".join(f'<div class="actor reveal"><b>{esc(a.get("nombre",""))}</b><span class="pill pill-{esc(a.get("tipo",""))}">{esc(a.get("tipo",""))}</span><p>{esc(" · ".join(a.get("rol_en_escenario",[])))}</p><div class="sig-meta">Posicion: <b>{esc(a.get("posicion",""))}</b> · Influencia: {num(a.get("capacidad_de_influencia",0)):.0f}/100</div></div>' for a in e.get("actores",[]))
lin_html="".join(f'<div class="line reveal"><p><b>{esc(l.get("pregunta",""))}</b></p><p class="muted">Metodo: {esc(l.get("metodologia_sugerida",""))} · Urgencia: <b>{esc(l.get("urgencia",""))}</b></p></div>' for l in e.get("lineas_investigacion",[]))

# ---- Interdependencias ----
import urllib.request
def url_ok(url, timeout=8):
    try:
        req=urllib.request.Request(url, method="HEAD", headers={"User-Agent":"Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status < 400
    except Exception:
        try:
            with urllib.request.urlopen(url, timeout=timeout) as r:
                return r.status < 400
        except Exception:
            return False

# ---- Interdependencias con popover ----
inter=e.get("interdependencias",{})
REL_LABELS={"convergencia":"Convergencia","catalizador":"Catalizador","precedente":"Precedente",
            "compatible":"Compatible","emergente":"Emergente"}
def rel_pop(x):
    rid=esc(x.get("id","")); tipo=esc(x.get("tipo_relacion",""))
    lab=REL_LABELS.get(tipo.lower(),tipo)
    return (f'<span class="dep dep-rel" tabindex="0">{esc(rid).replace("FUTURIA-2026-","#")} · {lab}'
            f'<span class="dep-pop"><b>{esc(rid)}</b><br>Relación: <b>{lab}</b><br>'
            f'<span class="muted">Escenario del universo PRISM. Al crearlo, completar título y motivo de vinculación.</span></span></span>')
def inc_pop(x):
    rid=esc(x.get("id","")); razon=esc(x.get("razon_incompatibilidad",""))
    return (f'<span class="dep dep-inc" tabindex="0">{esc(rid).replace("FUTURIA-2026-","#")} · {razon[:40]}…'
            f'<span class="dep-pop"><b>{esc(rid)}</b><br><span class="muted">{razon}</span></span></span>')
rel_html="".join(rel_pop(x) for x in inter.get("escenarios_relacionados",[]))
inc_html="".join(inc_pop(x) for x in inter.get("escenarios_incompatibles",[]))

# ---- Fundamentos (con cite-link) ----
f=e.get("fundamentos",{})
fund_html=""
fund_fig=f'<figure class="fig reveal"><img loading="lazy" src="{ASSETS}/{esc(IMG["fundamentos"])}" alt="{esc(e.get("titulo","")[0:32])}"><figcaption>{esc(e.get("titulo",""))}</figcaption></figure>' if IMG.get("fundamentos") else ""
for sec,label in [("cientificos","Cientificos"),("tecnologicos","Tecnologicos"),("sociales","Sociales"),("economicos","Economicos")]:
    items=f.get(sec,[])
    if not items: continue
    rows=""
    for it in items:
        if sec=="cientificos":
            c=cite(it.get("referencia",""),it.get("campo",""))
            rows+=f'<div class="fund"><b>{esc(it.get("campo",""))}</b><p>{gloss(it.get("hallazgo_relevante",""))}</p>{c} <span class="muted">{esc(it.get("referencia",""))} · {esc(it.get("ano",""))}</span></div>'
        elif sec=="tecnologicos":
            c=cite(it.get("referencia",""),it.get("nombre",""))
            rows+=f'<div class="fund"><b>{esc(it.get("nombre",""))}</b><span class="pill pill-{esc(it.get("estado",""))}">{esc(it.get("estado",""))}</span><p>TRL {num(it.get("madurez_tecnologica",0)):.0f} · {gloss(it.get("referencia",""))}</p>{c}</div>'
        elif sec=="sociales":
            c=cite(it.get("fuente",""),it.get("tendencia",""))
            rows+=f'<div class="fund"><b>{esc(it.get("tendencia",""))}</b><span class="pill pill-{esc(it.get("direccion",""))}">{esc(it.get("direccion",""))}</span><p>{gloss(it.get("evidencia",""))}</p>{c}</div>'
        else:
            c=cite(it.get("fuente",""),it.get("indicador",""))
            rows+=f'<div class="fund"><b>{esc(it.get("indicador",""))}</b><p>{gloss(it.get("valor_actual",""))} → {gloss(it.get("tendencia",""))}</p>{c}</div>'
    secfig=fund_fig if sec=="tecnologicos" else ""
    fund_html+=f'<div class="fund-sec reveal"><h3>{label}</h3>{rows}{secfig}</div>'

# ---- Tecnologias ----
tech=e.get("tecnologias",{}); tech_html=""
for sec,label in [("existentes","Existentes (TRL 7-9)"),("en_desarrollo","En desarrollo (TRL 4-6)"),("teoricas","Teoricas / Ruptura (TRL 1-3)")]:
    items=tech.get(sec,[])
    if not items: continue
    rows=""
    for it in items:
        if sec=="existentes":
            rows+=f'<div class="tech"><b>{esc(it.get("nombre",""))}</b><div class="bar sm"><i style="width:{num(it.get("madurez",0))}%"></i></div><span class="muted">{esc(", ".join(it.get("proveedores_principales",[])))}</span></div>'
        elif sec=="en_desarrollo":
            rows+=f'<div class="tech"><b>{esc(it.get("nombre",""))}</b><span class="pill pill-en_desarrollo">~{esc(it.get("madurez_estimada_para",""))}</span><p class="muted">{esc(", ".join(it.get("actores_clave",[])))}</p></div>'
        else:
            rows+=f'<div class="tech"><b>{esc(it.get("nombre",""))}</b><p>{esc("; ".join(it.get("barreras_cientificas",[])))}</p><span class="muted">Demo: {esc(it.get("tiempo_estimado_hasta_primer_demo",""))}</span></div>'
    tech_html+=f'<div class="fund-sec reveal"><h3>{label}</h3>{rows}</div>'

# ---- Referencias / Metadatos ----
def ref_line(r):
    extra = ""
    if r.get("doi_url"):
        u = esc(r.get("doi_url",""))
        extra = f' · <a href="{u}" target="_blank" rel="noopener">{u}</a>'
    hint = " ".join([r.get("autores",""), r.get("titulo",""), r.get("fuente",""), r.get("doi_url","")])
    badge = cite(hint, r.get("autores",""))
    return f'<div class="ref reveal"><span class="ref-type">{esc(r.get("tipo",""))}</span> {esc(r.get("autores",""))} ({esc(r.get("ano",""))}). <i>{esc(r.get("titulo",""))}</i>. {esc(r.get("fuente",""))}{extra} {badge}</div>'
ref_html = "".join(ref_line(r) for r in ref)
auth=", ".join(f'{a.get("nombre","")} ({a.get("rol",[""])[0] if a.get("rol") else ""})' for a in m.get("autores",[]))
chg_html="".join(f'<div class="ref">v{esc(c.get("version",""))} · {esc(c.get("fecha",""))} · {esc(c.get("cambios",""))} <span class="muted">— {esc(c.get("autor",""))}</span></div>' for c in chg)
pop_html="".join(f'<div class="pop reveal"><img loading="lazy" src="{ASSETS}/{esc(img)}" alt="{esc(title)}"><div class="pop-body"><h4>{esc(title)}</h4><p>{esc(desc)}</p><p class="muted">{esc(theme)}</p><a href="{esc(link)}" target="_blank" rel="noopener">Referencia oficial →</a></div></div>' for title,desc,theme,img,link in POP)

narr=gloss(e.get("narrativa","")).replace("\n","<br>")
res=gloss(e.get("resumen_ejecutivo","")).replace("\n","<br>")
ht=e.get("horizonte_temporal",{}) or {}; phases=ht.get("fases",[]) or []
phase_html="".join(f'<div class="line reveal"><b>{esc(p.get("fase",""))}</b><span class="muted"> ~{esc(p.get("ano_estimado",""))}</span><p>{esc(p.get("descripcion",""))}</p></div>' for p in phases)

CHAPS=[("sec-1","01 Narrativa"),("sec-2","02 Resumen"),("sec-3","03 Fundamentos"),("sec-4","04 Plausib."),
("sec-5","05 Horizonte"),("sec-6","06 Tecnolog."),("sec-7","07 Impactos"),("sec-8","08 Riesgos"),
("sec-9","09 Oportun."),("sec-10","10 Senales"),("sec-11","11 Interdep."),("sec-12","12 Actores"),
("sec-13","13 Investig."),("sec-ref","Referencias"),("sec-meta","Metadatos")]
chapnav='<nav class="chapnav"><div class="chap-inner">'+''.join(f'<a href="#{i}">{l}</a>' for i,l in CHAPS)+'<button class="chap-cult" id="chapCult">🎬 Cultura Pop</button></div></nav>'

HTML=f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>FUTURIA — {esc(e.get("titulo",""))}</title>
<style>
:root{{--bg:#06060a;--text:#e4e4ec;--muted:#8a8a9e;--accent:#ff5230;--border:rgba(255,255,255,.08);--card:rgba(255,255,255,.03)}}
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
html{{scroll-behavior:smooth}}body{{font-family:system-ui,-apple-system,'Inter',sans-serif;background:var(--bg);color:var(--text);line-height:1.7;overflow-x:hidden;padding-top:0}}
a{{color:var(--accent);text-decoration:none}}.muted{{color:var(--muted);font-size:.85rem}}
.container{{max-width:1120px;margin:0 auto;padding:0 1.6rem}}
nav.top{{position:fixed;top:0;left:0;right:0;z-index:50;background:rgba(6,6,10,.9);backdrop-filter:blur(14px);border-bottom:1px solid var(--border)}}
.nav-inner{{max-width:1120px;margin:0 auto;padding:.9rem 1.6rem;display:flex;align-items:center;justify-content:space-between}}
.brand{{font-weight:900;letter-spacing:-.04em;font-size:1.25rem;color:#fff}}.brand em{{color:var(--accent);font-style:normal}}
.back{{color:var(--muted);font-size:.9rem}}
.chapnav{{position:fixed;top:52px;left:0;right:0;z-index:49;background:rgba(6,6,10,.92);backdrop-filter:blur(12px);border-bottom:1px solid var(--border);overflow-x:auto}}
.chap-inner{{max-width:1120px;margin:0 auto;display:flex;gap:.3rem;padding:.5rem 1.6rem}}
.chap-inner a{{white-space:nowrap;font-size:.7rem;color:var(--muted);padding:.28rem .6rem;border-radius:99px;border:1px solid var(--border)}}
.chap-inner a:hover{{color:var(--accent);border-color:var(--accent)}}
.hero{{position:relative;min-height:80vh;display:flex;align-items:center;overflow:hidden}}
.hero img{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:.34;filter:saturate(1.1)}}
.hero::after{{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(6,6,10,.5),rgba(6,6,10,.92))}}
.hero .container{{position:relative;z-index:2}}
.meta-tag{{text-transform:uppercase;letter-spacing:.18em;font-size:.75rem;color:var(--accent);margin-top:6rem}}
.hero h1{{font-size:clamp(2rem,5vw,3.4rem);line-height:1.08;color:#fff;letter-spacing:-.03em;margin:.6rem 0}}
.lead{{font-size:1.12rem;max-width:760px;color:var(--text);margin-top:1rem}}
section{{padding:4.5rem 0;border-top:1px solid var(--border);scroll-margin-top:120px}}
.sec-num{{color:var(--accent);font-weight:900;font-size:.85rem;letter-spacing:.2em}}
h2.sec{{font-size:1.9rem;color:#fff;letter-spacing:-.02em;margin:.3rem 0 1.6rem}}
h3{{color:#fff;font-size:1.2rem;margin:.4rem 0}}
p{{color:var(--muted);margin:.6rem 0}}
.reveal{{opacity:0;transform:translateY(24px);transition:opacity .7s ease,transform .7s ease}}
.reveal.in{{opacity:1;transform:none}}
.gauge-wrap{{display:flex;gap:2.5rem;flex-wrap:wrap;align-items:center}}
.gauge{{--p:{pt};width:170px;height:170px;border-radius:50%;background:conic-gradient(var(--accent) calc(var(--p)*1%),rgba(255,255,255,.08) 0);display:grid;place-items:center;position:relative;flex:none}}
.gauge::before{{content:"";position:absolute;inset:14px;border-radius:50%;background:var(--bg)}}
.gauge b{{position:relative;font-size:2.2rem;color:#fff}}
.gauge small{{position:relative;display:block;text-align:center;color:var(--muted);font-size:.7rem}}
.dim{{display:grid;grid-template-columns:160px 1fr 36px;gap:.6rem;align-items:center;margin:.5rem 0}}
.dim span{{font-size:.82rem;color:var(--muted)}}
.bar{{height:8px;background:rgba(255,255,255,.08);border-radius:99px;overflow:hidden}}
.bar i{{display:block;height:100%;background:linear-gradient(90deg,var(--accent),#ff8a5c)}}
.bar.sm{{width:120px;display:inline-block;vertical-align:middle}}
.dim b{{color:#fff;font-size:.85rem;text-align:right}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:1rem;margin-top:1.2rem}}
.impact-card,.risk,.opp,.actor,.fund,.tech,.line,.sig,.ref{{background:var(--card);border:1px solid var(--border);border-radius:1rem;padding:1.2rem}}
.imp-head,.risk-top{{display:flex;justify-content:space-between;align-items:center;gap:.5rem}}
.imp-head h4{{color:#fff;font-size:1.05rem;margin:0}}
.mag{{font-size:.7rem;text-transform:uppercase;letter-spacing:.1em;padding:.25rem .6rem;border-radius:99px}}
.mag-alto,.mag-transformador{{background:rgba(255,82,48,.16);color:#ff7a5c}}
.mag-medio{{background:rgba(255,180,80,.14);color:#ffc266}}
.mag-bajo{{background:rgba(120,180,255,.14);color:#8ab4ff}}
.mag-significativo{{background:rgba(255,82,48,.14);color:#ff7a5c}}
.mag-incremental{{background:rgba(120,180,255,.14);color:#8ab4ff}}
.pill{{font-size:.68rem;text-transform:uppercase;letter-spacing:.08em;padding:.2rem .55rem;border-radius:99px;background:rgba(255,255,255,.06);color:var(--muted)}}
.pill-tecnologico,.pill-existente,.pill-favorable{{color:#7affb0;background:rgba(120,255,176,.1)}}
.pill-politico,.pill-estado,.pill-opuesto{{color:#ff7a5c;background:rgba(255,82,48,.12)}}
.pill-social,.pill-en_desarrollo,.pill-creciente{{color:#ffc266;background:rgba(255,180,80,.12)}}
.pill-etico,.pill-teorica,.pill-no_detectada{{color:#b98aff;background:rgba(185,138,255,.12)}}
.pill-organization,.pill-humano,.pill-agente_ia,.pill-dependiente,.pill-confirmada,.pill-emergente{{color:#8ab4ff;background:rgba(120,180,255,.12)}}
.pill-ambiental,.pill-bajo{{color:#8affd0;background:rgba(120,255,208,.1)}}
.tags{{display:flex;flex-wrap:wrap;gap:.4rem;margin-top:.6rem}}
.tags span{{font-size:.72rem;padding:.2rem .55rem;border:1px solid var(--border);border-radius:99px;color:var(--muted)}}
.risk-meta,.sig-meta{{font-size:.78rem;color:var(--muted);margin:.4rem 0}}
.st-confirmada{{color:#7affb0}}.st-emergente{{color:#ffc266}}.st-no_detectada{{color:#b98aff}}
.fund-sec{{margin-bottom:1.6rem}}.fund-sec h3{{margin-bottom:.7rem}}
.fund,.tech{{margin-bottom:.7rem}}
.cite{{display:inline-block;font-size:.72rem;color:var(--accent);margin-top:.3rem}}
.cite-wrap{{position:relative;display:inline-block;margin:.2rem .4rem .2rem 0}}
.cite-badge{{display:inline-flex;align-items:center;gap:.35rem;font-size:.72rem;font-weight:600;color:var(--c,#fff);
  background:color-mix(in srgb,var(--c,#888) 14%,transparent);border:1px solid var(--c,#888);
  padding:.25rem .6rem;border-radius:99px;cursor:pointer;text-decoration:none}}
.cite-badge img{{width:14px;height:14px;object-fit:contain;filter:drop-shadow(0 0 2px var(--c))}}
.cite-pop{{position:absolute;left:0;bottom:calc(100% + 10px);z-index:30;width:260px;
  background:#0d0d14;border:1px solid var(--c,#888);border-radius:.9rem;padding:.9rem;
  box-shadow:0 12px 40px rgba(0,0,0,.6);opacity:0;visibility:hidden;transform:translateY(8px);
  transition:opacity .18s ease,transform .18s ease,visibility .18s;pointer-events:none}}
.cite-wrap:hover .cite-pop,.cite-wrap:focus-within .cite-pop{{opacity:1;visibility:visible;transform:none;pointer-events:auto}}
.cite-pop::after{{content:"";position:absolute;top:100%;left:24px;border:7px solid transparent;border-top-color:var(--c,#888)}}
.cite-pop-icon{{width:34px;height:34px;object-fit:contain;float:left;margin-right:.6rem;filter:drop-shadow(0 0 3px var(--c))}}
.cite-pop-type{{display:block;font-size:.68rem;text-transform:uppercase;letter-spacing:.1em;color:var(--c,#fff)}}
.cite-pop-title{{display:block;font-size:.86rem;color:#fff;margin-top:.2rem;line-height:1.3}}
.cite-pop-domain{{display:block;font-size:.74rem;color:var(--muted);margin-top:.25rem;word-break:break-all}}
.cite-pop-hint{{display:block;font-size:.68rem;color:var(--c,#aaa);margin-top:.4rem}}
.cite-broken{{opacity:.6;border-style:dashed !important}}
/* Glosario: banderas de pais */
.flag{{white-space:nowrap;font-weight:600}}
/* Glosario: siglas con popover */
.acr{{position:relative;cursor:help;font-weight:700;border-bottom:1px dotted var(--accent);color:#fff}}
.acr-pop{{position:absolute;left:0;bottom:calc(100% + 8px);z-index:40;width:240px;background:#0d0d14;border:1px solid var(--accent);
  border-radius:.7rem;padding:.7rem;font-weight:400;font-size:.8rem;color:var(--text);box-shadow:0 10px 36px rgba(0,0,0,.6);
  opacity:0;visibility:hidden;transform:translateY(8px);transition:.18s;pointer-events:none}}
.acr:hover .acr-pop,.acr:focus .acr-pop{{opacity:1;visibility:visible;transform:none;pointer-events:auto}}
/* Interdependencias popovers */
.dep{{position:relative;display:inline-flex;flex-direction:column;gap:.4rem;max-width:100%}}
.dep-rel{{background:rgba(74,163,255,.12);color:#9ec5ff;border:1px solid #4aa3ff;cursor:pointer;padding:.5rem .8rem;border-radius:.6rem;font-size:.82rem;font-weight:600}}
.dep-inc{{background:rgba(178,34,52,.16);color:#ff9aa6;border:1px solid #b22234;cursor:pointer;padding:.5rem .8rem;border-radius:.6rem;font-size:.82rem;font-weight:600}}
.dep-pop{{position:absolute;left:0;top:calc(100% + 8px);z-index:40;width:280px;background:#0d0d14;border:1px solid var(--accent);
  border-radius:.7rem;padding:.8rem;font-weight:400;font-size:.82rem;color:var(--text);box-shadow:0 10px 36px rgba(0,0,0,.6);
  opacity:0;visibility:hidden;transform:translateY(8px);transition:.18s;pointer-events:none}}
.dep-rel:hover .dep-pop,.dep-rel:focus-within .dep-pop,.dep-inc:hover .dep-pop,.dep-inc:focus-within .dep-pop{{opacity:1;visibility:visible;transform:none;pointer-events:auto}}
/* Cultura Pop dos columnas */
.cult-grid{{display:grid;grid-template-columns:0.9fr 1.4fr;gap:1.6rem;margin-top:1.2rem;align-items:start}}
.cult-left{{background:var(--card);border:1px solid var(--border);border-radius:1rem;padding:1.3rem}}
.cult-left h3{{color:#fff;margin-bottom:.6rem}}
.cult-right{{display:flex;flex-direction:column;gap:1rem}}
.pop{{display:flex;gap:1rem;background:var(--card);border:1px solid var(--border);border-radius:1rem;padding:1rem;align-items:center}}
.pop img{{width:120px;height:120px;object-fit:cover;border-radius:.7rem;flex-shrink:0;border:1px solid var(--border)}}
.pop-body{{flex:1}}
.pop-body h4{{color:#fff;margin-bottom:.3rem}}
.pop-body p{{font-size:.85rem;color:var(--text)}}
.pop-body a{{display:inline-block;margin-top:.4rem;font-size:.82rem;font-weight:600}}
/* Layout principal + panel Cultura Pop lateral */
.layout{{display:flex;align-items:flex-start;gap:0;max-width:1480px;margin:0 auto;padding:0 1.6rem}}
.main{{flex:1;min-width:0;max-width:100%}}
.cult-panel{{position:sticky;top:104px;align-self:flex-start;width:25%;min-width:300px;max-height:calc(100vh - 124px);
  overflow-y:auto;background:rgba(255,255,255,.025);border-left:1px solid var(--border);
  border-radius:0 0 0 1rem;padding:1.4rem 1.2rem;scroll-behavior:smooth}}
.cult-panel::-webkit-scrollbar{{width:7px}}
.cult-panel::-webkit-scrollbar-thumb{{background:var(--border);border-radius:4px}}
.cult-toggle{{position:absolute;top:.8rem;right:.8rem;background:var(--card);border:1px solid var(--border);
  color:var(--muted);width:28px;height:28px;border-radius:50%;cursor:pointer;font-size:.9rem;line-height:1}}
.cult-toggle:hover{{color:var(--accent);border-color:var(--accent)}}
.cult-inner .sec-num{{margin-top:0}}
.cult-intro{{background:var(--card);border:1px solid var(--border);border-radius:1rem;padding:1rem;margin:1rem 0}}
.cult-intro h3{{color:#fff;margin-bottom:.4rem;font-size:1rem}}
.cult-panel .pop{{flex-direction:column;text-align:center;padding:1rem}}
.cult-panel .pop img{{width:100%;height:140px}}
.cult-panel .pop-body{{text-align:left}}
/* Estado colapsado */
.layout.cult-hidden .cult-panel{{display:none}}
.layout.cult-hidden .main{{max-width:100%}}
/* Boton en nav */
.chap-cult{{background:transparent;border:1px solid var(--accent);color:var(--accent);border-radius:99px;
  padding:.3rem .8rem;font-size:.78rem;font-weight:600;cursor:pointer;white-space:nowrap}}
.chap-cult:hover{{background:var(--accent);color:#06060a}}
@media(max-width:980px){{.layout{{flex-direction:column;padding:0 1.1rem}}.cult-panel{{position:static;width:100%;max-height:none;border-left:none;border-top:1px solid var(--border);border-radius:0}}.layout.cult-hidden .cult-panel{{display:none}}}}
.fig{{margin-top:1rem;text-align:center}}
.fig img{{max-width:100%;border-radius:1rem;border:1px solid var(--border);max-height:260px;object-fit:cover}}
.fig figcaption{{display:block;margin-top:.4rem;font-size:.8rem;color:var(--muted)}}
.narr-fig{{margin:1.4rem 0}}
.narr-fig img{{width:100%;max-height:320px;object-fit:cover;border-radius:1rem;border:1px solid var(--border)}}
.pop{{display:grid;grid-template-columns:140px 1fr;gap:1rem;align-items:center;background:var(--card);border:1px solid var(--border);border-radius:1rem;padding:1rem;margin-bottom:1rem}}
.pop img{{width:140px;height:180px;object-fit:cover;border-radius:.6rem}}
.pop-body h4{{color:#fff;font-size:1rem;margin-bottom:.3rem}}
.dep{{display:inline-block;font-size:.74rem;padding:.25rem .6rem;border-radius:99px;margin:.2rem .3rem .2rem 0}}
.dep-rel{{background:rgba(120,180,255,.12);color:#8ab4ff}}
.dep-inc{{background:rgba(255,82,48,.12);color:#ff7a5c}}
.ref-type{{font-size:.68rem;text-transform:uppercase;color:var(--accent)}}
@media(max-width:640px){{.pop{{grid-template-columns:1fr}}.pop img{{width:100%;height:160px}}}}
</style>
</head>
<body>
<nav class="top"><div class="nav-inner"><a href="/" class="brand">FUTU<em>RIA</em></a><a href="/" class="back">← Volver</a></div></nav>
{chapnav}
<div class="hero"><img src="{ASSETS}/{esc(IMG['hero'])}" alt="{esc(e.get('titulo',''))}">
<div class="container">
<div class="meta-tag">Escenario PRISM · {esc(e.get("id",""))} · {esc(e.get("estado","").replace("_"," "))}</div>
<h1>{esc(e.get("titulo",""))}</h1>
<p class="lead">{res[:420]}…</p>
</div></div>

<div class="layout" id="layout">
<div class="main">

<section id="sec-1"><div class="sec-num">01 · NARRATIVA</div><h2 class="sec">El escenario</h2><p>{narr}</p>
{narr_fig}</section>

<section id="sec-2"><div class="sec-num">02 · RESUMEN EJECUTIVO</div><h2 class="sec">Para ejecutivos</h2><p>{res}</p></section>

<section id="sec-3"><div class="sec-num">03 · FUNDAMENTOS</div><h2 class="sec">Bases del escenario</h2>{fund_html}</section>

<section id="sec-4"><div class="sec-num">04 · PLAUSIBILIDAD</div><h2 class="sec">Que tan probable es</h2>
<div class="gauge-wrap"><div class="gauge"><b>{pt:.0f}</b><small>PLAUSIBILIDAD</small></div>
<div style="flex:1;min-width:260px">{dim_rows}<p class="muted" style="margin-top:.8rem">{pl_metodologia}</p>
<p style="margin-top:.6rem"><a class="cite" href="../metodologia/plausibilidad-metodologia.html" target="_blank" rel="noopener">Metodología del Instituto (criterio y fórmula) ↗</a></p></div></div></section>

<section id="sec-5"><div class="sec-num">05 · HORIZONTE TEMPORAL</div><h2 class="sec">Cuando pasa</h2>
<p class="muted">Rango {esc(ht.get("rango",""))} · Punto medio {esc(ht.get("punto_medio_estimado",""))} · Confianza {esc(ht.get("confianza",""))}</p>
<div class="grid">{phase_html}</div></section>

<section id="sec-6"><div class="sec-num">06 · TECNOLOGIAS CLAVE</div><h2 class="sec">Que lo hace posible</h2>{tech_html}</section>

<section id="sec-7"><div class="sec-num">07 · IMPACTOS</div><h2 class="sec">Lo que cambia</h2><div class="grid">{imp_html}</div></section>

<section id="sec-8"><div class="sec-num">08 · RIESGOS</div><h2 class="sec">Lo que puede salir mal</h2><div class="grid">{risk_html}</div></section>

<section id="sec-9"><div class="sec-num">09 · OPORTUNIDADES</div><h2 class="sec">Lo que se puede capturar</h2><div class="grid">{opp_html}</div></section>

<section id="sec-10"><div class="sec-num">10 · SENALES TEMPRANAS</div><h2 class="sec">Que monitorear hoy</h2>{sig_html}</section>

<section id="sec-11"><div class="sec-num">11 · INTERDEPENDENCIAS</div><h2 class="sec">Conexiones PRISM</h2>
<p class="muted">Relacionados</p><div class="tags" style="margin-bottom:.8rem">{rel_html}</div>
<p class="muted">Incompatibles</p><div class="tags">{inc_html}</div></section>

<section id="sec-12"><div class="sec-num">12 · ACTORES CLAVE</div><h2 class="sec">Quien importa</h2><div class="grid">{act_html}</div></section>

<section id="sec-13"><div class="sec-num">13 · LINEAS DE INVESTIGACION</div><h2 class="sec">Que falta saber</h2>{lin_html}</section>

<section id="sec-ref"><div class="sec-num">REFERENCIAS</div><h2 class="sec">Fuentes primarias</h2>{ref_html}</section>

<section id="sec-meta"><div class="sec-num">METADATOS</div><h2 class="sec">Trazabilidad</h2>
<p>Autores: {esc(auth)}</p>
<p class="muted">Version {esc(m.get("version",""))} · {esc(m.get("licencia",""))} · Creado {esc(m.get("fecha_creacion",""))} · Hash blockchain: {esc(m.get("hash_blockchain") or "pendiente")}</p>
{chg_html}</section>

</div><!-- /main -->

<aside class="cult-panel" id="cultPanel">
<button class="cult-toggle" id="cultToggle" aria-label="Ocultar Cultura Pop">✕</button>
<div class="cult-inner">
<div class="sec-num">CULTURA POP</div><h2 class="sec">Neurotech en el cine</h2>
<p class="muted">Referentes que anticiparon el debate. Imagenes originales generadas por IA (homenaje, no la pelicula real).</p>
<div class="cult-intro"><h3>Por que importa</h3><p>La ficcion lleva decadas explorando la frontera mente-maquina: desde la intrusion neural hasta el borrado de memorias. Estos referentes popularizaron intuitivamente dilemas que hoy debatimos como neuro-derechos. No son predictivos, pero son el imaginario que moldea la aceptacion social de la tecnologia.</p></div>
{pop_html}
</div>
</aside>

</div><!-- /layout -->
<script>
const io=new IntersectionObserver((es)=>{{es.forEach(e=>{{if(e.isIntersecting){{e.target.classList.add('in');io.unobserve(e.target)}}}})}},{{threshold:.12}});
document.querySelectorAll('.reveal').forEach(el=>io.observe(el));
// Toggle panel Cultura Pop
const layout=document.getElementById('layout');
const togglePanel=()=>layout.classList.toggle('cult-hidden');
const bt=document.getElementById('cultToggle'); if(bt) bt.addEventListener('click',togglePanel);
const chapBt=document.getElementById('chapCult'); if(chapBt) chapBt.addEventListener('click',()=>{{ if(layout.classList.contains('cult-hidden')) layout.classList.remove('cult-hidden'); document.getElementById('cultPanel').scrollIntoView({{behavior:'smooth'}}); }});
</script>
</body>
</html>'''

OUT.write_text(HTML, encoding="utf-8")
print("OK ->", OUT, len(HTML), "bytes")

# ---- Doble control de citas: reporte de URLs (no bloquea el render) ----
print("\n=== DOBLE CONTROL DE CITAS (verificacion de URLs) ===")
all_urls = []
for r in ref:
    if r.get("doi_url"):
        all_urls.append(("ref:"+str(r.get("autores",""))[:30], r["doi_url"]))
broken = []
for name, u in all_urls:
    try:
        ok = url_ok(u, timeout=10)
    except Exception:
        ok = False
    status = "OK " if ok else "ROTA"
    if not ok: broken.append((name, u))
    print(f"  [{status}] {name} -> {u}")
if broken:
    print(f"\n  ⚠ {len(broken)} URL(s) ROTA(S) — corregir en el YAML antes de publicar.")
else:
    print("\n  ✓ Todas las URLs de referencias resuelven.")
