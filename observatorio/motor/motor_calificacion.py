#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
FUTURIA - Observatorio de Vigilancia Estrategica
Motor de calificacion de senales (Estadio 2).

Implementa las formulas del Manual de Metodologia v1.0, seccion 3:
  IES (Indice de Evidencia de Senal, 0-100)  -> sustituye al IRS deprecado
  PS  (Peso Sistemico, 0-100)                -> formula idéntica a v0.9
  cuadrante (Q1/Q2/Q3/Q4)                    -> matriz Evidencia x Peso, corte 60/60

Uso:
  python motor_calificacion.py --self-test          # valida contra ejemplo del manual
  python motor_calificacion.py --score biblioteca/senales.json   # recalcula un archivo

No inventa datos: solo calcula a partir de los 8 puntajes 0-5 de cada ficha.

Brecha #6 (METODOLOGIA-FUTURIA-v1.0.md §11): migracion IRS -> IES + PS + cuadrante.
El IRS queda deprecado; si se invoca, el motor emite WARNING y no lo recalcula.
"""
import json
import sys
import argparse
import warnings

# Pesos IES (seccion 3.1). Suman 100.
# IES NO usa profundidad/convergencia/irreversibilidad (esas dimensiones son del PS).
IES_PESOS = {
    "credibilidad":    30,
    "corroboracion":   20,
    "novedad":         15,
    "velocidad":       20,
    "alcance":         15,
}

# Pesos PS (seccion 3.1). Suman 100. Formula IDENTICA a v0.9.
PS_PESOS = {
    "profundidad":      40,
    "convergencia":     35,
    "irreversibilidad": 25,
}

# Umbral de corte de la matriz Evidencia x Peso (seccion 3.3)
CORTE = 60

# --- Compat legacy (v0.9): el pipeline sigue leyendo estado_relevancia para el resumen. ---
# Mapeo cuadrante -> estado_relevancia (solo para no romper el resumen del pipeline).
_CUADRANTE_A_ESTADO = {
    "Q1": "prioritaria",
    "Q2": "prioritaria",
    "Q3": "en_maduracion",
    "Q4": "archivo",
}


def calcular_ies(p):
    """IES = sum( puntaje_i/5 * peso_i ) para las 5 dimensiones de evidencia. Entero."""
    total = 0.0
    for dim, peso in IES_PESOS.items():
        val = p.get(dim)
        if val is None:
            raise ValueError("Falta dimension '%s' en puntajes" % dim)
        if not (0 <= val <= 5):
            raise ValueError("Dimension '%s'=%s fuera de rango 0-5" % (dim, val))
        total += (val / 5.0) * peso
    return int(round(total))


def calcular_ps(p):
    """PS = profundidad*40% + convergencia*35% + irreversibilidad*25% (cada uno 0-100). Entero."""
    total = 0.0
    for dim, peso in PS_PESOS.items():
        val = p.get(dim)
        if val is None:
            raise ValueError("Falta dimension '%s' en puntajes" % dim)
        if not (0 <= val <= 5):
            raise ValueError("Dimension '%s'=%s fuera de rango 0-5" % (dim, val))
        total += (val / 5.0) * peso
    return int(round(total))


def cuadrante(ies, ps):
    """Matriz Evidencia (IES) x Peso (PS), corte 60/60 (seccion 3.3)."""
    if ies >= CORTE and ps >= CORTE:
        return "Q1"   # DRIVER ACTIVO
    if ies < CORTE and ps >= CORTE:
        return "Q2"   # CARTA SALVAJE
    if ies >= CORTE and ps < CORTE:
        return "Q3"   # RUIDO CONFIRMADO
    return "Q4"       # DESCARTE


def debe_escalar(ies, ps, ficha=None):
    """Escala a humano si Q1 o Q2, o si la mejor fuente es T4 (regla de fichado),
    o si tasa_base aplica y es <30% con PS>=60 (seccion 3.3)."""
    q = cuadrante(ies, ps)
    if q in ("Q1", "Q2"):
        return True
    if ficha:
        tiers = [f.get("tier", "T4") for f in ficha.get("fuentes", [])]
        mejor = min([int(t[1]) for t in tiers if t and t[0] == "T"] or [4])
        if mejor >= 4:  # solo T4 disponible
            return True
        tb = ficha.get("tasa_base") or {}
        if tb.get("aplica") and isinstance(tb.get("estimacion"), (int, float)) \
           and tb["estimacion"] < 30 and ps >= CORTE:
            return True
    return False


def calificar_ficha(ficha):
    """Recalcula IES, PS, cuadrante, estado_relevancia y escalar_a_humano. Muta y devuelve.

    Si la ficha trae 'IRS' (legacy v0.9), se ignora y se emite WARNING: el IRS esta
    deprecado en v1.0 (seccion 3.1).
    """
    if "IRS" in ficha:
        warnings.warn("IRS deprecado en v1.0: la ficha %s traia IRS; se ignora y se calcula IES."
                      % ficha.get("id", "?"), DeprecationWarning, stacklevel=2)

    p = ficha["puntajes"]
    ies = calcular_ies(p)
    ps = calcular_ps(p)
    q = cuadrante(ies, ps)

    ficha["IES"] = ies
    ficha["PS"] = ps
    ficha["cuadrante"] = q
    ficha["estado_relevancia"] = _CUADRANTE_A_ESTADO[q]   # compat pipeline (resumen)
    ficha["escalar_a_humano"] = debe_escalar(ies, ps, ficha)

    # validacion de integridad de fichado (seccion 3.4)
    faltas = []
    if not ficha.get("contra_senal", "").strip():
        faltas.append("contra_senal_vacia")
    if not ficha.get("fuentes"):
        faltas.append("sin_fuentes")
    ficha["_integridad"] = "ok" if not faltas else faltas
    return ficha


def self_test():
    """Valida contra el ejemplo trabajado del manual (seccion 3.1 / 4.3): IES~72, PS=90.

    NOTA de erratum del manual: el texto dice 'IES = 70', pero aplicando su propia
    formula literal (cred 4->24, corr 3->12, nov 4->12, vel 3->12, alc 4->12 = 72) da 72.
    El motor respeta la formula literal, no el total mal sumado (igual que con el IRS
    en v0.9, donde el manual decia 74.7 y la formula da 79.8). PS=90 es correcto.
    """
    ejemplo = {
        "credibilidad": 4, "corroboracion": 3, "novedad": 4, "velocidad": 3,
        "alcance": 4, "profundidad": 5, "convergencia": 5, "irreversibilidad": 3,
    }
    ies = calcular_ies(ejemplo)
    ps = calcular_ps(ejemplo)
    q = cuadrante(ies, ps)
    print("SELF-TEST (ejemplo manual 3.1/4.3 - Proyecto Pampa GPU soberano):")
    print("  IES calculado: %s   (formula literal; manual dice 70 por erratum)" % ies)
    print("  PS  calculado: %s   (esperado 90.0)" % ps)
    print("  Cuadrante:      %s   (esperado Q1)" % q)
    ok_ies = abs(ies - 72) < 0.5
    ok_ps = abs(ps - 90) < 0.5
    ok_q = q == "Q1"
    print("  IES %s | PS %s | Q %s" % ("OK" if ok_ies else "FALLA",
                                        "OK" if ok_ps else "FALLA",
                                        "OK" if ok_q else "FALLA"))
    if ok_ies:
        print("  (Erratum manual 3.1: dice 70; la suma correcta de su formula es 72)")
    return ok_ies and ok_ps and ok_q


def score_file(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    fichas = data if isinstance(data, list) else data.get("senales", [])
    for ficha in fichas:
        calificar_ficha(ficha)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    prio = [x for x in fichas if x.get("cuadrante") in ("Q1", "Q2")]
    escaladas = [x for x in fichas if x.get("escalar_a_humano")]
    q_counts = {q: sum(1 for x in fichas if x.get("cuadrante") == q) for q in ("Q1", "Q2", "Q3", "Q4")}
    print("Recalculadas %d fichas en %s" % (len(fichas), path))
    print("  Cuadrantes -> Q1:%d Q2:%d Q3:%d Q4:%d" % (q_counts["Q1"], q_counts["Q2"], q_counts["Q3"], q_counts["Q4"]))
    print("  Drivers/cartas (Q1+Q2): %d" % len(prio))
    print("  Escaladas a humano:     %d" % len(escaladas))
    return fichas


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--score", metavar="ARCHIVO.json")
    args = ap.parse_args()
    if args.self_test:
        sys.exit(0 if self_test() else 1)
    elif args.score:
        score_file(args.score)
    else:
        ap.print_help()
