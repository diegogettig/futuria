# PROTOCOLO DE VALIDACIÓN ANTI-ALUCINACIÓN
## FUTURIA Institute · Informes PRISM · v1.0

> **Regla fundacional:** una afirmación sin fuente verificada no se corrige ni se suaviza. Se marca o se elimina. No existe la categoría "probablemente correcto".

---

## 0. POR QUÉ ESTO EXISTE

Un informe de prospectiva que cita una disposición ANMAT inexistente ante una institución argentina que puede consultar el Boletín Oficial en 30 segundos no pierde un cliente: pierde la licencia moral para llamarse instituto. La credibilidad es el único activo de FUTURIA y es de acumulación lenta y destrucción instantánea.

Este protocolo es un **portón (gate)**, no una sugerencia. Ningún informe sale sin pasarlo.

---

## 1. TAXONOMÍA DE AFIRMACIONES

Todo enunciado de un informe pertenece a una de cinco clases. Cada clase tiene una fuente autoritativa distinta y un nivel de exigencia distinto.

| Clase | Ejemplo | Fuente autoritativa | Exigencia |
|---|---|---|---|
| **N — Normativa** | "Disposición ANMAT 4359/2025", "Ley 25.326", "expediente 4356-D" | Boletín Oficial, InfoLEG, SAIJ, sitio del organismo, HCDN/Senado | **Máxima.** Link directo al texto oficial + fecha de publicación. Sin excepción. |
| **E — Evento fáctico** | "eGenesis implantó el primer xenocorazón en 2025" | Comunicado oficial, paper, registro público, prensa T1-T2 | Alta. Dos fuentes independientes o una T1. |
| **D — Dato cuantitativo** | "64M de pacientes con HF global", "$1,2M costo de trasplante" | Organismo estadístico, paper revisado, informe institucional | Alta. Fuente + año del dato + metodología si es estimación. |
| **T — Técnica** | "TRL 6-7", "supervivencia 61 días en babuino" | Paper revisado, preprint, registro de ensayo | Alta. Cita académica completa. |
| **P — Proyección** | "TAH < $80k unidad para 2030" | **Ninguna. Es inferencia propia.** | Debe declararse como proyección FUTURIA, con supuesto y método explícitos. |

**El error de categoría más común y más grave:** presentar una **P** con el tono de una **N** o una **D**. Una proyección propia disfrazada de dato es una alucinación aunque el número sea razonable.

---

## 2. LOS TRES VEREDICTOS

Cada afirmación termina en uno de tres estados. No hay un cuarto.

### ✅ VERIFICADO
Existe fuente autoritativa, el link funciona, la fecha coincide, la cifra coincide. Se publica con su cita.

### ⚠️ ILUSTRATIVO
No hay información pública disponible, pero el enunciado tiene valor analítico. Se publica **con etiqueta visible en el cuerpo del texto**, no en una nota al pie:

> `[ILUSTRATIVO — sin información disponible]`

Reglas del ilustrativo:
- Nunca se usa para números normativos. **No existe una "disposición ilustrativa".** Un número de norma inventado no es ilustrativo: es falso. Va a ELIMINAR.
- Se admite para escenarios, ejemplos hipotéticos y magnitudes de orden ("del orden de los cientos de millones").
- Si un informe tiene más de un 15% de contenido ilustrativo, no está listo: está especulando.

### ❌ ELIMINAR
La afirmación es falsa, no verificable, o cita una fuente inexistente. Se borra. **No se reescribe con hedging** ("se estima que...", "algunas fuentes indican..."). Esa maniobra convierte una alucinación en una alucinación evasiva, que es peor porque es indetectable.

---

## 3. PATRONES DE ALUCINACIÓN A CAZAR

Detectados en PRISM #001. Estos son los que el verificador busca activamente:

### 3.1 Norma fantasma
Número de disposición, resolución o ley con formato correcto pero inexistente. Ejemplo: `ANMAT 4359/2025`.
**Por qué es letal:** el formato es perfecto, así que pasa cualquier lectura casual. Solo cae contra el registro oficial.
**Verificación:** buscar el número exacto en el sitio del organismo Y en Boletín Oficial. Si no aparece en ninguno, no existe. La ausencia de resultado **es** el resultado.

### 3.2 Expediente inventado
Ejemplo: `4356-D`, `2201-B`, `0872-E`.
**Verificación:** los expedientes de Diputados y Senado son consultables por número en los sitios oficiales de trámite parlamentario. Sin registro, se elimina.

### 3.3 ⚠️ Entidad real, hecho falso (la más peligrosa)
El caso del "hospital italiano de Buenos Aires". **El Hospital Italiano de Buenos Aires existe y es una institución de primer nivel.** Lo alucinado no es el hospital: es el hecho que se le atribuyó.
Este es el patrón más difícil de detectar porque la verificación superficial "confirma" la entidad y da luz verde al enunciado completo. **Regla: se verifica el hecho atribuido, no la existencia del actor.** Que Pfizer exista no valida que Pfizer haya anunciado algo.
Corolario: nunca se atribuye una acción, declaración o resultado a una institución real sin fuente de esa institución o de un tercero T1-T2 que lo reporte.

### 3.4 Cita zombi
Paper, autor o revista con formato académico impecable y DOI plausible que no existe, o que existe pero no dice lo que se le atribuye.
**Verificación:** resolver el DOI. Abrir el abstract. Confirmar que la afirmación esté efectivamente ahí.

### 3.5 Precisión espuria
"El 42% aceptaría un corazón artificial" sin encuesta rastreable. La precisión decimal genera falsa autoridad.
**Regla:** todo porcentaje lleva encuestadora, año, N y universo. Sin eso, o se elimina o pasa a orden de magnitud ilustrativo.

### 3.6 Fecha a la deriva
El hecho existe pero el año está corrido. Frecuente y subestimado: destruye la credibilidad de un informe de prospectiva, donde las fechas *son* el producto.

---

## 4. EL CICLO MULTI-AGENTE (obligatorio)

El generador nunca se valida a sí mismo. Un modelo que produjo una alucinación tiende a confirmarla cuando se le pregunta. La separación de roles no es burocracia: es la única defensa que funciona.

```
[AGENTE REDACTOR]
      ↓ produce el informe con marcas de clase (N/E/D/T/P)
[AGENTE EXTRACTOR]
      ↓ disecciona: extrae TODA afirmación verificable a una lista plana
      ↓ salida: registro-fuentes.json (una fila por claim)
[AGENTE VERIFICADOR]  ← contexto limpio, NO ve el informe original
      ↓ recibe solo la lista de claims, sin narrativa ni justificación
      ↓ busca fuente para cada uno de forma independiente
      ↓ emite veredicto: VERIFICADO / ILUSTRATIVO / ELIMINAR
[AGENTE ADVERSARIO]
      ↓ toma los VERIFICADO y trata de refutarlos
      ↓ pregunta: ¿la fuente dice exactamente esto o algo parecido?
[CHAIRMAN]
      ↓ revisa el registro final, no el informe
      ↓ firma o rechaza
```

**Punto crítico del diseño:** el verificador trabaja **con contexto limpio**. No debe ver el informe ni el razonamiento del redactor, porque la narrativa es persuasiva y contamina el juicio. Solo ve claims desnudos. Es la diferencia entre auditar y leer.

**Regla del adversario:** su trabajo no es aprobar sino romper. Si no encontró nada en una ronda, no hizo bien su trabajo o el informe es sólido — y eso se decide mirando cuántos claims revisó, no cuántos aprobó.

---

## 5. REGISTRO DE FUENTES (estructura)

Una sola fuente de verdad que alimenta las tres variantes. Cada claim tiene ID estable; las variantes citan el mismo ID.

```json
{
  "claim_id": "C-001-017",
  "informe": "PRISM-2026-001",
  "clase": "N",
  "enunciado": "Texto exacto de la afirmación tal como aparece en el informe",
  "ubicacion": "Sección 2.3, párrafo 4",
  "veredicto": "ELIMINAR",
  "fuente": {
    "url": null,
    "organismo": "ANMAT",
    "identificador": "Disposición 4359/2025",
    "fecha_publicacion": null,
    "tier": null,
    "fecha_consulta": "2026-07-14"
  },
  "busquedas_realizadas": [
    "sitio ANMAT disposiciones 2025 — sin resultado",
    "Boletín Oficial 'Disposición 4359/2025' — sin resultado"
  ],
  "nota_verificador": "Número con formato válido, sin registro en ninguna fuente oficial. Norma fantasma (patrón 3.1).",
  "accion_aplicada": "Eliminado del cuerpo. Reemplazado por descripción del marco regulatorio general vigente, con cita a ANMAT.",
  "verificado_por": "agente-verificador-v1",
  "revisado_por_humano": true
}
```

**Por qué el campo `busquedas_realizadas` importa:** documenta la ausencia. Es lo que te permite defender, ante un cliente, que buscaste y no había — en lugar de que simplemente no miraste.

---

## 6. SISTEMA DE CITAS PARA LAS 3 VARIANTES

Un único registro, tres presentaciones. Nunca se re-investiga por variante: se re-presenta.

| Variante | Densidad de cita | Formato visible | Trata el ILUSTRATIVO |
|---|---|---|---|
| **Ejecutiva** | Baja | Superíndice numerado → anexo de fuentes al final | Etiqueta inline, sin excepción |
| **Técnica** | Alta | Cita autor-año inline + bibliografía completa + DOI | Etiqueta + explicación del vacío de información |
| **Política** | Media | Cita normativa completa inline (organismo, número, fecha, BO) | Etiqueta + señalamiento del vacío regulatorio como hallazgo |

**Nota sobre la variante Política:** el vacío de información no es una debilidad del informe, es un hallazgo. "No existe normativa argentina sobre X" es exactamente el tipo de dato que un funcionario necesita. Presentarlo como hallazgo, no como limitación.

---

## 7. FUENTES AUTORITATIVAS — ARGENTINA

| Tipo de claim | Fuente oficial |
|---|---|
| Leyes, decretos, resoluciones nacionales | Boletín Oficial de la República Argentina · InfoLEG · SAIJ |
| Disposiciones ANMAT | Sitio oficial ANMAT (argentina.gob.ar/anmat) + Boletín Oficial |
| Expedientes parlamentarios | HCDN (trámite parlamentario) · Senado de la Nación |
| Estadística oficial | INDEC |
| Normativa provincial (Santa Fe) | Boletín Oficial de la Provincia de Santa Fe |
| Ensayos clínicos | ClinicalTrials.gov · registro ANMAT |
| Normativa sanitaria comparada | FDA (fda.gov) · EMA (ema.europa.eu) |
| Papers | DOI resuelto · PubMed · arXiv/bioRxiv |

**Regla de oro para normativa:** si no está en Boletín Oficial, no es norma. Punto.

---

## 8. GATE DE PUBLICACIÓN

Ningún informe sale sin estos ocho ítems en verde. Es una lista binaria: no hay "casi".

- [ ] **1.** Toda afirmación clasificada (N/E/D/T/P) y presente en `registro-fuentes.json`.
- [ ] **2.** Cero claims clase N sin link oficial funcional. **Cero es cero.**
- [ ] **3.** Todos los links abiertos y confirmados en las últimas 72hs (no confiar en links de contexto previo).
- [ ] **4.** Toda cifra con fuente + año + universo.
- [ ] **5.** Toda proyección declarada como proyección FUTURIA, con supuesto explícito.
- [ ] **6.** Todo ILUSTRATIVO etiquetado en el cuerpo, no al pie. Contenido ilustrativo < 15% del total.
- [ ] **7.** Ronda de agente adversario ejecutada y documentada.
- [ ] **8.** Logo FUTURIA INSTITUTE en portada y pie de las tres variantes.

**Firma del Chairman:** _______________  **Fecha:** ___________

---

## 9. INSTRUCCIÓN PARA EL AGENTE VERIFICADOR

> Copiar como prompt del agente verificador. Contexto limpio: no le pases el informe.

```
Sos el AGENTE VERIFICADOR de FUTURIA Institute. Tu único trabajo es
determinar si cada afirmación de la lista adjunta tiene respaldo en una
fuente oficial verificable. NO ves el informe original y no lo necesitás.

Para cada claim:
1. Identificá su clase (N/E/D/T/P) y la fuente autoritativa que corresponde.
2. Buscá la fuente. Documentá TODAS las búsquedas, incluidas las que no
   dieron resultado.
3. Emitilo como VERIFICADO / ILUSTRATIVO / ELIMINAR según el protocolo.
4. Si es clase N y no aparece en el registro oficial: ELIMINAR. Sin
   excepción, sin importar cuán plausible sea el número.
5. Si el actor es real pero el hecho atribuido no tiene fuente: ELIMINAR.
   Verificá el HECHO, no la existencia del actor.
6. Devolvé el registro-fuentes.json completo.

REGLAS ABSOLUTAS:
- No inventes fuentes. Si no encontrás, escribí "sin resultado". La ausencia
  de evidencia es tu hallazgo más valioso, no un fracaso.
- No completes con conocimiento propio. Si no hay link, no está verificado.
- No suavices. Está prohibido reescribir un claim falso como "se estima que...".
- Ante la duda, ELIMINAR. El costo de omitir un dato cierto es cero.
  El costo de publicar uno falso es la institución.
```

---

*FUTURIA Institute · Documento interno de operación · v1.0 · Julio 2026*
*Este protocolo aplica a todo entregable, sin excepción de urgencia, cliente ni formato.*
