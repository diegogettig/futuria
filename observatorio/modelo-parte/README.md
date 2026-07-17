# PARTE FUTURIA — Informe quincenal de tendencias

Producto público del Instituto. Un PARTE = **una inmersión narrativa en un ángulo de un
escenario PRISM**. No es un resumen del PRISM: es una *traducción con cambio de régimen de
verdad* (modo escenario → modo público). El PRISM es semilla, nunca fuente.

## Archivos de este directorio

| Archivo | Qué es |
|---|---|
| `PROMPT-AGENTE-PARTE-v1.0.md` | **System prompt canónico** del Agente PARTE. Pegarlo como system prompt + adjuntar MODELO + demo + PRISM semilla. Prevalece sobre cualquier prompt anterior. |
| `MODELO-PARTE-FUTURIA-v1.0.md` | Especificación del producto: estructura de 7 secciones, reglas de estilo, vocabulario fijo, checklist de publicación de 11 ítems, flujo de 14 días. |
| `parte-001.html` | Esqueleto HTML de referencia (PRISM #006, ángulo "leasing del cuerpo"). 7 secciones + Capa 2 en `<details>` + CSS `@media print`. |

> **Nota de marca (corregida):** el rojo institucional FUTURIA es **`#e90100`** sobre fondo
> **`#0d1419`** (texto `#e8eef2`), coherentes con el logo. Cualquier referencia a `#FF1240` o
> `#0A0A0D` en material previo es un error y debe descartarse.

## Dónde encaja (ecosistema)

```
LAB (Flujo 1 · diario)  ──señales──►  PRISM (escenarios generales)
       ▲                                        │
       │                                    semilla
  señales nuevas                               ▼
  origen: parte_NN  ◄──────────────────  PARTE (quincenal · público)
                                               │
                                         credibilidad
                                               ▼
                                   CONVERGENCIA (Flujo 2 · cliente · pago)
```

| Producto | Público | Relación con el PARTE |
|---|---|---|
| **Lab** (Flujo 1) | Interno | El PARTE le **devuelve** ≥2 señales nuevas (`origen: parte_NN`). |
| **PRISM** | Interno/técnico | **Semilla** del ángulo. Nunca fuente. |
| **PARTE** | **Público amplio** | Lo produce el Agente PARTE. |
| **Convergencia** | Cliente · pago | No lo toca el PARTE; el PARTE le abre la puerta. |

## Cómo producir un PARTE (cadencia quincenal)

1. El Chairman elige el PRISM y el ángulo (el Agente propone 3 con fundamento).
2. `PROMPT-AGENTE-PARTE-v1.0.md` como system prompt + adjuntar `MODELO-PARTE-FUTURIA-v1.0.md`
   + `parte-001.html` + el PRISM semilla del número en curso.

3. roles separados: **Editorial** escribe → **Extractor** lista claims → **Verificador**
   (contexto limpio) valida → **Adversario** rompe → **Chairman** firma.
4. Maquetar en HTML siguiendo `parte-001.html`.
5. Verificar estructura con el script del skill:
   `python <skill>/scripts/verify_parte_html.py parte-NNN.html parte_NNN`
6. Publicar + **alta de señales en el Lab** con `origen: parte_NNN`.

## Reglas duras (no redefinir)

- **Clases SAT N/E/D/T/P**: N=Normativa (link Boletín Oficial obligatorio), E=Evento,
  D=Dato, T=Técnica, P=Proyección (nuestra). La clase N caza "normas fantasma"
  (ANMAT 4359/2025, "Ley 27.890 AR" en PRISM #006).
- **Actor ficticio + disclosure en el cuerpo** para empresa real haciendo hecho proyectado.
- **Verificación desde cero**: el PRISM no es fuente. Los 8 PRISM #002–#009 son
  pruebas de concepto PRE-Protocolo (sin fuente, con normas sin link).
- **Normas fantasma pendientes** (no entran en un PARTE hasta resolverse contra Boletín
  Oficial): ANMAT 4359/2025 (PRISM #001) y "Ley 27.890 AR" (PRISM #006, bloqueante para #001).

## Skill reutilizable

`futuria-parte` (en el perfil de Hermes) carga este conocimiento y el verificador HTML.
