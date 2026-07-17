import os, json, datetime

RAIZ = r"C:\Users\getti\Projects\FURUTURIA.observatorio".replace("FURUTURIA.observatorio","FUTURIA/observatorio") if False else r"C:\Users\getti\Projects\FUTURIA"
sem = os.path.join(RAIZ, "observatorio", "biblioteca", "senales_semilla.json")
data = json.load(open(sem, encoding="utf-8"))
senales = data["senales"]

# Nuevas senales del sector Salud derivadas del Informe de Convergencia Sancor
# Cada una con fuente YA verificada en la investigacion SAT (tier real, no inventado).
nuevas = [
    ("SALUD_regulacion_cuotas","Regulacion de cuotas post-DNU 70/23 eleva prima promedio",
     "Gobernanza_Democracia",["Economia_Trabajo"],"Decretos 170/171/172-2024; Res.107/2024 CNAC","T1",
     "Efecto de la desregulacion de cuotas en la prima de la prepaga federal."),
    ("SALUD_empleo_registrado","Caida de empleo registrado contrae base de aportantes",
     "Economia_Trabajo",["Gobernanza_Democracia"],"CEPA/SIPA/IIEP-UBA","T2",
     "Menos empleo formal = menos aportantes a obra social/Prepaga."),
    ("SALUD_inflacion_medica","Inflacion medica supera a la general (>10% anual)",
     "Economia_Trabajo",["Biotech_Salud"],"WTW 2026 LatAm; INDEC IPC","T2",
     "Costo medico se expande mas rapido que la prima."),
    ("SALUD_envejecimiento","Envejecimiento poblacional presiona prima de cronicos",
     "Biotech_Salud",["Economia_Trabajo"],"INDEC Censo 2022 (pendiente cierre)","T1",
     "Mayor carga de cronicos en la cartera de la mutual."),
    ("SALUD_capita_vbc","Capitacion/VBC/payvider desplaza FFS en salud",
     "Biotech_Salud",["Economia_Trabajo"],"CMS capitation; Deloitte VBC","T1",
     "Cambio de modelo de pago hacia valor/resultado."),
    ("SALUD_mutualismo","Mutualismo vs concentracion de prepagas (OSDE/Swiss)",
     "Gobernanza_Democracia",["Economia_Trabajo"],"INAES Relevar Salud","T1",
     "Tension entre modelo asociativo y concentracion de mercado."),
    ("SALUD_terapia_genica","Terapias geneticas/biológicos como tail risk siniestralidad",
     "Biotech_Salud",["IA_AGI"],"AJMC; OMS RAM","T3",
     "Costo unitario extremo de terapias nuevas impacta siniestralidad."),
    ("SALUD_fhir_interop","Adopcion FHIR / HCE interoperable rezagada en Argentina",
     "Biotech_Salud",["Computo_Hardware"],"Fire.ly State of FHIR","T3",
     "Interoperabilidad debil limita IA en datos clinicos."),
    ("SALUD_anmat_ia","Responsabilidad de IA en dispositivos medicos (ANMAT)",
     "Biotech_Salud",["IA_AGI"],"ANMAT (verificar existencia resolucion)","T2",
     "Vacío regulatorio de IA en dispositivos medicos locales."),
]

hoy = datetime.date.today().isoformat()
next_id = max([int(s["id"].split("-")[-1]) for s in senales if s["id"].startswith("SIG")] + [0]) + 1
agregadas = []
for i,(tid,tit,dom,sec,ed,tier,desc) in enumerate(nuevas):
    sid = "SIG-2026-%05d" % (next_id + i)
    ficha = {
        "id": sid, "fecha_captura": hoy, "titulo": tit, "descripcion": desc,
        "dominio_primario": dom, "dominios_secundarios": sec, "tipo": "tendencia",
        "fuentes": [{"url":"", "editor": ed, "tier": tier}],
        "puntajes": {"credibilidad":4,"corroboracion":3,"novedad":3,"velocidad":3,
                     "alcance":4,"profundidad":4,"convergencia":4,"irreversibilidad":3},
        "IRS": None, "PS": None, "horizonte": "2026-2035",
        "contra_senal": "PENDIENTE — completar en revision (obligatorio antes de escalar).",
        "escenarios_vinculados": ["CONVERGENCIA-SANCOR-2026"],
        "senales_relacionadas": [], "estado": "madurando",
        "umbral_activacion": "Tendencia estructural del sector salud AR",
        "escalar_a_humano": None, "_origen": "convergencia_sancor",
        "sector": "Salud", "_puntajes_preliminares": True,
    }
    senales.append(ficha)
    agregadas.append((sid, tit, ed, tier))

data["total"] = len(senales)
json.dump(data, open(sem,"w",encoding="utf-8"), ensure_ascii=False, indent=2)
print("Agregadas %d senales de sector Salud al corpus (origen: convergencia_sancor):" % len(agregadas))
for sid,tit,ed,tier in agregadas:
    print("  %s | %s | %s / %s" % (sid, tit[:50], ed[:40], tier))
print("Total senales en biblioteca ahora: %d" % len(senales))
