# VERSIONADO FUTURIA

Registro maestro de versiones: **landing**, **componentes** y **escenarios PRISM**.

> Regla de oro: cada vez que un escenario cambia, se le sube la versión y se guarda
> la versión anterior en `escenarios/archive/` (o `plataforma/escenarios/archive/`
> para los publicados). Nunca se sobrescribe sin archivo.

---

## Reglas de versionado

- **Landing / componentes**: versionado semántico `vMAYOR.MENOR` (MINOR = cambio; MAYOR = cambio estructural).
- **Escenarios**: cada escenario tiene su propia versión (`v1.0`, `v1.1`, `v2.0`...).
- **Formato canónico (a partir de 010)**: PRISM v1.0 estricto = YAML según `metodologia/PRISM-template-v1.md`.
- **Archivo obligatorio**: al editar un escenario, copiar el archivo previo a
  `escenarios/archive/PRISM-XXXX-vN.N.ext` antes de sobrescribir.
- **Estados**: `borrador | en_revision | verificado | publicada | archivada`.

---

## 🌐 Landing (plataforma/index.html)

| Versión | Fecha | Cambio | Autor |
|---------|-------|--------|-------|
| v1.0 | 2026-07-06 | Landing canónica con nav PRISM, hero, metodología 6 ejes, grid escenarios | Hermes |
| v1.1 | 2026-07-06 | Alineación landing-v1.html + cards escenarios 001-005 | Hermes |
| v1.2 | 2026-07-06 | Inclusión escenarios 006-009 en grid | Hermes |
| v2.0 | PENDIENTE | 5 fixes (Lanzamiento Operativo): newsletter #2 link, Neurodatos HTML, noticias URLs, referentes botones, CTA Beehiiv | Lanzamiento Operativo |

---

## 🧩 Componentes

| Componente | Versión | Último cambio | Notas |
|-----------|---------|---------------|-------|
| `scripts/publish_all.py` | v1.0 | 2026-07-06 | Motor: escenario, newsletter, noticias, referentes, deploy, gerencia |
| `scripts/publish_scenario.py` | v1.0 | 2026-07-06 | Render MD→HTML escenario |
| `escenarios/template-escenario.html` | v1.0 | 2026-07-06 | Template HTML (molde 10 secciones) |
| `templates/template-newsletter.html` | v1.0 | 2026-07-06 | Template newsletter |
| `templates/template-referente.html` | v1.0 | 2026-07-06 | Template referentes |
| `metodologia/PRISM-template-v1.md` | v1.0 | 2026-07-06 | Template formal PRISM (13 secciones + YAML) |
| Deploy (wrangler → futuria-institute) | v1.0 | 2026-07-06 | Cloudflare Pages |

---

## 📊 Escenarios PRISM

| ID | Título | Versión | Formato | Fecha | Último cambio | Archivo | Versión anterior |
|----|--------|---------|---------|-------|---------------|---------|------------------|
| 001 | El año en que una IA reclama personalidad jurídica | v1.0-landing | MD (10 sec) | 2026-07-06 | Publicado landing | `escenarios/PRISM-2026-0001-personalidad-juridica-ia.md` | — |
| 002 | Las primeras 10 Sociedades Automatizadas argentinas | v1.0-landing | MD (10 sec) | 2026-07-06 | Publicado landing | `escenarios/PRISM-2026-002-sociedades-automatizadas.md` | — |
| 003 | El primer corazón humano no biológico funcional | v1.0-landing | MD (10 sec) | 2026-07-06 | Publicado landing | `escenarios/PRISM-2026-003-cardio-bionico.md` | — |
| 004 | La pila tecnológica soberana (Hard Tech) | v1.0-landing | MD (10 sec) | 2026-07-06 | Publicado landing | `escenarios/PRISM-2026-004-hard-tech-foundations.md` | — |
| 005 | Gobernanza Algorítmica del Estado | v1.0-landing | MD (10 sec) | 2026-07-06 | Publicado landing | `escenarios/PRISM-2026-005-gobernanza-algoritmica.md` | — |
| 006 | Economía de la Longevidad / CaaS Médico | v1.0-landing | MD (10 sec) | 2026-07-06 | Publicado landing | `escenarios/PRISM-2026-006-longevidad-caas.md` | — |
| 007 | Conciencia Artificial Verificable | v1.0-landing | MD (10 sec) | 2026-07-06 | Publicado landing | `escenarios/PRISM-2026-007-conciencia-verificable.md` | — |
| 008 | Bioprinting Distribuido | v1.0-landing | MD (10 sec) | 2026-07-06 | Publicado landing | `escenarios/PRISM-2026-008-bioprinting-distribuido.md` | — |
| 009 | Geopolítica del Dato | v1.0-landing | MD (10 sec) | 2026-07-06 | Publicado landing | `escenarios/PRISM-2026-009-geopolitica-datos.md` | — |
| 010 | Neurodatos como soberanía digital | **v1.0** | **YAML v1.0** | 2026-07-12 | **CERRADO como MODELO v1.0** — render dinámico, glosario, citas clasificadas, panel Cultura Pop, doble control de URLs, metodología protegida | `testing/escenarios/PRISM-2026-010-neurodatos-soberania-digital.yaml` | — |

> ✅ **MODELO v1.0 CERRADO (2026-07-12)**: el piloto 010 define el formato canónico
> PRISM v1.0 (YAML estricto → HTML dinámico). Motor reutilizable vía skill `prism-escenario`.
> Los escenarios 001-009 se migran progresivamente a este formato (se crean/en conjunto con el usuario).

---

## 🛠️ Motor Genérico PRISM v1.0 (Skill: `prism-escenario`)

Flujo canónico para cualquier escenario:

1. **Fuente única**: `escenarios/PRISM-2026-XXX-titulo.yaml` (schema `metodologia/PRISM-template-v1.md`).
2. **Render**: `testing/escenarios/render_010.py` (parametrizable por ID) → HTML estático.
   - Glosario de siglas/países (`metodologia/glosario.md`) con bandera+popover.
   - Citas clasificadas por tipo (paper/company/lab/search/news/law) con popover + doble control de URLs.
   - Panel lateral Cultura Pop con scroll propio y toggle de ocultar.
   - Cap. 11 Interdependencias con popovers clickables.
3. **Metodología de plausibilidad**: `metodologia/plausibilidad-metodologia.md` → `plausibilidad-metodologia.html` (página propia, hash SHA-256 + protección blockchain).
4. **Doble control de citas**: el render reporta URLs rotas; corregir en YAML antes de publicar.
5. **Protección**: hash_blockchain + tx_blockchain + firma revisor (§9 de la metodología).

---

## 📰 Newsletters

| ID | Título | Versión | Fecha | Archivo |
|----|--------|---------|-------|---------|
| 001 | Argentina, ¿primer país con empresas gobernadas por IA? | v1.0 | 2026-07-06 | `newsletter/newsletter-001.html` |
| 002 | Las primeras 10 Sociedades Automatizadas argentinas | v1.0 | 2026-07-06 | `newsletter/newsletter-002.html` (borrador en `contenido/newsletter/borradores/`) |
| 003 | Base conocimiento Salud/IA/Cardio | v1.0 | 2026-07-06 | `newsletter/newsletter-003.html` |
| 004 | La pila tecnológica soberana | v1.0 | 2026-07-06 | `newsletter/newsletter-004.html` |
| 005 | Gobernanza Algorítmica del Estado | v1.0 | 2026-07-06 | `newsletter/newsletter-005.html` |
| 006 | Economía de la Longevidad / CaaS | v1.0 | 2026-07-06 | `newsletter/newsletter-006.html` |
| 007 | Conciencia Artificial Verificable | v1.0 | 2026-07-06 | `newsletter/newsletter-007.html` |
| 008 | Bioprinting Distribuido | v1.0 | 2026-07-06 | `newsletter/newsletter-008.html` |
| 009 | Geopolítica del Dato | v1.0 | 2026-07-06 | `newsletter/newsletter-009.html` |

---

## 🗂️ Convención de archivo (versionado de escenarios)

```
escenarios/
├── PRISM-2026-010-neurodatos-soberania-digital.yaml   # actual (v1.0-strict)
└── archive/
    └── PRISM-2026-010-neurodatos-soberania-digital-v1.0.yaml   # copia al editar
```

Al editar cualquier escenario:
1. Copiar archivo actual → `archive/PRISM-XXXX-vN.N.ext`
2. Aplicar cambios y subir versión (`v1.0` → `v1.1`, o `v1.0-landing` → `v1.0-strict`)
3. Actualizar esta tabla (columna "Versión anterior")

---

*Documento vivo. Cualquier cambio de landing/componente/escenario debe registrarse aquí.*
