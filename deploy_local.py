#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pasos de despliegue LOCAL (no toca servidores externos).
1. Renderiza los 10 escenarios v1.0 (YAML -> HTML) en testing/escenarios.
2. Copia los .html generados a plataforma/escenarios/.
3. Copia la metodologia HTML a plataforma/metodologia/ (para enlazar en prod).
4. Regenera las cards de la landing y reemplaza el bloque escenarios-grid en index.html.
Uso: python deploy_local.py   (desde raiz del repo)
El deploy a produccion (Cloudflare Pages / Vercel) lo ejecuta el usuario con su mecanismo.
"""
import sys, pathlib, shutil, yaml, re, subprocess

ROOT = pathlib.Path(__file__).resolve().parent
SCEN = ROOT / "testing" / "escenarios"
PLAT = ROOT / "plataforma"
PLAT_ESC = PLAT / "escenarios"
PLAT_MET = PLAT / "metodologia"
PY = r"C:\Users\getti\AppData\Roaming\uv\python\cpython-3.11.15-windows-x86_64-none\python.exe"

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

PLAT_ESC.mkdir(parents=True, exist_ok=True)
PLAT_MET.mkdir(parents=True, exist_ok=True)

print("== 1. Renderizando escenarios ==")
for base in ORDER:
    yml = SCEN / f"{base}.yaml"
    if not yml.exists():
        print(f"  [SKIP] falta {base}.yaml")
        continue
    r = subprocess.run([PY, str(SCEN/"render_prism.py"), base], cwd=str(SCEN),
                       capture_output=True, text=True)
    if r.returncode != 0:
        print(f"  [ERROR] {base}: {r.stderr[-300:]}")
    else:
        print(f"  [OK] {base}")

print("== 2. Copiando HTML a plataforma/escenarios ==")
for base in ORDER:
    src = SCEN / f"{base}.html"
    if src.exists():
        shutil.copy(src, PLAT_ESC / f"{base}.html")
        print(f"  [OK] {base}.html")

print("== 2b. Copiando assets (imagenes) a plataforma/escenarios/assets ==")
assets_src = SCEN / "assets"
if assets_src.exists():
    dst = PLAT_ESC / "assets"
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(assets_src, dst)
    n = sum(len(f) for _, _, f in os.walk(dst))
    print(f"  [OK] assets -> {n} archivos")
else:
    print("  [WARN] no existe testing/escenarios/assets")

print("== 3. Copiando metodologia HTML ==")
met_src = ROOT / "metodologia" / "plausibilidad-metodologia.html"
if met_src.exists():
    shutil.copy(met_src, PLAT_MET / "plausibilidad-metodologia.html")
    print("  [OK] plausibilidad-metodologia.html")
idx_src = ROOT / "metodologia" / "index.html"
if idx_src.exists():
    shutil.copy(idx_src, PLAT_MET / "index.html")
    print("  [OK] metodologia/index.html")

print("== 4. Regenerando cards de la landing ==")
cards = []
for base in ORDER:
    yml = SCEN / f"{base}.yaml"
    if not yml.exists():
        continue
    d = yaml.safe_load(yml.read_text(encoding="utf-8"))
    e = d["escenario"]
    pl = e.get("plausibilidad", {})
    pt = pl.get("puntuacion_total", 0)
    ht = e.get("horizonte_temporal", {})
    rango = ht.get("rango", "")
    titulo = e.get("titulo", "")
    res = e.get("resumen_ejecutivo", "") or ""
    desc = res.split(". ")[0]
    if len(desc) > 180:
        desc = desc[:177] + "..."
    def esc(s): return str(s).replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
    cards.append(f'''      <div class="card">
        <div class="tag">Escenario PRISM v1.0</div>
        <h3>{esc(titulo)}</h3>
        <p>Horizonte {esc(rango)} · Plausibilidad {pt}/100</p>
        <p style="margin-top:0.6rem;">{esc(desc)}</p>
        <a href="escenarios/{base}.html" target="_blank" rel="noopener" class="btn btn-primary" style="margin-top:0.8rem;padding:0.55rem 1.1rem;font-size:0.85rem;">Leer escenario completo →</a>
        <p style="margin-top:0.6rem;font-size:0.85rem;color:var(--muted);">Metodología PRISM v1.0 · En revisión continua</p>
      </div>''')

idx = PLAT / "index.html"
html = idx.read_text(encoding="utf-8")
new_block = "\n".join(cards)
# Reemplaza todo lo que este entre <div class="grid-2" id="escenarios-grid"> y su </div> de cierre
pat = re.compile(r'(<div class="grid-2" id="escenarios-grid">).*?(</div>\s*</section>)', re.S)
new_html, n = pat.subn(lambda m: m.group(1) + "\n" + new_block + "\n    " + m.group(2), html)
if n:
    idx.write_text(new_html, encoding="utf-8")
    print(f"  [OK] {n} bloque de cards reemplazado ({len(cards)} escenarios)")
else:
    print("  [WARN] no se encontro el bloque escenarios-grid")

print("== Listo. Pendiente: deploy a produccion por el usuario. ==")
