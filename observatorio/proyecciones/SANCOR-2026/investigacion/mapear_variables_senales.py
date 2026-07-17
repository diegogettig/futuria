import os, json, re

RAIZ = r"C:\Users\getti\Projects\FUTURIA"
sem = os.path.join(RAIZ, "observatorio", "biblioteca", "senales_semilla.json")
data = json.load(open(sem, encoding="utf-8"))
senales = data["senales"]

# Variables del negocio de Sancor Salud (del estudio del cliente ya verificado)
variables = {
    "V1_regulacion_precios": "Desregulacion de cuotas (DNU 70/23) y cartelizacion 2024",
    "V2_empleo_registrado": "Base de aportantes depende de empleo formal (caida 2023-2026)",
    "V3_costos_medicos": "Inflacion medica > general; tecnologia y medicamentos alto costo",
    "V4_envejecimiento": "Envejecimiento poblacional + cronicos presionan prima",
    "V5_ia_siniestralidad": "IA en diagnostico/claims reduce o dispara siniestralidad",
    "V6_modelos_negocio": "FFS->capitacion/VBC/payvider; telemed+RPM",
    "V7_mutualismo": "Modelo mutual/cooperativo vs concentracion OSDE/Swiss",
    "V8_alto_costo": "Terapias geneticas/biológicos como tail risk de siniestralidad",
    "V9_interop": "HCE interoperable (FHIR) rezagada en Argentina",
    "V10_personalidad_ia": "Responsabilidad juridica de IA en salud (eje PRISM #001)",
}

# Mapeo heuristico: palabras clave en titulo/desc/dominios de cada senal
kw = {
    "V1_regulacion_precios": ["regul", "cuota", "cartel", "precio", "desregul", "competencia"],
    "V2_empleo_registrado": ["empleo", "trabajo", "formal", "aport", "seguro social"],
    "V3_costos_medicos": ["costo", "inflac", "medic", "tecnolog", "farmaco", "precio"],
    "V4_envejecimiento": ["envejec", "demograf", "cronic", "geriatr", "poblacion"],
    "V5_ia_siniestralidad": ["ia", "agente", "algoritm", "diagnost", "automat", "siniestr"],
    "V6_modelos_negocio": ["capitac", "value", "payvider", "telemed", "prevenc", "modelo"],
    "V7_mutualismo": ["mutu", "cooper", "asociativ", "social"],
    "V8_alto_costo": ["gen", "biolog", "terapia", "farmaco", "alto costo", "raro"],
    "V9_interop": ["interoper", "fhir", "historia clinic", "hce", "dato"],
    "V10_personalidad_ia": ["personalidad", "jurid", "responsab", "agente ia", "derecho"],
}

def score(s, kws):
    txt = (s.get("titulo","") + " " + s.get("descripcion","") + " " + " ".join(s.get("dominios_secundarios",[])) + " " + s.get("dominio_primario","")).lower()
    return sum(1 for k in kws if k in txt)

mapeo = {v: [] for v in variables}
for s in senales:
    for v, kws in kw.items():
        if score(s, kws) >= 2:
            mapeo[v].append((s["id"], s.get("titulo","")[:55], s.get("IRS"), s.get("dominio_primario")))

print("=== MAPEO VARIABLES SANCOR -> SENALES DEL CORPUS ===\n")
for v, desc in variables.items():
    print("## %s — %s" % (v, desc))
    if mapeo[v]:
        for sid, tit, irs, dom in mapeo[v][:6]:
            print("   - %s | IRS %s | %s | %s" % (sid, irs, dom, tit))
    else:
        print("   (sin senal directa en corpus — REQUIERE nueva captura en Flujo 1)")
    print()

tot_mapeadas = sum(len(v) for v in mapeo.values())
print("Total de vinculos variable->senal: %d" % tot_mapeadas)
print("Variables sin senal en corpus: %d" % sum(1 for v in mapeo.values() if not v))
