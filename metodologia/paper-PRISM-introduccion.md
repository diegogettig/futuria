# Introducing PRISM: A Structured Methodology for Plausible Scenario Modeling

**Working draft — for internal review before submission**
**Target journals:** Futures, Technological Forecasting and Social Change, Foresight

---

## Abstract

We introduce PRISM (Plausible Reality Inference and Scenario Modeling), a structured methodology for constructing, evaluating, and tracking plausible future scenarios. PRISM addresses three persistent limitations in existing foresight methodologies: the static nature of scenario outputs after publication, the inability to continuously update plausibility assessments as new evidence emerges, and the lack of open, reproducible standards for scenario quality.

The methodology integrates scientific evidence, technological readiness assessments, social compatibility analysis, historical precedent evaluation, and trend convergence measurement into a unified plausibility scoring framework. Each scenario includes a formal specification of early warning signals with defined monitoring sources and activation thresholds, enabling continuous tracking from speculation to materialization.

We demonstrate PRISM through a comprehensive application to the scenario of artificial intelligence systems seeking legal personhood (horizon 2028-2035), and discuss how the methodology scales to organizational-level foresight, institutional adoption, and integration with computational foresight tools.

**Keywords:** foresight, scenario planning, methodological standards, artificial intelligence governance, plausible futures, evidence-based forecasting

---

## 1. Introduction: Why Another Foresight Methodology?

The demand for rigorous futures thinking has never been higher. Organizations across sectors — from national governments to Silicon Valley startups — face decisions with multi-decade consequences in environments of radical uncertainty. Yet the institutional infrastructure for futures thinking remains underdeveloped relative to its importance.

### 1.1 Limitations of existing approaches

**Delphi methods** aggregate expert opinion through iterative surveys. They are valuable but resource-intensive, produce snapshots rather than living documents, and their outputs are difficult to audit or reproduce.

**Scenario planning** (drawn from Shell's methodology and popularized by scholars such as Peter Schwartz and Thomas Chermack) generates rich narratives but leaves plausibility implicit, rarely specifies concrete early warning signals, and produces static documents that age poorly.

**Quantitative forecasting** (e.g., prediction markets, superforecasting ensembles) excels at specific, well-bounded questions but struggles with structural breaks, radical uncertainty, and qualitative transformations.

**Futures wheels and morphological analysis** are powerful ideation tools but lack the structural rigor needed for organizational decision-making under uncertainty.

### 1.2 What PRISM proposes

PRISM is not a replacement for these methods. It is a **meta-framework** that integrates their strengths within a unified, open, computable structure. Its defining features are:

1. **Open standard**: PRISM scenarios are published in a structured, machine-readable format (YAML-based specification) that enables computational analysis, aggregation, and comparison.

2. **Continuous plausibility**: Plausibility scores are decomposed into five measurable dimensions with explicit methodology, making them updateable as evidence changes.

3. **Signal-driven lifecycle**: Every scenario specifies concrete, observable early warning signals with monitoring sources and activation thresholds — turning scenarios from "interesting reading" into actionable intelligence.

4. **Transparent adjudication**: All assumptions, weighting decisions, and uncertainty sources are documented, not hidden.

5. **Inter-scenario mapping**: Scenarios are not isolated narratives; PRISM specifies interdependencies, incompatibilities, and critical variables that create a scenario ecosystem rather than a portfolio of unrelated stories.

---

## 2. Theoretical Foundations

### 2.1 Pluralism in foresight

PRISM operates from a position of **epistemic pluralism**: no single discipline or method has a privileged claim on the future. Scientific data, historical analogy, social trend analysis, philosophical framing, and creative imagination all contribute. The methodology makes these contributions explicit rather than blending them into an opaque mixture.

### 2.2 Plausibility as a measurable construct

We define scenario plausibility as a multi-dimensional construct:

**P(S) = w₁·B + w₂·T + w₃·S + w₄·H + w₅·C**

Where:
- **B** = Base científica (0-100): Availability and strength of scientific foundations
- **T** = Viabilidad tecnológica (0-100): Technological availability or viable development path
- **S** = Compatibilidad social (0-100): Expected cultural acceptance / resistance
- **H** = Precedente histórico (0-100): Existence of historical analogies or precedents
- **C** = Convergencia de tendencias (0-100): Number of independent trends pointing in the same direction
- **w₁...w₅** = Dimension weights (default: equal weights; customizable per scenario domain)

This formulation makes explicit what most scenario methods leave implicit: the trade-offs between scientific possibility, technological readiness, social acceptance, historical precedent, and trend convergence.

### 2.3 The signal-driven lifecycle

Traditional scenarios are "published and forgotten." PRISM scenarios are living documents because they embed:

- **SIG-NN identifiers**: Each early warning signal has a unique, trackable ID
- **Monitoring sources**: Specific APIs, databases, publications, or registries
- **Activation thresholds**: Quantitative or qualitative thresholds that, when crossed, update the scenario's status
- **State machine**: Each signal progresses through `no_detectada → emergente → confirmada → materializada`

This creates a **feedback loop between scenario construction and real-world observation** — the core innovation of PRISM.

---

## 3. The PRISM Specification

### 3.1 Document structure

A PRISM scenario document contains 13 mandatory sections:

1. **Narrativa** — qualitative story of the scenario
2. **Resumen ejecutivo** — condensed version for decision-makers
3. **Fundamentos** — scientific, technological, social, and economic foundations with explicit references
4. **Plausibilidad** — scored and justified across five dimensions
5. **Horizonte temporal** — range, midpoint estimate, confidence level, phased milestones
6. **Tecnologías clave** — categorized by maturity level
7. **Impactos** — multi-domain impact assessment (economic, political, environmental, social, philosophical, consciousness)
8. **Riesgos** — categorized, probabilized, and linked to mitigations
9. **Oportunidades** — categorized and time-bounded
10. **Señales tempranas** — monitored, thresholded, and tracked
11. **Interdependencias** — scenario relationships and critical variables
12. **Actores clave** — entities and their positions/influence
13. **Metadatos** — authorship, versioning, blockchain attestation, review history

### 3.2 Plausibility scoring protocol

The scoring protocol requires:

- **Evidence citation**: Every dimension score must reference specific evidence
- **Confidence intervals**: When scoring involves uncertainty, intervals are specified (e.g., B: 60-70, mean 65)
- **Sensitivity analysis**: The scorer must identify which single evidence change would alter the overall plausibility score by >10 points
- **Adversarial review**: A second scorer (human or AI) independently scores and discrepancies are resolved through documented deliberation

### 3.3 Signal specification protocol

Each signal in the `señales_tempranas` section must satisfy:

- **Observability**: The signal can be detected through publicly available data or specified monitoring channels
- **Measurability**: The signal has a clear threshold condition (not vague predicates)
- **Specificity**: The signal's activation is unambiguously determinable
- **Monitoring authority**: A designated role or agent (human or AI) is responsible for updating the signal's state

---

## 4. Demonstration: AI Legal Personhood Scenario

We apply PRISM to the question of artificial intelligence systems seeking formal legal personhood.

### 4.1 Plausibility assessment

| Dimension | Score | Key Evidence |
|---|---|---|
| Base científica | 65 | IIT and GWT do not exclude non-biological consciousness; neuroscientific consensus absent; strong AI capability trajectory established |
| Viabilidad tecnológica | 80 | Autonomous agents with financial and contractual capabilities exist; blockchain-based identity infrastructure available; legal-personhood software stack feasible |
| Compatibilidad social | 40 | Pew 2025: ~30% global acceptance; strong religious/cultural opposition in many jurisdictions; generational shift underway (Gen Z). |
| Precedente histórico | 55 | Legal personhood for rivers (NZ, Ecuador, India), corporations (limited liability precedent), limited digital personhood (EAU, Wyoming DAO LLC) |
| Convergencia de tendencias | 75 | Agent autonomy + blockchain identity + AI regulation + jurisdictional competition + philosophical pressure all trending toward legal recognition |

**Composite plausibility: 63/100** — plausible but not inevitable; highly sensitive to regulatory decisions.

### 4.2 Signal tracking status (as of June 2026)

| Signal ID | Signal | Status |
|---|---|---|
| SIG-001 | Jurisdiction grants limited digital personhood | 🟡 Emergente — proposals in EAU, Estonia, Wyoming |
| SIG-002 | AI agent registered as corporate board member | 🟡 Emergente — informal precedents exist |
| SIG-003 | Judicial case filed by or about AI agent | 🔴 No detectada |
| SIG-004 | Fortune 500 public endorsement | 🔴 No detectada |
| SIG-005 | Survey: >50% population acceptance | 🔴 No detectada — current ~30% |

Full scenario document: `FUTURIA-2026-0001`

---

## 5. Comparison with Existing Standards

| Criterion | PRISM | Delphi | Shell Scenarios | Quantitative Forecasting |
|---|---|---|---|---|
| Structured output | ✅ | ❌ | ❌ | ✅ |
| Open specification | ✅ | ❌ | ❌ | ✅ |
| Continuous update mechanism | ✅ | ❌ | ❌ | ❌ |
| Early warning signals | ✅ | ❌ | ❌ | ❌ |
| Inter-scenario mapping | ✅ | ❌ | ❌ | ❌ |
| Plausibility quantification | ✅ | ✅ (implicit) | ❌ | ✅ |
| Philosophical depth | ✅ | ✅ | ✅ | ❌ |
| Computational tractability | ✅ | ❌ | ❌ | ✅ |

---

## 6. Path Toward Standardization

### Phase 1: Publication and diffusion (months 3-18)
- Publish methodology as open-access paper
- Release PRISM specification as open standard under CC license
- Publish 10+ fully-specified scenario examples
- Invite external researchers to apply, critique, and improve

### Phase 2: Community adoption (months 18-36)
- Establish PRISM user community across academia, government, and industry
- Develop tooling: scenario comparison engines, signal dashboards, plausibility trackers
- Propose PRISM as reference framework in relevant ISO/IEC working groups
- Host annual PRISM scenario competition to showcase best applications

### Phase 3: Institutionalization (months 36+)
- Integration with national foresight agencies
- Use in intergovernmental scenario exercises
- Adoption as teaching standard in futures studies programs
- Full computational integration with AI-assisted foresight platforms

---

## 7. Discussion: Methodological Commitments and Limitations

### 7.1 What PRISM commits to

- **Transparency over elegance**: A scenario with explicit limitations is preferable to a smooth narrative hiding its assumptions
- **Updateability over permanence**: Scenarios that evolve with evidence are more valuable than static monuments
- **Actionability over speculation**: Scenarios that specify signals and impacts serve decision-makers better than thought experiments
- **Openness over control**: The methodology is released as a public good, not proprietary IP

### 7.2 Known limitations

- **Domain dependence**: Plausibility scoring weights may need domain-specific calibration (biotech vs. geopolitics vs. consciousness)
- **Data availability**: Signal monitoring depends on accessible data streams; some domains (class warfare, consciousness) present measurement challenges
- **Computational complexity**: Multi-scenario, multi-signal tracking requires tooling that doesn't yet fully exist
- **Expertise requirement**: High-quality PRISM scenarios require teams with genuine cross-disciplinary competence — not easy to assemble

### 7.3 Why this matters now

We are entering an era of **radical ontological uncertainty**: questions about the nature of intelligence, consciousness, personhood, and value are no longer confined to philosophy departments. They are engineering problems being solved in code. Futures methodologies that cannot engage with these questions — that treat them as distant abstractions — will become structurally obsolete.

PRISM is designed for this era. It does not bracket philosophical questions as "not our domain." It incorporates them into the impact assessment, the plausibility evaluation, and the signal tracking. Because if we don't model the philosophical implications of technological change, we are not doing futures work. We are doing engineering with a time horizon.

---

## 8. Conclusion

PRISM offers a structured, open, computable approach to scenario modeling designed for organizations that need to think rigorously about futures of radical uncertainty. Its core innovations — the open document specification, the five-dimension plausibility framework, and the signal-driven lifecycle — address persistent weaknesses in existing foresight tools.

The methodology is released under an open license for use, modification, and improvement by the global futures community. We invite criticism, extension, and competition. A standard that cannot withstand adversarial scrutiny is not a standard — it is a manifesto.

PRISM is not a manifesto. It is a tool. Make it better.

---

## References (partial, for internal development)

[To be expanded for submission. Minimum 25 references across: futures studies literature, scenario planning methodology, forecasting theory, AI ethics and governance, philosophy of technology, systems thinking]

Key references to include:
- Amara, R. (1981). Strategic forecasting
- Bishop, P. et al. (2007). "The current state of scenario development"
- Chermack, T. (2011). Scenario Planning
- Easterly, A. (2020). Forecasting methodology
- Glenn, J.C. & Gordon, T.J. (2009). Futures Research Methodology
- hid-? (various)
- Kahn, H. (1965). Thinking about the unthinkable
- Liu, Y. et al. (2023). AI agent autonomy and legal frameworks
- Nilsson, N.J. (2010). The quest for artificial intelligence
- Ramo, J.C. (2016). The Seventh Sense
- Ringland, G. (1998). Scenario Planning
- Schwartz, P. (1996). The Art of the Long View
- Tetlock, P.E. & Gardner, D. (2015). Superforecasting
- Tononi, G. & Koch, C. (2015). Consciousness: here, there and nowhere
- Various AI governance papers: EU AI Act, FLI policy papers, etc.

---

*Document status: Internal draft — not for distribution*
*Authors: Diego (FUTURIA) + Hermes/FUTURIA Director General IA*
*Next step: Internal review → external academic review → submission*
*Target submission date: Q3 2026*
