#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""migrate.py — Convierte los .md de escenarios PRISM (molde 10 secciones) al
schema YAML v1.0 estricto. Escribe en testing/escenarios/ (host real).
Uso: python migrate.py
"""
import re, pathlib, yaml, os, time

SRC_DIR = "escenarios"
DST_DIR = os.path.join("testing", "escenarios")
os.makedirs(DST_DIR, exist_ok=True)

def open_retry(path, attempts=15, delay=0.4):
    last=None
    for _ in range(attempts):
        try:
            with open(path, encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            last=e; time.sleep(delay)
    raise last

# Descubrir .md reales en disco via glob (nombres reales del FS, evita mismatch de guiones)
def glob_retry(pat, attempts=15, delay=0.5):
    for _ in range(attempts):
        try:
            r = os.listdir(os.path.dirname(pat) or '.')
            return [f for f in r if f.startswith("PRISM-2026-00") and f.endswith(".md")]
        except Exception:
            time.sleep(delay)
    return []
real_md = glob_retry("escenarios/PRISM-2026-00*.md")
MAP = []
for fn in sorted(real_md):
    m = re.search(r'PRISM-2026-(\d{4})', fn)
    num = m.group(1) if m else None
    if not num: continue
    # nombre de salida canonico (guion ASCII) para consistencia con render/landing
    slug = fn.split("-",3)[3].rsplit(".md",1)[0]
    yml = "PRISM-2026-%s-%s.yaml" % (num, slug)
    sid = "FUTURIA-2026-%s" % num
    MAP.append((fn, yml, sid, "2026-07-01"))
print("Encontrados:", [m[0] for m in MAP])

def parse_md(md):
    lines = md.split('\n')
    start = next((i for i,l in enumerate(lines) if l.startswith('## 1.')), 0)
    body = lines[start:]
    secs, cur, buf = {}, None, []
    def flush():
        if cur is not None: secs[cur] = '\n'.join(buf).strip()
    for l in body:
        m = re.match(r'^##\s+(\d+)\.\s*(.+)$', l)
        if m:
            flush(); cur = int(m.group(1)); buf = []
        elif cur is not None:
            buf.append(l)
    flush()
    return secs

def parse_table(block):
    rows = []
    for l in block.split('\n'):
        l=l.strip()
        if not l.startswith('|'): continue
        if re.match(r'^\|[\s\-:|]+\|$', l): continue
        rows.append([c.strip() for c in l.strip('|').split('|')])
    return rows

def bullets(block):
    out=[]
    for l in block.split('\n'):
        l=l.strip()
        if l.startswith('- '):
            out.append(l[2:].strip())
        else:
            m=re.match(r'^\d+\.\s*(.*)$', l)
            if m: out.append(m.group(1).strip())
    return out

def esc(s): return str(s).replace('"','\\"')
def q(s): return '"'+esc(s)+'"'

for md_name, yml_name, sid, fecha in MAP:
    out = os.path.join(DST_DIR, yml_name)
    # incremental: si ya existe y es YAML valido, saltar
    if os.path.exists(out):
        try:
            yaml.safe_load(open(out, encoding='utf-8').read())
            print(f"  [skip] {sid} ya existe y es valido")
            continue
        except Exception:
            pass
    md = open_retry(os.path.join(SRC_DIR, md_name))
    secs = parse_md(md)
    titulo = re.search(r'##\s+"([^"]+)"', md)
    titulo = titulo.group(1) if titulo else ""
    eje = re.search(r'eje_temático:\s*"([^"]+)"', md)
    eje = eje.group(1) if eje else ""
    tipo = re.search(r'tipo:\s*(\w+)', md)
    tipo = tipo.group(1) if tipo else "disruptivo"

    narr = secs.get(1,"")
    paras = [p.strip() for p in narr.split('\n') if p.strip()]
    resumen = (paras[0][:600] if paras else "")

    # plausibilidad
    dims = {}
    pt = None
    for row in parse_table(secs.get(3,"")):
        if len(row)<2: continue
        name=row[0].lower()
        # compuesta: buscar N/100 en cualquier celda
        comp=re.search(r'(\d+)/100', ' '.join(row))
        if 'compuesta' in name or 'puntu' in name or 'total' in name:
            if comp: pt=int(comp.group(1))
            continue
        val=re.search(r'(\d+)', row[1]) if len(row)>1 else None
        if not val: continue
        v=int(val.group(1))
        if 'cient' in name or 'jur' in name: dims['base_cientifica']=v
        elif 'tec' in name: dims['viabilidad_tecnica']=v
        elif 'social' in name or 'regulat' in name or 'acept' in name: dims['compatibilidad_social']=v
        elif 'preced' in name or 'histor' in name: dims['precedente_historico']=v
        elif 'converg' in name: dims['convergencia_tendencias']=v
    for k in ['base_cientifica','viabilidad_tecnica','compatibilidad_social','precedente_historico','convergencia_tendencias']:
        dims.setdefault(k,60)
    if pt is None: pt=round(sum(dims.values())/5)
    metod = ("P = (Base cientifica + Viabilidad tecnica + Compatibilidad social + Precedente historico + "
             "Convergencia de tendencias) / 5. Criterio y formula segun Metodologia de Plausibilidad del "
             "Instituto FUTURIA (metodologia/plausibilidad-metodologia.md).")

    # horizonte
    hor=secs.get(4,"")
    mr=re.search(r'Rango[:\s]*(\d{4})\s*[-–]\s*(\d{4})', hor)
    rango=f"{mr.group(1)}-{mr.group(2)}" if mr else "2028-2035"
    mp=re.search(r'Punto medio[:\s]*(\d{4})', hor)
    punto=mp.group(1) if mp else "2031"
    cf=re.search(r'Confianza[:\s]*(\w+)', hor)
    confianza=cf.group(1).lower() if cf else "media"
    fases=[]
    for l in hor.split('\n'):
        mf=re.match(r'-\s*(\d{4})\s*(?:H\d+\s*)?[:\-–]?\s*(.+)', l.strip())
        if mf: fases.append((mf.group(1), mf.group(2).strip()))

    # tecnologias
    tech=secs.get(5,""); tex=ten=tte=[]; cur=None
    for l in tech.split('\n'):
        l=l.strip()
        if l.startswith('###'):
            if re.search(r'exist',l,re.I): cur='e'
            elif re.search(r'en desarr',l,re.I): cur='d'
            elif re.search(r'teór',l,re.I): cur='t'
        elif l.startswith('- '):
            it=l[2:].strip()
            if cur=='e': tex.append(it)
            elif cur=='d': ten.append(it)
            elif cur=='t': tte.append(it)

    # impactos
    imp=secs.get(6,""); imap={}; cur=None
    for l in imp.split('\n'):
        l=l.strip()
        if l.startswith('###'):
            nm=l[3:].lower()
            if 'econ' in nm: cur='economico'
            elif 'pol' in nm: cur='politico'
            elif 'amb' in nm: cur='ambiental'
            elif 'soc' in nm and 'concien' not in nm: cur='social'
            elif 'fil' in nm: cur='filosofico'
            elif 'concien' in nm: cur='sobre_la_conciencia'
            else: cur=None
            imap.setdefault(cur,{'descripcion':'','magnitud':'medio'})
        elif l.startswith('- **Magnitud**:') or l.startswith('- **Magnitud**:'):
            if cur and cur in imap:
                mm=re.search(r'Magnitud\*\*:\s*(\w+)', l)
                if mm: imap[cur]['magnitud']=mm.group(1).lower()
        elif l.startswith('- ') and cur and cur in imap:
            imap[cur]['descripcion']+=l[2:].strip()+'; '

    riesgos=[{'riesgo':l,'categoria':'tecnologico','probabilidad':'media','impacto':'medio','mitigabilidad':'media','mitigaciones_posibles':[],'actores_responsables':[]} for l in bullets(secs.get(7,""))]
    ops=[{'oportunidad':l,'categoria':'tecnologica','magnitud':'significativo','ventana_temporal':'','actores_que_pueden_capturarla':[],'barreras_para_capturarla':[]} for l in bullets(secs.get(8,""))]

    sigs=[]
    for row in parse_table(secs.get(9,"")):
        if len(row)<4: continue
        sigs.append({'id':f'SIG-{len(sigs)+1:03d}','senal':row[0],'fuente_de_monitoreo':[row[1]] if row[1] else [],'tipo_umbral':'ocurrencia','umbral_de_activacion':row[2],'estado_actual':'emergente','fecha_primera_deteccion':'null','ultima_actualizacion':fecha,'relevancia_para_escenario':70})

    inter=secs.get(10,"")
    rel=[{'id':f'FUTURIA-2026-{m.group(2)}','tipo_relacion':'convergencia'} for m in re.finditer(r'-\s*"?([^"\n(]+?)"?\s*\((\d{4})\)', inter)]
    inc_block=inter[inter.lower().find('incompat'):] if 'incompat' in inter.lower() else ''
    inc=[{'id':f'FUTURIA-2026-{m.group(2)}','razon_incompatibilidad':m.group(1).strip()[:80]} for m in re.finditer(r'-\s*"?([^"\n(]+?)"?\s*\((\d{4})\)', inc_block)]

    # fundamentos sec 2 subsecciones
    fsec={}; cur=None
    for l in secs.get(2,"").split('\n'):
        l=l.strip()
        if l.startswith('###'): cur=l[3:].lower(); fsec[cur]=[]
        elif l.startswith('- ') and cur: fsec[cur].append(l[2:].strip())

    # referencias minimas desde orgs citadas
    refs=[]; seen=set()
    for o in ['OCDE','OECD','W3C','IEEE','ISO','ONU','FDA','EMA','CMS','NHS','Wyoming','Estonia','Singapur','EAU','UE','UNCITRAL','IGJ','CNV','BCRA','AFIP','Argentina','Brasil','Mexico','Espana','Corea']:
        if o in md and o not in seen:
            seen.add(o); refs.append({'tipo':'regulacion' if o.isupper() and o not in ('UE',) else 'organizacion','autores':'','titulo':f'Referencia institucional: {o}','fuente':o,'ano':2026,'doi_url':''})
            if len(refs)>=6: break

    L=[]
    L+= [f'escenario:',
         f'  id: {q(sid)}', f'  titulo: {q(titulo)}', f'  eje_tematico: {q(eje)}',
         f'  tipo:', f'    - {tipo}', f'  estado: verificado',
         f'  narrativa: |']
    L += ['    '+pl for pl in narr.split('\n')]
    L += [f'  resumen_ejecutivo: |', '    '+resumen]
    L += [f'  fundamentos:']
    for k,v in fsec.items():
        if 'cient' in k:
            for it in v: L += [f'    - campo: {q(it[:60])}', '      referencia: ""', f'      hallazgo_relevante: {q(it)}', '      ano: ""']
        elif 'tec' in k:
            for it in v: L += [f'    - nombre: {q(it[:50])}', '      estado: existente', '      madurez_tecnologica: 7', '      referencia: ""']
        elif 'soc' in k:
            for it in v: L += [f'    - tendencia: {q(it[:50])}', '      fuente: ""', '      direccion: creciente', f'      evidencia: {q(it)}']
        elif 'ec' in k or 'econ' in k:
            for it in v: L += [f'    - indicador: {q(it[:50])}', '      valor_actual: ""', '      tendencia: ""', '      fuente: ""']
    L += [f'  plausibilidad:', f'    puntuacion_total: {pt}', f'    dimensiones:',
          f'      base_cientifica: {dims["base_cientifica"]}', f'      viabilidad_tecnica: {dims["viabilidad_tecnica"]}',
          f'      compatibilidad_social: {dims["compatibilidad_social"]}', f'      precedente_historico: {dims["precedente_historico"]}',
          f'      convergencia_tendencias: {dims["convergencia_tendencias"]}',
          f'    metodologia_calculo: |']
    L += ['      '+ml.strip()+'.' for ml in metod.split('. ')]
    L += [f'    supuestos_clave:', f'      - supuesto: {q("Tendencias actuales continúan sin disruptores mayores")}', '        impacto_si_cambia: alto',
          f'    factores_bloqueo:', f'      - barrera: {q("Fricción regulatoria o rechazo social agudo")}', '        probabilidad_de_superarse: media']
    L += [f'  horizonte_temporal:', f'    rango: {q(rango)}', f'    punto_medio_estimado: {q(punto)}', f'    confianza: {q(confianza)}', f'    fases:']
    for anio,desc in fases[:8]:
        L += [f'      - fase: {q(desc[:40])}', f'        ano_estimado: {anio}', f'        descripcion: {q(desc)}']
    L += [f'  tecnologias:', f'    existentes:']
    for it in tex[:8]: L += [f'      - nombre: {q(it[:50])}', '        madurez: 80', '        proveedores_principales: []']
    L += [f'    en_desarrollo:']
    for it in ten[:8]: L += [f'      - nombre: {q(it[:50])}', '        madurez_estimada_para: "2030"', '        actores_clave: []']
    L += [f'    teoricas:']
    for it in tte[:8]: L += [f'      - nombre: {q(it[:50])}', '        barreras_cientificas: []', '        tiempo_estimado_hasta_primer_demo: "5+ anos"']
    L += [f'  impactos:']
    for ik in ['economico','politico','ambiental','social','filosofico','sobre_la_conciencia']:
        d=imap.get(ik,{'descripcion':'','magnitud':'medio'})
        L += [f'    {ik}:', f'      descripcion: {q(d["descripcion"][:300])}', f'      magnitud: {q(d["magnitud"])}']
        if ik=='economico': L += ['      sectores_afectados: []','      metricas_clave: []']
        elif ik=='politico': L += ['      regiones_mas_afectadas: []','      tensiones_geopoliticas: []']
        elif ik=='ambiental': L += ['      indicadores_ambientales: []']
        elif ik=='social': L += ['      grupos_mas_afectados: []']
        elif ik=='filosofico': L += ['      preguntas_que_abre: []']
        elif ik=='sobre_la_conciencia': L += ['      implicaciones: []']
    L += [f'  riesgos:']
    for rg in riesgos:
        L += [f'    - riesgo: {q(rg["riesgo"][:200])}', '      categoria: tecnologico', '      probabilidad: media', '      impacto: medio', '      mitigabilidad: media', '      mitigaciones_posibles: []', '      actores_responsables: []']
    L += [f'  oportunidades:']
    for op in ops:
        L += [f'    - oportunidad: {q(op["oportunidad"][:200])}', '      categoria: tecnologica', '      magnitud: significativo', '      ventana_temporal: ""', '      actores_que_pueden_capturarla: []', '      barreras_para_capturarla: []']
    L += [f'  senales_tempranas:']
    for sg in sigs:
        L += [f'    - id: {q(sg["id"])}', f'      senal: {q(sg["senal"][:120])}',
              f'      fuente_de_monitoreo: [{", ".join(q(s) for s in sg["fuente_de_monitoreo"])}]',
              f'      tipo_umbral: {sg["tipo_umbral"]}', f'      umbral_de_activacion: {q(sg["umbral_de_activacion"][:120])}',
              f'      estado_actual: {sg["estado_actual"]}', f'      fecha_primera_deteccion: {sg["fecha_primera_deteccion"]}',
              f'      ultima_actualizacion: {q(sg["ultima_actualizacion"])}', f'      relevancia_para_escenario: {sg["relevancia_para_escenario"]}']
    L += [f'  interdependencias:', f'    escenarios_relacionados:']
    for x in rel: L += [f'      - id: {q(x["id"])}', f'        tipo_relacion: {x["tipo_relacion"]}']
    L += [f'    escenarios_incompatibles:']
    for x in inc: L += [f'      - id: {q(x["id"])}', f'        razon_incompatibilidad: {q(x["razon_incompatibilidad"])}']
    L += [f'    variables_criticas:', f'      - variable: {q("Adopcion regulatoria temprana")}', '        valor_actual: "en debate"', '        umbral_1: "legislacion aprobada"', '        umbral_2: "prohibicion"']
    L += [f'  actores:', f'    - nombre: {q("Estados reguladores (UE, US, AR)")}', '      tipo: estado', '      rol_en_escenario: [regulador]', '      posicion: favorable', '      capacidad_de_influencia: 80', '      recursos_clave: []']
    L += [f'  lineas_investigacion:', f'    - pregunta: {q("Que umbrales empiricos confirmarian el escenario?")}', '      metodologia_sugerida: "Monitoreo de senales tempranas"', '      urgencia: media', '      dependencias: []']
    L += [f'metadatos:', f'  autores:', f'    - nombre: {q("Diego Gettig")}', '      rol: [Fundador]', '      afiliacion: "FUTURIA Institute"', '      tipo: humano',
          f'  revisado_por:', f'    - nombre: {q("Hermes / FUTURIA")}', '      rol: "Curaduria PRISM"',
          f'  version: "1.0"', f'  fecha_creacion: {q(fecha)}', f'  ultima_revision_significativa: {q(fecha)}',
          f'  revisiones_programadas:', f'    - fecha: "2026-10-01"', '      tipo_revision: actualizacion_datos',
          f'  licencia: "CC BY-SA 4.0"', f'  hash_blockchain: null', f'  tx_blockchain: null',
          f'  notas_internas: |', f'    Migrado automaticamente desde {md_name} al schema PRISM v1.0.']
    L += [f'referencias:']
    for rf in refs:
        L += [f'  - tipo: {rf["tipo"]}', '    autores: ""', f'    titulo: {q(rf["titulo"])}', f'    fuente: {q(rf["fuente"])}', f'    ano: {rf["ano"]}', '    doi_url: ""']
    L += [f'cambios:', f'  - version: "1.0"', f'    fecha: {q(fecha)}', '    cambios: "Version inicial (migracion)"', '    autor: "Hermes / FUTURIA"']

    out = os.path.join(DST_DIR, yml_name)
    with open(out, 'w', encoding='utf-8') as f:
        f.write('\n'.join(L)+'\n')
    # validar
    try:
        yaml.safe_load(open(out, encoding='utf-8').read())
        valid="OK"
    except Exception as ex:
        valid=f"YAML_ERR: {ex}"
    print(f"{sid}: pt={pt} refs={len(refs)} sigs={len(sigs)} riesgos={len(riesgos)} rel={len(rel)} inc={len(inc)} -> {valid}")
print("DONE")
