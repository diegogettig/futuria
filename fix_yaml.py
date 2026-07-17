#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""fix_yaml.py — Normaliza un YAML PRISM migrado: separa fundamentos planos en
sub-listas (cientificos/tecnologicos/sociales/economicos) segun el tipo de clave,
para cumplir el schema que espera render_prism.py. Uso: python fix_yaml.py <archivo.yaml>
"""
import sys, yaml, os

path = sys.argv[1]
d = yaml.safe_load(open(path, encoding='utf-8'))
e = d['escenario']
fnd = e.get('fundamentos', [])
if isinstance(fnd, list):
    cien=[]; tec=[]; soc=[]; eco=[]
    for it in fnd:
        if not isinstance(it, dict): continue
        if 'campo' in it: cien.append(it)
        elif 'nombre' in it: tec.append(it)
        elif 'tendencia' in it: soc.append(it)
        elif 'indicador' in it: eco.append(it)
    e['fundamentos'] = {'cientificos':cien,'tecnologicos':tec,'sociales':soc,'economicos':eco}
    print(f"fundamentos -> cien={len(cien)} tec={len(tec)} soc={len(soc)} eco={len(eco)}")
# impactos: asegurar que cada seccion tenga dict (no lista)
imp = e.get('impactos', {})
if isinstance(imp, dict):
    for k,v in list(imp.items()):
        if isinstance(v, list):
            # tomar primer elemento si es dict
            imp[k] = v[0] if v and isinstance(v[0], dict) else {'descripcion': (v[0] if v else ''), 'magnitud':'medio'}
# riesgos/oportunidades: asegurar listas de dict
for key in ('riesgos','oportunidades','senales_tempranas'):
    val = e.get(key, [])
    if val is None: e[key]=[]
# interdependencias listas
inter = e.get('interdependencias', {})
if isinstance(inter, dict):
    for k in ('escenarios_relacionados','escenarios_incompatibles'):
        if inter.get(k) is None: inter[k]=[]

open(path, 'w', encoding='utf-8').write(yaml.safe_dump(d, allow_unicode=True, sort_keys=False))
print("OK ->", path)
