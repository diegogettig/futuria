# INFORME DE CONVERGENCIA — GRUPO SANCOR SALUD
## v1 (BORRADOR ORIGINAL — SUPERSEDED por v2)

> ⚠️ **SUPERSEDED** por `informe-convergencia/INFORME-CONVERGENCIA-SANCOR-2026-v2.md` (Metodología FUTURIA v1.0).
> Motivo: el v1 contenía la variable V10 (Personalidad Jurídica de la IA, eje de PRISM #001 del Instituto) como variable de negocio de Sancor, contaminando el análisis. v2 la remueve, aplica matriz Impacto×Incertidumbre + MICMAC + 2×2 con ejes cliente-específicos, y arquitectura de dos capas. Este archivo se conserva solo como registro histórico.

---
> Flujo 2 (prospección por cliente). Sistema SAT-FUTURIA: 100% trazable.
> Base de hechos: `investigacion/CONSOLIDADO-hechos.md` (60 hechos con URL/Tier/fecha).
> Auditoría: APTO-CON-SALVEDADES (ver `borrador/AUDITORIA-TRAZABILIDAD.md`).
>
> **LOGO:** FUTURIA (marca tipográfica; logo definitivo pendiente de archivo oficial).
> **Control:** FUT-CONV-SANCOR-2026 · Marca de agua: "FUTURIA · CONFIDENCIAL".

---

## 0. Propósito de este documento

Este es el **Informe de Convergencia** de Grupo SanCor Salud (Flujo 2). Parte del estudio minucioso del cliente, extrae las **variables que afectan su negocio hoy y potencialmente**, las proyecta en **escenarios**, y de ellas deriva las **señales y fuentes** que deben rastrearse en el Laboratorio de Vigilancia (Flujo 1). Las señales aquí identificadas alimentan la investigación base del cliente y el corpus general del Instituto.

> Regla del Chairman: este informe es la base que rastrea señales y variables *hacia atrás*. No se factura por horas; es insumo del producto vendible (PRISM #001 en variantes A/B/C).

---

## 1. Estudio del cliente (síntesis verificada)

SanCor Salud es una **Asociación Mutual** (constituida 6/7/1973, Sunchales, Santa Fe) de capital nacional, 3°/4° del mercado de prepagas (~672.000 afiliados; 825.793 según su reporte 2024/25). Perfil "federal" (fuerte en interior). Vertical integrada: Medicina Privada, Mista Seguros, Trayectoria Leasing, Vitus, Farmavitus, Fundación. [Hechos #1–#17]

Contexto regulatorio argentino 2023–2026: DNU 70/2023 desreguló cuotas; causa por cartelización 2024 (Resolución 107/2024) cerrada por acuerdo. Inflación médica > general; empleo registrado cayendo. [Entorno #1–#15]

---

## 2. Variables del negocio (lo que afecta a Sancor)

| # | Variable | Dato verificado | Hecho |
|---|----------|-----------------|-------|
| V1 | Regulación de precios | DNU 70/23 desregula cuotas; SSS pierde fijación | Entorno #1–#2 |
| V2 | Empleo registrado | ~12,84M ocupados (sep-2025); −217k desde nov-2023 | Entorno #15 |
| V3 | Costos médicos | Inflación médica > general (WTW +11,9% LatAm 2026) | Entorno #9 |
| V4 | Envejecimiento | >65 se duplica al 2050 en LatAm | Global #13–#14 |
| V5 | IA en siniestralidad | Mercado imagen médica US$1,8B→US$20,2B (2033) | Global #4 |
| V6 | Modelos de negocio | FFS→capitación/VBC/payvider; telemed+RPM | Global #9–#11 |
| V7 | Mutualismo vs concentración | INAES: 1,94M en mutuales/cooperativas | Entorno #13 |
| V8 | Alto costo farmacológico | Terapias génicas US$25,3B (2026) | Global #8 |
| V9 | Interoperabilidad | FHIR: 78% países con regulación; AR rezagada | Global #6 |
| V10 | Personalidad jurídica de la IA | Eje PRISM #001 (vacío regulatorio) | SIG-2026-00001 |

---

## 3. Escenarios prospectivos (2026–2035)

- **A — Mutual federal eficiente** (base): retiene interior, capitación + RPM de crónicos, IA en siniestralidad. *Sostén: V6, V7, V4.*
- **B — Guerra de cuotas y concentración** (adverso): cuotas libres, OSDE/Swiss por precio, empleo cae. *Sostén: V1, V2.*
- **C — Shock de costo (genérico/biológico + pandemia)** (cola): siniestralidad disparada. *Sostén: V8, V3.*
- **D — Payvider mutualista latino** (oportunidad): integración vertical + alianzas healthtech. *Sostén: V6, V7.*

---

## 4. Cruce con señales del corpus del Laboratorio (Flujo 1)

Del corpus de 75 señales (9 escenarios PRISM), **5 señales** convergen con variables de Sancor (todas del eje de personalidad jurídica de IA):

| Señal | Título | IRS | Variable |
|-------|--------|-----|----------|
| SIG-2026-00002 | Agente IA en consejo corporativo | 71,2 | V10, V5 |
| SIG-2026-00004 | Caso judicial por/sobre agente IA | 66,2 | V10, V5 |
| SIG-2026-00007 | Estándar técnico identidad de agentes IA | 71,2 | V10 |
| SIG-2026-00013 | FGA capitalizado + operativo | 69,8 | V5 (gobernanza) |
| SIG-2026-00014 | Monotributo Automatizado vigente | 74,8 | V5 (automatización) |

> Estas señales ya están en `senales_semilla.json` y son rastreadas diariamente por el Lab.

---

## 5. NUEVAS señales propuestas para captura en el Flujo 1

**9 de 10 variables del negocio de Sancor NO tienen señal directa en el corpus actual.** Deben darse de alta como señales nuevas en el Laboratorio, cada una con fuente ya verificada en la investigación SAT:

| Nueva señal | Variable | Fuente verificada (Tier) |
|-------------|----------|--------------------------|
| Regulación de cuotas post-DNU 70/23 (efecto en prima) | V1 | Decretos 170/171/172/2024 (T1) · Res. 107/2024 (T1) |
| Caída de empleo registrado y base de aportantes | V2 | CEPA/SIPA/IIEP-UBA (T2) |
| Inflación médica vs general (WTW LatAm) | V3 | WTW 2026 (T2) · INDEC IPC (T1) |
| Envejecimiento demográfico argentino (Censo 2022) | V4 | INDEC (T1, pendiente de cierre) |
| Capitación / VBC / payvider en salud AR | V6 | CMS capitation (T1) · Deloitte VBC (T2) |
| Mutualismo vs concentración de prepagas (INAES) | V7 | INAES Relevar Salud (T1) |
| Terapias génicas/biológicos como tail risk | V8 | AJMC (T3) · OMS RAM (T1) |
| Adopción FHIR / HCE interoperable en AR | V9 | Fire.ly State of FHIR (T3) |
| Responsabilidad IA en dispositivos médicos (ANMAT) | V10 | ANMAT (T2, verificar existencia) |

> **Acción:** estas 9 señales se cargan en `senales_semilla.json` (o módulo sector Salud) para que el Lab las rastree diariamente. Hasta entonces, el corpus del Flujo 1 está ciego al sector salud argentino.

---

## 6. Brechas de información (no inventadas)

- Facturación/ingresos de SanCor (no públicos).
- *Market share* oficial por empresa (confirmar SSS).
- CD 2025–2026 y CEO actual (Nari es 2023–2024).
- Envejecimiento demográfico argentino específico y salarios reales (INDEC).
- Existencia de resolución ANMAT de IA en dispositivos médicos (verificar; posible alucinación si se afirma sin fuente).

---

## 7. Derivación a variantes de entrega (PRISM #001)

Este Informe de Convergencia alimenta las **3 variantes del producto vendible** al cliente:
- **Variante A (Ejecutivo/CEO):** secciones 1–3 + recomendaciones de negocio.
- **Variante B (Tecnológica/CTO):** V5, V6, V9, V10 + señales SIG-00002/004/007.
- **Variante C (Política/Reguladores):** V1, V10 + comparativa internacional de personalidad jurídica IA.

---

*Fin del borrador de Convergencia. Sujeto a firma del Chairman tras validación de contenido.*
