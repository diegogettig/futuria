# MODELO «PARTE FUTURIA»
## Especificación del informe quincenal de tendencias · v1.0

> Producto nuevo. No es el Lab (Flujo 1), no es Convergencia (Flujo 2), no es un PRISM.
> **Firma del Chairman:** ____________ **Fecha:** ___________

---

## 0. CORRECCIONES AL PROMPT DE ORIGEN

Antes de la especificación, tres rectificaciones. El prompt que originó este pedido contiene errores que, de no corregirse, se vuelven canónicos en el producto nuevo.

### 0.1 Las clases SAT estaban mal definidas

El prompt dice: *«clase N/E/D/T/P (numérico / estructural / derivado / tendencia / proyección)»*. **Esas son las definiciones alucinadas** — las mismas que el agente inventó en el Informe Sancor v2 y que se rectificaron en su Anexo E.4. Las correctas:

| Clase | Definición real | Fuente autoritativa | Exigencia |
|---|---|---|---|
| **N** | **Normativa** — leyes, decretos, resoluciones, disposiciones, expedientes | Boletín Oficial · InfoLEG · SAIJ · sitio del organismo | Link oficial funcional. Sin excepción. |
| **E** | **Evento fáctico** — algo que ocurrió | Comunicado oficial, paper, registro, prensa T1-T2 | Dos fuentes independientes o una T1. |
| **D** | **Dato cuantitativo** — cifras, mercados, porcentajes | Organismo estadístico, paper, informe institucional | Fuente + año + universo. |
| **T** | **Técnica** — TRL, resultados de ensayo, especificaciones | Paper revisado, preprint, registro de ensayo | Cita académica completa. |
| **P** | **Proyección** — inferencia propia | **Ninguna. Es nuestra.** | Declarada como proyección FUTURIA, con supuesto explícito. |

La diferencia no es cosmética: **la clase N existe para forzar el link al Boletín Oficial en toda cita normativa.** Es el control que atrapa el patrón «norma fantasma» (ANMAT 4359/2025). Si N pasa a significar «numérico», ese control desaparece y las normas inventadas entran sin filtro.

### 0.2 Los tokens estéticos no coinciden con la landing

El prompt indica `#0d1419` / `#e90100` / `#e8eef2`. La landing en producción usa un fondo más cercano a `#0A0A0D` y un rojo `#FF1240`. **Son dos paletas distintas.** Esta especificación adopta los tokens del prompt por ser los declarados, pero la discrepancia debe resolverse antes del Parte #001: dos rojos institucionales es no tener ninguno.

### 0.3 «Bloque visual» es una mala idea

El prompt pide *«un bloque visual»*. Un bloque de visuales es un depósito: el lector lo saltea porque no sabe qué mira. **Los visuales van interleaved**, uno por sección como máximo, pegados al párrafo que los motiva. Ver §5.

---

## 1. EL HALLAZGO QUE DEFINE EL PRODUCTO

Antes de nombrar nada, hay que resolver un problema que atraviesa a los ocho escenarios semilla y que, si no se resuelve, hace **impublicable** el producto.

### 1.1 Los PRISM están llenos de empresas reales haciendo cosas que no hicieron

Del PRISM #006, textual:

> *«Primer CaaS comercial (Bivacor + Munich Re + Cleveland Clinic) — 100 pacientes, $3.5k/mes, todo incluido.»*

Bivacor existe. Munich Re existe. Cleveland Clinic existe. **El acuerdo no existe.** Es una proyección del escenario.

Dentro de un PRISM —documento interno, técnico, leído por analistas que entienden que están viendo un escenario— eso es tolerable. **Publicado a un público amplio, es otra cosa:** es atribuirle a tres organizaciones reales un producto, un precio y una fecha que nunca anunciaron. Es el patrón 3.3 del Protocolo —*entidad real, hecho falso*— en su forma más peligrosa, porque la verificación superficial confirma que las tres empresas existen y da luz verde al enunciado completo.

Y no es un caso aislado. El mismo escenario proyecta emisiones financieras, aprobaciones regulatorias y un ataque de ransomware, todos con actores reales identificados.

### 1.2 La regla del actor ficticio

Es exactamente el problema que AI 2027 resolvió, y su solución es la que adoptamos. Ellos escriben, sin vueltas: *«para evitar señalar a una empresa existente, describiremos una compañía ficticia que llamaremos OpenBrain»*.

**Regla dura del Parte:**

| Situación | Tratamiento |
|---|---|
| Empresa real, hecho que **efectivamente ocurrió**, con fuente | Se la nombra y se la cita con link. |
| Empresa real, hecho **proyectado** por el escenario | **Actor ficticio + disclosure explícito.** Nunca se nombra a la real. |
| Empresa real como **contexto de capacidad actual** | Se la nombra solo para lo que ya hace, con fuente. |

El disclosure va **visible en el cuerpo**, no en una nota al pie:

> *«Para no atribuirle a ninguna empresa existente un movimiento que no anunció, vamos a llamar Meridian al primer proveedor que lance el modelo.»*

Nombrar concreta —por eso AI 2027 funciona—. El disclosure es lo que lo vuelve legítimo.

### 1.3 Por qué esto define el producto

Porque establece la operación central del Parte: **no es un resumen del PRISM, es una traducción con cambio de régimen de verdad.** El PRISM opera en modo escenario, donde todo es hipótesis declarada. El Parte opera en modo público, donde el lector no distingue una hipótesis de una noticia salvo que se lo digas en cada párrafo.

Esa traducción es el trabajo. Todo lo que sigue lo instrumenta.

---

## 2. NOMBRE

**Propuesta: «PARTE».** Numerado: *Parte #001*, *Parte #002*. Marca completa: *Parte FUTURIA*.

Un parte es lo que emite un observatorio a intervalo fijo. Parte meteorológico, parte médico: en el Río de la Plata la palabra ya significa «informe periódico de quien observa algo con instrumentos». Es sobrio, es institucional, es corto, y es lo contrario de un newsletter. Encaja con la analogía madre ya establecida en el material divulgativo (*FUTURIA como servicio meteorológico del futuro*), y cierra el trío del ecosistema con ritmo propio:

> **El Lab observa. El PRISM descompone. El Parte informa.**

### Objeciones a las dos opciones del prompt

**«Informe de Señal»** colisiona con el vocabulario del Flujo 1. En FUTURIA, *señal* es la unidad atómica del Lab: tiene ficha, IES, PS, contra-señal y cuadrante. Un producto divulgativo llamado «Informe de Señal» hace pensar que reporta señales, cuando reporta escenarios. El costo de esa ambigüedad se paga en cada conversación interna, para siempre.

**«Brief de Tendencia»** es un anglicismo en un instituto que publica en español para LATAM, y «tendencia» es además un tipo de señal específico dentro de la taxonomía (señal débil → cuestión emergente → **tendencia** → megatendencia). Misma colisión, más ruido.

**Alternativas si PARTE no convence:** *Espectro* (el PRISM descompone, el Espectro muestra una banda) o *Corte* (una sección vertical del futuro). Ambas conceptualmente sólidas, ambas con más riesgo de homonimia.

---

## 3. IDENTIDAD DEL PRODUCTO

| Atributo | Definición |
|---|---|
| **Qué es** | Inmersión narrativa quincenal en **un** escenario PRISM, para público amplio. |
| **Qué no es** | No es alerta, no es resumen, no es informe de cliente, no es noticia de tecnología. |
| **Lector** | Decisor, profesional, curioso culto. Inteligente, sin tiempo, sin jerga del campo. |
| **Cadencia** | Cada 15 días. Fija. La frecuencia sostenida *es* la credibilidad. |
| **Extensión** | 1.800–2.500 palabras de Capa 1. Lectura 9–12 min. |
| **Semilla** | Un PRISM (#002–#009 disponibles). Un Parte, un escenario. |
| **Rol en el embudo** | Es la vidriera. El PRISM es interno y técnico; Convergencia es pago. El Parte es lo único que el mercado ve. |
| **Prueba de éxito** | Que un ejecutivo lo termine y piense *«esta gente debería hacer esto para nosotros»*. |

---

## 4. ESTRUCTURA

Siete secciones fijas. **Fijas es la palabra**: la repetición construye ritual, el lector aprende la forma y sabe dónde está parado. AI 2027 hace lo mismo con sus encabezados por mes.

### 1 · LA ESCENA
El momento de quiebre del PRISM, dramatizado. Presente, fechado, concreto, con un actor (ficticio si corresponde) y una consecuencia física. **Sin contexto, sin preámbulo, sin carraspeo.** Se tira al lector adentro.
*Propósito:* que siga leyendo. *Extensión:* 200–300 palabras. *Prohibido:* explicar qué es FUTURIA, qué es PRISM, o por qué el tema importa.

### 2 · EL PRESENTE
El giro: qué de todo eso **ya existe**. Es la sección de la credibilidad, y por eso es donde vive la mayor densidad de citas verificadas con link. Sin esta sección, la anterior es ciencia ficción.
*Propósito:* convertir el asombro en atención. *Regla:* toda afirmación acá es clase E, D o T con fuente. Cero P.

### 3 · LA MECÁNICA
Cómo funciona. El corazón explicativo. Analogías con su punto de quiebre declarado. Es donde se enseña.
*Propósito:* que el lector pueda reconstruir el argumento solo. *Regla:* un concepto técnico se explica la primera vez o no se usa.

### 4 · LOS FRENOS
Qué podría impedirlo. **Sección obligatoria, nunca opcional.** Contra-señales, cuellos de botella técnicos, resistencias regulatorias y culturales.
*Propósito:* es lo que separa a FUTURIA de un blog de hype. Un informe sin frenos no es análisis: es entusiasmo con tipografía. *Regla:* mínimo tres frenos, cada uno con su fundamento.

### 5 · EL TABLERO
Qué mirar para saber si esto está pasando. Las señales tempranas del PRISM, traducidas a observables que el lector puede rastrear él mismo.
*Propósito:* devolverle agencia al lector y **retroalimentar el Lab** (ver §9). *Formato:* la única lista tolerada de la Capa 1.

### 6 · Y ENTONCES QUÉ
Implicancias por tipo de lector: quien decide, quien ejerce, quien mira. Concreto, sin consejos genéricos.
*Propósito:* responder la pregunta que el lector tiene desde el párrafo uno.

### 7 · EL APARATO *(Capa 2)*
Fuentes con link, veredictos por claim, clase SAT, metodología, criterio de defunción del escenario semilla, y qué es proyección y qué es hecho.
*Propósito:* que cualquier afirmación sea rastreable — o que se vea con claridad dónde no hay origen.

---

## 5. ESTILO Y VISUALES

### 5.1 Reglas de escritura

- **Concreto antes que abstracto.** Se muestra una cosa, después se define la categoría. Nunca al revés.
- **Una idea por párrafo.** Si hay dos, hay dos párrafos.
- **Un número por párrafo**, adentro de la frase. Los números en fila van a la Capa 2.
- **Voz activa. Presente. Segunda persona cuando toca el bolsillo o el cuerpo del lector.**
- **Analogía con su punto de quiebre declarado.** Toda analogía miente en algún lado; decir dónde es lo que la vuelve honesta.
- **Marcá dónde baja tu confianza.** Decirlo la sube. AI 2027: *«por qué nuestra incertidumbre aumenta sustancialmente después de 2026»*.
- **Cero tablas en Capa 1.** Si el lector necesita una tabla para entender, el relato está mal escrito.
- **Prohibido:** «cabe destacar», «en un mundo cada vez más», «revolucionario», «disruptivo» (sí, aunque el PRISM lo diga), «el futuro ya llegó».

### 5.2 Visuales

Uno por sección como máximo, **interleaved**, pegado al párrafo que lo motiva. Nunca agrupados.

| Tipo | Dónde | Qué comunica |
|---|---|---|
| **Diagrama de mecanismo** | §3 Mecánica | Cómo funciona la cosa. El visual más importante del Parte. |
| **Línea de tiempo** | §1 o §5 | Hitos del escenario, distinguiendo pasado verificado de futuro proyectado. |
| **Comparación antes/después** | §3 | El cambio de modelo (ej.: comprar vs. suscribir). |
| **Mapa de bloques** | §2 o §6 | La fractura geopolítica, cuando aplica. |
| **Radar de plausibilidad** | §7 Aparato | Las dimensiones del PRISM. Va en Capa 2, no en el relato. |

**Regla de honestidad visual:** todo gráfico que mezcle hecho y proyección debe distinguirlos gráficamente —línea sólida para lo ocurrido, punteada para lo proyectado— y decirlo en el epígrafe. Un gráfico que presenta una proyección con la misma tinta que un dato es una alucinación visual, y es peor que la textual porque no se lee: se cree.

**Producción:** programática (SVG generado desde datos), no diseño manual pieza por pieza. Si no se puede automatizar, no entra al modelo.

**Fuentes de figuras:** epígrafe con fuente y link. Nunca se reproduce una figura ajena; si el dato sirve, se re-grafica con datos propios y se cita el origen.

---

## 6. CITAS

**Formato inline:** el link va en la palabra que nombra el hecho, no en un «(ver aquí)». Al final, bloque de fuentes numerado con: autor/editor, título, medio, fecha, URL, fecha de consulta y **tier**.

**Regla del origen independiente:** cinco medios que reescriben el mismo comunicado son **una** fuente. Se cuentan orígenes, no links.

**Regla dura:** ningún caso concreto entra al Parte sin fuente real accesible. Si no hay fuente, hay dos caminos y ninguno es inventar:
1. **Actor ficticio + disclosure** (si es proyección del escenario).
2. **«Sin información disponible»** visible en el cuerpo (si es un hueco).

---

## 7. FLUJO DE PRODUCCIÓN (14 días)

| Día | Etapa | Responsable |
|---|---|---|
| 1–2 | Selección de semilla + **ángulo**. Un PRISM tiene diez ángulos; el Parte elige uno. | Chairman |
| 3–5 | Borrador narrativo Capa 1 | Agente Editorial |
| 6–8 | Extracción de claims → lista plana → **verificación SAT** | Agente Extractor → **Verificador (contexto limpio)** |
| 9 | Ronda de adversario sobre los VERIFICADO | Agente Adversario |
| 10 | Correcciones. Aplicación de actor ficticio donde corresponda. | Agente Editorial |
| 11 | Visuales (SVG programático) | Agente Editorial |
| 12 | **Firma** | Chairman |
| 13 | Maquetado HTML | Agente Editorial |
| 14 | Publicación + **alta de señales nuevas en el Lab** | Agente Editorial |

**El verificador no ve el borrador.** Solo la lista de claims desnudos. La narrativa es persuasiva y contamina el juicio: es la diferencia entre auditar y leer.

**El editorial no verifica y el verificador no escribe.** Es la lección organizacional de AI 2027, que trajo una voz externa a reescribir a sus analistas y lo dice sin vueltas: *«las partes divertidas son suyas y las aburridas nuestras»*. La voz editorial es una **función separada**, no un talento.

---

## 8. ESPECIFICACIÓN HTML

- **Un solo archivo.** Sin dependencias externas. Sin CDN, sin Google Fonts: `system-ui` y stack de sistema.
- **Responsive.** Una columna, medida de lectura ~38rem, sin scroll horizontal en 360px.
- **Accesible.** Contraste AA mínimo, jerarquía `h1→h2→h3` real, `<figure>/<figcaption>`, `alt` en todo SVG, foco visible, `prefers-reduced-motion`.
- **Capa 2 en `<details>`** — plegada por defecto. Es la implementación HTML de los *expandables* de AI 2027: el rigor disponible, no en el camino.
- **Sin JS** salvo que sea imprescindible. El Parte tiene que leerse con JS desactivado.
- **Peso objetivo** < 150 kB con visuales.

### 8.1 Impresión — la decisión no obvia

```css
@media print { /* invertir a fondo claro */ }
```

**Pantalla oscura, impresión clara.** El fondo `#0d1419` en papel se come el tóner, se ve sucio y vuelve el texto ilegible en impresoras domésticas. La marca se sostiene con el rojo y la tipografía, no con el fondo.

La regla de impresión completa: fondo blanco, tinta negra, rojo institucional preservado en títulos, `<details>` **forzados a abiertos** (en papel no hay clic), links con la URL expandida vía `content: attr(href)`, nav y UI ocultos, `@page { size: A4; margin: 18mm }`, y `break-inside: avoid` en figuras y bloques de cita.

---

## 9. VÍNCULO CON EL ECOSISTEMA

```
    LAB (Flujo 1, diario)  ──señales──►  PRISM (escenarios)
         ▲                                     │
         │                                  semilla
    señales nuevas                             ▼
         │                              ►  PARTE (quincenal, público)
         └──────────────────────────────────┘
                                               │
                                          credibilidad
                                               ▼
                                     CONVERGENCIA (Flujo 2, pago)
```

**Hacia abajo:** cada Parte nace de un PRISM y elige **un ángulo**. Un escenario alimenta varios Partes a lo largo del año; no se agota en uno.

**Hacia arriba:** cada Parte devuelve al Lab las señales que su §5 Tablero define como observables, dadas de alta con `origen: parte_<nn>`. **Publicar obliga a mirar.** Un Parte que no genera al menos dos señales nuevas para el Lab no investigó: resumió.

**Hacia adelante:** el Parte es la muestra gratuita del método. Un lector que vio a FUTURIA razonar sobre longevidad en público es un lector que entiende qué compra cuando compra un Convergencia.

---

## 10. CHECKLIST ANTI-ALUCINACIÓN DEL PARTE

Once ítems binarios. No hay «casi».

- [ ] **1.** Toda afirmación clasificada N/E/D/T/P **según las definiciones de §0.1** (no las del prompt original).
- [ ] **2.** Cero claims clase N sin link oficial funcional. **Cero es cero.**
- [ ] **3.** Todos los links abiertos y confirmados en las últimas 72 h.
- [ ] **4.** Toda cifra con fuente + año + universo.
- [ ] **5.** Toda proyección declarada como proyección — del escenario o de FUTURIA.
- [ ] **6.** **Ningún hecho proyectado atribuido a una organización real.** Actor ficticio + disclosure visible en el cuerpo.
- [ ] **7.** Corroboración contada por origen independiente, no por cantidad de links.
- [ ] **8.** §4 Frenos presente, con mínimo tres, cada uno fundado.
- [ ] **9.** Todo gráfico distingue hecho de proyección gráficamente y lo dice en el epígrafe.
- [ ] **10.** Verificador de contexto limpio ejecutado + ronda de adversario documentada.
- [ ] **11.** Señales nuevas dadas de alta en el Lab (mínimo dos).

**Firma del Chairman:** ____________ **Fecha:** ___________

---

## 11. RIESGO REGISTRADO

El prompt de origen pide *«desarrollar a profundidad divulgativa»* los escenarios PRISM. Corresponde marcar el riesgo con claridad:

**Los ocho PRISM no están verificados.** Son pruebas de concepto de la metodología, redactadas antes del Protocolo Anti-Alucinación y sin pasar su ciclo. Contienen cifras sin fuente, normas con número específico y sin link, y —como se documentó en §1.1— empresas reales ejecutando movimientos que no anunciaron.

**Consecuencia operativa:** el Parte **no puede tratar al PRISM como fuente.** El PRISM es la **semilla del ángulo narrativo**, no evidencia. Cada afirmación fáctica del Parte se verifica desde cero contra fuente primaria, aunque aparezca en el escenario.

Un ejemplo concreto, del propio PRISM #006:

> *«Propiedad TAH: proveedor = dueño (arrendamiento vitalicio); paciente = licenciatario; **inembargable (Ley 27.890 AR** / MDR UE Art. 5)»*

Un número de ley argentina, con formato correcto, otorgando inembargabilidad a órganos artificiales. Es un claim **clase N**. Tiene la firma exacta del patrón «norma fantasma»: formato impecable, número plausible, atribución específica, cero link. Es el mismo perfil que ANMAT 4359/2025.

**Hasta que ese número no se resuelva contra el Boletín Oficial, no puede aparecer en un Parte.** Y si no existe, corresponde revisar cuántas de las otras normas citadas en los ocho escenarios comparten el mismo origen.

---

*FUTURIA Institute · Modelo PARTE v1.0 · Julio 2026 · Pendiente firma del Chairman*
