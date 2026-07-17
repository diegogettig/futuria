# METODOLOGÍA FUTURIA — Sistema de Vigilancia, Convergencia y Escenarios
## v0.9 (reconstrucción de código y prompts — PENDIENTE DE FIRMA DEL CHAIRMAN)

> ⚠️ **SUPERSEDED** por `METODOLOGIA-FUTURIA-v1.0.md` (15/07/2026). El v1.0 retira el IRS y adopta IES + PS ortogonales, rúbricas ancladas, matriz Evidencia×Peso, MICMAC, ejes Shell/GBN y arquitectura de dos capas. Este documento se conserva solo como histórico de la reconstrucción. No usar como método vigente.

> **ESTADO DE ESTE DOCUMENTO:** borrador de reconstrucción. No es el "Manual de Metodología v1.0" citado en el repo (ese documento fuente **no se encontró en el repositorio** al 15/07/2026). Lo que sigue se reconstruyó literalmente desde `motor/motor_calificacion.py`, `prompts/AGENTE_OBSERVATORIO.md`, `observatorio/README.md` y `protocolo-validacion-antialucinacion.md`. Toda cifra de fórmula aquí está verificada contra el motor (`--self-test` pasa: IRS 79.8 / PS 90.0). El contenido narrativo sobre "por qué" es interpretación del autor del borrador y requiere tu validación.
>
> **Firma del Chairman para elevar a v1.0:** ____________  **Fecha:** ___________

---

## 0. QUÉ ES ESTO Y QUÉ NO ES

FUTURIA Institute opera un **Observatorio de Vigilancia Estratégica** cuya salida es el **Laboratorio de Escenarios** (escenarios PRISM) y, por encargo, **Informes de Convergencia** por cliente. El flujo es una tubería de 5 estadios:

```
[1] CAPTACIÓN      mundo → señal con fuente verificable        (diario)
[2] CALIFICACIÓN  señal → IRS + PS                            (diario)
[3] CORRELACIÓN   señales → racimos + impacto cruzado        (semanal)
[4] CONSTRUCCIÓN  racimos → escenario PRISM (10 componentes) (quincenal)
[5] PROYECCIÓN    escenario → decisión para cliente          (por encargo)
```

**Esto es propio de FUTURIA.** No es un estándar de mercado ni de otra organización. Los dos únicos elementos que SÍ son estándar externo se marcan explícitamente: **TRL** (Technology Readiness Level, de NASA/ESA, ISO 16290) y las prácticas de **calibración de probabilidades** (escuela Tetlock/Brier, adoptadas como disciplina transversal). Todo lo demás (SAT, Tiers T1–T4, IRS, PS, la taxonomía de dominios, el ciclo de 5 estadios) es método FUTURIA.

---

## 1. SAT — SISTEMA DE TRAZABILIDAD (propio FI)

SAT es la regla fundacional de operación. Toda afirmación fáctica en cualquier entregable debe remitir a una **fuente verificable con URL, tier y fecha de consulta**. Lo no verificable se marca explícitamente como *"Sin información disponible"* — no se omite, no se suaviza.

SAT es el techo bajo el cual viven todas las demás métricas. Una señal con fuente T4 (rumor) no suma crédito hasta corroborarse con T1/T2, sin importar su IRS.

> SAT se integra y refuerza con el **Protocolo de Validación Anti-Alucinación v1.0** (ver Sección 7). El Protocolo es quien define *cómo* se valida cada afirmación antes de publicar; SAT es la política de que toda afirmación debe ser trazable.

---

## 2. TIERS — NIVELES DE FUENTE (propio FI, inspirado en sourcing de inteligencia)

Clasifican la **autoridad de la fuente**, no la relevancia de la señal. Son 4 niveles:

| Tier | Qué es | Crédito |
|---|---|---|
| **T1** | Papers revisados, prensa T1, registros oficiales, patentes, ensayos clínicos, presentaciones regulatorias (FDA/SEC/ANMAT), datos primarios (INDEC, Boletín Oficial, EUR-Lex) | Pleno |
| **T2** | Prensa especializada, analistas, instituciones reconocidas, blogs oficiales de empresas | Alto |
| **T3** | Prensa general, agregadores, divulgación | Medio — verificar |
| **T4** | Redes, foros, rumores, filtraciones | Nulo hasta corroborar con T1/T2 |

**Regla dura:** si la mejor fuente de una ficha es T4 → `escalar_a_humano = true` y `estado = "madurando"` hasta corroborar. T4 nunca es fuente de publicación.

> **Diferencia crítica que el lector debe tener clara:** el **Tier** califica a la *fuente*; el **IRS/PS** (Sección 3) califica a la *señal*. Una señal puede tener fuente T1 (autoritativa) pero IRS bajo (poco relevante todavía), o fuente T3 pero IRS alto (muy relevante pero menos sólida). Ambas dimensiones se reportan juntas en el informe diario: `FUENTE (editor / tier)`.

---

## 3. IRS y PS — CALIFICACIÓN DE SEÑALES (propio FI)

Cada señal se puntúa en **8 dimensiones, 0 a 5**. De ahí se derivan dos índices 0–100. Las fórmulas están implementadas en `motor/motor_calificacion.py` y validadas por `--self-test`.

### 3.1 Las 8 dimensiones

`credibilidad · corroboración · novedad · velocidad · alcance · profundidad · convergencia · irreversibilidad`

### 3.2 IRS — Índice de Relevancia de Señal

`IRS = Σ (puntaje_i / 5 × peso_i)`  — los pesos suman 100 y ya están en escala 0–100:

| Dimensión | Peso |
|---|---|
| profundidad | 18 |
| convergencia | 13 |
| novedad | 12 |
| velocidad | 12 |
| credibilidad | 15 |
| corroboración | 10 |
| alcance | 10 |
| irreversibilidad | 10 |

**Umbrales IRS:** `≥ 70` prioritaria (escala a humano) · `45–69` en maduración · `< 45` archivo.

### 3.3 PS — Peso Sistémico

Mide cuán capaz es la señal de mover el tablero (cuán estructural/irreversible):

`PS = (profundidad/5 × 100)·0,40 + (convergencia/5 × 100)·0,35 + (irreversibilidad/5 × 100)·0,25`

**Umbral PS:** `≥ 70` escala a humano.

### 3.4 Ejemplo verificado (self-test del motor)

Puntajes: credibilidad 4, corroboración 3, novedad 4, velocidad 3, alcance 4, profundidad 5, convergencia 5, irreversibilidad 3.
→ **IRS = 79,8** · **PS = 90,0**.

> **ERRATUM DOCUMENTADO:** el "Manual de Metodología v1.0" (§4.3) imprime IRS ≈ 74,7 para este ejemplo, pero la suma correcta de sus propios términos es 79,8. El motor respeta la fórmula literal (§4.1), no el total mal sumado. Al elevar este borrador a v1.0, corregir el manual.

### 3.5 Reglas de fichado (integridad)

- Título y descripción **neutros** (qué se observó, no qué significa).
- `contra_senal` **obligatoria** (principio anti-sesgo: por cada tendencia, al menos una contra-señal). Ficha incompleta si está vacía.
- Umbral de escalamiento a humano: **IRS ≥ 70 O PS ≥ 70 O mejor fuente = T4**.

---

## 4. CICLO DE 5 ESTADIOS (propio FI)

1. **Captación** — rastreo diario de fuentes asignadas (prioriza T1–T2), deduplicación contra la biblioteca, fichado JSON con contra-señal.
2. **Calificación** — `motor_calificacion.py` calcula IRS/PS y estado; marca lo que escala.
3. **Correlación** — racimos por driver/dominio/horizonte; impacto cruzado (qué señal habilita a otra = mayor convergencia = candidata a eje de escenario).
4. **Construcción** — escenario PRISM de 10 componentes (narrativa con quiebre datable, fundamentos, plausibilidad derivada de IRS/PS del racimo, horizonte en Tres Horizontes H1/H2/H3, tecnologías con TRL, impactos, riesgos, oportunidades, señales tempranas, interdependencias). Cierra con predicciones calibradas (probabilidad numérica + fecha de resolución).
5. **Proyección** — para un cliente: matriz de exposición (driver × función del sujeto), priorización (probabilidad × impacto × proximidad), recomendaciones (sin arrepentimiento / opciones reales / coberturas / apuestas), tablero de indicadores tempranos.

---

## 5. INFORMES DE CONVERGENCIA (Flujo 2) y VARIABLES

El Informe de Convergencia es el producto por cliente (Sancor es el piloto). Parte del estudio del cliente, extrae **variables del negocio** (V1…Vn), las proyecta en escenarios (A/B/C/D) y de ellas deriva **señales** que el Lab debe rastrear (Flujo 1).

- **Variables del negocio**: NO son un set cerrado ni estándar. Las define el analista del estudio de cada cliente a partir de su cadena de valor, vulnerabilidades y horizonte de decisión. En Sancor (ej.) salieron 10: regulación de precios, empleo, costos médicos, envejecimiento, IA en siniestralidad, modelos de negocio, mutualismo, costo farmacológico, interoperabilidad, personalidad jurídica de la IA.
- **"Sostén" en un escenario** = qué variables lo justifican causalmente. El escenario A "Mutual federal eficiente" se apoya en V6 (modelos VBC) + V7 (mutualismo) + V4 (envejecimiento). Si esas variables se mueven así, el escenario es plausible.
- **Variables ↔ Señales**: cada variable se cruza con el corpus del Lab. Si la variable no tiene señal directa (en Sancor, 9 de 10 no la tenían), se crea una **señal nueva** etiquetada `origen: convergencia_<cliente>` para que el Lab la rastree diario. Eso es "rastrear señales hacia atrás".

---

## 6. TRL — Technology Readiness Level (ESTÁNDAR EXTERNO, NO de FI)

TRL (1–9) es escala de NASA/ESA, adoptada como ISO 16290. Mide madurez tecnológica. FUTURIA lo usa en el componente "Tecnologías" de los escenarios PRISM. **No es métrica FUTURIA**; se cita con su escala de origen y los valores asignados a un caso particular deben etiquetarse como asignados por FUTURIA (no como medición oficial).

---

## 7. PROTOCOLO DE VALIDACIÓN ANTI-ALUCINACIÓN (propio FI, v1.0)

Documento canónico: `observatorio/protocolo-validacion-antialucinacion.md`. Es un **gate obligatorio** que se aplica encima de SAT. Sus aportes a la metodología:

- **Clasificación de afirmaciones en 5 clases** (distinto a los Tiers de fuente): **N** normativa · **E** evento · **D** dato · **T** técnica · **P** proyección. El error de categoría más grave es presentar una **P** (proyección propia) con el tono de una **N** o **D** (dato). Una proyección disfrazada de dato es alucinación aunque el número sea razonable.
- **Tres veredictos**: ✅ VERIFICADO · ⚠️ ILUSTRATIVO (etiqueta visible en el cuerpo, nunca al pie; no para normativas) · ❌ ELIMINAR (se borra, no se suaviza con hedging).
- **Ciclo multi-agente**: Redactor → Extractor (lista plana de claims) → **Verificador con contexto limpio** (NO ve el informe, solo claims desnudos) → Adversario (refuta los VERIFICADO) → Chairman (firma el registro, no el informe).
- **registro-fuentes.json**: una fila por claim con `busquedas_realizadas` (documenta la ausencia de evidencia) y veredicto.
- **GATE de 8 ítems binarios** antes de publicar: cero claims clase N sin link oficial funcional; links confirmados en últimas 72h; toda cifra con fuente+año+universo; toda proyección declarada como FUTURIA; ilustrativo < 15%; ronda de adversario ejecutada; logo FUTURIA en portada y pie.

> **Implicancia para este borrador:** el "Manual de Metodología" y el "Protocolo Anti-Alucinación" son dos capas distintas. El Manual define *cómo se mide* (SAT/Tiers/IRS/PS). El Protocolo define *cómo se valida antes de publicar* (clases N/E/D/T/P, veredictos, ciclo). Ambos son obligatorios y coherentes: SAT exige trazabilidad; el Protocolo exige que la trazabilidad pase por veredicto de un verificador independiente.

---

## 8. CALIBRACIÓN (disciplina transversal, estándar adoptado)

Toda predicción lleva probabilidad numérica + fecha de resolución (nunca "probable": siempre "70%"). Se registra en `calibracion/registro_predicciones.json` y se mide con score Brier al vencer. Método Fermi para descomponer preguntas grandes; tasa base antes del caso. (Escuela Tetlock — adoptada, no de FI.)

---

## 9. BRECHAS DE TRAZABILIDAD (para cerrar antes de v1.0)

1. El "Manual de Metodología v1.0" **no existe como archivo** en el repo; se cita en README y prompts. Este borrador lo reconstruye.
2. Erratum §4.3 del manual (IRS 74,7 vs 79,8) debe corregirse en la fuente.
3. Las **variantes A/B/C del PRISM #001 para Sancor** fueron redactadas y pasaron una auditoría interna, pero **NO** pasaron el ciclo completo del Protocolo Anti-Alucinación (verificador con contexto limpio + registro-fuentes.json + adversario). Están en PREVIEW, no validadas para publicación.
4. Las "variables del negocio" no tienen taxonomía oficial; se derivan por cliente.

---

*FUTURIA Institute · Metodología v0.9 (reconstrucción) · 15/07/2026 · Pendiente firma Chairman para v1.0*
