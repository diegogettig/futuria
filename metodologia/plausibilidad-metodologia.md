# METODOLOGÍA FUTURIA — Cálculo de Plausibilidad PRISM

**Versión:** 1.0 (borrador para validación)  
**Propietario:** FUTURIA Institute — Dirección de Escenarios  
**Estado:** en revisión · pendiente de aprobación del Directorio  
**Aplica a:** todos los Escenarios PRISM (FUTURIA-2026-NNNN)  
**Relacionado:** `metodologia/PRISM-template-v1.md` (Sección 4)

---

## 1. Propósito

La **Plausibilidad PRISM** es una métrica de *transparencia radical*: no pretende
ser una predicción probabilística (eso sería falso), sino una **evaluación
estructurada de qué tan sólidas son las condiciones de posibilidad** de un
escenario dado. Su objetivo es que cualquier lector — técnico o no — pueda
reconstruir el número desde sus componentes y los supuestos.

Toda puntuación debe ser **reproducible**: dados los mismos insumos y el mismo
criterio, dos analistas independientes deben llegar a la misma puntuación
±5 puntos.

---

## 2. Escala

- Rango: **0–100** (sin decimales en la compuesta; dimensiones permiten 0–100 enteras).
- Interpretación por bandas:

| Banda | Rango | Significado institucional |
|-------|-------|---------------------------|
| Muy baja | 0–24 | Condiciones de posibilidad ausentes o contradictorias |
| Baja | 25–44 | Requiere quiebres no evidenciados |
| Media-baja | 45–59 | Posible bajo supuestos fuertes |
| **Media** | **60–74** | **Plausible; vigilancia activa** |
| Media-alta | 75–89 | Muy plausible; tendencias actuando |
| Alta | 90–100 | Casi determinista dadas las tendencias actuales |

> El escenario 010 (Neurodatos) obtuvo **72 → banda "Media"**.

---

## 3. Dimensiones (5 factores, peso igual por defecto)

Cada dimensión se puntúa 0–100 con evidencia explícita (ver §5).

| Clave | Dimensión | Pregunta que responde |
|-------|-----------|------------------------|
| `base_cientifica` | Base científica | ¿El fenómeno es físicamente posible según conocimiento actual? |
| `viabilidad_tecnica` | Viabilidad técnica | ¿Existen o son alcanzables las tecnologías requeridas (TRL)? |
| `compatibilidad_social` | Compatibilidad social | ¿Hay aceptación cultural / evita aversión fuerte? |
| `precedente_historico` | Precedente histórico | ¿Existen analogías históricas que hagan el patrón familiar? |
| `convergencia_tendencias` | Convergencia de tendencias | ¿Múltiples fuerzas (BCI+IA+ley+geo+priv) apuntan juntas? |

### 3.1 Justificación de las 5 dimensiones
Se eligió un modelo de **5 ejes independientes** (no una matriz factorial) para
mantener trazabilidad: cada eje puede ser auditado por un experto distinto.
El conjunto cubre las 4 "condiciones de posibilidad" clásicas de prospectiva
técnica (ciencia, tecnología, sociedad, historia) más un eje de **convergencia**
propio de la metodología PRISM (T-PRISM), que captura el efecto de
tecnologías transversales actuando en simultáneo.

---

## 4. Fórmula (criterio oficial)

**Promedio simple de pesos iguales** (default del Instituto):

```
P = (Bc + Vt + Cs + Ph + Ct) / 5
```

Donde:
- `Bc` = base_cientifica
- `Vt` = viabilidad_tecnica
- `Cs` = compatibilidad_social
- `Ph` = precedente_historico
- `Ct` = convergencia_tendencias

### 4.1 Worked example — Escenario 010
```
Bc = 78  (decodificación neuronal demostrada: Willett et al. 2023, Nature)
Vt = 75  (BCIs en TRL 7-8; decodificación en producción temprana)
Cs = 58  (entusiasmo por restauración, rechazo a vigilancia neural)
Ph = 65  (analogías: GDPR, derechos de datos, trusts de datos abiertos)
Ct = 85  (BCI + IA + leyes neuroderechos + geopolítica + privacidad alineadas)

P = (78+75+58+65+85) / 5 = 361 / 5 = 72.2 → 72
```

### 4.2 Variantes permitidas (deben declararse)
Si un escenario justifica **pesos desiguales** (p. ej. un escenario puramente
tecnológico donde la base científica domina), se permite una media ponderada:

```
P = Σ(wᵢ · Dᵢ) / Σ(wᵢ),   con wᵢ documentado y Σwᵢ = 1
```

La elección (igual vs ponderada) y los pesos **deben figurar en
`metodologia_calculo` del YAML** del escenario. El default del Instituto es
**peso igual**.

---

## 5. Reglas de asignación de puntaje (para auditores)

Para cada dimensión, el analista debe:

1. **Citar evidencia primaria** (paper / ley / dato) que justifique la cifra.
2. **Anclar la escala**: 100 = condición plenamente satisface el criterio hoy;
   0 = contradictorio con evidencia actual.
3. **Declarar supuestos**: toda dimensión >70 implica un supuesto explícito en
   `supuestos_clave`.
4. **Señalar factores bloqueo**: toda dimensión <60 debe listar al menos una
   barrera en `factores_bloqueo` con su probabilidad de superarse.

### 5.1 Umbral de publicación
Un escenario puede publicarse con cualquier P, pero:
- Si `P < 60`: requiere sección explícita de "Por qué lo consideramos".
- Si `compatibilidad_social < 50` o `base_cientifica < 40`: requiere
  revisión del Directorio antes de `publicada`.

---

## 6. Limitaciones (transparencia radical)

- La plausibilidad **no es probabilidad de ocurrencia**. Mide solidez de
  condiciones, no timing ni certidumbre.
- Las dimensiones pueden correlacionarse (p. ej. base y viabilidad técnica);
  el promedio simple no lo corrige. Si la correlación es fuerte, usarse
  media ponderada o reportar la correlación.
- La métrica es **re-evaluable**: `metadatos.revisiones_programadas` con
  `tipo_revision: re_evaluacion_plausibilidad` debe recalcular P con datos
  nuevos y versionar el cambio.

---

## 7. Checklist de cumplimiento (por escenario)

- [ ] Las 5 dimensiones puntudas 0–100 con evidencia citada cada una.
- [ ] `puntuacion_total` = promedio (o media ponderada declarada) de las 5.
- [ ] `metodologia_calculo` cita la fórmula de §4 y los supuestos.
- [ ] `supuestos_clave` presentes para dimensiones >70.
- [ ] `factores_bloqueo` presentes para dimensiones <60.
- [ ] Banda de §2 declarada en la narrativa o resumen.
- [ ] Re-evaluación programada en `metadatos.revisiones_programadas`.

---

## 9. Protección de integridad (mismo esquema que el análisis PRISM)

Este documento de método es un **activo metodológico del Instituto** y se protege
con el mismo mecanismo que los escenarios PRISM (`PRISM-template-v1.md`,
`metadatos.hash_blockchain` / `metadatos.tx_blockchain` / checklist firmado):

1. **Hash SHA-256**: se calcula sobre el contenido canónico del `.md` (sin la
   cabecera de hash ni los campos de registro). El valor se documenta abajo y en
   el escenario que lo cite. Cualquier edición cambia el hash → tampering detectable.
2. **Registro en cadena (blockchain)**: el hash se ancla en una transacción; el
   `tx_blockchain` se guarda junto al hash. Hasta el registro, ambos campos = `null`.
3. **Checklist firmado por revisor humano**: al menos un revisor humano (Directorio
   FUTURIA) firma la sección §8 antes de publicar un escenario que use este método.
4. **Versionado**: cualquier cambio de criterio (pesos, bandas, dimensiones) incrementa
   la versión y se anota en §8. Los escenarios citan la versión exacta
   (`metodologia/plausibilidad-metodologia.md vX.Y`).

### 9.1 Estado de registro (se completa al aprobar)

| Campo | Valor |
|-------|-------|
| Versión | 1.0 (borrador, pendiente de aprobación del Directorio) |
| Hash SHA-256 | `255a5c998034e9b1fb4c55c06095d6d60f8a59da013885d72e5b225f40c6efcb` |
| Tx blockchain | `null` |
| Revisor firmante | `___PENDIENTE___` |
| Fecha de firma | `___PENDIENTE___` |

> Nota: el hash se calcula con `python -c "import hashlib,sys;print(hashlib.sha256(open('metodologia/plausibilidad-metodologia.md','rb').read()).hexdigest())"`
> sobre la versión final. El render del escenario debe mostrar el hash y enlazar al
> método como fuente protegida (mismo tratamiento que el análisis PRISM).

---

## 8. Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0 | 2026-07-12 | FUTURIA (Diego G. + Hermes) | Creación inicial del documento de método a partir del piloto 010. |
| 1.0 | 2026-07-13 | FUTURIA (Hermes) | Añadido §9 Protección de integridad (hash SHA-256 + registro + checklist firmado), alineado con el análisis PRISM. |
