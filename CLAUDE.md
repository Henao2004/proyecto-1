# proyecto-1 — Agentes de Copilot para una asistente de fiscal

## Propósito
Analizar el trabajo de una asistente de fiscal (Fiscalía General de la Nación, Colombia, Sistema
Penal Oral Acusatorio — Ley 906 de 2004) y diseñarle **agentes de Microsoft 365 Copilot** que mejoren
su rendimiento. Flujo: prompt de radiografía en Copilot → informe anonimizado → análisis con Claude
→ agentes listos para copiar en Copilot.

## Estructura
- `prompts/` — prompts para pegar en Copilot, numerados (`01-…`).
- `agentes/` — un archivo por agente (`NN-nombre.md`) con estos campos: Nombre, Descripción,
  Instrucciones, Conocimiento, Indicaciones iniciales y Cómo probarlo. Basarse en
  `agentes/plantilla-agente.md`; los pasos para crearlos están en `agentes/COMO-CREAR-AGENTES.md`.
- `agentes/habilidades/<nombre>/SKILL.md` — habilidades para cargar en Agent Builder (Copilot exige un
  `SKILL.md` o un `.zip` que lo contenga). Frontmatter YAML: `name` igual al nombre de la carpeta, en
  minúsculas y con guiones; `description` entre comillas, de 1.024 caracteres o menos, que diga
  cuándo invocarla. Las referencias normativas van como orientativas, con la marca "verificar". Los
  `.zip` no se suben al repositorio: se generan para entregarlos.
- `analisis/` — diagnósticos y planes de mejora a partir del informe de Copilot (solo datos anonimizados).
- `plantillas/` — plantillas vacías (CSV/Excel/Word) sin ningún dato real.
- `datos/` — documentos reales para uso local. **Está en `.gitignore` y nunca se sube.**

## Reglas obligatorias
- **El repositorio es público.** Nunca hagas commit de nombres, cédulas, números de noticia criminal,
  direcciones, teléfonos ni contenido de documentos reales. Si el usuario pega un informe con esos
  datos, anonimízalo antes de guardarlo en `analisis/` y avísale.
- La información de las investigaciones tiene reserva y datos personales sensibles (Ley 1581 de 2012).
  Los agentes se usan con documentos reales solo si la entidad autoriza Copilot para eso.
- No proponer automatizar ni extraer datos del SPOA u otros sistemas institucionales sin
  autorización expresa.
- Las decisiones jurídicas son del fiscal: los agentes organizan y redactan borradores, no dan
  asesoría jurídica. Toda norma o término procesal citado lleva "verificar con la norma vigente".

## Convenciones
- Todo en español, con lenguaje sencillo: la usuaria final no es técnica.
- Las instrucciones de cada agente deben quedar por debajo de ~8.000 caracteres, el límite de Copilot.
  Mídelo con `wc -m` sobre el bloque de instrucciones.
- Los prompts para el chat de Copilot deben ser compactos (menos de ~4.000 caracteres).
- Los CSV usan punto y coma (`;`) como separador para que Excel en español los abra bien. Si cambias
  las columnas del agente 1, actualiza `plantillas/registro-documentos.csv`.
- `plantillas/matriz-seguimiento.xlsx` es compartida por los agentes 3 y 4 y el prompt 02: columnas B..L
  y estados (Pendiente, Radicada, Reiterada, Respondida, Programada, Cerrada) deben ser idénticos en los
  cuatro. Se regenera con un script de openpyxl; probar las alertas con LibreOffice antes de publicar.
- Commits cortos con el formato `tipo: descripción`.
