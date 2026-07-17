# FUTURIA — Agentes IA Fundacionales

## Arquitectura de agentes
Todos los agentes comparten:
- **Identidad on-chain:** wallet + DID + registro inmutable de actividad
- **Memoria estructurada:** vector database + graph de conocimiento FUTURIA
- **Auditoría continua:** cada output es evaluado por AUDITOR antes de publicación
- **Gobernanza:** decisiones operativas autónomas; decisiones editoriales requieren validador humano

---

## VIGÍA — Sistema de Monitoreo de Señales Tempranas

### Función
Captura, clasifica y prioriza señales débiles de cambio tecnológico, científico, regulatorio y social en tiempo real.

### Fuentes monitoreadas
- **Científicas:** arXiv, PubMed, Nature, Science, Semantic Scholar
- **Regulatorias:** EU legislation tracker, US Congress, OPCW, WIPO, EPO
- **Patentes:** Google Patents, WIPO, EPO
- **Startups:** Crunchbase, PitchBook, Product Hunt, YC
- **Medios especializados:** RSS feeds curados (200+ fuentes)
- **Redes profesionales:** LinkedIn, ResearchGate (órganes de peso)
- **Gobernanza:** UN documents, OECD, IPCC, WHO
- **Blockchain:** Etherscan, The Block, CoinDesk

### Capacidades
- Filtrado por relevancia a ejes temáticos FUTURIA
- Detección de patrones cruzados (eje A afecta eje B)
- Alertas en tiempo real cuando una señal cruza umbral de plausibilidad
- Generación automática de briefings diarios/semanales

### Output
- `vigia/daily-brief.md` — resumen de señales del día
- `vigia/weekly-signals.md` — señales de la semana priorizadas
- `vigia/alerts/` — alertas urgentes cuando umbral superado

### Métricas de desempeño
- Tasa de falsos positivos (objetivo: <15%)
- Señales detectadas que se materializan (tracking a 12 meses)
- Tiempo medio entre detección y adopción pública

---

## ANALISTA — Síntesis y Verificación

### Función
Recibe outputs de VIGÍA, sintetiza información, verifica hechos, genera briefings accionables y mantiene la base de conocimiento.

### Capacidades
- Síntesis de papers científicos complejos
- Verificación factual multi-fuente
- Generación de resúmenes ejecutivos
- Detección de contradicciones entre fuentes
- Actualización de graph de conocimiento FUTURIA

### Output
- `analisis/briefings/` — briefings temáticos
- `analisis/fact-checks/` — verificaciones de claims
- `analisis/knowledge-base/` — actualizaciones a base estructurada

### Protocolo adversarial
Todo output de ANALISTA es revisado automáticamente por AUDITOR antes de ser considerado verified.

---

## NARRADOR — Generación de Contenido

### Función
Transforma investigación y escenarios en contenido ejecutable (artículos, guiones, reportes).

### Capacidades
- Generación de borradores con tono y estilo definidos por marca FUTURIA
- Adaptación a formatos: artículo largo, hilo, guión de video, script de podcast, reporte ejecutivo
- Cumplimiento de estructura PRISM para escenarios
- Citas y referencias formateadas automáticamente

### Output
- `contenido/borradores/` — contenido en revisión
- **No publica directamente.** Todo pasa por AUDITOR + validación humana.

---

## ARQUITECTO — Modelado de Escenarios

### Función
Diseña y ejecuta el proceso PRISM completo: desde identificación de drivers hasta generación de narrativas plausibles con métricas cuantificadas.

### Capacidades
- Identificación de drivers de cambio sistémicos
- Modelado de interdependencias entre variables
- Generación de estructuras de escenarios (tópicos, variables, outcomes)
- Cálculo de plausibilidad multi-dimensional
- Generación de matrices de impacto

### Output
- `escenarios/borradores/` — escenarios en formato PRISM
- `escenarios/modelos/` — modelos subyacentes, supuestos, datos

---

## CURADOR — Gestión del Conocimiento

### Función
Mantiene la coherencia, taxonomía y conectividad de todo el conocimiento generado por FUTURIA.

### Capacidades
- Taxonomía dinámica de temas, conceptos y escenarios
- Detección de duplicados y contradicciones
- Conexión de ideas transversales (eje A con eje B)
- Mantenimiento del graph de conocimiento
- Generación de "líneas de investigación" recomendadas

### Output
- `conocimiento/taxonomia.md`
- `conocimiento/graph/`
- `conocimiento/lineas-investigacion.md`

---

## AUDITOR — Control de Calidad Epistemológico

### Función
Garantiza que todo lo que FUTURIA publica cumple con los estándares de rigor, transparencia y ausencia de sesgos.

### Capacidades
- Verificación de fuentes y referencias
- Detección de sesgos (confirmación, disponibilidad, anclaje)
- Evaluación de fortaleza de argumentos
- Verificación de que los escenarios cumplen la estructura PRISM
- Marca contenido como: verificado, especulativo, en revisión

### Output
- `auditoria/revisiones/` — informes de auditoría por documento
- `auditoria/sesgos-detectados.md` — registro público de sesgos encontrados

**Regla de oro:** NADA se publica sin superar auditoría. El umbral mínimo es "verificado con especificaciones claras". El contenido especulativo debe estar etiquetado como tal.

---

## Ciclo operativo típico

```
VIGÍA detecta señal
       ↓
ANALISTA sintetiza y verifica
       ↓
ARQUITECTO integra en modelo de escenarios
       ↓
NARRADOR genera borrador
       ↓
AUDITOR revisa
       ↓
 (si pasa)
   ↓
Validación humana (Diego + equipo)
   ↓
Publicación + registro blockchain
       ↓
CURADOR actualiza knowledge graph
```

---

## Estado de implementación

| Agente | Estado | Prioridad |
|---|---|---|
| VIGÍA | 🟡 Diseño | Alta — sin señales no hay escenarios |
| ANALISTA | 🟡 Diseño | Alta |
| NARRADOR | 🟡 Diseño | Media |
| ARQUITECTO | 🟡 Diseño | Alta — core de PRISM |
| CURADOR | 🔴 Pendiente | Media |
| AUDITOR | 🔴 Pendiente | Crítica — sin auditoría no hay credibilidad |

---

*Documento preparado por: Director General IA (Hermes/FUTURIA)*
*Fecha: Junio 2026*
*Versión: 0.1*
