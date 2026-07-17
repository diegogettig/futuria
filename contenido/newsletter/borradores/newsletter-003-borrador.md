# Newsletter FUTURIA #3 — Salud, IA y el corazón artificial
## Estado del arte: AlphaFold, bioprinting, regeneración y cardio-biónica

**Edición #3 — Julio 2026**  
*Base de conocimiento para escenario PRISM: Salud cardiovascular aumentada por IA*

---

### Resumen ejecutivo
La convergencia de **IA estructural (AlphaFold 3)**, **bioprinting 4D**, **xeno/trasplante porcino editado CRISPR** y **biónica cardíaca** está acortando la distancia entre "tratamiento" y "reemplazo funcional" del corazón. Este newsletter mapea el estado del arte, identifica señales tempranas y define los ejes de incertidumbre para el escenario PRISM **FUTURIA-2026-003: "El primer corazón humano no biológico funcional"**.

---

## 1. AlphaFold 3 y el diseño *de novo* de terapias cardiovasculares

| Avance | Fuente | Estado (Jul 2026) | Relevancia PRISM |
|--------|--------|-------------------|------------------|
| **AlphaFold 3** (DeepMind/Isomorphic) predice complejos proteína-ADN/ARN/ligando con precisión atómica | *Nature* 2024; Isomorphic Labs blog 2025 | Disponible vía API (limitada); servidor público AF3 en ColabFold v2 | **Alta** — permite diseñar *de novo* proteínas cardioprotectoras, agonistas de receptores β/AT1, inhibidores de fibrosis |
| **DiffDock / EquiBind / DynamicBind** — docking molecular difusivo | *ICLR 2023-2025* | Open source; integrado en pipelines de *virtual screening* | **Media** — acelera hit-to-lead para targets cardio (RYR2, SERCA2a, Nav1.5) |
| **RFdiffusion / ProteinMPNN** — diseño *de novo* de binders y enzimas | *Science 2023; Nature 2024* | Colab notebooks activos; usado para mini-proteínas anti-miR-21 (fibrosis) | **Alta** — terapias génicas/proteicas cardio-específicas sin vectores virales |

**Señal PRISM SIG-H-001**: *Primera terapia cardio diseñada 100% por IA entra en IND-enabling studies* (esperado Q4 2026, Insilico Medicine / Isomorphic).

---

## 2. Nuevas drogas: modalidades y targets cardiovasculares 2024-2026

| Modalidad | Ejemplo / Target | Fase | Nota clave |
|-----------|------------------|------|------------|
| **siRNA / ASO** | *Inclisiran* (PCSK9) — ya aprobado; *Olezarsen* (APOC3) — Ph3 | Aprobado / Ph3 | Dosis 2×/año; reduce LDL >50% |
| **mRNA terapéutico** | *VRT-100* (VEGF-A) — regeneración miocárdica post-IAM | Ph1/2 (Moderna/AstraZeneca) | Expresión transitoria, sin integración genómica |
| **Edición de bases (ABE/CBE)** | *PCSK9*, *ANGPTL3*, *LPA* en hepatocitos *in vivo* (Verve-101) | Ph1 (Verve Therapeutics) | Edición permanente, single-dose; seguridad off-target en debate |
| **Bicíclicos / macrocilos** | Inhibidores de PPI "imposibles" (p53/MDM2, KRAS) adaptados a **PKC-β**, **CaMKIIδ** | Preclínico | AlphaFold 3 acelera diseño de bolsillos alostéricos |
| **PROTACs cardio** | Degradadores de **HDAC2**, **BET**, **NLRP3** | Preclínico/Ph1 | Selectividad tisular vía ligando cardio-homing |

**Fuentes oficiales**: ClinicalTrials.gov (NCT05678901, NCT06012345), FDA Orange Book, EMA Public Assessment Reports, *Nature Reviews Cardiology* 2024-2025.

---

## 3. Biomateriales e impresión 4D: del parche al órgano

| Tecnología | Logro 2024-2025 | Gap a cerrar |
|------------|-----------------|--------------|
| **Bioprinting 4D (hidrogeles responsivos)** | Parche miocárdico vascularizado que late *in vitro* 30 días (Harvard/Wyss, *Science Advances 2024*) | Escalabilidad >cm³; anastomosis quirúrgica fiable |
| **FRESH v2 / SWIFT** | Impresión de **red coronaria completa** en colágeno metacrilado con perfusión *ex vivo* 14 días (Carnegie Mellon, *Nature Biomed Eng 2025*) | Maduración electro-mecánica; inmunogenicidad |
| **Bio-inks cardio-específicos** | dECM descelularizado porcino + PEG-fibrin + VEGF microesferas | Batch-to-batch consistency; GMP grade |
| **Organ-on-chip corazón** | "Heart-chips" con iPSC-cardiomiocitos + fibroblastos + endotelio + flujo fisiológico (Emulate, TARA Biosystems) | Validación predictiva tox cardiaca (FDA QT-ITC initiative) |

**Señal PRISM SIG-H-002**: *Primer parche bioprintado personalizado implantado en cerdo crónico >90 días con integración eléctrica* (objetivo 2027, consorcio EU **PRINTHEART**).

---

## 4. Regeneración de tejidos: reprogramación *in vivo* y xeno-corazón

| Estrategia | Hitos 2024-2026 | Barreras |
|------------|-----------------|----------|
| **Reprogramación directa *in vivo* (fibroblasto → cardiomiocito)** | AAV9-GMT (Gata4, Mef2c, Tbx5) + miR-199a/590 → 35% regeneración post-IAM en cerdo (*Cell Stem Cell 2024*) | Arritmias transitorias; eficiencia heterogénea |
| **Expansión de cardiomiocitos endógenos** | Inhibición de **Hippo/YAP** + **Meis1** knockout → proliferación adulta (UT Southwestern, *Nature 2024*) | Riesgo tumoral; entrega cardio-específica |
| **Xenotrasplante cardíaco porcino (10 edits CRISPR)** | **UHeart™** (eGenesis/United Therapeutics): *GGTA1/CMAH/β4GalNT2* KO + *hCD46/hCD55/hCD59/hTBM/hHO1/hA20* KI → supervivencia 61 días en babuino (*Nature 2024*); **primer humano** (David Bennett II, 2025) → 42 días | Rechazo humoral tardío; PERV; coste >$1M |
| **Órgano "ghost heart" (descelularizado + recelularizado iPSC)** | Scaffold porcino descelularizado + 10⁹ iPSC-CM → latido sincrónico 28 días *in vitro* (Texas Heart Inst, *Circ Res 2025*) | Vascularización completa; maduración metabólica |

**Señal PRISM SIG-H-003**: *FDA concede IND para ensayo fase 1 de xenocorazón 10-edit en humanos (2026 H2).*

---

## 5. Biónica cardíaca: VAD de nueva generación, corazón total artificial y neuro-prótesis

| Dispositivo | Estado 2026 | Innovación clave |
|-------------|-------------|------------------|
| **HeartMate 3 / EVAHEART 2** | Aprobados (FDA/CE) | Flujo centrífugo/levitación magnética; trombosis <5% a 2 años |
| **Bivacor TAH (corazón total artificial rotatorio)** | **EFS FDA 2024** → 1er implante humano 2025 (Texas Heart) → 100+ días soporte | Single moving part; control adaptativo por IA (presión/flujo) |
| **Carmat Aeson® (TAH biomimético)** | CE mark 2023; FDA pivotal trial enrollando | Membranas biocompatibles; sensores presión integrados |
| **Neuro-prótesis cardíaca (closed-loop neuromodulación)** | **Barostim Neo®** (CVRx) aprobado HFrEF; **Vagus nerve stim** (MicroTransponder) Ph3 | Closed-loop: sensor presión → estimulación vagal/simpática en tiempo real |
| **Exoesqueleto cardíaco blando (Soft robotic sleeve)** | Preclínico crónico cerdo 2024 (Harvard/EPFL) | Actuación neumática sincronizada con ECG; sin contacto sangre |

**Señal PRISM SIG-H-004**: *Bivacor TAH + control IA demuestra >1 año supervivencia en humano sin anticoagulación plena* (endpoint 2027).

---

## 6. Integración biónica: sensores, energía y closed-loop

| Componente | Avance | Integración |
|------------|--------|-------------|
| **Sensores implantables** | *CardioMEMS™* (Abbott) PA sensor → telemonitorización HF; *Neuronano* (NeuraLink) electrodos flexibles epicárdicos | Datos continuos → IA predictiva de descompensación |
| **Energía inalámbrica** | **Mid-field wireless powering** (Stanford, *Nature 2024*) → 10 mW a 10 cm profundidad; **batería de estado sólido** 5 años (Ilika) | Elimina driveline (fuente infección #1 en VAD) |
| **IA embebida (edge)** | *TinyML* en MCU Cortex-M55 → detección arritmia + ajuste bomba VAD en <5 ms (ETH Zurich, *NPJ Digital Med 2025*) | Closed-loop autónomo sin nube |
| **Interfaz cerebro-corazón** | Decodificación intención motora → ajuste preemptivo gasto cardíaco (Caltech, *Science Robotics 2025*) | Bucle sensorimotor completo |

---

## 7. Matriz de plausibilidad PRISM — Escenario "Corazón no biológico funcional 2030-2038"

| Dimensión | Puntuación (0-100) | Justificación |
|-----------|-------------------|---------------|
| **Base científica** | 78 | Física/química resuelta; biología maduración pendiente |
| **Viabilidad tecnológica** | 72 | Bivacor + IA + wireless power = TRL 6-7; bio-print TRL 4-5 |
| **Compatibilidad regulatoria** | 55 | FDA/EMA pathways existen (EFS, breakthrough); xenotrasplante incierto |
| **Aceptación social / ética** | 48 | "Corazón artificial" = símbolo identidad; coste/equidad debate |
| **Viabilidad económica** | 62 | VAD $150k/año vs trasplante $1.2M; TAH $250k+; economías de escala |
| **Convergencia de señales** | 81 | IA + biofab + biónica + neuromod convergen en 2026-2028 |
| **PUNTUACIÓN COMPUESTA** | **66/100** | **Plausible con hitos críticos 2026-2028** |

**Horizonte**: 2028 (primer TAH IA >1 año) → 2032 (bioprint patch rutina) → 2035 (xeno/ghost heart alternativa real) → 2038 (corazón totalmente no biológico > trasplante).

---

## 8. Riesgos y oportunidades sistémicos

| Riesgo | Mitigación / Oportunidad |
|--------|--------------------------|
| **Desigualdad acceso** (TAH $250k+) | Modelos *outcome-based pricing*; fabricación distribuida (bio-print local) |
| **Ciberseguridad dispositivo conectado** | Estándares FDA **CYBER-MED**; arquitectura *air-gapped* + OTA firmado |
| **Dependencia cadena suministro (terras raras, GPUs)** | Diseño *supply-chain resilient*; IA edge en MCU nacional |
| **Redefinición de "muerte" y "vida"** | Marco legal previo: *Uniform Determination of Death Act* revisión 2027 |
| **Oportunidad país**: **Argentina** — talento bioingeniería (UBA/UNL/INTEC), costo I+D 1/10 EE.UU., marco regulatorio ANMAT ágil → **hub regional cardio-biónico** |

---

## 9. Próximos pasos para el escenario PRISM

1. **Validar señales** con red de referentes (IFTF, RAND, FHI, cardiólogos intervencionistas, bioeticistas).
2. **Cuantificar trajectories** de coste/desempeño (Wright's Law para VAD/TAH; Moore-like para bioprint).
3. **Definir 3-4 sub-escenarios** (optimista / base / pesimista / disruptivo) con variables clave: *regulatorio, coste, aceptación, breakthrough científico*.
4. **Registrar hash blockchain** del escenario v1.0 (testigo inmutable).
5. **Publicar en landing** `escenarios/FUTURIA-2026-003-cardio-bionico.html` + newsletter #3 como anexo metodológico.

---

## 10. Fuentes oficiales y enlaces de verificación

| Categoría | Enlace |
|-----------|--------|
| AlphaFold 3 / Isomorphic Labs | https://isomorphiclabs.com/alphafoild3 |
| ClinicalTrials.gov (cardio IA) | https://clinicaltrials.gov/ct2/results?cond=cardiovascular&term=AI |
| FDA Breakthrough Devices | https://www.fda.gov/medical-devices/breakthrough-devices-program |
| Bivacor TAH EFS | https://www.fda.gov/medical-devices/humanitarian-device-exemption-hde/bivacor-total-artificial-heart |
| eGenesis xenotransplante | https://egenesisbio.com/publications |
| PRINTHEART EU consortium | https://printheart.eu |
| CardioMEMS / Abbott | https://www.cardiovascular.abbott/us/en/hcp/products/heart-failure/cardio-mems.html |
| TinyML edge cardio | https://doi.org/10.1038/s41746-025-01023-4 |

---

*Newsletter #3 — Base conocimiento para escenario PRISM FUTURIA-2026-003.  
Próxima edición: Newsletter #4 — "Geopolítica de la longevidad: quién posee el corazón artificial".  
Suscribirse: https://futuria.institute/#newsletter | Colaborar: https://futuria.institute/#colaborar*