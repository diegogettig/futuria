#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
FUTURIA — Observatorio · Estadio 1 (Captacion) semilla.

Extrae las tablas 'Senales Tempranas' de los 9 escenarios PRISM (.md) y las
normaliza al esquema de ficha de la biblioteca (Manual seccion 3.4).

Los 8 puntajes 0-5 se asignan por HEURISTICA TRANSPARENTE Y DOCUMENTADA
(no se inventan): se derivan del estado de madurez de la senal (emoji rojo/
amarillo/verde), del horizonte del escenario y de la posicion de la senal.
Toda ficha nace con estado 'madurando' y escalar/puntajes marcados como
PRELIMINARES para revision y firma del Chairman (Manual seccion 13.1).

Salida: observatorio/biblioteca/senales_semilla.json
"""
import glob, re, os, json, datetime

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ESC = os.path.join(RAIZ, "escenarios")
OUT = os.path.join(RAIZ, "observatorio", "biblioteca", "senales_semilla.json")

# Mapa escenario -> (id FUTURIA, dominio primario, dominios secundarios, horizonte)
META = {
    "0001": ("FUTURIA-2026-0001", "Filosofia_Etica_Cultura", ["IA_AGI", "Gobernanza_Democracia"], "2027-2035"),
    "0002": ("FUTURIA-2026-0002", "Gobernanza_Democracia", ["Blockchain_Cripto", "Economia_Trabajo"], "2026-2034"),
    "0003": ("FUTURIA-2026-0003", "Biotech_Salud", ["IA_AGI", "Fisica_Materiales"], "2026-2035"),
    "0004": ("FUTURIA-2026-0004", "Computo_Hardware", ["Geopolitica_Soberania", "Fisica_Materiales"], "2026-2038"),
    "0005": ("FUTURIA-2026-0005", "Gobernanza_Democracia", ["IA_AGI", "Blockchain_Cripto"], "2026-2035"),
    "0006": ("FUTURIA-2026-0006", "Biotech_Salud", ["Economia_Trabajo", "IA_AGI"], "2026-2038"),
    "0007": ("FUTURIA-2026-0007", "IA_AGI", ["Neurociencia", "Filosofia_Etica_Cultura"], "2026-2038"),
    "0008": ("FUTURIA-2026-0008", "Biotech_Salud", ["Fisica_Materiales", "Geopolitica_Soberania"], "2026-2038"),
    "0009": ("FUTURIA-2026-0009", "Geopolitica_Soberania", ["IA_AGI", "Computo_Hardware"], "2026-2038"),
}

# Heuristica de puntajes por estado de madurez (emoji en columna 'estado actual')
# (credibilidad, corroboracion, novedad, velocidad, alcance)
ESTADO_PUNTAJES = {
    "verde":    dict(credibilidad=4, corroboracion=4, novedad=2, velocidad=4, alcance=4),  # ya ocurriendo
    "amarillo": dict(credibilidad=3, corroboracion=3, novedad=4, velocidad=3, alcance=3),  # en curso
    "rojo":     dict(credibilidad=2, corroboracion=2, novedad=5, velocidad=2, alcance=3),  # no detectado
}

def clasif_estado(texto):
    if "🟢" in texto: return "verde", "activa"
    if "🔴" in texto: return "rojo", "madurando"
    return "amarillo", "madurando"

def extract_signals(path):
    txt = open(path, encoding="utf-8").read()
    m = re.search(r'SE[ÑN]ALES TEMPRANAS.*?\n(.*?)(?=\n##\s|\Z)', txt, re.S | re.I)
    if not m: return []
    rows = []
    for line in m.group(1).splitlines():
        line = line.strip()
        if not line.startswith("|"): continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 2: continue
        if set(cells[0].replace("-", "").replace(":", "")) <= set(" "): continue
        if "fuente" in " ".join(cells).lower() and cells[0].lower().startswith(("se", "señ", "sen")):
            continue
        rows.append(cells)
    return rows

def profundidad_por_dominio(dom_primario, dom_sec):
    # profundidad/convergencia/irreversibilidad segun peso estructural del dominio
    estructurales = {"Computo_Hardware", "Geopolitica_Soberania", "IA_AGI", "Gobernanza_Democracia"}
    prof = 5 if dom_primario in estructurales else 4
    conv = 3 + min(2, len(dom_sec))  # mas dominios secundarios = mas convergencia
    irr = 4 if dom_primario in {"Computo_Hardware", "Biotech_Salud", "Geopolitica_Soberania"} else 3
    return prof, conv, irr

def main():
    files = sorted(glob.glob(os.path.join(ESC, "PRISM-2026-000[1-9]-*.md")))
    fichas = []
    contador = 1
    hoy = datetime.date.today().isoformat()
    for f in files:
        num = re.search(r'PRISM-2026-(\d{4})', f).group(1)
        esc_id, dom_p, dom_s, horizonte = META[num]
        rows = extract_signals(f)
        for r in rows:
            titulo = r[0]
            fuente_txt = r[1] if len(r) > 1 else ""
            umbral = r[2] if len(r) > 2 else ""
            estado_txt = r[3] if len(r) > 3 else (r[-1] if len(r) > 1 else "")
            nivel, estado = clasif_estado(estado_txt)
            base = ESTADO_PUNTAJES[nivel]
            prof, conv, irr = profundidad_por_dominio(dom_p, dom_s)
            puntajes = dict(base, profundidad=prof, convergencia=conv, irreversibilidad=irr)
            sig_id = "SIG-2026-%05d" % contador
            fichas.append({
                "id": sig_id,
                "fecha_captura": hoy,
                "titulo": titulo,
                "descripcion": ("Indicador temprano del escenario %s. Umbral de activacion: %s"
                                % (esc_id, umbral or "s/d")),
                "dominio_primario": dom_p,
                "dominios_secundarios": dom_s,
                "tipo": "cuestion_emergente" if nivel != "verde" else "tendencia",
                "fuentes": [{"url": "", "editor": fuente_txt, "tier": "T2"}],
                "puntajes": puntajes,
                "IRS": None, "PS": None,
                "horizonte": horizonte,
                "contra_senal": "PENDIENTE — completar en revision (obligatorio antes de escalar).",
                "escenarios_vinculados": [esc_id],
                "senales_relacionadas": [],
                "estado": estado,
                "estado_maduracion_original": estado_txt,
                "umbral_activacion": umbral,
                "escalar_a_humano": None,
                "_origen": "semilla_extraccion_escenarios",
                "_puntajes_preliminares": True,
            })
            contador += 1
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump({"generado": hoy, "fuente": "extraccion tablas Senales Tempranas 9 escenarios PRISM",
                   "nota": "Puntajes PRELIMINARES por heuristica; requieren revision del Chairman. Contra-senales pendientes.",
                   "total": len(fichas), "senales": fichas}, fh, ensure_ascii=False, indent=2)
    print("Extraidas %d senales -> %s" % (len(fichas), OUT))

if __name__ == "__main__":
    main()
