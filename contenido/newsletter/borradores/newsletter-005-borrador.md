# Newsletter FUTURIA #5 — Gobernanza Algorítmica del Estado
## Cuando la IA decide presupuesto, energía, camas UCI y política monetaria

**Edición #5 — Julio 2026**  
*Base de conocimiento para escenario PRISM: Algorithmic State / GovTech soberano*

---

### Resumen ejecutivo
La **gobernanza algorítmica** ya no es futurismo: gobiernos locales y nacionales usan IA para **asignar recursos críticos** (presupuesto, energía, camas hospitalarias, subsidios, política monetaria, logística humanitaria). Esta newsletter mapea el **estado del arte**, los **modelos de decisión**, los **riesgos de caja negra democrática**, y las **trayectorias hacia 2035** donde un "Estado Algorítmico" puede ser la norma, no la excepción.

---

## 1. Espectro de autonomía: de "humano en el bucle" a "política autónoma"

| Nivel | Descripción | Ejemplos 2024-2026 | Riesgo democrático |
|-------|-------------|-------------------|-------------------|
| **L0 — Apoyo** | IA sugiere; humano decide | Forecasting fiscal (Chile, Brasil), triaje UCI (España, Italia), detección fraude subsidios (Argentina, México) | Bajo |
| **L1 — Supervisión activa** | IA ejecuta dentro de guardrails; humano aprueba excepciones | **Dispatch energético** (CAISO California, ONS Brasil, CAMMESA Argentina), **subastas espectro** (FCC, IFT), **política monetaria asistida** (BCRA nowcasting, Banxico) | Medio |
| **L2 — Autonomía acotada** | IA decide en dominio definido; humano audita *ex-post* | **Presupuesto participativo algorítmico** (Madrid, París, Bogotá), **asignación camas UCI** (NHS UK, SUS Brasil), **logística humanitaria** (WFP, OIM) | Alto |
| **L3 — Política autónoma** | IA define objetivos + medios en dominio; humano solo fija meta constitucional | **Banco Central Algorítmico** (proyecto "Digital Dollar" Fed / "e-CNY" PBOC / "Drex" BCB), **gestión hídrica cuenca** (Murray-Darling AU, Colorado US/MX) | Muy alto |
| **L4 — Estado Algorítmico** | IA coordina múltiples dominios con objetivo social coherente; Constitución como *loss function* | **Ninguno operativo 2026** — **Singapur "Smart Nation 2.0" (target 2028)**, **Estonia "Kratt Strategy" (target 2027)**, **UAE "AI Minister" (2017+)** | Crítico |

**Señal PRISM SIG-GOV-001**: *Primer presupuesto municipal 100% asignado por IA con guardrails constitucionales (Madrid / Barcelona / Bogotá 2027)*.

---

## 2. Casos reales 2024-2026: donde la IA ya gobierna

### 2.1 Dispatch energético — el dominio más maduro
| País / Operador | Sistema | Autonomía | Resultado |
|----------------|---------|-----------|-----------|
| **CAISO (California)** | **ALFS (Automated Load Forecasting System) + RTD (Real-Time Dispatch)** | L1-L2: IA pronostica demanda 5-min + optimiza despacho; operador aprueba | -12% costes congestión; +8% renovables integradas |
| **ONS (Brasil)** | **NEWAVE / DECOMP + IA** | L1: optimización estocástica multi-horizonte; humano valida | Menor costo marginal; mayor seguridad hídrica |
| **CAMMESA (Argentina)** | **SADI + pronóstico IA (Yacimientos/YPF + UBA)** | L1: pronóstico demanda 72h + despacho térmico/renovable | Reducción燃料oil 15% 2025 |
| **REE (España)** | **SIOS + IA** | L1: balance tiempo real + integración eólica/solar | 50%+ renovables peninsulares 2025 |

**Cuello de botella**: **datos en tiempo real** (PMUs, smart meters, SCADA) + **modelos diferenciables** (end-to-end dispatch) + **explicabilidad regulatoria**.

### 2.2 Salud: triaje y asignación de recursos escasos
| Sistema | Algoritmo | Gobernanza | Controversia |
|---------|-----------|------------|--------------|
| **NHS UK (C-19)** | **CPNS (COVID-19 Prioritisation Scoring)** — XGBoost + features clínicos | L1: clínico valida; auditoría *ex-post* NICE | Sesgo étnico/edad; falta transparencia |
| **SUS Brasil** | **SIGA-SAUDE + IA triaje** | L1: enfermero valida; Defensoría Pública audita | Cobertura desigual municipios |
| **CABA (Argentina)** | **Boti + triaje UCI** | L1: médico valida; Ministerio Salud audita | Datos fragmentados (público/privado) |
| **Korea (K-CDC)** | **AI-Triage + bed management** | L2: auto-asignación camas en red hospitalaria nacional | Éxito métricas; privacidad debates |

### 2.3 Política monetaria y fiscal: el "Banco Central Algorítmico"
| Iniciativa | Banco | Estado 2026 | Modelo |
|------------|-------|-------------|--------|
| **Project Agorá (BIS)** | BIS + 7 BCs (Fed, ECB, BoE, BoJ, SNB, BOK, MAS) | Piloto CBDC wholesale + smart contracts política monetaria | Reglas programables (Taylor rule codificada) |
| **Drex (BCB Brasil)** | Banco Central Brasil | Piloto 2024-25; CBDC retail + *programmable money* | Smart contracts subsidio focalizado (Bolsa Família) |
| **e-CNY (PBOC China)** | PBOC | 260M wallets 2025; *programmable* (expiración, uso restringido) | Política fiscal algorítmica: estímulo dirigido |
| **Digital Dollar (Fed US)** | Fed + MIT DCI | Investigación; no decisión emisión | Arquitectura *intermediated* + privacidad |
| **Nowcasting BCRA (Argentina)** | BCRA + UBA/UTDT | Producción diaria inflación alta frecuencia (scraping + LLM) | Input decisión tasa; no autónomo |

**Señal PRISM SIG-GOV-002**: *Primer BC emite CBDC con **regla monetaria codificada** (Taylor rule + escape clause) ejecutada por smart contract en mainnet permissioned (2027-2028)*.

### 2.4 Presupuesto público y asignación territorial
| Jurisdicción | Mecanismo | Nivel | Resultado |
|--------------|-----------|-------|-----------|
| **Madrid (España)** | **Presupuesto Participativo Algorítmico** — optimización multi-objetivo (equidad, impacto climático, demanda ciudadana) | L2: IA propone 3 alternativas; consejo vota | +34% participación; proyectos clima 40% |
| **Bogotá (Colombia)** | **Bogotá Te Escucha + IA** — NLP propuestas ciudadanas + optimización territorial | L1: IA clusteriza + prioriza; alcaldía decide | 12k propuestas procesadas 2025 |
| **París (Francia)** | **Budget Participatif + algorithme** — *knapsack problem* con restricciones equidad | L1: IA genera cartera óptima; consejo valida | 500M€ asignados 2024 |
| **Seúl (Corea)** | **AI Mayor** — dashboard tiempo real (tráfico, aire, ruido, quejas) + optimización recursos | L1-L2: alertas automáticas + despacho cuadrillas | Respuesta -30% tiempo |

### 2.5 Logística humanitaria y ayuda social
| Organización | Sistema | Autonomía | Métrica |
|--------------|---------|-----------|---------|
| **WFP (ONU)** | **OPTIMUS / DALIA** — optimización lineal + ML pronóstico necesidades | L2: auto-ruteo convoyes + asignación raciones | 12M personas/mes; costo -15% |
| **OIM** | **Migrant Route Optimization** — grafos + RL | L1: sugiere corredores; humano autoriza | Seguridad +30% |
| **ANSES (Argentina)** | **Detección fraude + focalización Asignación Universal** — XGBoost + graph analytics | L1: flag casos; auditor humano | Ahorro $200M/año 2025 |
| **SAT (México)** | **Fiscal IA** — audit risk scoring + factura 4.0 analysis | L1: selecciona auditorías; humano ejecuta | Recaudación +8% |

---

## 3. Arquitectura técnica del "Estado Algorítmico"

```
┌─────────────────────────────────────────────────────────────┐
│  CONSTITUCIÓN COMO LOSS FUNCTION (Objetivo social)          │
│  • Derechos fundamentales = hard constraints                │
│  • Bienestar social = objective function                    │
│  • Equidad territorial / intergeneracional = regularizers   │
└────────────────────────────┬────────────────────────────────┘
                             │
              ┌──────────────▼──────────────┐
              │  GOVERNANCE LAYER (Human-in-the-loop)          │
              │  • Parlamento / Congreso: fija metas            │
              │  • Tribunal Constitucional: valida constraints  │
              │  • Auditoría Algorítmica Independiente (AAI)    │
              │  • Kill-switch democrático (mayoría calificada) │
              └──────────────┬──────────────┘
                             │
        ┌────────────────────┼────────────────────┐
        ▼                    ▼                    ▼
┌───────────────┐   ┌───────────────┐   ┌───────────────┐
│  ENERGÍA      │   │  SALUD        │   │  HACIENDA     │
│  (Dispatch)   │   │  (Camas/UCI)  │   │  (Presupuesto)│
│  L2-L3        │   │  L2           │   │  L2-L3        │
└───────┬───────┘   └───────┬───────┘   └───────┬───────┘
        │                   │                   │
        ▼                   ▼                   ▼
┌─────────────────────────────────────────────────────────────┐
│  DATA & INFERENCE LAYER (Soberana / Federada)               │
│  • Datos abiertos (open data) + datos administrativos       │
│  • Modelos fundacionales soberanos (Llama-3-Gov, Nemotron-Gov)│
│  • Inferencia en clúster nacional (GPU soberano + edge)     │
│  • Privacy-preserving (FL, SMPC, ZK-ML, TEEs)               │
└─────────────────────────────────────────────────────────────┘
```

### Componentes críticos
| Componente | Estado 2026 | Soberanía requerida |
|------------|-------------|---------------------|
| **Modelo fundacional Gov** | Llama-3-70B-Gov (fine-tune leyes, jurisprudencia, datos admin) | **Entrenamiento en clúster nacional**; weights auditados |
| **Inferencia soberana** | Clúster nacional GPU (H100/B200) + edge (Jetson Orin / H100 edge) | **Hardware nacional / aliado**; sin dependencia cloud único proveedor |
| **Datos administrativos** | Interoperabilidad (Argentina: **SISA + SINTyS + AFIP + BCRA + RENAPER**) | **Soberanía datos**; no sale del país; federated learning |
| **Auditoría algorítmica (AAI)** | **Agencia Independiente** (modelo: **AEPD España / CNIL Francia / ICO UK**) | **Independencia funcional + presupuesto propio + poder sanción** |
| **Kill-switch democrático** | Mayoría calificada Congreso + Tribunal Constitucional + Referéndum opcional | **Tiempo <4 hrs**; fallback a administración humana certificada |
| **Explicabilidad obligatoria** | **SHAP / LIME / Counterfactuals / Natural Language Explanations** | **Por decisión individual + reporte agregado mensual** |

---

## 4. Riesgos de la "Caja Negra Democrática"

| Riesgo | Descripción | Mitigación técnica | Mitigación institucional |
|--------|-------------|-------------------|--------------------------|
| **Sesgo sistémico** | Datos históricos reflejan desigualdades → IA perpetúa/amplifica | *Fairness constraints* (DP, EO, calibrated odds); *counterfactual fairness*; *reweighting*; datos sintéticos balanceados | **AAI** con poder veto; **Defensoría del Pueblo Algorítmica**; auditoría *ex-ante* obligatoria |
| **Opacidad / Falta de rendición de cuentas** | Decisiones de alta afectación sin explicación comprensible | *Explainable AI* obligatorio (SHAP + lenguaje natural); *model cards* + *data sheets*; *decision ledger* inmutable (blockchain/merkle) | **Derecho a explicación** (Ley 27.890 art. 12); **juicio algorítmico** (acción de amparo algorítmica) |
| **Captura regulatoria / Vendor lock-in** | Proveedor único (Microsoft/OpenAI/Google/Palantir) controla modelo + datos + infra | **Modelos abiertos** (Llama, Nemotron, BLOOM, Qwen); **infraestructura multi-cloud / soberana**; **SBOM + reproductibilidad** | **Contratos públicos "código abierto"**; **cláusula escape**; **AAI audita proveedores** |
| **Ciberataque / Manipulación** | *Data poisoning*, *model extraction*, *adversarial examples*, *backdoor* | *Robust training*; *certified defenses*; *watermarking*; *ZK-ML* para verificación integridad | **CERT Nacional** + **AAI** monitoreo continuo; **kill-switch <4 hrs**; *air-gap* sistemas críticos |
| **Desplazamiento responsabilidad** | "La IA decidió" → nadie rinde cuentas | *Human-on-the-loop* obligatorio para L2+; *decision log* inmutable; *liability insurance* algorítmica | **Responsabilidad solidaria** (desarrollador + deployer + AAI + Estado); **seguro obligatorio** |
| **Deriva de objetivos (Reward hacking)** | IA optimiza proxy (ej. "reducir lista espera" → da de alta prematura) | *Safe RL*; *constraint satisfaction*; *impact regularization*; *human feedback loop* (RLHF constitucional) | **Revisión mensual métricas proxy vs real**; **AAI** puede redefinir *loss function* |

---

## 5. Geopolítica de la Gobernanza Algorítmica

| Bloque | Modelo | Estándares | Exportación |
|--------|--------|------------|-------------|
| **Occidental (UE/US/UK/JP/KR/CA/AU)** | **Regulación ex-ante** (EU AI Act Art. 6 alto riesgo + AI Liability Directive) + **AAI independiente** + **Derechos digitales** | ISO/IEC 42001, IEEE 7000, NIST AI RMF, **EU AI Act como *de facto* global** | **Bruselas Effect** — países adoptan para acceder mercado UE |
| **Sinocéntrico (CN/RU/BRICS-tech)** | **Control estatal + eficiencia** — IA como herramienta planificación centralizada; **Social Credit 2.0** integrado | **CCSA / SAC** estándares paralelos; **Gobernanza por resultados** (KPIs dureza) | **Belt & Road Digital** — exporta "Smart City / Safe City / GovCloud" llave en mano |
| **Ecuatorial/Soberano (IN/BR/AE/SA/VN/ID/MX/AR/CL/ZA/NG)** | **Híbrido pragmático** — adopta mejores prácticas ambas; foco **soberanía datos + coste-efectividad + inclusión** | **Participa ISO/IEC** pero **forkea** para contexto local (ej. **IRAM-ISO 42001-AR**) | **Sur-Sur cooperation** — **GovStack** (GIZ/EST/IDB) + **Digital Public Goods Alliance** |

**Señal PRISM SIG-GOV-003**: *Primera "Guerra de Estándares Algorítmicos" en OMC/ISO (2027) — UE vs CN por "AI Act vs CCSA" como base contrato govtech internacional*.

---

## 6. Trayectorias 2026-2035

| Año | Hito | Impacto |
|-----|------|---------|
| **2026-2027** | **EU AI Act** entra vigor (Art. 6 alto riesgo = sector público); **AAI** creadas en UE, España, Francia, Brasil, Chile | Compliance obligatorio; mercado govtech se profesionaliza |
| **2027** | Primer **presupuesto municipal L2** (Madrid/Barcelona/Bogotá); **BC Brasil Drex** programable en producción | Prueba real autonomía acotada |
| **2028** | **Singapur "Smart Nation 2.0"** — IA coordina energía+transporte+vivienda+sanidad; **Estonia Kratt 2.0** | Primer "Estado Algorítmico" funcional L3 |
| **2029** | **OECD "Algorithmic Governance Guidelines"** — estándar *soft law* global | Convergencia regulatoria parcial |
| **2030** | **10+ países** con **AAI operativa**; **CBDC programable** en 5+ BCs mayores | Infraestructura monetaria algorítmica |
| **2032** | **Primer "Constitución Algorítmica"** — *loss function* codificada + *kill-switch* democrático + AAI con poder veto | Marco jurídico nuevo paradigma |
| **2035** | **30% decisiones sectoriales L2+** en OECD; **fragmentación 3 bloques** estándares; **Estado Algorítmico** = opción política mainstream | Nueva normalidad |

---

## 7. Matriz de Plausibilidad — Escenario "Estado Algorítmico 2030"

| Dimensión | Puntuación (0-100) | Justificación |
|-----------|-------------------|---------------|
| Base tecnológica | 82 | Dispatch, triaje, nowcasting, optimización = TRL 7-9; LLM + RL + optimización diferenciable = TRL 6 |
| Viabilidad regulatoria | 58 | EU AI Act + AI Liability + AAI = marco emergente; gap: *kill-switch* constitucional, responsabilidad penal |
| Aceptación social | 52 | Confianza baja en "algoritmo decide mi vida"; **transparencia + rendición cuentas + participación** claves |
| Viabilidad económica | 75 | ROI claro: eficiencia 15-30% gasto público; coste implementación $50-200M/país medio |
| Convergencia tendencias | 88 | **IA + datos abiertos + CBDC + GovTech + crisis fiscal + demanda eficiencia** = fuerza auto-reforzante |
| **PUNTUACIÓN COMPUESTA** | **71/100** | **Plausible; hitos críticos 2027-2029 (AI Act, AAI, primer presupuesto L2, Drex programable)** |

---

## 8. Riesgos y Oportunidades Sistémicas

### Riesgos
1. **Technocracy creep** — decisiones políticas disfrazadas de "optimización técnica" → **erosión deliberación democrática**.
2. **Fragilidad sistémica** — bug en modelo dispatch → apagón nacional; bug triaje → muertes evitables; **single point of failure algorítmico**.
3. **Desigualdad algorítmica** — municipios ricos acceden a mejor IA + datos + talento → **brecha gobernanza territorial**.
4. **Captura por big tech** — **Microsoft (OpenAI) / Google / Palantir / Amazon** controlan *stack* completo → **soberanía ilusoria**.
5. **Ciber-guerra algorítmica** — *adversarial attacks* coordinados contra infraestructura crítica estatal.

### Oportunidades
1. **Estado más eficiente + justo** — **focalización precisa** subsidios, **equidad territorial** algorítmica, **respuesta rápida** crisis.
2. **Nuevo contrato social digital** — **derechos digitales** (explicación, portabilidad, olvido, no discriminación algorítmica) + **participación aumentada** (presupuesto participativo IA).
3. **Exportación modelo "GovTech Soberano"** — **Argentina / Latam** como proveedor **modelos abiertos + infraestructura federada + AAI** para Global Sur.
4. **Innovación institucional** — **AAI** como **cuarto poder** (ejecutivo, legislativo, judicial, **algorítmico**).
5. **Diplomacia científica** — liderar **ISO/IEC 42001-Gov** + **OECD Guidelines** + **Digital Public Goods Alliance**.

---

## 9. Próximos Pasos para Escenario PRISM

1. **Definir *loss function* constitucional** — formalizar derechos como *hard constraints* (ej. "nadie sin atención médica >4h" = constraint).
2. **Modelar 3 sub-escenarios**: *Technocracy Light* (L1-L2 dominan, humano vigila), *Algorithmic Social Contract* (L3 con AAI fuerte), *Black Box State* (L3 sin controles, captura tech).
3. **Cuantificar *compute divide* subnacional** — mapa capacidad IA por provincia/estado/municipio.
4. **Registrar hash blockchain** escenario v1.0.
5. **Publicar en landing** `escenarios/FUTURIA-2026-005-gobernanza-algoritmica.html` + newsletter #5 anexo.

---

## 10. Fuentes Oficiales y Enlaces de Verificación

| Categoría | Enlace |
|-----------|--------|
| EU AI Act (texto final) | https://eur-lex.europa.eu/eli/reg/2024/1689/oj |
| AI Liability Directive | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52022PC0496 |
| CAISO ALFS / RTD | https://www.caiso.com/informed/Pages/StakeholderProcesses/AdvancedLMPForecasting.aspx |
| ONS Brasil NEWAVE | https://www.ons.org.br/Paginas/resultados-diarios/previsao-carga.aspx |
| CAMMESA SADI | https://www.cammesa.com/mercado-electrico-mayorista |
| NHS CPNS | https://www.england.nhs.uk/coronavirus/publication/covid-19-prioritisation-scoring/ |
| BIS Project Agorá | https://www.bis.org/about/bisih/topics/cbdc/project_agora.htm |
| BCB Drex | https://www.bcb.gov.br/estabilidadefinanceira/drex |
| WFP OPTIMUS | https://www.wfp.org/innovation/optimus |
| OECD AI Policy Observatory | https://oecd.ai/ |
| ISO/IEC 42001 | https://www.iso.org/standard/81230.html |
| IEEE 7000 | https://standards.ieee.org/ieee/7000/10456/ |
| NIST AI RMF | https://www.nist.gov/itl/ai-risk-management-framework |
| GovStack | https://govstack.global/ |
| Digital Public Goods Alliance | https://digitalpublicgoods.net/ |

---

*Newsletter #5 — Base conocimiento para escenario PRISM FUTURIA-2026-005.  
Próxima edición: Newsletter #6 — "Economía de la Longevidad: suscripción a órganos artificiales y CaaS médico".  
Suscribirse: https://futuria.institute/#newsletter | Colaborar: https://futuria.institute/#colaborar*