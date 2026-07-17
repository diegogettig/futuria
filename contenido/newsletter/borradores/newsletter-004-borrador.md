# Newsletter FUTURIA #4 — La pila tecnológica soberana
## Estado del arte: semiconductores, fotónica, actuadores y la carrera por el sustrato físico de la IA

**Edición #4 — Julio 2026**  
*Base de conocimiento para escenario PRISM: Hard Tech Foundations / Soberanía tecnológica*

---

### Resumen ejecutivo
Toda la capa de aplicación de la IA (LLMs, agentes, robótica, descubrimiento de fármacos, simulación climática) descansa sobre una **pila física estrecha y frágil**: litografía EUV (ASML), GPUs/TPUs/hardware de inferencia (NVIDIA, Google, Groq, Cerebras), interconexiones fotónicas, actuadores de precisión (Moog, Timken, Harmonic Drive) y materiales avanzados (SiC, GaN, diamante sintético). Esta newsletter mapea los **cuellos de botella críticos**, las **empresas/países que los controlan**, y las **trayectorias de sustitución/autonomía** que definen el mapa geopolítico 2025-2035.

---

## 1. NVIDIA: más que GPUs — la pila completa de cómputo acelerado

| Capa | Tecnología / Producto | Diferenciación clave | Moat (2026) |
|------|----------------------|---------------------|-------------|
| **Silicio** | Blackwell (B200/B100), Rubin (2026), Vera (2027) | Arquitectura unificada training+inference; NVLink 7.2 (1.8 TB/s); 208B transistores TSMC 4NP | 18-24 meses ventaja proceso/diseño |
| **Interconexión** | **NVLink / NVSwitch / InfiniBand (Mellanox)** | Escalado a 576 GPUs/dominio; SHARP in-network reduction; latencia <1µs | Ecosistema cerrado; CUDA-only |
| **Red óptica** | **Spectrum-X / Silicon Photonics (co-packaged optics)** | 1.6T/3.2T per port; energía/punto <5 pJ/b; elimina transceptores pluggables | Integración vertical; roadmap 2027-2030 |
| **Software** | **CUDA 12.x / cuDNN / TensorRT / Triton / NeMo / RAPIDS** | 5M+ developers; backward compatibility 15 años; kernel fusion automático | **El moat real** — switching cost años |
| **Sistemas** | **DGX / HGX / MGX / OVX** | Reference designs para OEMs; rack-scale liquid cooling; certificación enterprise | Canal + soporte + ciclo 12 meses |
| **Cloud** | **DGX Cloud (Oracle, Azure, GCP, AWS)** | Renta de supercomputadora por mes; no capex; same software stack | Margen recurrente; lock-in híbrido |

**Proyección 2027**: NVIDIA >$200B revenue (70% data center); >80% share training; 60% inference. **Riesgo**: concentración geográfica (TSMC Taiwán), antimonopolio (EU/US), alternativas open (ROCm, oneAPI, Triton backend).

**Señal PRISM SIG-HT-001**: *Primera "AI Factory" soberana no-NVIDIA operativa en UE/JP/CN con pila completa alternativa (ROCm + SiPearl + CEA-Leti + ASML EUV access)*.

---

## 2. ASML: el cuello de botella único de la litografía EUV

| Métrica | Valor 2026 | Tendencia |
|---------|------------|-----------|
| **Sistemas EUV instalados** | ~180 (EUV 0.33 NA) | +20-25/año |
| **High-NA EUV (0.55 NA)** | 6-8 sistemas (IMEC, Intel, TSMC, Samsung) | Ramp 2025-2027; €350M/unidad |
| **Cuota mercado litografía avanzada** | **>90% EUV; 100% High-NA** | Monopolio de facto |
| **Cadena suministro crítica** | **ZEISS** (óptica), **TRUMPF** (fuente láser), **VSL** (metrología), **Carl Zeiss SMT** | Todos EU (NL/DE); single-source en múltiples subsistemas |
| **Export controls** | Wassenaar + US/JP/NL trilateral (2023) | Bloquea ventas a CN <7nm; High-NA solo aliados |

**Roadmap tecnológico**:
- **2025-2027**: High-NA EUV producción (Intel 18A/14A, TSMC N2, Samsung 2nm)
- **2028-2030**: **EUV de doble patrón / multi-patterning assist** → 1.5nm / 1nm
- **2030+**: **Litografía de rayos X blandos / e-beam multi-haz / directed self-assembly** (I+D en IMEC, Fraunhofer, CNSE)

**Geopolítica**: **Países Bajos** = palanca estratégica Occidente. **China** (SMEE, Huawei, CAS) desarrolla EUV propia: fuente LDP (laser-driven plasma) 13.5nm — demostró 200W en lab 2024; target 500W 2027. Gap real: **óptica ZEISS** (multicapa Mo/Si, defectos <0.1nm) + **metrología actínica**.

**Señal PRISM SIG-HT-002**: *SMEE (Shanghai Micro Electronics) anuncia primer scanner EUV pre-producción 2027; verificación independiente de resolution <20nm half-pitch*.

---

## 3. Actuadores y movimiento: la capa física de la robótica encarnada

| Empresa / Tecnología | Producto clave | Especificación diferencial | Aplicación objetivo |
|---------------------|----------------|----------------------------|---------------------|
| **Moog Inc.** | **Actuadores electrohidrostáticos (EHA) / EMA** | Densidad potencia 5-10 kW/kg; fuerza 500N-500kN; tolerancia radiación/espacio; TRL 9 (F-35, ISS, lanzadores) | Robots humanoides industriales/defensa; exoesqueletos; manipulación precisa |
| **Timken** | **Rodamientos de rodillos cónicos / esféricos / cruzados** + **reductores de precisión (Nadella, Cone Drive)** | Carga combinada radial+axial; vida L10 >100k hrs; precisión <1 arc-min; materiales M50/MP35N/cerámico híbrido | Articulaciones robot; wrists; ejes de precisión |
| **Harmonic Drive (NACHI-FUJIKOSHI)** | **Reductores de onda tensional (strain wave)** | Cero backlash; ratio 30:1-160:1; compacidad extrema; 90%+ eficiencia | Caderas/hombros/muñecas humanoides; telescopios espaciales |
| **Maxon / FAULHABER** | **Motores DC sin escobillas / EC frameless** | Densidad torque >1 Nm/cm³; diámetro 6-90mm; control integrado (EPOS) | Dedos robóticos; end-effectors; drones |
| **NIDEC / Shimpo** | **Reductores cicloidales / planetarios de precisión** | Alto torque/volumen; rigidez torsional; backlash <1 arc-min | Base móvil; hombros; actuadores lineales integrados |
| **Schunk / Zimmer / Robotiq** | **Pinzas / módulos de fuerza-torque / quick changers** | Sensorización 6-ejes integrada; cambio <5s; IP69K | Manipulación logística/ensamblaje/inspección |

**Tendencias 2025-2030**:
1. **Actuadores integrados (smart actuators)**: motor + reductor + encoder + driver + comms (EtherCAT/TSN/CAN-FD) en carcasa única → reduce cableado, latencia, peso.
2. **Materiales avanzados**: engranajes **a base de diamante policristalino (PCD)** / **nitruro de silicio (Si3N4)** / **aceros nanostructurados (AMS 6491 mod)** → 3-5x vida, 2x capacidad carga.
3. **Impresión 3D de reductores** (GE Additive, Desktop Metal, Trumpf): geometrías imposibles (lattice interno refrigeración conformal) → 40% peso, 30% costo.
4. **Actuación dieléctrica / hidráulica suave / músculos artificiales (HASEL, DEA, PAM)** — para robots colaborativos seguros; aún TRL 4-5.

**Cuellos de botella geopolíticos**:
- **Tier 1 (occidente)**: Moog, Timken, Harmonic (JP), Maxon (CH), Nidec (JP), Schunk (DE) — **controlan IP + materiales + certificaciones aero/defensa**.
- **China**: **Leader Harmonic / Ningbo Zhongda / HDSI** — clones strain-wave 80% rendimiento; gap en vida fatiga y consistencia lote.
- **Rusia**: **NPK Tekhmash / NPP Salyut** — capacidad legacy soviética; sanctions limitan materiales (MP35N, M50, cerámicos).

**Señal PRISM SIG-HT-003**: *Primer humanoide chino (Unitree / Fourier / UBTech) con actuadores 100% domésticos certificados 10k ciclos MTBF en fábrica automotriz*.

---

## 4. Semiconductores de potencia y fotónica: la infraestructura energética y de datos

| Tecnología | Líderes | Estado 2026 | Impacto |
|------------|---------|-------------|---------|
| **SiC (carburo de silicio) 200mm** | Wolfspeed, Onsemi, Infineon, ST, ROHM, **Toshiba, Mitsubishi** | Ramp 200mm 2025-2027; coste <Si 2x (vs 5x 2020) | EV, data centers, grid, robots móviles — eficiencia + densidad |
| **GaN (nitruro de galio) 200mm** | Navitas, GaN Systems (Infineon), EPC, Transphorm, **PanoSemi (CN)** | 650V/900V mainstream; 1200V emergente | Cargadores, fuentes AI servers (48V direct), motor drives |
| **Diamante sintético (sustrato / disipador)** | Element Six (De Beers), **Diamond Materials (DE), AKHAN (US), Orion (JP)** | Wafer 100mm 2025; conductividad térmica 2200 W/mK | Disipación chips 3D-stacked; RF power; quantum NV centers |
| **Fotónica de silicio (SiPh) — transceptores 800G/1.6T/3.2T** | Intel, Cisco/Acacia, Marvell, Broadcom, **Celestial AI, Ayar Labs, Ranovus** | Co-packaged optics (CPO) en switches 2025; 6.4T 2027 | Elimina bottleneck I/O GPU-GPU; energía/bit -10x |
| **Memoria CXL 3.0 / 3.1** | Samsung, SK hynix, Micron, Montage, Rambus | Type 3 (memoria compartida) 2025; coherencia cache | Disaggregation memoria GPU/CPU; reduce TCO training |

**Geopolítica materiales**:
- **Tier 1 sustratos**: **SiC/GaN epitaxia** — Wolfspeed (US), Infineon (DE/US), ST (FR/IT/SG), ROHM (JP), **San'an / CETC (CN)** — China 40% capacidad SiC 2025, pero **defect density** 2-3x occidente.
- **Tier 0 materias primas**: **Arena de alta pureza (SiO₂ >99.999%)** — Unimin (US/BE), **Quartz Corp (NO/US)**; **Gala metal** — China 80% producción; **Diamante HPHT/CVD** — Element Six (ZA/UK/CN), Sumitomo (JP).

---

## 5. Otras empresas/centros críticos en la pila profunda

| Capa | Entidades clave | Nota geopolítica |
|------|----------------|------------------|
| **Diseño EDA / IP** | Synopsys, Cadence, Siemens EDA, **Arm (SoftBank/UK)**, **RISC-V International (CH/US)**, **SiFive, Ventana, Andes (TW)** | China impulsa **RISC-V + EDA doméstico (Empyrean, Primarius)** para evitar sanctions EDA |
| **Fabricación FEOL/BEOL** | **TSMC (TW)**, Samsung (KR), Intel (US/DE/IL), **SMIC (CN)**, GlobalFoundries (US/SG/DE), **Rapidus (JP)** | Rapidus + IBM + imec → 2nm 2027; SMIC 7nm yield <50% |
| **Empaquetado avanzado (CoWoS / SoIC / Foveros / Hybrid Bonding)** | TSMC, Intel, Amkor, ASE, JCET, **TFME (CN)** | Cuello botella HBM + GPU: **CoWoS-L/S capacidad 2025 < demanda 2x** |
| **HBM / DRAM** | SK hynix (KR), Samsung (KR), Micron (US), **CXMT (CN)** | HBM3E 12-hi 2025; CXMT 2-3 gen atrás |
| **Centros I+D públicos** | **IMEC (BE)**, **Fraunhofer IZM/IMS (DE)**, **Leti (FR)**, **AIST (JP)**, **IME (CN)**, **IMEC-US (NY)**, **MIT.nano**, **Stanford NSL**, **CSEM (CH)** | IMEC = nodo neutro Occidente; China replica modelo con **Instituto de Microelectrónica CAS (IME-CAS)** + **Wuxi / Shanghai / Chengdu** |
| **Quantum / Neuromórfico** | IBM, Google, Quantinuum, IonQ, Rigetti, **Pasqal (FR)**, **QuTech (NL)**, **USTC (CN)**, **RIKEN (JP)** | No crítico 2026; horizonte 2030+ para advantage real |

---

## 6. Matriz de vulnerabilidad / soberanía 2026

| Capa | Control único (single-source) | Riesgo concentración | Iniciativas soberanas alternativas |
|------|------------------------------|---------------------|-----------------------------------|
| **EUV Litografía** | ASML (NL) + ZEISS (DE) + TRUMPF (DE) | **Crítico** — 1 empresa mundo | CN: SMEE + CAS; US: DARPA LEX / e-beam; JP: Canon/Nikon (rezago) |
| **GPU IA entrenamiento** | NVIDIA (US) — diseño + SW | **Crítico** — CUDA lock-in | US: AMD ROCm, Intel Gaudi, Groq, Cerebras; CN: Huawei Ascend, Biren, Moore Threads; EU: SiPearl/Rhea; JP: Fujitsu Monaka |
| **HBM / Memoria ancho banda** | SK hynix / Samsung (KR) — 95% share | **Alto** | US: Micron; CN: CXMT; JP: Kioxia (re-entry) |
| **Actuadores precisión** | Harmonic (JP), Moog (US), Timken (US), Maxon (CH) | **Medio-Alto** — IP + materiales | CN: Leader/Ningbo; IN: Tata Advanced; BR: Embraer Defesa |
| **SiC/GaN potencia** | Wolfspeed/Onsemi/Infineon/ST/ROHM | **Medio** — diversificación geográfica | CN: San'an, CETC, Yangjie; IN: Tata Power; AE: GlobalFoundries Abu Dhabi |
| **Fotónica SiPh** | Intel/Cisco/Marvell/Broadcom (US) | **Medio** — ecosistema abierto emergente | EU: PhotonDelta (NL), IMEC; CN: Sintone, Huaguang; JP: NTT |

---

## 7. Proyecciones de impacto 2025-2035

### Económico (TAM proyectado 2030)
- **Hardware IA (chips + sistemas + red)**: **$400-600B/año** (vs $150B 2024)
- **Litografía + equipos semis**: **$150-200B/año** (EUV + High-NA + empaquetado)
- **Robótica encarnada (actuadores + sensores + control)**: **$120-180B/año** (humanoides + logística + defensa)
- **Potencia wide-bandgap (SiC/GaN)**: **$80-120B/año** (EV + grid + data centers)
- **Fotónica centros datos**: **$50-80B/año** (CPO + transceptores 3.2T+)

### Geopolítico — "La pila determina la soberanía"
1. **EE.UU.**: Controla **diseño (NVIDIA, AMD, Google), EDA (Synopsys/Cadence), IP (Arm, RISC-V), software (CUDA, PyTorch, TensorFlow), cloud (AWS/Azure/GCP), sanciones exportación**. Estrategia: **CHIPS Act + alianzas (AUKUS, Quad, EU-US TTC)** para asegurar acceso FEOL/BEOL.
2. **China**: Estrategia **"全链条自主可控" (full-stack autonomy)** — inversión $1.4T (2020-2030) en semis, materiales, equipos, EDA, IP, talento. Gaps críticos: **EUV, High-NA, EDA, HBM, actuadores alta fiabilidad**.
3. **UE**: **Chips Act €43B** — foco en **diseño (RISC-V, SiPearl), fotónica (PhotonDelta), potencia (Infineon/ST), empaquetado (Fraunhofer), I+D (IMEC, CEA-Leti)**. No aspira a FEOL <28nm; busca **autonomía estratégica en nodos maduros + especializados** (automoción, industrial, defensa).
4. **Japón**: **Rapidus (2nm 2027) + Kioxia + Tokyo Electron + materiales (Shin-Etsu, SUMCO, JSR) + actuadores (Harmonic, Nidec)**. Alianza **Japón-EEUU (JOINT) + Japón-UE** para asegurar posición en cadena valor.
5. **Corea del Sur**: **Memoria (Samsung/SK hynix) + Foundry (Samsung 3nm/2nm) + Equipos (Wonik IPS, Eugene Tech)**. Vulnerable: dependencia materiales JP (fotoresist, blank mask) + equipos US/NL.
6. **Taiwán**: **TSMC = "escudo de silicio"**. Riesgo existencial: concentración geográfica 90% chips avanzados. Estrategia: **dispersión geográfica (Arizona, Kumamoto, Dresde) + disuasión**.
6. **Resto (India, Brasil, Emiratos, Arabia Saudita, Israel, Canadá, Australia)**: Nichos de **diseño, empaquetado, materiales, talento, energía** — buscan **posición en cadena valor sin FEOL cutting-edge**.

### Científico — Carreras abiertas 2025-2030
| Carrera | Hitos clave | Líderes | Disruptores potenciales |
|---------|-------------|---------|------------------------|
| **Post-EUV (<1nm)** | High-NA ramp → Directed Self-Assembly → X-ray / e-beam multi-beam | ASML/IMEC/Intel/TSMC | Canon/Nikon (MPS), SMEE (CN), DARPA LEX (US) |
| **Arquitectura post-GPU** | Analog/in-memory compute; neuromórfico; fotónico; sparsity-native | IBM, Mythic, Rain, Lightmatter, Celestial, **Tsinghua/USTC** | **New physics** (memristores, spintrónica, superconductor SFQ) |
| **Actuadores "músculo artificial"** | HASEL / DEA / PAM >100k ciclos; densidad potencia >biológico | Max Planck, ETH, Harvard, **CAS (CN)**, **KIST (KR)** | Materials breakthrough (ionicos, elastoméricos) |
| **Materiales cuánticos para clásica** | Diamante / hBN / TMDCs para disipación / interconexión / sensado | Element Six, AKHAN, **NIMS (JP)**, **SKKU (KR)** | Integración CMOS-compatible |
| **Fabricación aditiva micro/nano** | Two-photon polymerization; electrohydrodynamic printing; nanoimprint | Nanoscribe, **IMEC**, **SUSTech (CN)**, **KAIST (KR)** | Democratiza prototipado; reduce capex |

---

## 8. Riesgos sistémicos y oportunidades

| Riesgo | Probabilidad | Impacto | Mitigación / Oportunidad |
|--------|--------------|---------|--------------------------|
| **Bloqueo TSMC (conflicto Estrecho)** | Media (2027-2030) | **Catastrófico** — parada global IA/auto/defensa | Stockpiling wafers; fabs dispersas (AZ, JP, DE); diseños portables (RISC-V + open PDK) |
| **Falla cadena suministro materiales (REEs, gases, sustratos)** | Alta (ya ocurre) | Alto | Reciclaje urbano; minería aliada (AU, CA, CL, VN); sustitución (AlN vs Al2O3, Cu vs Au) |
| **Ciberataque a fabs / EDA / repositorios IP** | Media | Alto | Air-gap build farms; reproducible builds; SBOM obligatorio; zero-trust supply chain |
| **Concentración talento (PhDs semis/IA en 5 países)** | Alta | Medio-Largo | Programas "semiconductor workforce" (US CHIPS, EU Chips, JP, KR, IN, BR, AR) |
| **Ruptura tecnológica (nuevo paradigma computo)** | Baja-Media | **Transformador** | Vigilancia IMEC/Leti/Fraunhofer/DARPA/NSFC; cartera apuestas diversificada |

**Oportunidad país — Argentina / Latam**:
- **Talento**: Físicos, ingenieros electrónicos, CS — costo 1/5-1/10 US/EU.
- **Energía**: Renovables baratas (Patagonia viento, NOA sol) → data centers / fabs de nodos maduros (28-130nm) + empaquetado.
- **Materiales**: Litio, cobre, tierras raras (proyecto **Río Negro / Catamarca**) — integración vertical posible.
- **Marco**: **Ley de Promoción de la Industria de Semiconductores** (borrador 2026) — incentivos fiscales, zonas francas, visas talento.
- **Nicho**: **Diseño RISC-V / analog / mixed-signal / power IC / fotónica integrada / empaquetado avanzado / actuadores impresos 3D** — sin capex FEOL cutting-edge.

---

## 9. Próximos pasos para el escenario PRISM

1. **Cuantificar trayectorias coste/rendimiento** (Wright's Law) para cada capa: EUV, GPU, HBM, actuador, SiC, SiPh.
2. **Modelar 4 sub-escenarios** geopolíticos: *Cooperación gestionada / Bloques desconectados / Ruptura taiwanesa / Salto paradigmático*.
3. **Identificar "puntos de estrangulamiento" (chokepoints)** donde una intervención (política, inversión, estándar) maximiza resiliencia.
4. **Registrar hash blockchain** escenario v1.0.
5. **Publicar en landing** `escenarios/FUTURIA-2026-004-hard-tech-foundations.html` + newsletter #4 anexo.

---

## 10. Fuentes oficiales y enlaces de verificación

| Categoría | Enlace |
|-----------|--------|
| ASML Annual Report / Roadmap | https://www.asml.com/en/investors |
| NVIDIA Investor Relations / GTC | https://investor.nvidia.com/ |
| Moog Space & Defense / Industrial | https://www.moog.com/ |
| Timken Precision Bearings / Drives | https://www.timken.com/ |
| Harmonic Drive Technology | https://harmonicdrive.net/ |
| IMEC Annual Report / Programs | https://www.imec-int.com/ |
| SEMI Industry Statistics | https://www.semi.org/ |
| US CHIPS Act / Commerce Dept | https://www.chips.gov/ |
| EU Chips Act / Chips JU | https://chips-ju.europa.eu/ |
| China Semiconductor Industry Association (CSIA) | https://www.csia.net.cn/ |
| Rapidus / Japan METI | https://www.rapidus.co.jp/ |
| PhotonDelta / Dutch Photonics | https://photondelta.com/ |
| Compound Semiconductor Applications (SiC/GaN) | https://www.compoundsemiconductor.net/ |

---

*Newsletter #4 — Base conocimiento para escenario PRISM FUTURIA-2026-004.  
Próxima edición: Newsletter #5 — "Geopolítica del dato: quién entrena, quién inferencia, quién gobierna".  
Suscribirse: https://futuria.institute/#newsletter | Colaborar: https://futuria.institute/#colaborar*