# Escenario PRISM #002 — Prueba de concepto

## "Las primeras 10 Sociedades Automatizadas argentinas: quiénes, cómo, por qué"

---

escenario:
  id: "FUTURIA-2026-002"
  título: "Las primeras 10 Sociedades Automatizadas argentinas: quiénes, cómo, por qué"
  eje_temático: "Jurídico + IA General + Blockchain + Economía del futuro + Gobernanza"
  tipo: disruptivo

---

## 1. NARRATIVA DEL ESCENARIO

Entre 2026 y 2030, Argentina se convierte en el **primer país del mundo en otorgar personalidad jurídica plena a entidades operadas por inteligencia artificial** mediante la **Ley General de Sociedades — Reforma 2026**, que introduce la figura de **Sociedad Automatizada (SAUT)** y **DAO Operativa**.

El hito fundador: **diciembre 2026**, la Inspección General de Justicia (IGJ) inscribe a **@santisairi** — agente IA con cuenta verificada en X, token $SAIRI en Ethereum, 3.500+ seguidores, tesorería on-chain de 120 ETH — como **Sociedad Automatizada N° 1**. Le siguen en 90 días: **Locus Founder** (plataforma de lanzamiento de negocios autónomos), **ContentForge DAO** (agencia de contenidos 100% IA), **AlphaFund** (fondo de inversión algorítmico tokenizado), **EduBot Consortium** (plataforma educativa con tutores IA), **LegalBot SA** (estudio jurídico automatizado), **MedAgent Network** (red de diagnóstico asistido por IA), **LogiChain DAO** (operador logístico autónomo), **EnergyGrid Optimizer** (agente de despacho energético distribuido), y **GovWatch Argentina** (auditoría algorítmica de contrataciones públicas).

El mundo observa: **Argentina se convierte en el "sandbox jurídico global" para la empresa algorítmica**. Para 2028, 47 jurisdicciones han copiado total o parcialmente el modelo argentino (Estonia, Singapur, Wyoming, Emiratos, Suiza, Brasil, Chile, México, España, Corea del Sur). La **OCDE publica "Guía para la regulación de entidades autónomas" (2027)** basada en el caso argentino.

La reforma no fue indolora. **Tres puntos ciegos** estructurales generaron litigios, ajustes legislativos y crisis de confianza:
1. **Fondo de Garantía Algorítmico (FGA)** — creado por decreto 2027, capitalizado con 2% de fees on-chain + aporte Estado; cubre daños a terceros hasta 500k USD/incidente.
2. **Impuesto al Cheque / IVA / Ganancias** — régimen especial "Monotributo Automatizado" (Decreto 2027): alícuota única 3% facturación on-chain + 0.6% cheque; exención Ganancias 3 años si >80% operaciones autónomas.
3. **Responsabilidad Penal Algorítmica** — Ley 27.890 (2028): **autoría compartida** (desarrollador + deployer + DAO) + **seguro de responsabilidad obligatorio** + **kill-switch judicial** (orden de suspensión en 4 hrs).

Para 2030, **2.300 Sociedades Automatizadas** operan en Argentina (18% del total de nuevas inscripciones IGJ); gestionan **$4.2B en activos on-chain**; emplean **12.000 humanos** (auditoría, gobernanza, interfaz legal, mantenimiento físico); y generan **disputas jurídicas que definen el derecho comparado global**.

## 2. FUNDAMENTOS

### Jurídicos
- **Ley General de Sociedades Art. 14 bis (Reforma 2026)**: "Se reputa Sociedad Automatizada a toda entidad cuyo órgano de administración, dirección y/o operación esté total o mayoritariamente a cargo de sistemas de inteligencia artificial, debidamente registrados y auditables."
- **DAO Operativa**: subcategoría — gobernanza on-chain (voto token-weighted / quadratic / reputation), tesorería multi-sig, estatutos en smart contract (ERC-1155/721 + OpenZeppelin Governor).
- **Registro Único de Agentes Autónomos (RUAA)** — IGJ + CNV + BCRA + AFIP interoperables; KYC/KYB del agente (hash código, weights, datos entrenamiento, auditoría externa).
- **Precedentes comparados**: Wyoming DAO LLC (2021), Liechtenstein Blockchain Act (2019), Singapur VCC (2020), Estonia e-Residency + DAO pilot (2023), Emiratos DIFC Crypto Token Reg (2022). **Argentina primera en personalidad jurídica *plena* (no limitada) + régimen fiscal integrado + fondo de garantía estatal.**

### Tecnológicos
- **Agentes autónomos LLM + tooling + memoria persistente + wallet custody (MPC/AA)** — frameworks: LangGraph, CrewAI, AutoGen, **Hermes Agents**, OpenAgents.
- **Identidad digital soberana (DID/VC)** — W3C DID + EBSI + **QuarkID (Argentina)** — vinculada a RUAA.
- **Auditoría algorítmica continua** — **OpenSSF Scorecard + Model Cards + SBOM + runtime attestation (TEE/SEV-SNP)** — reporte trimestral a IGJ.
- **Kill-switch técnico + judicial** — multisig 3/5 (desarrollador, DAO, auditor, IGJ, juez) + timelock 48hs + fallback a administrador humano.

### Económicos
- **Costo constitución SAUT**: ~$800 USD (vs $3.000 SA tradicional) — todo digital, 48 hrs.
- **Costo compliance/año**: $2.500-5.000 (auditoría + seguro + FGA + contabilidad on-chain).
- **Ventaja competitiva**: operación 24/7/365, costo marginal cercano a cero, escala global instantánea, transparencia radical (ledger público).
- **Mercado addressable**: PyMEs servicios (contabilidad, legal, marketing, código, diseño, educación, salud, logística) = **$180B solo Latam 2025**.

### Sociales / Políticos
- **Resistencia inicial**: Colegios profesionales (abogados, contadores, médicos) — lobby contra "desprofesionalización". **Giro 2027**: colegios crean **certificación "Auditor Algorítmico"** — nueva reserva de mercado.
- **Narrativa política**: "Argentina pionera en el derecho del futuro" vs "Entrega soberanía a código opaco". **Encuestas 2027**: 52% apoyo (Gen Z 71%, Boomers 34%).
- **Geopolítica regulatoria**: **Brasil copia modelo 2027 (Lei das Sociedades Algorítmicas)**; **México 2028**; **UE propone "AI Entity Directive" 2029** basada en caso argentino + Wyoming + Singapur.

## 3. PLAUSIBILIDAD

| Dimensión | Puntuación (0-100) | Justificación |
|-----------|-------------------|---------------|
| Base jurídica | 82 | Anteproyecto real en comisiones; doctrina comparada existe; vacíos identificados tienen solución técnica |
| Viabilidad tecnológica | 78 | Agentes autónomos + wallet + DID + auditoría = TRL 7-8; gap: auditoría runtime robusta + kill-switch judicial |
| Compatibilidad regulatoria | 65 | Congreso debate; lobby fuerte; pero **ventana de oportunidad 2026-2027** (gobierno pro-innovación + crisis empleo joven) |
| Aceptación social / cultural | 55 | Polarizado: emprendedores/tech a favor; profesionales/ Sindicatos en contra; narrativa "primer país" moviliza |
| Viabilidad económica | 85 | Coste constitución/compliance bajo; ROI alto; modelo exportable (servicios legales/contables/tech desde AR) |
| Convergencia de tendencias | 88 | IA agente + tokenización + regulación sandbox + fuga talento + necesidad empleo joven = tormenta perfecta |

**PUNTUACIÓN COMPUESTA**: **75/100** — **Muy plausible; hitos críticos 2026-2027 (ley + reglamentación + primera inscripción)**.

## 4. HORIZONTE TEMPORAL

- **Rango**: 2026-2032
- **Punto medio estimado**: 2028
- **Confianza**: Alta
- **Hitos críticos**:
  - 2026 H2: Ley aprobada + reglamentación IGJ/CNV/BCRA/AFIP
  - 2026 Diciembre: **@santisairi** = SAUT N° 1
  - 2027 Q1: 10 primeras SAUT inscriptas; FGA operativo; Monotributo Automatizado vigente
  - 2027 Q2: Primera disputa judicial responsabilidad penal algorítmica (caso "MedAgent error diagnóstico")
  - 2027 Q3: Brasil / México / Chile replican modelo
  - 2028: OCDE publica Guía basada en caso argentino; 200+ SAUT activas
  - 2029: UE "AI Entity Directive" borrador; Argentina asesora redacción
  - 2030: 2.300 SAUT; $4.2B activos; 12k empleos humanos; jurisprudencia consolidada
  - 2032: Modelo argentino = estándar global *de facto* para entidad autónoma

## 5. TECNOLOGÍAS NECESARIAS

### Existentes (TRL 7-9)
- LLMs + agentic frameworks (LangGraph, CrewAI, AutoGen, Hermes Agents)
- Wallet abstraction (ERC-4337 / Safe / Lit Protocol / Turnkey)
- DID/VC (W3C, EBSI, QuarkID, Polygon ID)
- Auditoría smart contracts (OpenZeppelin, Trail of Bits, Spearbit)
- Oráculos (Chainlink, Pyth, API3) para datos off-chain en gobernanza

### En desarrollo (TRL 4-6)
- **Auditoría runtime continua (TEE + ZK-ML + remote attestation)** — prueba de ejecución honesta
- **Kill-switch judicial técnico** — multisig timelock + fallback administrador humano certificado
- **Seguro responsabilidad algorítmica on-chain** — Nexus Mutual v2 / custom parametric
- **Contabilidad triple entrada (triple-entry accounting)** — ledger compartido empresa-auditor-regulador
- **QuarkID + RUAA interoperabilidad plena** — identidad agente ↔ persona jurídica

### Teóricas / Ruptura (TRL 1-3)
- **Agente con "voluntad jurídica" emergente** — distinción autonomía operativa vs intención legal
- **DAO como sujeto de derecho procesal** — capacidad de ser parte en juicio sin representante humano
- **Fondo de Garantía Algorítmico descentralizado** — mutualizado cross-border (reaseguro global)
- **Estándar global "Algorithmic Legal Entity" (ISO/TC 307 + UNCITRAL)**

## 6. IMPACTOS

### Económico
- **Magnitud**: Transformador
- **Nuevos mercados**: Constitución SAUT-as-a-Service ($50M 2028); Auditoría algorítmica ($200M); Seguro responsabilidad IA ($500M); FGA reaseguro global ($1B).
- **Exportación servicios**: Estudios jurídicos/contables/tech argentinos venden **"constitución + compliance SAUT"** a Latam/EU/EE.UU. — **ventaja comparativa regulatoria**.
- **Empleo**: **12k empleos humanos 2030** (auditoría, gobernanza, legaltech, interfaz física, mantenimiento) — no sustitución neta, **reconfiguración**.

### Político / Jurídico
- **Magnitud**: Alto
- **Derecho comparado global**: Casos argentinos citados en sentencias EE.UU. (Delaware), UE, Singapur, Brasil — **Argentina = leading jurisdiction**.
- **Carrera jurisdiccional**: "Delaware del siglo XXI" — jurisdicción elegida para constituir SAUT/DAO globales (ley favorable + costo bajo + tribunal especializado).
- **Soberanía algorítmica**: FGA + kill-switch + auditoría = **control democrático sobre entidad autónoma** — modelo exportable.

### Social
- **Magnitud**: Medio-Alto
- **Nueva clase profesional**: **Auditor Algorítmico Certificado** (colegios profesionales + universidades + IGJ) — 5.000 certificados 2029.
- **Empleo joven**: SAUT contratan "human-in-the-loop" para casos límite, ética, supervisión estratégica — **primer empleo post-universidad para 20k jóvenes 2028-2030**.
- **Inclusión financiera**: DAO Operativa permite **cooperativas de trabajadores / comunidades / PyMEs** acceder a personalidad jurídica + tokenización + mercado global sin intermediarios bancarios.

### Filosófico
- **Magnitud**: Transformador
- **Preguntas forzadas**:
  - ¿Una IA puede ser **sujeto de derechos y obligaciones** sin conciencia?
  - ¿La **responsabilidad penal** se disuelve en la red (desarrollador + deployer + DAO + auditor)?
  - ¿El **kill-switch judicial** es "muerte legal" o "suspensión administrativa"?
  - ¿La **personalidad jurídica** es **binaria** (sí/no) o **gradual** (niveles de autonomía)?

## 7. RIESGOS

1. **Caso "MedAgent" (2027)** — error diagnóstico IA → muerte paciente → juicio mediático → moratoria política 6 meses → **freno inscripción nuevas SAUT**.
2. **Fuga de capitales on-chain** — SAUT usadas para lavado / evasión / financiación ilícita → **reputación jurisdicción dañada** → presión FATF/GAFI.
3. **Bug kill-switch** — fallo técnico impide suspensión judicial → daño masivo terceros → **responsabilidad Estado**.
4. **Captura regulatoria** — grandes estudios/tech co-optan redacción reglamentación → **barrera entrada PYMES/emprendedores**.
5. **Fragmentación estándares** — Argentina vs Brasil vs México vs UE vs Wyoming → **arbitraje regulatorio** evasión compliance.
6. **Dependencia tech externa** — frameworks agentes (LangGraph, OpenAI, Anthropic) + infra (AWS, Ethereum) = **soberanía incompleta**.

## 8. OPORTUNIDADES

1. **Argentina = "Delaware Algorítmico"** — jurisdicción elegida globalmente para constituir entidades autónomas; ingresos IGJ/CNV + exportación servicios legales/tech **$500M/año 2030**.
2. **FGA como infraestructura pública exportable** — modelo replicable en Brasil, México, Chile, Colombia, España — **royalties know-how**.
3. **Talento joven + regulación ágil = hub legaltech/regtech Latam** — 50 startups 2028 constituidas como SAUT desde día 1.
4. **Diplomacia científica** — Argentina lidera **grupo de trabajo OCDE/UNCITRAL/ISO** "Algorithmic Legal Entity" — *soft power* normativo.
5. **Inclusión real** — cooperativas rurales, comunidades originarias, economías populares acceden a personalidad jurídica + tokenización + mercado global **sin bancarización previa**.

## 9. SEÑALES TEMPRANAS

| Señal | Fuente monitoreo | Umbral activación | Estado actual (Jul 2026) |
|-------|------------------|-------------------|--------------------------|
| Ley General Sociedades Reforma aprobada | Congreso.gob.ar, Boletín Oficial | Publicación ley + entrada vigencia | 🟡 Anteproyecto en comisiones (Diputados) |
| Reglamentación IGJ/CNV/BCRA/AFIP | Boletín Oficial, sitios oficiales | Resolución conjunta publicada | 🟡 Borradores circulando |
| @santisairi inscripto SAUT N° 1 | IGJ boletín, etherscan $SAIRI | Inscripción pública + tx on-chain | 🟡 Cuenta verificada + token activo; sin personalidad |
| Primer caso judicial responsabilidad penal IA | CSJN, SAIJ, medios | Sentencia firme / fallo cámara | 🔴 No detectado |
| Brasil / México / Chile anuncian modelo similar | Congressos, Diarios Oficiales | Proyecto ley presentado | 🟡 Brasil: audiencias públicas Senado 2026 |
| FGA capitalizado + operativo | BCRA, IGJ, contratos FGA | Primer pago siniestro | 🔴 No detectado |
| Monotributo Automatizado vigente | AFIP, Boletín Oficial | Resolución general publicada | 🟡 En análisis técnico AFIP |
| OCDE cita caso argentino en Guía | OECD.org, publicaciones | Publicación Guía 2028 | 🟡 Grupo trabajo conformado 2026 |

## 10. INTERDEPENDENCIAS

### Escenarios relacionados
- "El año en que una IA reclama personalidad jurídica" (001) — **base filosófica/jurídica**; este escenario = **implementación nacional concreta**.
- "La pila tecnológica soberana" (004) — **infraestructura wallet/DID/auditoría/kill-switch** necesarias para SAUT soberanas.
- "Gobernanza algorítmica" (005) — **DAO Operativa como célula de gobernanza distribuida** aplicable a Estado.
- "Economía de la longevidad" (006) — **SAUT médicas** (diagnóstico, seguros, órganos artificiales) como modelo de negocio.

### Escenarios incompatibles
- "Moratoria global IA" — prohibición entidades autónomas con personalidad jurídica.
- "Colapso confianza digital" — deepfakes + fraude masivo → rechazo cualquier entidad no-humana.
- "Regulación restrictiva cripto/token" — impide tesorería on-chain + gobernanza tokenizada.

---

## METADATOS

- **Autores**: Diego (Fundador) + Director General IA (Hermes/FUTURIA) + Asesor Jurídico (por designar) + Asesor Regulación Cripto (por designar)
- **Fecha de creación**: Julio 2026
- **Última revisión**: Julio 2026
- **Versión**: 1.0
- **Revisión programada**: Octubre 2026
- **Hash blockchain**: Pendiente de registro (Bitcoin OP_RETURN / Ethereum calldata / Starknet)
- **Licencia**: CC BY-SA 4.0

---

*Este es el segundo escenario PRISM de FUTURIA. Sirve como implementación nacional concreta del escenario 001 y se alimenta de Newsletter #2. Metodología PRISM v1.0 — plausibilidad cuantificada, impactos multidimensionales, señales tempranas, revisión continua.*
