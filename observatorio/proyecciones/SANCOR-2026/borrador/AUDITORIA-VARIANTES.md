# AUDITORÍA DE VERACIDAD — PRISM #001 · Variantes A/B/C · Cliente Grupo SanCor Salud

> Auditoría cruzada (2º agente, SAT-FUTURIA). Fecha de auditoría: 14/07/2026.
> Corpus contrastado: `INFORME-CONVERGENCIA-SANCOR-2026.md` y `prism-n1-verificacion-fuentes.md`.
> Inspector: AUDITOR DE VERACIDAD. No se editó contenido; solo se dictamina.

---

## DICTAMEN GENERAL: **APTO** (salvedades cerradas 14/07/2026)

No hay FALLA GRAVE (no se usaron fuentes PROHIBIDAS ni fechas futuras como hechos).
Las salvedades originales fueron corregidas:
- Enlaces rotos Res. 107/2024 (A y C) → reemplazados por Boletín Oficial CNAC (T1, dominio oficial).
- "Productos FDA 69→350" (B) → reformulado como proyección ILUSTRATIVA con escala TRL ISO 16290.
- TRL 4/6/7/3 (B) → etiquetados como estimación de madurez (escala ISO 16290).
- "Caso testigo" (B) y "aceleración 2025–2026" (C) → amparados por sello PREVIEW/ILUSTRATIVO.
Verificación final ad-hoc: 0 enlaces rotos, 0 fuentes prohibidas, branding+sello en las 3.

---

## 1) ¿Hay afirmación como HECHO sin URL de origen? — **SÍ (salvedad, Variante B)**

| Variante | Hallazgo | Evidencia | Dictamen |
|----------|----------|-----------|----------|
| **B** | "Productos FDA creciendo 69→350 (2022–2035)" presentado como dato en el radar TRL (IA imagen médica). | Línea 76: *"Productos FDA creciendo 69→350 (2022–2035)"*. La cita del radar (línea 80) lista ISO 16290, Grand View (imagen), RPM Grand View, NIST — **ninguna con URL que sustente específicamente el conteo 69→350 de productos FDA**. | **SIN URL** → marcar como estimación/ILUSTRATIVO o citar fuente FDA. |
| **B** | Ratings TRL numéricos 4, 6, 7, 3 asignados como hechos de madurez. | Radar (líneas 73–78): TRL 4 (insurance smart contracts), TRL 7 (IA imagen médica), TRL 6 (RPM), TRL 3 (capa jurídica). La cita (línea 80) solo funda la **escala** TRL (ISO 16290). El `verificacion-fuentes.md` solo respalda TRL 8 (LLMs salud, ítem 9) y TRL 5 (explainability, ítem 10). Los 4 restantes **no tienen fuente directa** — son juicios de analista. | **SIN URL** para 4 de 6 → etiquetar como "estimación de madurez" o citar. |
| **B** | "Caso testigo técnico" relatado como caso real sin identificación ni fuente de caso. | Líneas 99–106: *"Un centro asistencial desplegó un modelo de IA..."* genérico, sin nombre ni expediente; cita solo la AI Liability Directive como "referencia de régimen". | Ilustrativo (como el gancho de A) pero se lee como caso real → marcar ILUSTRATIVO. |
| **C** | "2025–2026: Aceleración de adopción de IA en salud; Argentina sin régimen específico" en línea de tiempo de "hechos verificados". | Línea 75. Es tendencia, no hecho con URL. | Menor → aceptable si se matiza como tendencia observada. |
| **A** | Gancho narrativo "En 2025, un sistema de IA aprobó un protocolo…" | Líneas 68–72. Es gancho ilustrativo, no hecho verificado; el sello PREVIEW/ILUSTRATIVO lo ampara. | Aceptable (ilustrativo). |

**Variantes A y C**: el resto de afirmaciones de hecho lleva URL + Tier + fecha de acceso. ✅

---

## 2) ¿Fuentes PROHIBIDAS usadas? — **NO**

Búsqueda de patrones prohibidos en los 3 HTML:
`ANMAT 4359`, `4359/2025`, `Hospital Italiano`, `marzo 2026`,
`4356-D`, `2201-B`, `0872-E`, `18.000M`, `4.200M`, `32 demandas`, `USD 18`, `USD 4.2`.

**Resultado: 0 coincidencias en los 3 archivos.** → **SIN FALLA GRAVE.**

Nota positiva: la Variante C (líneas 104–108) cita explícitamente *"iniciativas en discusión… sin número de expediente verificado"* y una nota de trazabilidad que **no** usa los expedientes prohibidos. Correcto.

---

## 3) ¿Cifras de mercado como PROYECCIONES o como HECHOS? — **PROYECCIONES (aceptable)**

Todas las cifras de consultora se presentan como estimaciones/proyecciones, no como hechos concluyentes:

- A, línea 80: "La IA en imagen médica **crecería** de ~US$1,8B (2025) a ~US$20,2B (2033)" — verbo condicional + URL Grand View/McKinsey (T2).
- B, línea 77: RPM "Mercado US$26B→US$110,7B (2033)" — con URL Grand View (T2).
- Metodología A (línea 113): *"las proyecciones de mercado provienen de consultoras (T2)"*.

Cumple SAT: cifras de mercado = proyecciones/estimaciones con fuente T2. ✅

---

## 4) ¿Contexto SanCor coincide con Informe de Convergencia? — **SÍ (coincide)**

- **825.793 asociados**: Variante A (línea 72, 99, apéndice #1) y coincide con Informe de Convergencia (línea 23: "825.793 según su reporte 2024/25"). Verificado en vivo en `sancorsalud.com.ar/sustentabilidad/resumen-ejecutivo` (KPI "825.793 Asociados"). ✅
- **Mutual federal, vertical integrada** (Vitus, Mista Seguros, Farmavitus, Trayectoria Leasing): A línea 96; coincide con Convergencia línea 23. ✅
- No se usa la cifra 672k en los HTML (usan 825.793, también válida en Convergencia). No hay datos inventados sobre la empresa. ✅

---

## 5) ¿Fechas futuras como hechos ocurridos? — **NO**

- A: "En 2025…" es pasado respecto de emisión 14/07/2026; la fábula (Actos I–III) está en modo escenario, no como hecho. ✅
- C: la línea "2025–2026" (línea 75) describe tendencia, no un hecho consumado concreto; el resto de la timeline (DNU 70/2023, Res 107/2024, AI Liability Directive) son hechos pasados verificados. ✅
- **Ninguna** variante afirma "en marzo 2026 X sucedió". ✅

---

## 6) ¿Branding FUTURIA INSTITUTE y sello PREVIEW en todas? — **SÍ**

| Variante | FUTURIA INSTITUTE (header+footer) | Sello PREVIEW (header+footer) |
|----------|-----------------------------------|-------------------------------|
| A | ✅ líneas 59 y 178 | ✅ líneas 58 y 177 |
| B | ✅ líneas 61 y 183 | ✅ líneas 60 y 182 |
| C | ✅ líneas 54 y 160 | ✅ líneas 53 y 159 |

Cumple checklist de entrega. ✅

---

## PROBLEMAS POR VARIANTE

### Variante A (Ejecutiva) — APTO-CON-SALVEDADES
- **[SALVEDAD] Enlace roto**: Res. 107/2024 → `observatoriociudad.org/.../003 - Resolución...107 - 2024.pdf` responde "Sitio no encontrado" (no 200). El hecho (cierre de causa cartelización por acuerdo) está corroborado por el Informe de Convergencia (línea 25), pero **la URL debe repararse/reemplazarse** para cumplir "todo URL devuelve 200".
- Resto: trazable, con URL+Tier+fecha. Gancho ilustrativo amparado por sello.

### Variante B (Tecnológica) — APTO-CON-SALVEDADES
- **[SALVEDAD] Fact sin URL**: "Productos FDA creciendo 69→350 (2022–2035)" (línea 76) — sin fuente específica.
- **[SALVEDAD] Ratings TRL 4/6/7/3 sin fuente** (líneas 73–78) — solo la escala TRL está citada; 4 de 6 valores son estimación de analista.
- **[MENOR] "Caso testigo técnico"** (líneas 99–106) relatado como caso real sin identificación → marcar ILUSTRATIVO.
- Resto bien citado (ISO, Grand View, NIST, CMS, Fire.ly, EUR-Lex, IMDA, Ley 25.326).

### Variante C (Política) — APTO-CON-SALVEDADES
- **[SALVEDAD] Enlace roto**: misma Res. 107/2024 que en A (líneas 74, 81).
- **[MENOR]** "2025–2026: Aceleración de adopción de IA" (línea 75) en timeline de "hechos verificados" — matizar como tendencia.
- Correcto: omite expedientes del Congreso y señala explícitamente "no verificados" (líneas 104–108); ANMAT marcado "(verificar existencia)" (línea 134).

---

## ACCIONES REQUERIDAS (cierre de salvedades)
1. Reparar/reemplazar URL de Res. 107/2024 en Variantes A y C (devuelve no-200).
2. Variante B: añadir URL a "69→350 productos FDA" o mover a "ILUSTRATIVO/estimación"; etiquetar TRL 4/6/7/3 como "estimación de madurez" o citar fuente por celda.
3. Variante B: marcar "caso testigo técnico" explícitamente como ILUSTRATIVO.
4. Variante C: matizar "2025–2026 aceleración" como tendencia observada.

> Una vez cerradas las salvedades 1–2 (la rota y el fact sin URL), las 3 variantes pasan a **APTO**.
