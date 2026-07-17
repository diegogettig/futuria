# OBSERVATORIO DE VIGILANCIA ESTRATÉGICA — FUTURIA

> El motor de producción del Instituto. Del signo al escenario, del escenario a la decisión.
> Sistema operativo definido por el *Manual de Metodología v1.0* (Chairman, Diego Gettig).

Este directorio implementa la **tubería de 5 estadios** que alimenta al Laboratorio de Escenarios:

```
   MUNDO
     │
 [1] CAPTACIÓN        el mundo → señal registrada (ficha con fuente verificable)   ── diario
     │                motor/extraer_semilla.py  ·  prompts/AGENTE_OBSERVATORIO.md (MODO 1)
 [2] CALIFICACIÓN     señal → señal puntuada (IRS + PS)                            ── diario
     │                motor/motor_calificacion.py
 [3] CORRELACIÓN      señales sueltas → racimos + impacto cruzado                  ── semanal
     │                informes/INFORME-CONVERGENCIA-*.md
 [4] CONSTRUCCIÓN     racimos → escenario PRISM (10 componentes)                   ── quincenal
     │                ../escenarios/PRISM-*.md  (Laboratorio de Escenarios)
 [5] PROYECCIÓN       escenario → decisiones para un cliente (producto estrella)   ── por encargo
                      informes/PROYECCION-*.md
```

Dos disciplinas transversales: **calibración** (`calibracion/`) y **normas editoriales/citas** (Manual §9-11).

---

## Estructura

```
observatorio/
├── README.md                         ← este archivo
├── biblioteca/
│   └── senales_semilla.json          ← 75 señales normalizadas (§3.4), calificadas IRS/PS
├── motor/
│   ├── motor_calificacion.py         ← fórmulas IRS/PS (§4). `--self-test` valida contra el manual
│   └── extraer_semilla.py            ← extrae tablas "Señales Tempranas" de los 9 PRISM → biblioteca
├── informes/
│   └── INFORME-CONVERGENCIA-001.md   ← Apéndice A: 3 meta-racimos + 2 meta-señales
├── prompts/
│   └── AGENTE_OBSERVATORIO.md        ← system prompt del agente (3 modos)
└── calibracion/
    └── registro_predicciones.json    ← historial Brier (arranca con 10 predicciones)
```

## Comandos

```bash
# Validar el motor de cálculo contra el ejemplo trabajado del manual (§4.3)
python motor/motor_calificacion.py --self-test

# Regenerar el corpus semilla desde los escenarios y calificarlo
python motor/extraer_semilla.py
python motor/motor_calificacion.py --score biblioteca/senales_semilla.json
```

## Esquema de ficha de señal (§3.4)

`id · fecha_captura · titulo · descripcion · dominio_primario · dominios_secundarios · tipo · fuentes[{url,editor,tier}] · puntajes{8 dimensiones 0-5} · IRS · PS · horizonte · contra_senal · escenarios_vinculados · senales_relacionadas · estado · escalar_a_humano`

**Reglas duras:** título/descripción neutrales · `contra_senal` obligatoria (si está vacía la ficha está incompleta) · fuente T4 ⇒ `escalar_a_humano=true` y `estado="madurando"` hasta corroborar · umbrales de escalamiento **IRS ≥ 70 o PS ≥ 70**.

## Estado actual (Julio 2026)

- ✅ Estadios 1-2 operativos: 75 señales semilla calificadas (59 prioritarias, IRS 66.2–76.8).
- ✅ Estadio 3: Informe de Convergencia #001 producido.
- ✅ Estadios 4: 9 escenarios PRISM en `../escenarios/` (001–009); 010 en pipeline.
- ⏳ **Pendiente de curaduría humana (Chairman):** completar contra-señales, revisar puntajes preliminares, cargar URLs de fuentes, y asignar probabilidades definitivas.

## Erratum detectado

El *Manual §4.3* imprime IRS ≈ 74,7 para el ejemplo "Proyecto Pampa", pero la suma de sus propios términos (12+6+9.6+7.2+8+18+13+6) da **79.8**. El motor respeta la fórmula literal de §4.1. Corregir el manual en la próxima revisión.
