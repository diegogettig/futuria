import os, re

INV = r"C:\Users\getti\Projects\FUTURIA\observatorio\proyecciones\SANCOR-2026\investigacion"
OUT = r"C:\Users\getti\Projects\FUTURIA\observatorio\proyecciones\SANCOR-2026\investigacion\CONSOLIDADO-hechos.md"

# Escala unica de tiers (normalizada del Auditor)
LEYENDA = """**Escala de Tier (normalizada SAT-FUTURIA):**
- **T1** = Oficial / regulatoria / primaria (Boletín Oficial, SSS, INDEC, OMS/OPS, CMS, Banco Mundial, sitio oficial de la empresa, reportes RSE propios).
- **T2** = Prensa especializada / académica / consultoría (DiagnosticsNews, Informe Operadores, McKinsey, Deloitte, WEF, Grand View, CMS citing).
- **T3** = Prensa general / medios / marketplaces / redes sociales (frágil como evidencia primaria; usada solo como indicio).
- **T4** = Fuente secundaria mixta / paper académico citado sin URL primaria (se marca expresamente).
"""

files = ["01-empresa.md", "02-entorno-arg.md", "03-tendencias-global-latam.md"]
filas = []
for f in files:
    txt = open(os.path.join(INV, f), encoding="utf-8").read()
    bloques = re.split(r'\n## ', txt)
    tabla = ""
    for b in bloques:
        if "HECHOS CON ORIGEN" in b.upper()[:60]:
            tabla = b
            break
    capturando = False
    for ln in tabla.splitlines():
        s = ln.strip()
        if s.startswith("|") and ("Hecho" in s or "URL" in s):
            capturando = True
            continue
        if capturando:
            if s.startswith("|") and re.match(r'^\|[\s\-:|]+\|$', s):
                continue
            if s.startswith("|"):
                celdas = [c.strip() for c in s.strip("|").split("|")]
                if len(celdas) >= 4 and celdas[0].isdigit():
                    hecho, url, tier, fecha = celdas[0], celdas[2], celdas[3], (celdas[4] if len(celdas) > 4 else "")
                    # normalizar etiqueta de tier (quitar texto extra entre parentesis)
                    tier_clean = re.sub(r'\s*\(.*?\)', '', tier).strip()
                    if tier_clean not in ("T1", "T2", "T3", "T4"):
                        tier_clean = "T3"  # default conservador si ambiguo
                    filas.append((hecho, url, tier_clean, fecha))
            else:
                capturando = False

with open(OUT, "w", encoding="utf-8") as o:
    o.write("# CONSOLIDADO — HECHOS CON ORIGEN (Grupo SanCor Salud)\n\n")
    o.write("> Tabla maestra SAT-FUTURIA. Fuente: investigacion/01 (empresa), 02 (entorno AR), 03 (global/LatAm).\n> Toda afirmacion del informe final debe remitir a un n° de esta tabla.\n\n")
    o.write(LEYENDA + "\n")
    o.write("| # | Hecho (texto completo) | URL origen | Tier | Fecha |\n")
    o.write("|---|------------------------|-----------|------|-------|\n")
    for i, (h, u, t, d) in enumerate(filas, 1):
        o.write("| %d | %s | %s | %s | %s |\n" % (i, h, u, t, d))
    o.write("\n> **Advertencia del Auditor:** las cifras de *market share* y *afiliados por empresa* de T3 (prensa) deben confirmarse contra los datasets oficiales de la SSS (T1) antes de usarlas en proyección cuantitativa.\n")
print("Consolidado regenerado:", len(filas), "filas, tiers normalizados")
