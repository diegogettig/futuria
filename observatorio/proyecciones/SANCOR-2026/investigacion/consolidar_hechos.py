import os, re, json

INV = r"C:\Users\getti\Projects\FUTURIA\observatorio\proyecciones\SANCOR-2026\investigacion"
OUT = r"C:\Users\getti\Projects\FUTURIA\observatorio\proyecciones\SANCOR-2026\investigacion\CONSOLIDADO-hechos.md"

files = ["01-empresa.md", "02-entorno-arg.md", "03-tendencias-global-latam.md"]
filas = []
truncadas = []
for f in files:
    txt = open(os.path.join(INV, f), encoding="utf-8").read()
    # encontrar la primera tabla (HECHOS CON ORIGEN)
    bloques = re.split(r'\n## ', txt)
    tabla = ""
    for b in bloques:
        if "HECHOS CON ORIGEN" in b.upper()[:60]:
            tabla = b
            break
    lineas = tabla.splitlines()
    capturando = False
    for ln in lineas:
        s = ln.strip()
        if s.startswith("|") and ("Hecho" in s or "URL" in s):
            capturando = True
            continue
        if capturando:
            if s.startswith("|") and re.match(r'^\|[\s\-:|]+\|$', s):  # separador
                continue
            if s.startswith("|"):
                celdas = [c.strip() for c in s.strip("|").split("|")]
                if len(celdas) >= 4 and celdas[0].isdigit():
                    hecho, url, tier, fecha = celdas[0], celdas[2], celdas[3], celdas[4] if len(celdas) > 4 else ""
                    if "..." in url:
                        truncadas.append((f, celdas[0]))
                    filas.append((hecho, url, tier, fecha, f))
            else:
                capturando = False
print("Filas totales HECHOS CON ORIGEN:", len(filas))
print("URLs truncadas con '...':", truncadas)

# escribir consolidado
with open(OUT, "w", encoding="utf-8") as o:
    o.write("# CONSOLIDADO — HECHOS CON ORIGEN (Sancor Salud)\n\n")
    o.write("> Tabla maestra SAT-FUTURIA. Fuente: investigacion/01 (empresa), 02 (entorno AR), 03 (global/LatAm).\n\n")
    o.write("| # | Hecho (resumido) | URL origen | Tier | Fecha | Subfuente |\n")
    o.write("|---|------------------|-----------|------|-------|-----------|\n")
    for i, (h, u, t, d, src) in enumerate(filas, 1):
        o.write("| %d | %s | %s | %s | %s | %s |\n" % (i, h[:160], u, t, d, src))
print("Consolidado en:", OUT)
