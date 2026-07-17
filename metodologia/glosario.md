# GLOSARIO FUTURIA — Siglas, países e instituciones

Glosario controlado del Instituto para el render web de escenarios PRISM.
Toda sigla en el cuerpo del escenario que coincida con una entrada se resalta
(emoji de bandera para países; para instituciones, popover con definición).

Mantenido por: Dirección de Escenarios FUTURIA.
Estado: v0.1 (piloto 010). Ampliar por escenario según aparezcan nuevas siglas.

## Países (código ISO 3166-1 alpha-2 -> nombre + bandera)
IN: India 🇮🇳
BR: Brasil 🇧🇷
AE: Emiratos Árabes Unidos 🇦🇪
SA: Arabia Saudí 🇸🇦
AR: Argentina 🇦🇷
MX: México 🇲🇽
ZA: Sudáfrica 🇿🇦
VN: Vietnam 🇻🇳
ID: Indonesia 🇮🇩
NG: Nigeria 🇳🇬
CL: Chile 🇨🇱
ES: España 🇪🇸
US: Estados Unidos 🇺🇸
EU: Unión Europea 🇪🇺
CN: China 🇨🇳
UK: Reino Unido 🇬🇧
JP: Japón 🇯🇵

## Instituciones / estándares / acrónimos
IRAM: Instituto Argentino de Normalización y Certificación — ente de estándares de Argentina.
ABNT: Associação Brasileira de Normas Técnicas — ente de estándares de Brasil.
GovStack: Iniciativa de infraestructura digital pública (DPI) que provee building blocks reutilizables para servicios de gobierno.
DPGA: Digital Public Goods Alliance — coalición ONU que certifica bienes públicos digitales (software, modelos, datos abiertos).
GDPR: General Data Protection Regulation — reglamento de privacidad de la UE (2018).
AI Act: Ley de Inteligencia Artificial de la UE — primer marco legal vinculante de IA; clasifica neurodatos como categoría especial.
TRL: Technology Readiness Level — escala 1-9 de madurez tecnológica (NASA).
BCI: Brain-Computer Interface — interfaz cerebro-computadora.
ZK: Zero-Knowledge — prueba criptográfica sin revelar el dato subyacente.
zkML: Zero-Knowledge Machine Learning — inferencia de ML verificable sin exponer el modelo ni los datos.
PRISM: Metodología de modelado de escenarios del FUTURIA Institute.
FUTURIA: FUTURIA Institute — instituto de prospectiva tecnológica.

## Uso en el render
- País: se reemplaza ` XX` por `🇽🇽 XX` en el texto visible y se envuelve en <span class="flag">.
- Institución: se envuelve la sigla en <span class="acr" tabindex="0">SIGLA<popover>def</popover></span>.
- El render (render_010.py) carga este glosario y aplica el resaltado automáticamente.
