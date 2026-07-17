# PROMPT PARA DEFINIR EL MODELO DE «INFORME QUINCENAL DE TENDENCIAS» — FUTURIA

> Pegá este prompt en la IA que va a definir el modelo. Adjuntale los 8 archivos de escenarios PRISM #002–#009 (abajo listados) y, si los tenés, los archivos de la landing (HTML/CSS) para que extraiga la línea estética.

---

## CONTEXTO DE FUTURIA (leelo completo; esta IA parte de cero)

FUTURIA Institute es un observatorio de vigilancia estratégica. Su ecosistema de contenido tiene tres productos con jerarquía clara:

1. **Lab de Vigilancia Tecnológica (Flujo 1, diario):** radar de señales del ecosistema.
2. **Informe de Convergencia (Flujo 2, por cliente o tema puntual):** inmersión vertical (variables → MICMAC → 2×2 → escenarios con criterio de defunción).
3. **Escenarios PRISM (generales, por encima de todo):** evolución de ecosistemas tecnológicos.

El producto que debés definir es **NUEVO y distinto de los tres anteriores**: un **Informe quincenal de tendencias** (cadencia cada 15 días), de divulgación profunda, dirigido a un público amplio pero exigente (decisores, profesionales, curiosos cultos). NO es un newsletter de alertas; NO es un informe de cliente.

### Restricciones duras (obligatorias, no negociables)

- **Trazabilidad SAT:** toda cifra, hecho o caso concreto debe poder remitirse a una fuente real con su URL. Cada afirmación fáctica lleva una clase **N/E/D/T/P** (N=Normativa, E=Evento fáctico, D=Dato cuantitativo, T=Técnica, P=Proyección; NOTA: la clase N existe para forzar el link al Boletín Oficial y cazar «normas fantasma», por eso N NO significa «numérico») y un veredicto `VERIFICADO` / `ILUSTRATIVO` / `ELIMINAR`. Lo no verificable se marca «Sin información disponible»; NUNCA se inventan fuentes, URLs ni cifras.
- **Anti-alucinación:** si para sustentar una tendencia necesitás un caso concreto y no tenés fuente real, NO lo inventes; usá solo los casos que aparezcan en los escenarios adjuntos o en fuentes verificables que cités con link.
- **Arquitectura de dos capas (en la entrega final, no en la definición):** Capa 1 = relato atractivo, prosa, cero tablas; Capa 2 = aparato (fuentes, veredictos, metodología). Para la *definición del modelo* que hoy pedimos, describí cómo se distribuyen ambas capas.
- **Confidencialidad:** pie/disclaimer «FUTURIA · CONFIDENCIAL / BORRADOR» según corresponda; el contenido es ilustrativo, no asesoramiento profesional.

---

## QUÉ TENÉS COMO MATERIA PRIMA (archivos adjuntos)

Ocho escenarios PRISM ya redactados (pruebas de concepto, formato markdown, contienen ejes, drivers y casos). Son la **base narrativa** del Informe quincenal: cada entrega quincenal tomará uno o varios de estos escenarios como semilla y los desarrollará a profundidad divulgativa.

- `PRISM-2026-0002-sociedades-automatizadas.md` — Sociedades automatizadas
- `PRISM-2026-0003-cardio-bionico.md` — Cardio biónico
- `PRISM-2026-0004-hard-tech-foundations.md` — Hard-tech foundations
- `PRISM-2026-0005-gobernanza-algoritmica.md` — Gobernanza algorítmica
- `PRISM-2026-0006-longevidad-caas.md` — Economía de la longevidad (suscripción a órganos artificiales)
- `PRISM-2026-0007-conciencia-verificable.md` — Conciencia artificial verificable
- `PRISM-2026-0008-bioprinting-distribuido.md` — Bioprinting distribuido
- `PRISM-2026-0009-geopolitica-datos.md` — Geopolítica del dato

También podés recibir archivos de la **landing de futuria.institute** (HTML/CSS) para extraer la línea estética.

---

## QUÉ DEBÉS DEFINIR (entregable de esta IA)

Redactá una **especificación del modelo de Informe quincenal** que fije, como mínimo:

1. **Nombre del producto** (propuesta: «Informe de Señal FUTURIA» o «Brief de Tendencia»; podés sugerir otro, pero que NO sea «Newsletter»).
2. **Frecuencia y cadencia:** quincenal. Describí el flujo de producción (de la semilla escenario → borrador narrativo → verificación SAT → HTML).
3. **Estructura de secciones** del informe (p. ej.: apertura narrativa que engancha, desarrollo explicativo de la tendencia, bloque de casos concretos con cita+link, bloque visual, cierre con implicancias). Cada sección con su propósito.
4. **Estilo narrativo:** textos atractivos, explicativos, que adentren al lector en la temática; segunda persona o impersonal según convenga; voz activa; prohibido lenguaje académico hermético.
5. **Uso de gráficos e imágenes:** qué tipos de visualización acompañan cada entrega (diagramas de la tendencia, timelines, mapas conceptuales, capturas/figuras), y cómo se citan sus fuentes.
6. **Casos concretos con cita correcta:** regla de que todo caso mencionado debe tener su fuente real y un link accesible al origen (web/paper/noticia). Formato de cita inline + bloque de fuentes al pie.
7. **Especificación HTML:** documento autocontenido (un solo archivo, sin dependencias externas salvo fuentes de sistema), **imprimible desde el navegador** (CSS `@media print` que oculte elementos de UI y formatee para A4), responsive, accesible.
8. **Línea estética coherente con la landing:** extraé paleta, tipografías y feeling de los archivos de landing adjuntos; si no los recibís, usá los tokens FUTURIA conocidos: fondo oscuro `#0d1419`, acento rojo `#e90100`, tinta `#e8eef2`, tipografía sans-serif limpia (tipo Segoe UI / system-ui). El logo FUTURIA (rojo/blanco sobre negro) debe aparecer en el header.
9. **Vínculo con el resto del ecosistema:** cómo este Informe deriva de los escenarios PRISM (arriba) y cómo a su vez retroalimenta al Lab de Vigilancia (señales a rastrear).
10. **Checklist de calidad anti-alucinación** que todo Informe quincenal debe pasar antes de publicar.

Entregá la especificación como un documento claro y accionable (markdown), listo para que un redactor/desarrollador lo implemente. Incluí al final un **ejemplo esqueleto de HTML** (estructura + CSS base imprimible + bloque de citas) usando como demo el escenario `PRISM-2026-0006-longevidad-caas.md`.

---

## NOTAS PARA QUIEN EJECUTE

- No definas el producto como un resumen de los escenarios; definí cómo *transformar* un escenario técnico en un informe narrativo de divulgación quincenal.
- La trazabilidad SAT y el Protocolo Anti-Alucinación son innegociables: si el modelo propuesto los debilita, marcalo como riesgo.
- Asumí que la otra IA NO conoce FUTURIA; por eso todo el contexto va arriba.
