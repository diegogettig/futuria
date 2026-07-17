# AUDITORÍA DE TRAZABILIDAD SAT-FUTURIA — Grupo SanCor Salud

*Auditor: auditor SAT-FUTURIA independiente. Fecha de auditoría: 14 de julio de 2026.*
*Alcance: 01-empresa.md, 02-entorno-arg.md, 03-tendencias-global-latam.md, CONSOLIDADO-hechos.md.*
*Criterio: todo dato fáctico debe llevar URL completa y verificable + Tier + fecha. Lo no verificable debe estar marcado explícitamente. No se editó ningún archivo original; solo se reporta.*

## 1. Conteo

total_hechos_con_origen: 60
hechos_sin_origen: 0
urls_truncadas: 0
porcentaje_traceable: 100%

*Base del conteo:* el corpus estructurado de hechos (tablas "HECHOS CON ORIGEN" de 01/02/03 y la tabla maestra de CONSOLIDADO) suma 60 hechos, todos con URL de origen completa (17 de 01-empresa + 15 de 02-entorno-arg + 28 de 03-tendencias = 60). Ninguna URL presenta truncamiento literal (`...`). No se detectaron hechos en las tablas formales sin origen. Véase la sección 2 para salvedades sobre afirmaciones en el cuerpo narrativo y sobre la taxonomía de Tiers.

## 2. Lista de problemas (si hay)

- [MEDIA] **Taxonomía de Tiers inconsistente entre los tres archivos fuente, y el CONSOLIDADO los mezcla sin reconciliar.** En 01-empresa.md y 02-entorno-arg.md: T1=oficial/regulatoria, T2=prensa especializada/académica, T3=prensa general. En 03-tendencias-global-latam.md la escala se redefine: T1=organismos multilaterales (OMS/OPS/BM/ONU/GPMB/CMS/Lancet original), T2=consultoría/industria (McKinsey, Deloitte, WEF, Mapfre, GVR), T3=medios/marketplaces, e **introduce T4** (académico secundario). El mismo número de Tier significa cosas distintas según el archivo (p.ej. "T2" en 02 = prensa especializada; "T2" en 03 = consultoría). El CONSOLIDADO no unifica leyenda ni normaliza, lo que impide comparar calidad de origen de forma homogénea.
- [MEDIA] **Tratamiento desigual de una misma institución en 03-tendencias.** El paper de la *Revista Panamericana de Salud Pública* / OPS-WHO Collaborating Centre (hecho 2) se etiqueta **T4 (secundario)**, mientras que la OPS como organismo (hecho 15) es **T1**. Igual inconsistencia con "The Lancet": Lancet original = T1, pero papers secundarios vía PMC = T4. La frontera T1/T4 no está aplicada con un criterio uniforme.
- [BAJA] **La columna "Hecho (resumido)" del CONSOLIDADO contiene solo IDs numéricos** (1–17, 1–15, 1–28) en lugar de reescribir el hecho. El CONSOLIDADO no es autónomamente trazable: para saber QUÉ dice cada hecho hay que cruzar con los tres archivos fuente. Debilita al documento como artefacto de trazabilidad stand-alone.
- [BAJA] **Afirmaciones en cuerpo narrativo presentadas como hecho sin URL inline** (aunque algunas llevan solo tag de Tier): 02-entorno-arg.md línea 97 — *"Líderes: OSDE, Swiss Medical, Galeno, SanCor Salud, Omint, Medifé"* (sin URL ni Tier en esa frase). 01-empresa.md línea 138 — afirmación de que SanCor superó la inflación en ajuste de cuota, con solo "(T2)" y sin URL inline (respaldada indirectamente por el hecho 13 de su tabla). No son alucinaciones, pero no cumplen el estándar estricto SAT de URL por afirmación en el cuerpo.
- [BAJA] **Algunas fuentes T3 son posts de redes sociales de baja estabilidad archivística** (02-entorno-arg.md: facebook.com/diarioelciudadanoweb, facebook.com/INFO3Noticias, instagram.com p/DOgR32gjacy). Son URL válidas y trazables en formato, pero frágiles como evidencia primaria y no confirmables contra serie oficial (p.ej. "~742.000 personas perdieron cobertura" y "market share 71%"). El propio archivo las marca como no confirmadas, lo cual está bien, pero el auditor advierte su fragilidad.

## 3. Verificacion de no-alucinacion

- **¿Hay afirmaciones presentadas como hecho sin URL?** En las tablas formales: no. En el cuerpo narrativo: sí, de gravedad BAJA — ver problema 4 (lista de "líderes" en 02; claim de ajuste por encima de IPC en 01). Ninguna es una cifra clave suelta sin respaldo alguno; todas remiten (al menos por Tier) a una fuente ya listada.
- **¿Hay URLs que no resuelven o parecen falsas (por formato)?** No. Las 60 URLs del corpus tienen formato HTTPS válido y coherentes con su dominio declarado. La más larga (`observatoriociudad.org/public/.../003%20-%20Resoluci%C3%B3n...pdf`) está correctamente URL-encodeada (espacios como `%20`), no truncada. Ninguna presenta `...` ni dominios sospechosos.
- **¿Hay mezcla de T1/T2/T3 mal etiquetada?** Sí, de forma estructural — ver problemas 1 y 2. La inconsistencia es de *definición de la escala* entre archivos, no de etiquetas sueltas equivocadas dentro de un mismo archivo. El CONSOLIDADO hereda la mezcla sin normalizar.

*Nota positiva de no-alucinación:* las cifras contradictorias de asociados (672k / 700k / 825.793) se presentan cada una con su propia fuente y el documento explicita la discrepancia en vez de forzar un número único. Los ítems no verificables (facturación, market share oficial, composición de Comisión Directiva 2025-26, CEO actual, vigencia de Staff Médico/Visa, envejecimiento específico de Argentina, salarios reales puntuales, GLP-1 +8%) están **marcados explícitamente** como "Sin información disponible" o "no verificado". Esto es conforme al método SAT y descarta alucinación de datos faltantes.

## 4. Dictamen

APTO-CON-SALVEDADES

*Justificación:* el 100% de los 60 hechos estructurados llevan URL completa y verificable, sin truncamientos ni alucinaciones (lo no disponible está marcado), pero la taxonomía de Tiers no es uniforme entre los tres archivos y el CONSOLIDADO la mezcla sin reconciliar, además de usar IDs numéricos en lugar de reescribir los hechos.

## 5. Recomendacion de uso

El corpus es apto para alimentar el informe final siempre que se (a) unifique la leyenda de Tiers en un solo estándar antes de publicar, (b) se reescriba la columna "Hecho" del CONSOLIDADO con el texto del hecho (no solo el ID), y (c) se añada URL inline a las pocas afirmaciones del cuerpo narrativo señaladas en la sección 2. Las cifras de market share y afiliados por empresa (T3) deben confirmarse contra datasets SSS (T1) antes de usarse en proyección cuantitativa.
