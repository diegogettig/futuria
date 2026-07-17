# Newsletter FUTURIA #9 — Geopolítica del Dato
## Quién entrena, quién inferencia, quién gobierna: la nueva carrera por el sustrato del poder

**Edición #9 — Julio 2026**  
*Base de conocimiento para escenario PRISM: Data Sovereignty / Compute Governance / Federated Learning / Data Embassies*

---

### Resumen ejecutivo
La **IA no es el producto, es el síntoma**. El poder real en el siglo XXI se define por **quién controla los datos de entrenamiento, dónde se inferencia y bajo qué jurisdicción se gobierna**. Esta newsletter mapea la **geopolítica del dato**: la **concentración de datos de entrenamiento** (Common Crawl, GitHub, libros, papers, vídeo), la **inferencia soberana** (clústeres GPU nacionales), los **modelos federados** (federated learning + data embassies), y la **carrera por estándares de gobernanza de datos** (UE Data Act, China DSL/CSL, Global South forks). El resultado es un mundo de **tres regímenes de datos** que redefine soberanía, comercio y conflicto.

---

## 1. La cadena de valor del dato en IA: de la mina a la inferencia

|     |     |     |     |
| --- | --- | --- | --- |
| Capa | Qué es | Quién controla hoy | Riesgo |
| **Extracción (Data Mining)** | Common Crawl, GitHub, libros, papers, vídeo, sensores | **EE.UU. (OpenAI, Google, Meta, Anthropic)** + **CN (Baidu, Tencent, Bytedance)** | Monopolio de corpus; sesgo cultural anglo/sinocéntrico |
| **Curaduría (Labeling)** | RLHF, anotación, alineación | **Scale AI, Appen, Telus** (EE.UU.) + **Proveedores Global Sur** (fuerza laboral barata) | Explotación trabajo anotación; fuga valor |
| **Entrenamiento (Compute)** | Clústeres GPU H100/B200 | **EE.UU. (NVIDIA + hyperscalers)** + **CN (Huawei Ascend, Biren)** | Cuello botella hardware; embargo export |
| **Inferencia (Serving)** | API, edge, on-premise | **EE.UU. (Azure, AWS, GCP)** + **CN (Alibaba, Tencent)** + **UE (Mistral, Aleph Alpha)** | Dependencia infraestructura extranjera |
| **Gobernanza (Rules)** | Estándares, leyes, auditoría | **UE (Data Act, AI Act)** + **CN (DSL/CSL/PIPL)** + **EE.UU. (estado de derecho + case law)** | Fragmentación regulatoria; guerrapadrones |

**Señal PRISM SIG-DATA-001**: *Primer **clúster GPU soberano nacional** (≥10k H100-equivalent) operativo fuera de EE.UU./CN/UE — India (AI Compute Cyberspace) / Brasil (Sofia) / Argentina (Proyecto Pampa) — 2027*.

---

## 2. Concentración de datos de entrenamiento: el monopolio silencioso

### 2.1 Corpus dominantes (2026)

| Corpus | Tamaño | Controlador | Sesgo |
|--------|--------|-------------|-------|
| **Common Crawl** | ~400B tokens / 2024 snapshot | Fundación sin fines (pero scrapeado por EE.UU./CN) | Anglo-centrista; calidad variable |
| **GitHub** | ~100B tokens código | Microsoft (OpenAI licensing) | Anglosajón; inglés |
| **Libros (Books3, Gutenberg)** | ~20B tokens | Pirata / dominio público | Occidental; copyright gris |
| **Papers (arXiv, PubMed, Nature)** | ~15B tokens | Académico abierto (pero scrapeado) | Anglosajón; STEM |
| **Vídeo (YouTube, TikTok)** | ~500B frames | Google / Bytedance | Global pero filtrado algorítmicamente |
| **Sensores (IoT, satélite, médico)** | ~1PB/día | Estado + corporaciones | Fragmentado; soberano por jurisdicción |

### 2.2 El problema del "data drain"

Países del Global Sur generan **datos masivos** (sensores, satélite, médico, agrícola, lingüístico) pero **no los retienen**: fluyen a EE.UU./CN para entrenamiento, devolviendo solo **inferencia cara y opaca**. Es la **nueva extractiva colonial**: materia prima (datos) → producto terminado (modelo) → dependencia perpetua.

**Señal PRISM SIG-DATA-002**: *Primer **Data Embassy** (datos soberanos de un país alojados en infraestructura extranjera bajo jurisdicción origen) firmado — Estonia-style para IA — 2028*.

---

## 3. Inferencia soberana: el clúster GPU nacional

|     |     |     |     |
| --- | --- | --- | --- |
| Actor | Estrategia | Capacidad 2026 | Objetivo 2030 |
| **EE.UU.** | Hyperscalers (Azure, AWS, GCP) + NVIDIA | 3M+ H100-equivalent | Dominio global inferencia |
| **China** | Huawei Ascend 910B/920 + Biren + estado | 1.5M+ Ascend | Autarquía post-embargo |
| **UE** | Mistral (France), Aleph Alpha (DE), JUPITER supercomputer | 200k+ H100 | Soberanía interna |
| **Global Sur (IN/BR/AE/SA/AR/MX/ZA/VN/ID/NG)** | Clústeres soberanos + modelos abiertos (Llama-Gov, Nemotron-Gov) | 10k-50k H100/B200 cada uno | **Inferencia soberana + coste 1/5** |
| **África (ZA/NG/KE/ET)** | Leapfrog: clúster compartido continental (AI Africa) | 5k-20k H100 | Acceso equitativo |

**Señal PRISM SIG-DATA-003**: *Primer **modelo de Estado entrenado 100% con datos soberanos** (sin corpus extranjero) — Francia (Mistral Gov) / India (BharatGPT-Gov) / Brasil (Sofia-Gov) — 2028*.

---

## 4. Modelos federados y Data Embassies: la alternativa descentralizada

### 4.1 Federated Learning (FL)

| Enfoque | Descripción | Ventaja | Riesgo |
|---------|-------------|---------|--------|
| **Centralizado FL** | Modelo global entrenado en nodos locales sin mover datos | Privacidad por diseño | Centralización control |
| **Federado Descentralizado (Blockchain)** | Consenso entrenamiento multi-nodo | Resistencia censura | Escalabilidad |
| **FL + ZK-ML** | Prueba verificable de contribución sin revelar datos | Auditoría privada | Coste cómputo |
| **Data Embassy FL** | Datos soberanos en infraestructura extranjera bajo jurisdicción origen | Soberanía + disponibilidad | Dependencia hospedaje |

### 4.2 Data Embassies para IA

| Modelo | Descripción | Ejemplo |
|--------|-------------|---------|
| **Estonia-style** | Datos soberanos de un país alojados en infraestructura extranjera bajo jurisdicción origen | Estonia (datos gob en Luxemburgo/Bélgica) → fork IA |
| **Global South Commons** | Datos de múltiples países del Sur compartidos vía federación | **Alliance for Shared Data (ASD)** — BRICS+ data trust |
| **Sovereign Cloud (UE GAIA-X)** | Infraestructura cloud soberana con datos bajo ley UE | GAIA-X + Data Act |

**Señal PRISM SIG-DATA-004**: *Primer **tratado multilateral de datos soberanos** (BRICS+ / Global South) — intercambio federado sin extracción — 2029*.

---

## 5. Gobernanza de datos: tres regímenes

| Régimen | Marco legal | Principio | Exportación |
|---------|-------------|-----------|-------------|
| **Atlántico (UE/EE.UU./JP/UK)** | **UE Data Act + AI Act + GDPR**; **EE.UU. state law + case law** | **Derechos individuales + estándares técnicos** | *Brussels Effect* (UE) + *Silicon Valley model* (EE.UU.) |
| **Sinocéntrico (CN/RU/BRICS-tech)** | **China DSL/CSL/PIPL + Data Security Law + algoritmo registrado** | **Seguridad nacional + control estatal** | *Belt & Road Digital* (exporta stack) |
| **Global Sur (IN/BR/AE/SA/AR/MX/ZA/VN/ID/NG)** | **Fork pragmático** — IRAM/ABNT/DPDP/Lei Geral + GovStack + DPGA | **Soberanía + coste-efectividad + neutralidad** | *Global South Commons* |

**Señal PRISM SIG-DATA-005**: *Primera **guerra de estándares de datos** en **ISO/IEC JTC 1 SC 27 (security) + SC 42 (AI)** — UE (Data Act) vs CN (DSL) vs Global Sur (GovStack) — 2028*.

---

## 6. Economía de los datos soberanos

| Mercado | TAM 2030 | Modelo | Jugadores |
|---------|----------|--------|-----------|
| **Data Trusts (soberanos)** | $50-100B | Licensing datos anonimizados a entrenamiento | Estados + consorcios |
| **Compute-as-a-Service soberano** | $20-50B | Alquiler clúster GPU nacional a empresas | Hyperscalers soberanos |
| **Federated Learning Platforms** | $10-30B | Infraestructura FL + ZK-ML | NVIDIA Flare, OpenFL, Flower |
| **Data Embassies** | $5-15B | Hospedaje soberano + auditoría | Cloud soberano (GAIA-X, GovStack) |
| **Modelos de Estado (licensing)** | $10-20B | Licensing modelo soberano a agencias | Mistral Gov, BharatGPT-Gov |

**Señal PRISM SIG-DATA-006**: *Primer **Data Trust soberano** con ingresos >$1B/año por licensing datos a entrenamiento (India / Brasil / UE) — 2029*.

---

## 7. Riesgos y oportunidades

### Riesgos
1. **Data colonialism 2.0** — Extractiva de datos del Sur hacia EE.UU./CN → **Data Embassies + federated learning obligatorio**.
2. **Fragmentación balcanización** — 3 regímenes incompatibles → **guerra estándares + fricción comercio**.
3. **Modelo opaco soberano** — Estados entrenan modelos sin auditoría → **riesgo autoritario + sesgo estatal**.
4. **Embargo compute** — EE.UU. bloquea export GPU → **autarquía CN (Huawei) + retraso Sur**.
5. **Fuga de cerebros de datos** — talento Sur migra a EE.UU./CN → **centros excelencia locales**.
6. **Ciber-secuestro de datos soberanos** — ransomware a Data Embassies → **air-gap + ZK-ML + TEE**.

### Oportunidades
1. **Soberanía de datos real** — cada nación retiene y monetiza sus datos (no extractiva).
2. **Data Embassies** — disponibilidad + soberanía jurisdiccional.
3. **Modelos de Estado abiertos** — transparencia + auditoría + competencia.
4. **Global South Commons** — datos federados sin extracción = poder colectivo.
5. **Diplomacia de datos** — tratados de intercambio como nueva ayuda exterior.
6. **Mercado de datos soberanos** — licensing $50-100B/año 2030.

---

## 8. Matriz de Plausibilidad — Escenario "Geopolítica del Dato 2030"

|     |     |     |
| --- | --- | --- |
| Dimensión | Puntuación (0-100) | Justificación |
| Base tecnológica | 80 | FL + ZK-ML + TEE + clústeres GPU = TRL 6-9; data embassies TRL 5 |
| Viabilidad regulatoria | 70 | UE Data Act + CN DSL + leyes Sur claras; gap: estándares interoperables |
| Aceptación social | 65 | Preocupación privacidad + soberanía; pero beneficio claro (salud, agrícola) |
| Viabilidad económica | 75 | Licensing datos $50-100B; compute soberano $20-50B; ROI claro |
| Convergencia tendencias | 85 | **IA + geopolítica + soberanía + estándares + comercio** = fuerza auto-reforzante |

**PUNTUACIÓN COMPUESTA**: **75/100** — **Muy plausible; hitos críticos 2027-2029 (clúster soberano, data embassy, modelo Estado, tratado multilateral)**.

---

## 9. Horizonte Temporal 2026-2038

| Año | Hito | Impacto |
|-----|------|---------|
| **2027** | **Primer clúster GPU soberano** (IN/BR/AR) operativo | Inferencia soberana nace |
| **2028** | **Primer Data Embassy** firmado (Estonia-style para IA) | Soberanía + disponibilidad |
| **2028** | **Primer modelo de Estado 100% datos soberanos** (FR/IN/BR) | Autonomía algorítmica |
| **2028** | **Guerra estándares datos ISO/IEC** (UE vs CN vs Sur) | Fragmentación |
| **2029** | **Tratado multilateral datos soberanos** (BRICS+/Sur) | Global South Commons |
| **2029** | **Primer Data Trust soberano** >$1B/año licensing | Monetización datos |
| **2030** | **3 regímenes de datos consolidados** (Atlántico/Sinocéntrico/Sur) | Nuevo orden |
| **2032** | **Federated Learning masivo** (50+ países) | Descentralización |
| **2035** | **Data Embassies ubicuas**; **soberanía datos operativa 50+ países** | Mainstream |
| **2038** | **Gobernanza datos global distribuida** (federada + ZK-ML + TEE) | Post-extractiva |

---

## 10. Fuentes Oficiales y Enlaces de Verificación

| Categoría | Enlace |
|-----------|--------|
| UE Data Act | https://digital-strategy.ec.europa.eu/en/policies/data-act |
| UE AI Act | https://artificial-intelligence-act.eu/ |
| China DSL/CSL/PIPL | https://www.cac.gov.cn/ |
| India DPDP Act | https://www.meity.gov.in/ |
| Brasil LGPD | https://www.gov.br/anpd/pt-br |
| Argentina Ley 25.326 | https://www.argentina.gob.ar/aaip |
| GAIA-X | https://gaia-x.eu/ |
| GovStack | https://www.govstack.global/ |
| DPGA | https://digitalpublicgoods.net/ |
| NVIDIA Flare (FL) | https://developer.nvidia.com/flare |
| OpenFL (Intel) | https://github.com/intel/openfl |
| Flower (FL) | https://flower.ai/ |
| Mistral | https://mistral.ai/ |
| Aleph Alpha | https://www.aleph-alpha.com/ |

---

*Newsletter #9 — Base conocimiento para escenario PRISM FUTURIA-2026-009.  
Próxima edición: Newsletter #10 — "Neurodatos como soberanía digital: el escenario de cierre".  
Suscribirse: https://futuria.institute/#newsletter | Colaborar: https://futuria.institute/#colaborar*