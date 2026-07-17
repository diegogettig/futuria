#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera el bloque HTML de cards de escenarios para la landing, leyendo los
YAML v1.0 desde testing/escenarios/. Produce el inner HTML del <div id="escenarios-grid">.
Uso: python gen_cards.py
Imprime el HTML en stdout (lo pegás dentro de <div class="grid-2" id="escenarios-grid">).
"""
import sys, pathlib, yaml

ROOT = pathlib.Path(__file__).resolve().parent
SCEN = ROOT / "testing" / "escenarios"

# Orden canónico de escenarios (ID 4 dígitos)
ORDER = [
    "PRISM-2026-010-neurodatos-soberania-digital",
    "PRISM-2026-0001-personalidad-juridica-ia",
    "PRISM-2026-0002-sociedades-automatizadas",
    "PRISM-2026-0003-cardio-bionico",
    "PRISM-2026-0004-hard-tech-foundations",
    "PRISM-2026-0005-gobernanza-algoritmica",
    "PRISM-2026-0006-longevidad-caas",
    "PRISM-2026-0007-conciencia-verificable",
    "PRISM-2026-0008-bioprinting-distribuido",
    "PRISM-2026-0009-geopolitica-datos",
]

def esc(s):
    return (str(s).replace("&","&amp;").replace("<","&lt;").replace(">","&gt;"))

cards = []
for base in ORDER:
    yml = SCEN / f"{base}.yaml"
    if not yml.exists():
        print(f"# FALTA: {base}.yaml", file=sys.stderr)
        continue
    d = yaml.safe_load(yml.read_text(encoding="utf-8"))
    e = d["escenario"]
    pl = e.get("plausibilidad", {})
    pt = pl.get("puntuacion_total", 0)
    ht = e.get("horizonte_temporal", {})
    rango = ht.get("rango", "")
    titulo = e.get("titulo", "")
    # descripcion corta del resumen ejecutivo (primeras 2 frases)
    res = e.get("resumen_ejecutivo", "") or ""
    desc = res.split(". ")[0]
    if len(desc) > 180:
        desc = desc[:177] + "..."
    # newsletter asociada (placeholder segun convencion existente)
    news = {"010":"#1","0001":"#1","0002":"#2","0003":"#3","0004":"#4",
            "0005":"#5","0006":"#6","0007":"#7","0008":"#8","0009":"#9"}.get(base.split("-")[2],"#1")
    html = f'''      <div class="card">
        <div class="tag">Escenario PRISM v1.0</div>
        <h3>{esc(titulo)}</h3>
        <p>Horizonte {esc(rango)} · Plausibilidad {pt}/100</p>
        <p style="margin-top:0.6rem;">{esc(desc)}</p>
        <a href="escenarios/{base}.html" target="_blank" rel="noopener" class="btn btn-primary" style="margin-top:0.8rem;padding:0.55rem 1.1rem;font-size:0.85rem;">Leer escenario completo →</a>
        <p style="margin-top:0.6rem;font-size:0.85rem;color:var(--muted);">Metodología PRISM v1.0 · En revisión continua</p>
      </div>'''
    cards.append(html)

print("\n".join(cards))
print(f"\n<!-- {len(cards)} escenarios generados -->", file=sys.stderr)
