#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
FUTURIA - Laboratorio de Vigilancia Tecnologica (Flujo 1, diario)
Pipeline diario: Estadio 1 (extraer semilla) -> Estadio 2 (calificar IES/PS)
-> Informe general de Convergencia / Newsletter del dia.

Metodologia vigente: METODOLOGIA-FUTURIA-v1.0.md (IRS retirado; IES + PS ortogonales,
matriz Evidencia x Peso con cuadrantes Q1/Q2/Q3/Q4, corte 60/60).

Regla SAT-FUTURIA: todo dato del informe remite a senal con fuente (editor/tier).
No inventa senales: solo reprocesa el corpus de escenarios PRISM existente.
Salida: observatorio/informes-diarios/INFORME-DIARIO-YYYY-MM-DD.md
"""
import os, sys, json, datetime, subprocess

RAIZ = r"C:\Users\getti\Projects\FUTURIA"
MOTOR = os.path.join(RAIZ, "observatorio", "motor")
OUT_DIR = os.path.join(RAIZ, "observatorio", "informes-diarios")
SEMILLA = os.path.join(RAIZ, "observatorio", "biblioteca", "senales_semilla.json")

def run(cmd):
    if isinstance(cmd, str):
        cmd = [sys.executable, cmd]
    else:
        cmd = [sys.executable] + cmd
    r = subprocess.run(cmd, cwd=RAIZ, capture_output=True, text=True)
    print(r.stdout.strip())
    if r.returncode != 0:
        print("ERR", r.stderr.strip()[:400])
    return r.returncode == 0

def main():
    hoy = datetime.date.today()
    ymd = hoy.isoformat()
    print("=== LAB VIGILANCIA DIARIO %s ===" % ymd)

    # Estadio 1 + 2
    ok1 = run([os.path.join(MOTOR, "extraer_semilla.py")])
    ok2 = run([os.path.join(MOTOR, "motor_calificacion.py"), "--score", SEMILLA])

    # Cargar senales calificadas
    try:
        data = json.load(open(SEMILLA, encoding="utf-8"))
    except Exception as e:
        print("No se pudo leer semilla:", e); return 1
    senales = data.get("senales", [])

    # Detectar schema del corpus: v1.0 (IES+PS+cuadrante) o legacy (IRS)
    es_v1 = any(("IES" in s or "cuadrante" in s) for s in senales)
    escal = [s for s in senales if s.get("escalar_a_humano")]
    madur = [s for s in senales if s.get("estado_relevancia") == "en_maduracion"]

    if es_v1:
        prio = [s for s in senales if s.get("cuadrante") in ("Q1", "Q2")]
        orden = lambda s: -(s.get("PS") or 0)
        col_ies, col_ps, col_q = "IES", "PS", "Cuadrante"
        meta = "> Metodologia vigente: v1.0 (IES + PS; matriz Evidencia x Peso; cuadrantes Q1-Q4)."
        nota = "> Nota (v1.0): relevamiento de FUENTES NUEVAS como Estadio 0; recalcula IES/PS/cuadrante. IRS deprecado.\n"
        res_prio = "- Drivers activos / cartas salvajes (Q1+Q2): **%d**" % len(prio)
        tit_prio = "## Senales prioritarias (Q1 Driver Activo + Q2 Carta Salvaje)\n"
        def fmt_prio(s, f):
            return "| %s | %s | %s | %s | %s | %s | %s / %s |" % (
                s.get("id"), s.get("titulo","")[:60], s.get("dominio_primario"),
                s.get("IES"), s.get("PS"), s.get("cuadrante"), f.get("editor",""), f.get("tier",""))
        def fmt_esc(s):
            return "- %s — %s (IES %s / PS %s / %s)" % (s.get("id"), s.get("titulo","")[:70], s.get("IES"), s.get("PS"), s.get("cuadrante"))
    else:
        # MODO LEGACY: el motor aun no migra a v1.0 (brecha #6). No romper el Lab.
        prio = [s for s in senales if s.get("estado_relevancia") == "prioritaria"]
        orden = lambda s: -(s.get("IRS") or 0)
        col_ies, col_ps, col_q = "IRS", "PS", "Estado"
        meta = "> Metodologia: v0.9 LEGACY — motor sin migrar a v1.0 (brecha #6). IRS vigente hasta migrar motor."
        nota = "> Pendiente: migrar motor_calificacion.py a IES+PS+cuadrantes (METODOLOGIA-FUTURIA-v1.0.md §11, brecha #6).\n"
        res_prio = "- Prioritarias (IRS>=70): **%d**" % len(prio)
        tit_prio = "## Senales prioritarias\n"
        def fmt_prio(s, f):
            return "| %s | %s | %s | %s | %s | %s | %s / %s |" % (
                s.get("id"), s.get("titulo","")[:60], s.get("dominio_primario"),
                s.get("IRS"), s.get("PS"), s.get("estado_relevancia"), f.get("editor",""), f.get("tier",""))
        def fmt_esc(s):
            return "- %s — %s (IRS %s / PS %s)" % (s.get("id"), s.get("titulo","")[:70], s.get("IRS"), s.get("PS"))

    os.makedirs(OUT_DIR, exist_ok=True)
    out = os.path.join(OUT_DIR, "INFORME-DIARIO-%s.md" % ymd)
    L = []
    L.append("# INFORME DIARIO DE CONVERGENCIA - FUTURIA\n")
    L.append("> **Laboratorio de Vigilancia Tecnologica (Flujo 1).** Fecha: %s." % ymd)
    L.append("> Sistema SAT-FUTURIA: toda senal remite a su fuente (editor / tier). Corpus base: 9 escenarios PRISM.")
    L.append(meta)
    L.append("> Documento de trabajo interno del Instituto. No es entregable de cliente.\n")
    L.append("## Resumen del dia\n")
    L.append("- Senales en biblioteca: **%d**" % len(senales))
    L.append(res_prio)
    L.append("- En maduracion: **%d**" % len(madur))
    L.append("- Escaladas a revision humana: **%d**\n" % len(escal))
    L.append(nota)
    L.append(tit_prio)
    L.append("| ID | Titulo | Dominio | %s | %s | %s | Fuente (editor/tier) |" % (col_ies, col_ps, col_q))
    L.append("|----|--------|---------|-----|----|-----------|----------------------|")
    for s in sorted(prio, key=orden)[:15]:
        f = s.get("fuentes", [{}])[0]
        L.append(fmt_prio(s, f))
    L.append("\n## Escaladas a revision humana (requieren firma Chairman)\n")
    for s in escal[:15]:
        L.append(fmt_esc(s))
    L.append("\n---\n*Generado automaticamente por el Laboratorio de Vigilancia. Ver %s para auditoria.*" % os.path.relpath(SEMILLA, RAIZ))
    open(out, "w", encoding="utf-8").write("\n".join(L))
    print("Informe diario ->", out)
    return 0

if __name__ == "__main__":
    sys.exit(main())
