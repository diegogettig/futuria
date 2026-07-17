# FUTURIA — Template Formal PRISM v1.0

## Instrucciones de uso
Este documento define la estructura canónica de todo escenario PRISM.
Cumplirlo es obligatorio antes de publicación.
Cualquier desviación debe ser justificada y aprobada por AUDITOR.

Versión: 1.0
Mantenido por: CURADOR + AUDITOR
Próxima revisión del template: Diciembre 2026

---

## Estructura YAML canónica

Cada escenario PRISM se escribe como un documento YAML con la siguiente estructura.

> **NOTA:** Las líneas que comienzan con `#` son comentarios y NO deben incluirse en el archivo final.
> Los campos `null` indican ausencia de valor y DEben escribirse explícitamente como `null`.
> Los arrays vacíos `[]` también son válidos cuando no aplican.

```yaml
escenario:
  id: "FUTURIA-YYYY-NNNN"          # Formato: AÑO + número secuencial de 4 dígitos
  titulo: ""                        # Título descriptivo. Máximo 80 caracteres.
  eje_tematico: ""                  # Eje principal. Ver lista oficial de ejes en PLAN-ESTRATEGICO.md
  tipo:                             # Clasificación tipológica — al menos uno obligatorio
    - continuista                    # Extrapolación de tendencias actuales
  # - distopico                     # Resultado negativo no deseado
  # - utopico                       # Resultado positivo optimista
  # - disruptivo                    # Cambio de paradigma
  # - mixto                         # Combinación de elementos

  estado: [borrador | en_revision | verificado | publicada | archivada]

  # ─── SECCIÓN 1: NARRATIVA ───
  narrativa: |
    (3-5 párrafos. Debe capturar la esencia del escenario de forma narrativa,
    no meramente técnica. Debe ser comprensible por un público culto general.)

  # ─── SECCIÓN 2: RESUMEN EJECUTIVO ───
  resumen_ejecutivo: |
    (1-2 párrafos. Para ejecutivos y lectores con poco tiempo.
    Debe incluir: qué cambia, por qué importa, horizonte temporal,
    implicación principal.)

  # ─── SECCIÓN 3: FUNDAMENTOS ───
  fundamentos:
    cientificos:                    # Papers, teorías, datos empíricos
      - campo: ""
        referencia: ""              # DOI, arXiv ID, URL, o referencia bibliográfica completa
        hallazgo_relevante: ""
        ano: ""

    tecnologicos:                   # Tecnologías existentes, en desarrollo o teóricas
      - nombre: ""
        estado: [existente | en_desarrollo | teorica]
        madurez_tecnologica: 0      # TRL estimado (0-9)
        referencia: ""

    sociales:                       # Tendencias sociales, demográficas, culturales
      - tendencia: ""
        fuente: ""
        direccion: [creciente | decreciente | estable]
        evidencia: ""

    economicos:                     # Datos económicos, modelos de mercado
      - indicador: ""
        valor_actual: ""
        tendencia: ""
        fuente: ""

  # ─── SECCIÓN 4: PLAUSIBILIDAD ───
  plausibilidad:
    puntuacion_total: 0             # 0-100 (compuesta de las dimensiones siguientes)

    dimensiones:
      base_cientifica: 0            # 0-100 — solidez del fundamento científico
      viabilidad_tecnologica: 0     # 0-100 — disponibilidad o viabilidad de las tecnologías requeridas
      compatibilidad_social: 0      # 0-100 — resistencia/aceptación cultural esperada
      precedente_historico: 0       # 0-100 — analogías históricas disponibles
      convergencia_tendencias: 0    # 0-100 — múltiples fuerzas apuntando en la misma dirección

    metodologia_calculo: |
      (Descripción de cómo se calculó la puntuación. Pesos, supuestos,
      límites del método. Transparencia radical obligatoria.)

    supuestos_clave:                # Supuestos que, si cambian, alteran drásticamente la plausibilidad
      - supuesto: ""
        impacto_si_cambia: [alto | medio | bajo]

    factores_bloqueo:               # Barreras que impedirían este escenario
      - barrera: ""
        probabilidad_de_superarse: [alta | media | baja]

  # ─── SECCIÓN 5: HORIZONTE TEMPORAL ───
  horizonte_temporal:
    rango: "YYYY-YYYY"             # Rango de años en que el escenario podría materializarse
    punto_medio_estimado: "YYYY"   # Año más probable
    confianza: [alta | media | baja]

    fases:
      - fase: ""
        ano_estimado: YYYY
        descripcion: ""

  # ─── SECCIÓN 6: TECNOLOGÍAS CLAVE ───
  tecnologias:
    existentes:                     # Disponibles hoy
      - nombre: ""
        madurez: 0                  # 0-100
        proveedores_principales: []

    en_desarrollo:                  # En I+D activo, 3-10 años para madurez
      - nombre: ""
        madurez_estimada_para: "YYYY"
        actores_clave: []

    teoricas:                       # Solo existen como concepto o prototipo de laboratorio
      - nombre: ""
        barreras_cientificas: []
        tiempo_estimado_hasta_primer_demo: ""

  # ─── SECCIÓN 7: IMPACTOS ───
  impactos:
    economico:
      descripcion: ""
      magnitud: [bajo | medio | alto | transformador]
      sectores_afectados: []
      metricas_clave: []            # Indicadores económicos específicos

    politico:
      descripcion: ""
      magnitud: [bajo | medio | alto | transformador]
      regiones_mas_afectadas: []
      tensiones_geopoliticas: []

    ambiental:
      descripcion: ""
      magnitud: [bajo | medio | alto | transformador]
      indicadores_ambientales: []

    social:
      descripcion: ""               # Impacto en estructuras sociales, trabajo, educación, familia
      magnitud: [bajo | medio | alto | transformador]
      grupos_mas_afectados: []

    filosofico:
      descripcion: ""
      magnitud: [bajo | medio | alto | transformador]
      preguntas_que_abre: []

    sobre_la_conciencia:
      descripcion: ""               # Impacto específico sobre la naturaleza y experiencia de la conciencia
      magnitud: [bajo | medio | alto | transformador]
      implicaciones: []

  # ─── SECCIÓN 8: RIESGOS ───
  riesgos:
    - riesgo: ""
      categoria: [tecnologico | politico | economico | social | existencial | ambiental | etico]
      probabilidad: [muy_baja | baja | media | alta | muy_alta]
      impacto: [bajo | medio | alto | catastrofico]
      mitigabilidad: [alta | media | baja]
      mitigaciones_posibles: []
      actores_responsables: []

  # ─── SECCIÓN 9: OPORTUNIDADES ───
  oportunidades:
    - oportunidad: ""
      categoria: [tecnologica | economica | social | politica | cientifica | artistica | educativa]
      magnitud: [incremental | significativo | transformador]
      ventana_temporal: ""         # Período en que esta oportunidad está disponible
      actores_que_pueden_capturarla: []
      barreras_para_capturarla: []

  # ─── SECCIÓN 10: SEÑALES TEMPRANAS ───
  # Cada señal debe ser observable, medible y con umbral definido.
  # FUTURIA monitorea estas señales continuamente.

  senales_tempranas:
    - id: "SIG-NNN"                # ID único de señal (ej: SIG-001)
      senal: ""                     # Descripción específica y observable
      fuente_de_monitoreo: []       # APIs, feeds, bases de datos, registros oficiales
      tipo_umbral: [ocurrencia | valor_numerico | porcentaje | consenso]
      umbral_de_activacion: ""      # Condición específica: ">50% en encuesta Pew"
      estado_actual: [no_detectada | emergente | confirmada | materializada]
      fecha_primera_deteccion: "YYYY-MM-DD" o "null"
      ultima_actualizacion: "YYYY-MM-DD"
      relevancia_para_escenario: 0-100

  # ─── SECCIÓN 11: INTERDEPENDENCIAS ───
  interdependencias:
    escenarios_relacionados:        # Escenarios que potencian o son potenciados por este
      - id: "FUTURIA-YYYY-NNNN"
        tipo_relacion: [convergencia | precedente | catalizador | version_alternativa]

    escenarios_incompatibles:       # Escenarios que no pueden coexistir con este
      - id: "FUTURIA-YYYY-NNNN"
        razon_incompatibilidad: ""

    variables_criticas:             # Variables cuyo valor determina dirección del escenario
      - variable: ""
        valor_actual: ""
        umbral_1: ""                # Si cruza este umbral: versión A
        umbral_2: ""                # Si cruza este umbral: versión B

  # ─── SECCIÓN 12: ACTORES CLAVE ───
  # Entidades (humanas, organizaciones, IA, estados) que influyen o son influidos

  actores:
    - nombre: ""
      tipo: [humano | organizacion | estado | ia | otro]
      rol_en_escenario: []
      posicion: [favorable | neutral | opuesto | dependiente]
      capacidad_de_influencia: 0   # 0-100
      recursos_clave: []

  # ─── SECCIÓN 13: LÍNEAS DE INVESTIGACIÓN SUGERIDAS ───
  lineas_investigacion:
    - pregunta: ""
      metodologia_sugerida: ""
      urgencia: [baja | media | alta | critica]
      dependencias: []             # Requiere acceso a datos, colaboración, etc.

# ─── METADATOS (OBLIGATORIOS) ───
metadatos:
  autores:
    - nombre: ""
      rol: []
      afiliacion: ""
      tipo: [humano | agente_ia]

  revisado_por:
    - nombre: ""
      rol: ""

  version: "1.0"
  fecha_creacion: "YYYY-MM-DD"
  ultima_revision_significativa: "YYYY-MM-DD"

  revisiones_programadas:          # Cuándo se re-evaluará automáticamente
    - fecha: "YYYY-MM-DD"
      tipo_revision: [actualizacion_datos | re_evaluacion_plausibilidad | expansion]

  licencia: "CC BY-SA 4.0"        # O la licencia que corresponda
  hash_blockchain: null            # Hash SHA-256 del documento. null hasta registrar.
  tx_blockchain: null              # ID de transacción en cadena. null hasta registrar.

  notas_internas: |
    (Información para el equipo que no debe publicarse.
    Aquí van discusiones internas, dudas, deudas metodológicas.)

# ─── APÉNDICE: FUENTES Y REFERENCIAS ───
# Referencias completas, formateadas según estilo académico.
# Obligatorio mínimo: 10 referencias primarias para escenarios publicadas.

referencias:
  - tipo: [paper | libro | informe | regulacion | articulo | otro]
    autores: ""
    titulo: ""
    fuente: ""
    ano: YYYY
    doi_url: ""

# ─── APÉNDICE: HISTORIAL DE CAMBIOS ───
cambios:
  - version: "1.0"
    fecha: "YYYY-MM-DD"
    cambios: "Versión inicial"
    autor: ""
```

---

## Checklist de publicación PRISM

Antes de marcar un escenario como `publicada`:

- [ ] Todas las secciones del template están completadas
- [ ] Puntuaciones de plausibilidad justificadas con evidencia explícita
- [ ] Metodología de cálculo documentada en `metadatos.metodologia_calculo`
- [ ] Mínimo 10 referencias primarias verificadas
- [ ] `fact-checking` completado por AUDITOR (sin errores críticos)
- [ ] Validación humana completada
- [ ] Hash blockchain generado y transacción registrada
- [ ] Estado de señales tempranas actualizado (fecha + fuente)
- [ ] Escenarios relacionados e interdependencias verificados
- [ ] Licencia aplicada correctamente
- [ ] Notas internas revisadas — no debe haber información sensible en documento público
- [ ] Checklist firmado por al menos un revisor humano

---

## Convenciones de formato

- **Fechas:** ISO 8601 (`YYYY-MM-DD`)
- **IDs de escenarios:** `FUTURIA-YYYY-NNNN` (ej: `FUTURIA-2026-0001`)
- **IDs de señales:** `SIG-NNN` (ej: `SIG-001`)
- **Puntuaciones:** número entero 0-100; decimales solo si hay metodología explícita
- **Enums:** usar solo valores de las listas definidas; cualquier valor nuevo requiere aprobación de AUDITOR
- **Null vs vacío:** usar `null` para "no aplica / no disponible"; usar `[]` o `""` para "campo requerido pero sin datos aún"
- **Markdown en campos:** campos con `|` permiten multi-línea en formato Markdown; el resto deben ser strings simples

---

## Evolución del template

El template es versiónado. Cambios en la estructura PRISM requieren:
1. Propuesta documentada con justificación
2. Revisión por AUDITOR
3. Aprobación por al menos un revisor humano
4. Actualización de todos los escenarios existentes si el cambio es breaking

Versiones futuras previstas:
- **v2.0:** Incorporar campos de evaluación ética estructurada
- **v2.1:** Incorporar campos de simulación computacional (inputs/outputs de modelos)
- **v3.0:** Formato compatible con estándares de futures studies (integración con ISO 31000, etc.)

---

*Template: PRISM v1.0*
*Mantenido por: CURADOR + AUDITOR*
*Próxima revisión del template: Diciembre 2026*
