# MODELO ESCENARIO PRISM — v.1 (EN CONSTRUCCIÓN)

Definido iterativamente por Diego (FUTURIA) sobre el piloto 010 (Neurodatos).
Cada observación se anota con estado: [hecho] ya aplicado al prototipo / [pendiente] / [en debate].

---

## Reglas acordadas (hasta ahora)

### Render / Navegación
- [hecho] **Nav de capítulos fijo (sticky)** arriba al hacer scroll, con acceso rápido a los 16 capítulos (13 PRISM + Cultura Pop + Referencias + Metadatos). Idioma: español.
- [hecho] **Cada capítulo condensado en cuadros** (cards), estilo de la imagen de referencia del cap. 5 (fase cards con año).
- [hecho] **Scroll-reveal** por sección (aparecen al entrar en viewport).

### Narrativa
- [hecho] **Imagen alusiva en la narrativa** (figura bajo el texto del cap. 1).
- [hecho] **Hero con imagen** del tema.

### Fundamentos (científicos / tecnológicos / sociales / económicos)
- [hecho] **Cada cita con popover clasificado** (Opción B): badge icono+color por tipo, hover abre popover con título/dominio/hint. Ver sección "Citas con popover" abajo.
- [hecho] Mapeo: autores conocidos (Yuste, Willett, Ienca) → DOI; empresas (Neuralink, Synchron, Meta, Apple, Zama, RISC Zero) → web oficial; leyes → web oficial; fallback → búsqueda Google.

### Citas con popover clasificado (Opción B) — VER OBSERVACIÓN ACTUAL
- [hecho] Cada cita es un **badge con icono + color por tipo**, y al pasar el cursor (hover/focus) abre un **popover** con: icono, etiqueta del tipo, título, dominio, hint de clic.
- [hecho] **6 categorías** con color + icono (badge generado por IA, estilo editorial):
  - 🔵 Paper revisado por pares → `#4aa3ff` (icono: documento)
  - 🟢 Web de empresa → `#36d399` (icono: fábrica/engranaje)
  - 🟣 Laboratorio/institución → `#a78bfa` (icono: frasco)
  - 🔷 Ley/legislación → `#2dd4bf` (icono: columna)
  - 🟠 Artículo/noticia → `#ff5230` (icono: periódico)
  - ⚪ Búsqueda/verificación → `#9aa0aa` (icono: lupa)
- [hecho] Detección automática por keywords (nature/science/doi → paper; neuralink/synchron/meta → company; ley/chile/gdpr → law; etc.). Fallback: búsqueda Google.
- [hecho] Iconos en `assets/cites/` (6 PNG). Popover CSS puro (sin JS), performante, estático.
- [hecho] Distribución en escenario 010: 7 paper, 5 company, 5 law, 5 search (22 badges total).
- [pendiente] Revisar que la detección no clasifique mal ninguna fuente.
- [pendiente] ¿Agregar más categorías (ej. "Repository/CSV", "Patente")?

### Cultura Pop
- [hecho] 6 tarjetas película (Matrix, Inception, Black Mirror Crocodile, Altered Carbon, Eternal Sunshine, Ghost in the Shell) con visual IA original + texto + link oficial.

### Metadatos / Trazabilidad
- [hecho] Sección Metadatos con autores, versión, licencia, hash blockchain, historial de cambios.

---

## Pendientes de validación de Diego (próximos mensajes)

- [ ] ¿Formato v1.0 estricto YAML como fuente única? (sí, propuesto)
- [ ] ¿Nivel de dinamismo suficiente? (gauge, reveal, nav sticky)
- [ ] ¿Imagen de narrativa correcta o rotar por sección?
- [ ] ¿Los links de citas abren lo correcto?
- [ ] Definir set final de películas / referencias cultura pop.
- [ ] ¿Skill `futuria-scenario-publish` debe incluir este motor de render v.1?

---

## Pipeline técnico (para la skill)

```
contenido/borradores/  ->  escenarios/PRISM-XXXX.md (o .yaml v1.0)
        |
        v
testing/escenarios/render_010.py  (YAML -> HTML dinámico v.1)
        |  validación humana (Diego)
        v
plataforma/escenarios/  +  publish_all.py (deploy Cloudflare)
```

Skill propuesta: `futuria-scenario-publish` v2 = borrador → YAML v1.0 → render dinámico → validación → deploy.
