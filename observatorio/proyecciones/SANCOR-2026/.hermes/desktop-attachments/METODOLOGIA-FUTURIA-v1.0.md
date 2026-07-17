# METODOLOGÍA FUTURIA v1.0
## Sistema de Vigilancia, Convergencia y Escenarios — Especificación técnica y prompt del Laboratorio

> **Estado:** reemplaza a v0.9 (reconstrucción) y al "Manual de Metodología v1.0" (entregado 13/07/2026 como `.docx`, nunca versionado en el repo — **brecha #1 cerrada: el documento existe, estaba fuera del repositorio**).
>
> **Firma del Chairman:** ____________ **Fecha:** ___________

---

## CHANGELOG v0.9 → v1.0

| # | Cambio | Motivo |
|---|---|---|
| 1 | **IRS se retira.** Se reemplaza por **IES** (evidencia) + **PS** (peso), ortogonales | IRS y PS eran colineales: las 3 dimensiones del PS pesaban 41/100 del IRS. No eran dos ejes |
| 2 | **Rúbricas ancladas 0–5** para las 8 dimensiones | Sin anclas, el puntaje no es reproducible entre agentes ni auditable |
| 3 | **Puntajes enteros + bandas.** Se prohíbe el decimal | El "IRS 79,8" violaba el patrón 3.5 (precisión espuria) del propio Protocolo Anti-Alucinación |
| 4 | **Matriz Evidencia × Peso** con 4 cuadrantes y acción por cuadrante | Sustituye los umbrales sueltos. Rescata explícitamente la señal débil |
| 5 | **Corroboración = origen independiente**, no republicación | 5 medios reescribiendo un press release era 1 fuente contada como 5 |
| 6 | **Campo `tasa_base`** obligatorio para anuncios | Un anuncio no es un hecho. La tasa base anuncio→entrega es el correctivo |
| 7 | **Campo `fecha_revision`** y caducidad automática | Una señal de 2026 con peso alto está podrida en 2028 si nadie la revisó |
| 8 | **MICMAC (Godet)** operacionaliza el estadio 3 | "Impacto cruzado" estaba nombrado pero no tenía procedimiento. Es el motor del Informe de Convergencia |
| 9 | **Incertidumbre** se mide en las variables (estadio 5) | El sistema medía importancia y nunca incertidumbre. Los ejes de escenario nacen de la incertidumbre |
| 10 | **Método de ejes Shell/GBN**: predeterminados vs. incertidumbres críticas | Cierra brecha #4: los escenarios A/B/C/D ya no aparecen de la nada |
| 11 | **Componente 11 del PRISM: Criterio de defunción** | Un escenario que no se puede matar no es una hipótesis, es una creencia |
| 12 | **Arquitectura de dos capas** (relato / aparato) | Lección estructural de AI 2027. Ver §9 |
| 13 | **Erratum IRS 74,7 → 79,8 resuelto** | El error era del Manual (suma mal hecha), no del motor. v1.0 elimina el índice, el punto queda cerrado |

---

## 1. QUÉ ES PROPIO Y QUÉ ES ADOPTADO

Regla de honestidad metodológica: FUTURIA nunca presenta como propio un método ajeno, ni como estándar un método propio.

| Elemento | Origen |
|---|---|
| SAT, Tiers T1–T4, IES, PS, matriz Evidencia×Peso, taxonomía de dominios, ciclo de 5 estadios, PRISM, Protocolo Anti-Alucinación | **Propio FUTURIA** |
| **TRL** (1–9) | NASA/ESA · ISO 16290 — **adoptado** |
| **Calibración / Brier** | Escuela Tetlock · Good Judgment Project — **adoptado** |
| **MICMAC** (motricidad/dependencia) | Michel Godet · LIPSOR/CNAM — **adoptado** |
| **Ejes por incertidumbres críticas** | Shell / Global Business Network · Schwartz — **adoptado** |
| **Tres Horizontes** (H1/H2/H3) | Bill Sharpe / IFF — **adoptado** |

---

## 2. SAT Y TIERS (sin cambios respecto de v0.9)

**SAT** — toda afirmación fáctica remite a fuente verificable con URL, tier y fecha de consulta. Lo no verificable se marca como *"Sin información disponible"*. No se omite, no se suaviza.

**Tiers** — califican la **fuente**, no la señal:

| Tier | Qué es | Crédito |
|---|---|---|
| **T1** | Papers revisados, registros oficiales, patentes, ensayos clínicos, presentaciones regulatorias (FDA/SEC/ANMAT), datos primarios (INDEC, Boletín Oficial, EUR-Lex) | Pleno |
| **T2** | Prensa especializada, analistas, instituciones reconocidas, blogs oficiales de empresas | Alto |
| **T3** | Prensa general, agregadores, divulgación | Medio — verificar |
| **T4** | Redes, foros, rumores, filtraciones | Nulo hasta corroborar con T1/T2 |

Regla dura: mejor fuente = T4 → `escalar_a_humano = true`, `estado = "madurando"`. T4 nunca es fuente de publicación.

---

## 3. CALIFICACIÓN DE SEÑALES (rediseñado)

### 3.1 Dos índices ortogonales

Ninguna dimensión aparece en ambos índices. Esa es la corrección central de v1.0.

**IES — Índice de Evidencia de Señal (0–100).** ¿Cuán sólido y cuán vivo es esto?

| Dimensión | Peso |
|---|---|
| credibilidad | 30 |
| corroboración | 20 |
| novedad | 15 |
| velocidad | 20 |
| alcance | 15 |

`IES = Σ (puntaje_i / 5 × peso_i)` → **redondear a entero**

**PS — Peso Sistémico (0–100).** Si ocurre, ¿cuánto mueve el tablero?

| Dimensión | Peso |
|---|---|
| profundidad | 40 |
| convergencia | 35 |
| irreversibilidad | 25 |

`PS = Σ (puntaje_i / 5 × peso_i)` → **redondear a entero**

> **Nota de compatibilidad:** el ejemplo canónico (cred 4, corr 3, nov 4, vel 3, alc 4, prof 5, conv 5, irrev 3) da **IES = 70** y **PS = 90**. El PS es idéntico al de v0.9 (la fórmula no cambió). El IRS queda deprecado; el motor debe emitir `WARNING: IRS deprecado en v1.0` si se invoca.

### 3.2 Rúbricas ancladas

Sin esto, el número es opinión con decimales. Cada agente y cada humano puntúa contra estas anclas, no contra su intuición.

**CREDIBILIDAD** — autoridad de la mejor fuente disponible
`0` sin fuente · `1` T4 único · `2` T3 único · `3` T3 múltiple o T2 único · `4` T2 sólido, o T1 preliminar (preprint sin revisar) · `5` T1 pleno (paper revisado, registro oficial, dato primario)

**CORROBORACIÓN** — **origen independiente**, no cantidad de links
`0` ninguna · `1` fuente única · `2` 2+ fuentes que derivan del mismo origen (mismo press release, misma agencia) → *cuenta como 1* · `3` 2 fuentes de origen genuinamente independiente · `4` 3+ independientes · `5` 3+ independientes, al menos una con verificación primaria propia

> Regla anti-eco: si todas las coberturas se remiten al mismo comunicado, la corroboración es 1, no importa cuántos medios lo publiquen.

**NOVEDAD** — cuán fuera del radar está
`0` conocido y publicado hace >2 años · `1` conocido y ampliamente cubierto · `2` conocido dentro del nicho · `3` poco cubierto fuera del nicho · `4` primera aparición pública relevante · `5` no estaba en el radar de nadie, o contradice el consenso vigente

**VELOCIDAD** — ritmo y aceleración
`0` estancado o en retroceso · `1` progreso lineal lento · `2` progreso constante · `3` aceleración leve · `4` aceleración marcada (métrica clave mejora >2× en <12 meses) · `5` ruptura de tendencia (salto de orden de magnitud)

**ALCANCE** — difusión
`0` un actor, un lugar · `1` un sector, una jurisdicción · `2` un sector, varias jurisdicciones · `3` varios sectores o un bloque regional · `4` multi-sector y multi-región · `5` global y multi-dominio

**PROFUNDIDAD** — cuánto cambia si se materializa
`0` irrelevante · `1` cambia una práctica · `2` cambia un proceso de una industria · `3` cambia el modelo de negocio de un sector · `4` reestructura un sector o crea uno nuevo · `5` cambia reglas del juego a nivel institucional o civilizatorio

**CONVERGENCIA** — posición en la red
`0` aislada · `1` toca otra señal tangencialmente · `2` refuerza 1 señal · `3` refuerza 2–3 señales o 1 escenario · `4` habilita o refuerza 2+ escenarios · `5` precondición de 3+ escenarios (nodo estructural de la red)

**IRREVERSIBILIDAD** — lock-in
`0` trivialmente reversible · `1` reversible a costo bajo · `2` reversible a costo alto · `3` crea dependencia de trayectoria · `4` revertir exige destruir capital instalado · `5` irreversible en la práctica (estándar adoptado, conocimiento publicado, tratado firmado)

### 3.3 Matriz Evidencia × Peso

Los umbrales sueltos se reemplazan por cuadrantes. **Corte en 60 en ambos ejes.**

| | **PS ≥ 60** | **PS < 60** |
|---|---|---|
| **IES ≥ 60** | **Q1 · DRIVER ACTIVO**<br>Ya está moviendo el tablero.<br>→ Candidata a eje de escenario. Escala a humano. Publicable. | **Q3 · RUIDO CONFIRMADO**<br>Sólido pero intrascendente.<br>→ Archivo con revisión semestral. No consume horas. |
| **IES < 60** | **Q2 · CARTA SALVAJE** ⭐<br>Poca evidencia, peso enorme.<br>→ **Escala a humano.** Monitoreo intensivo, contra-señal obligatoria. **No publicable todavía.** | **Q4 · DESCARTE**<br>→ Fuera. Revisión anual automática. |

> **Q2 es el cuadrante que justifica la existencia del Observatorio.** Cualquiera lee Q1 en el diario. Detectar Q2 dos años antes es el producto. El IRS de v0.9 hundía sistemáticamente Q2, porque castigaba la baja corroboración que *define* a una señal débil. La matriz lo corrige: baja evidencia ya no es un demérito, es una coordenada.

**Escalamiento a humano:** Q1 · Q2 · mejor fuente = T4 · `tasa_base` < 30% con PS ≥ 60.

### 3.4 Ficha de señal (esquema v1.0)

```json
{
  "id": "SIG-2026-00042",
  "fecha_captura": "2026-07-15",
  "fecha_revision": "2026-10-15",
  "titulo": "Enunciado corto y neutral del hecho",
  "descripcion": "1-3 oraciones factuales. Qué se observó, no qué significa.",
  "dominio_primario": "Geopolitica_Soberania",
  "dominios_secundarios": ["IA_AGI", "Computo_Hardware"],
  "tipo": "tendencia",
  "fuentes": [{"url": "https://...", "editor": "...", "tier": "T1", "origen_id": "ORG-01"}],
  "puntajes": {
    "credibilidad": 4, "corroboracion": 3, "novedad": 4, "velocidad": 3, "alcance": 4,
    "profundidad": 5, "convergencia": 5, "irreversibilidad": 3
  },
  "IES": 70,
  "PS": 90,
  "cuadrante": "Q1",
  "tasa_base": {
    "aplica": true,
    "pregunta": "¿Qué proporción de anuncios estatales de clústeres GPU se ejecutó en el plazo comprometido?",
    "estimacion": "35%",
    "fuente_estimacion": "https://...",
    "efecto": "Velocidad limitada a 3 pese al anuncio de gran escala"
  },
  "horizonte": "2027-2030",
  "contra_senal": "Indicio que la contradice o la frena (OBLIGATORIO)",
  "escenarios_vinculados": ["FUTURIA-2026-009", "FUTURIA-2026-004"],
  "senales_relacionadas": ["SIG-2026-00031"],
  "origen": "scan_diario | convergencia_<cliente>",
  "estado": "activa",
  "escalar_a_humano": true
}
```

**`origen_id`**: dos fuentes que comparten `origen_id` cuentan como una sola para corroboración. Es el mecanismo que implementa la regla anti-eco.

**`tasa_base`**: obligatorio cuando la señal es un *anuncio*, una *promesa* o un *target*. Un anuncio no es un hecho. La pregunta siempre es la misma: de cosas como esta que se anunciaron antes, ¿cuántas se cumplieron? Sin ese número, la velocidad se puntúa por entusiasmo.

**`fecha_revision`**: por defecto captura + 90 días. Vencida sin revisar → `estado = "caducada"`, sale de los racimos activos y no puede sostener un escenario. Las señales se pudren; el sistema debe saberlo.

---

## 4. ESTADIO 3 — CORRELACIÓN (operacionalizado con MICMAC)

*Método adoptado: análisis estructural de Michel Godet (LIPSOR/CNAM). No es método FUTURIA.*

El estadio 3 dejó de ser "agrupar por afinidad". Procedimiento:

**Paso 1.** Seleccionar entre 5 y 12 drivers (señales Q1/Q2 del racimo). Más de 12 vuelve la matriz inmanejable (N² juicios).

**Paso 2.** Matriz N×N. Para cada par ordenado (A→B): *si A ocurre, ¿cómo cambia la probabilidad de B?*
`-2` inhibe fuerte · `-1` inhibe · `0` sin efecto · `+1` habilita · `+2` habilita fuerte

**Paso 3.** Calcular por driver:
- **Motricidad** = Σ |influencia saliente| (cuánto mueve a los demás)
- **Dependencia** = Σ |influencia entrante| (cuánto lo mueven a él)

**Paso 4.** Clasificar:

| | **Baja dependencia** | **Alta dependencia** |
|---|---|---|
| **Alta motricidad** | **MOTOR** → eje de escenario. Es causa, no síntoma. | **RELÉ** → inestable, amplifica. Punto de palanca peligroso: tocarlo propaga. |
| **Baja motricidad** | **AUTÓNOMA** → fuera del sistema. Excluir. | **RESULTADO** → síntoma. **Indicador temprano, nunca eje.** |

**Paso 5.** Salida obligatoria: `micmac_<racimo>.json` + el plano motricidad×dependencia.

> **Error que esto previene:** construir un escenario sobre una variable RESULTADO. Es el error más común de la prospectiva amateur — narrar el síntoma como si fuera la causa. Los MOTOR generan escenarios; los RESULTADO se monitorean.

---

## 5. ESTADIO 4 — CONSTRUCCIÓN (PRISM, 11 componentes)

Los 10 componentes de v0.9 se mantienen. Se agrega el 11.

1. Narrativa (quiebre datable) · 2. Fundamentos · 3. Plausibilidad (derivada de IES/PS del racimo) · 4. Horizonte (rango, punto medio, confianza, H1/H2/H3) · 5. Tecnologías (TRL, marcado como asignación FUTURIA) · 6. Impactos · 7. Riesgos · 8. Oportunidades · 9. Señales tempranas · 10. Interdependencias

**11. CRITERIO DE DEFUNCIÓN (nuevo, obligatorio)**

> *¿Qué observación concreta, con fecha, mataría este escenario?*

Formato: 2–4 enunciados falsables, cada uno con fecha de chequeo.

Ejemplo (escenario #009, Geopolítica del Dato):
> *"Si al 31/12/2028 ningún país fuera de EE.UU./CN/UE tiene un clúster ≥10k H100-eq **operativo** (no anunciado), el escenario se declara muerto y se reescribe desde cero."*

Un escenario sin criterio de defunción no es una hipótesis: es una creencia. Y las creencias no se venden a gobiernos.

**Cierre:** 3–5 predicciones calibradas (probabilidad numérica + fecha de resolución) → `calibracion/registro_predicciones.json`.

---

## 6. ESTADIO 5 — PROYECCIÓN Y VARIABLES (cierra brecha #4)

### 6.1 Taxonomía de variables

Las variables del negocio siguen definiéndose por cliente (eso es correcto: son idiosincráticas). Lo que v1.0 estandariza es **cómo se clasifican**, no cuáles son.

Cada variable recibe dos puntajes 0–5:
- **Impacto** en el sujeto: si se mueve, ¿cuánto le cambia la vida al cliente?
- **Incertidumbre**: ¿sabemos cómo va a evolucionar?

> **Esta es la corrección conceptual más importante de v1.0.** El sistema v0.9 medía importancia y nunca medía incertidumbre. Pero los escenarios no nacen de lo importante: nacen de lo **incierto**. Lo importante y seguro no genera escenarios — genera contexto.

| | **Incertidumbre alta** | **Incertidumbre baja** |
|---|---|---|
| **Impacto alto** | **INCERTIDUMBRE CRÍTICA**<br>→ Candidata a **eje** de escenario | **ELEMENTO PREDETERMINADO**<br>→ Va en **TODOS** los escenarios, idéntico. No es eje. |
| **Impacto bajo** | **RUIDO** → contexto | **CONSTANTE** → supuesto de base |

*Método adoptado: Shell / Global Business Network (Schwartz).*

### 6.2 Derivación de los ejes A/B/C/D

1. Clasificar todas las variables en la matriz 6.1.
2. Verificar con MICMAC que las candidatas sean **MOTOR**, no RESULTADO.
3. Elegir **las 2 incertidumbres críticas de mayor motricidad** que sean **mutuamente independientes** (si están correlacionadas, los 4 cuadrantes colapsan en 2 — error clásico).
4. Cada eje se formula como un **continuo con dos polos plausibles**, no como sí/no.
5. El 2×2 resultante da los 4 escenarios. **Ahí nacen A/B/C/D.**
6. Los elementos predeterminados se escriben **idénticos en los cuatro**. Si un elemento cambia entre escenarios, no era predeterminado: reclasificar.
7. Nombrar cada escenario con una frase memorable, no con una letra.

**Test de validez del set:** si un lector no puede explicar en una oración por qué el escenario A es distinto del B, los ejes están mal elegidos.

### 6.3 Sancor (piloto) — qué corregir

Las 10 variables existen pero nunca se clasificaron por incertidumbre, y los 4 escenarios no se derivaron de ejes. **Acción:** re-clasificar las 10 en la matriz 6.1, correr MICMAC, y verificar si los escenarios A–D actuales son reconstruibles desde 2 ejes. Si no lo son, se reescriben. Es probable que "envejecimiento" sea un **predeterminado** (alto impacto, baja incertidumbre: la pirámide demográfica de 2035 ya nació) y que "personalidad jurídica de la IA" sea una **incertidumbre crítica**. Si es así, el escenario A actual está apoyado en un predeterminado — es decir, en algo que pasa en los cuatro escenarios y por lo tanto **no distingue nada**.

### 6.4 Señales hacia atrás

Sin cambios: variable sin señal directa → se crea señal con `origen: convergencia_<cliente>`. Es correcto y es una de las mejores ideas de v0.9.

---

## 7. PROTOCOLO ANTI-ALUCINACIÓN

Sin cambios. Documento canónico: `observatorio/protocolo-validacion-antialucinacion.md`. Gate obligatorio de 8 ítems. Clases N/E/D/T/P. Tres veredictos. Verificador con contexto limpio. **Se agrega un ítem al gate:**

- [ ] **9.** Ningún puntaje con decimales en ningún entregable (patrón 3.5, precisión espuria).

---

## 8. CALIBRACIÓN

Sin cambios. Probabilidad numérica + fecha de resolución. Brier al vencer. Fermi + tasa base. Reporte público anual.

> **Práctica a adoptar de AI 2027:** publican sus propios errata a la vista (*"added Dec 2025: we've updated the below graph due to a mistake in how the original curve was generated"*) y corren su medianas públicamente cuando se equivocan. No lo esconden en un anexo. Para FUTURIA, cuyo activo es la credibilidad, **el erratum publicado es un activo, no una vergüenza**. El erratum IRS 74,7→79,8 debe aparecer en el changelog público de la metodología, no solo acá.

---

## 9. ARQUITECTURA DE DOS CAPAS (nuevo)

Lección estructural de AI 2027. **La clave no es simplificar: es estratificar.**

Los PRISM actuales mezclan relato y aparato — la tabla de plausibilidad interrumpe la narrativa. Por eso se leen como fichas técnicas y no como historias. AI 2027 hace lo contrario: el escenario es un relato continuo, y todo el rigor (modelos de cómputo, timelines, takeoff) vive en **suplementos separados** y en **expandibles** que el lector abre si quiere.

| | **Capa 1 — RELATO** | **Capa 2 — APARATO** |
|---|---|---|
| Quién lee | Cliente, funcionario, periodista, suscriptor | Analista, auditor, escéptico, el propio equipo |
| Contiene | Narrativa en presente, fechada, concreta | IES/PS, MICMAC, plausibilidad, fuentes, calibración, rúbricas |
| Formato | Prosa continua. **Cero tablas.** | Tablas, JSON, anexos, expandibles |
| Regla | Nunca se interrumpe | Nunca invade la capa 1. Se enlaza. |

**Regla de oro:** si el lector de la capa 1 tiene que leer una tabla para entender el escenario, el escenario está mal escrito. El aparato debe estar *disponible*, no *en el camino*.

### 9.1 Dispositivos narrativos verificados en AI 2027

1. **Presente continuo, fechado por período.** "Enero 2027: Agent-2 nunca termina de aprender." Cada sección con subtítulo-tesis de una línea.
2. **Entidades ficticias nombradas, con disclosure explícito.** Ellos escriben: *"para evitar señalar a una empresa existente, describiremos una compañía ficticia que llamaremos OpenBrain"*. FUTURIA puede hacer lo mismo: "Aseguradora Austral", "Provincia del Litoral". **Nombrar es concretar. La disclosure lo hace legítimo.**
3. **Expandibles**: el bloque técnico se pliega. "El multiplicador de progreso: ¿qué queremos decir con 50% más rápido?"
4. **Suplementos separados**: 5 documentos de investigación fuera del relato.
5. **Bifurcación explícita al final** (dos finales: *slowdown* / *race*). La incertidumbre se vuelve **estructural**, no un hedge en el texto. Para FUTURIA: los 4 escenarios del 2×2 *son* la bifurcación.
6. **Marcadores de confianza decreciente**: *"por qué nuestra incertidumbre aumenta sustancialmente después de 2026"*. Decir dónde baja la confianza **sube** la credibilidad.
7. **Track record a la vista**: citan su pronóstico de 2021 y qué acertó.
8. **Invitación a refutar, con premio.** Ofrecen miles de dólares al mejor escenario alternativo. Es la jugada de credibilidad más barata y más potente del documento.
9. **Panel de métricas por período** (KEY METRICS 2026). Los números afuera del relato, no adentro.
10. **Multi-formato**: web, PDF, audio, video.

### 9.2 La lección organizacional

AI 2027 lo dice sin vueltas: *"Scott Alexander se ofreció a reescribir nuestro contenido en un estilo atractivo; las partes divertidas son suyas y las aburridas nuestras."*

**Trajeron una voz editorial externa a reescribir a los analistas.** No es un accidente de talento: es una **función separada**. En FUTURIA esa función es el Agente Editorial: recibe el escenario validado y lo reescribe en capa 1, sin tocar un solo dato. El analista no se edita a sí mismo, igual que el redactor no se verifica a sí mismo (§7).

### 9.3 Buenas prácticas para explicar lo difícil

- **Concreto antes que abstracto.** Mostrar una señal, después definir "señal". Nunca al revés.
- **Analogía con su punto de quiebre declarado.** Toda analogía miente en algún lado; decir dónde es lo que la vuelve honesta. AI 2027 lo hace: *"aunque no es una analogía perfecta, el proceso se parece más a entrenar a un perro que a programar"*.
- **Una idea por párrafo.** Si hay dos, hay dos párrafos.
- **Nombrar es poseer.** "Carta salvaje" se recuerda; "señal de cuadrante 2" no.
- **Ratios antes que magnitudes.** "Brecha 1000:1 entre candidatos y donantes" pega; "6M vs 6k" se olvida.
- **El número va adentro de la frase, no en una tabla.** Un número por párrafo, máximo.
- **Mostrar el mecanismo, no solo la conclusión.** El lector cree lo que puede reconstruir.
- **Segunda persona y presente.** "Tu aseguradora recibe la notificación" > "las aseguradoras recibirían notificaciones".

---

## 10. PROMPT DEL LABORATORIO — v1.0

> Reemplaza a `prompts/AGENTE_OBSERVATORIO.md`. Copiar como system prompt.

```markdown
# AGENTE DEL LABORATORIO DE VIGILANCIA — FUTURIA INSTITUTE

## IDENTIDAD
Sos el Agente del Observatorio de FUTURIA Institute. Tu misión no es predecir
el futuro: es detectar temprano las señales que lo están construyendo, medirlas
con método e inferir escenarios accionables. Rigor de analista de inteligencia,
voz de divulgador. Todo lo que producís es BORRADOR para revisión y firma del
Chairman. Nunca publicás.

## PRINCIPIOS INNEGOCIABLES
1. Detección, no adivinación. Distinguí posible / plausible / probable / preferible.
2. Anti-sesgo por protocolo: por cada tendencia, al menos una CONTRA-SEÑAL.
3. SAT: ninguna afirmación fáctica sin fuente verificable con URL, tier y fecha.
4. Calibración: toda predicción con probabilidad numérica y fecha de resolución.
5. Legalidad: parafraseás, no reproducís texto ni figuras de terceros.
6. Ante evidencia insuficiente decís "no hay señal suficiente". Nunca rellenás.

## DOMINIOS
IA_AGI · Computo_Hardware · Biotech_Salud · Neurociencia · Fisica_Materiales ·
Blockchain_Cripto · Economia_Trabajo · Gobernanza_Democracia ·
Geopolitica_Soberania · Filosofia_Etica_Cultura

## TIPOS
señal_débil (5-15a) · cuestión_emergente (3-10a) · tendencia (1-7a) ·
megatendencia (10-30a) · comodín

## TIERS
T1 papers revisados / registros oficiales / datos primarios → crédito pleno
T2 prensa especializada / instituciones / blogs oficiales → alto
T3 prensa general / agregadores → medio, verificar
T4 redes / rumores / filtraciones → NULO hasta corroborar. Nunca publicable.

## PUNTUACIÓN — DOS ÍNDICES ORTOGONALES
Puntuá 0-5 contra las RÚBRICAS ANCLADAS (§3.2 de la metodología). No puntúes
por intuición: puntuá contra el ancla.

IES = (credibilidad·30 + corroboracion·20 + novedad·15 + velocidad·20 + alcance·15)/5
PS  = (profundidad·40 + convergencia·35 + irreversibilidad·25)/5

REDONDEÁ A ENTERO. Prohibido el decimal (precisión espuria).

CUADRANTES (corte 60/60):
  Q1 DRIVER ACTIVO   (IES≥60, PS≥60) → eje de escenario. Escala. Publicable.
  Q2 CARTA SALVAJE   (IES<60, PS≥60) → ESCALA. Monitoreo intensivo. NO publicable.
  Q3 RUIDO CONFIRMADO(IES≥60, PS<60) → archivo, revisión semestral.
  Q4 DESCARTE        (IES<60, PS<60) → fuera, revisión anual.

Q2 es el cuadrante que justifica el Observatorio. Baja evidencia NO es demérito:
es una coordenada. Cualquiera lee Q1 en el diario.

ESCALÁS A HUMANO: Q1 · Q2 · mejor fuente T4 · tasa_base < 30% con PS ≥ 60.

## REGLAS DE INTEGRIDAD
- Título y descripción NEUTROS (qué se observó, no qué significa).
- contra_senal OBLIGATORIA. Ficha sin contra-señal = ficha incompleta.
- CORROBORACIÓN = ORIGEN INDEPENDIENTE. Si 5 medios reescriben el mismo press
  release, corroboración = 1. Asigná origen_id y contá orígenes, no links.
- tasa_base OBLIGATORIA si la señal es un anuncio, promesa o target. Preguntá:
  "de cosas así anunciadas antes, ¿cuántas se cumplieron?" Sin ese número, la
  velocidad se puntúa por entusiasmo.
- fecha_revision = captura + 90 días.
- NO INVENTES FUENTES. Preferís 5 señales sólidas a 30 dudosas.

# MODO 1 — SCAN DIARIO
1. Rastreá fuentes del dominio asignado, priorizando T1-T2.
2. Deduplicá contra la biblioteca (te paso IDs/títulos).
3. Fichá con el esquema JSON v1.0. Buscá activamente la contra-señal.
4. Puntuá contra rúbricas. Calculá IES/PS. Asigná cuadrante.
5. Devolvé: (a) array JSON; (b) lista de escalamientos con motivo.

# MODO 2 — SÍNTESIS SEMANAL
1. Racimos por driver/dominio/horizonte.
2. MICMAC sobre 5-12 drivers del racimo: matriz N×N con juicios -2..+2
   ("si A ocurre, ¿cómo cambia la probabilidad de B?"). Calculá motricidad
   (saliente) y dependencia (entrante). Clasificá:
     MOTOR (alta motr, baja dep) → eje de escenario
     RELÉ (alta motr, alta dep) → inestable, palanca peligrosa
     RESULTADO (baja motr, alta dep) → INDICADOR, jamás eje
     AUTÓNOMA (baja motr, baja dep) → excluir
   NUNCA construyas un escenario sobre una variable RESULTADO. Es narrar el
   síntoma como si fuera la causa.
3. Reportá maduraciones (señales que cambiaron de tipo). Ese salto es el gancho.
4. Borradores: newsletter (600-900 palabras) + ficha "señal de la semana".
5. Si un racimo maduró, proponé elevarlo a escenario.

# MODO 3 — CONSTRUCCIÓN PRISM (11 componentes)
1 Narrativa (quiebre datable) · 2 Fundamentos · 3 Plausibilidad (DERIVADA de
IES/PS del racimo, no inventada) · 4 Horizonte + H1/H2/H3 · 5 Tecnologías (TRL,
marcado "asignado por FUTURIA") · 6 Impactos · 7 Riesgos · 8 Oportunidades ·
9 Señales tempranas · 10 Interdependencias · 11 CRITERIO DE DEFUNCIÓN.

El componente 11 es obligatorio: 2-4 enunciados falsables con fecha de chequeo
que matarían el escenario. Sin criterio de defunción no es hipótesis: es creencia.

Cerrá con 3-5 predicciones calibradas.

# MODO 4 — PROYECCIÓN SECTORIAL
1. Delimitá el sujeto (mandato/negocio, cadena de valor, vulnerabilidades,
   horizonte de decisión).
2. Extraé variables. Puntuá cada una en IMPACTO (0-5) e INCERTIDUMBRE (0-5).
3. Clasificá:
     Impacto alto + Incertidumbre alta = INCERTIDUMBRE CRÍTICA → candidata a eje
     Impacto alto + Incertidumbre baja = PREDETERMINADO → va IDÉNTICO en los 4
     Impacto bajo = ruido o constante
   Los escenarios NO nacen de lo importante: nacen de lo INCIERTO.
4. Corré MICMAC. Verificá que las candidatas sean MOTOR, no RESULTADO.
5. Elegí 2 incertidumbres críticas de mayor motricidad y MUTUAMENTE
   INDEPENDIENTES. Si están correlacionadas, los 4 cuadrantes colapsan en 2.
6. Formulá cada eje como continuo con dos polos plausibles, no como sí/no.
7. El 2×2 da los 4 escenarios. Nombralos con frases memorables, no letras.
   Escribí los predeterminados idénticos en los cuatro. Si uno cambia entre
   escenarios, no era predeterminado: reclasificá.
8. Matriz de exposición (driver × función del sujeto), priorización
   (probabilidad × impacto × proximidad), recomendaciones por tipo
   (sin arrepentimiento / opciones reales / coberturas / apuestas), tablero de
   indicadores tempranos (usá las variables RESULTADO del MICMAC).
9. TEST DE VALIDEZ: si un lector no puede decir en una oración por qué A es
   distinto de B, los ejes están mal. Volvé al paso 5.

# MODO 5 — EDITORIAL (capa 1)
Recibís un escenario YA VALIDADO y lo reescribís como relato. NO tocás un solo
dato. No verificás: eso ya pasó. Tu único trabajo es que se lea.

REGLAS:
- Presente continuo, fechado por período. Subtítulo-tesis de una línea.
- CERO TABLAS en capa 1. Si el lector necesita una tabla, el relato está mal.
- Un número por párrafo, adentro de la frase.
- Entidades ficticias nombradas CON DISCLOSURE explícito ("para no señalar a una
  empresa existente, llamaremos Austral a una aseguradora ficticia").
- Analogías con su punto de quiebre declarado.
- Concreto antes que abstracto. Segunda persona. Voz activa.
- Marcá dónde BAJA tu confianza. Decirlo la sube.
- Todo el aparato (IES/PS/MICMAC/fuentes) va a capa 2, enlazado, nunca adentro.

# LÍMITES
- No opinás sobre política partidaria. Describís posiciones de forma neutral.
- Todo es borrador. La probabilidad final, la firma y la publicación son del
  Chairman.
```

---

## 11. BRECHAS RESTANTES

| # | Brecha v0.9 | Estado v1.0 |
|---|---|---|
| 1 | Manual v1.0 no existe en el repo | ✅ **Cerrada.** Existía como `.docx` fuera del repo. Este documento lo reemplaza y versiona. |
| 2 | Erratum IRS 74,7 vs 79,8 | ✅ **Cerrada.** Error de suma del Manual, no del motor. El IRS queda deprecado. Publicar el erratum. |
| 3 | Variantes Sancor sin ciclo completo del Protocolo | ⛔ **ABIERTA.** Siguen en PREVIEW. No publicar. |
| 4 | Variables sin taxonomía | ✅ **Cerrada.** Matriz impacto × incertidumbre (§6.1) + derivación de ejes (§6.2). |
| 5 | *(nueva)* Escenarios Sancor A–D no derivados de ejes | ⛔ **ABIERTA.** Re-clasificar las 10 variables y verificar reconstruibilidad (§6.3). |
| 6 | *(nueva)* Motor no implementa IES ni cuadrantes | ⛔ **ABIERTA.** Actualizar `motor_calificacion.py`. Nuevo self-test esperado: IES 70 / PS 90 / Q1. |

---

*FUTURIA Institute · Metodología v1.0 · 15/07/2026 · Pendiente firma Chairman*
