# proyecto-1 — Apoyo al trabajo de una asistente de fiscal

## Propósito
Analizar y mejorar el trabajo de una asistente de fiscal (Fiscalía General de la Nación, Colombia,
Sistema Penal Oral Acusatorio — Ley 906 de 2004) con prompts, plantillas y, más adelante,
automatizaciones sencillas (Excel, correo, scripts en Python).

## Estructura
- `prompts/` — prompts listos para copiar y pegar, numerados (`01-…`, `02-…`). En español.
- `plantillas/` — plantillas vacías (CSV/Excel/Word) sin ningún dato real.
- `analisis/` — diagnósticos y planes de mejora (solo información general y anonimizada).
- `datos/` — documentos reales para trabajar localmente. **Está en `.gitignore` y nunca se sube.**
- `scripts/` — (futuro) automatizaciones en Python 3; con pruebas en `tests/` usando pytest.

## Reglas obligatorias
- **El repositorio es público.** Nunca hagas commit de nombres, cédulas, números de noticia criminal,
  direcciones, teléfonos ni contenido de documentos reales. Usa ejemplos ficticios marcados como tales.
- La información de las investigaciones tiene reserva y datos personales sensibles (Ley 1581 de 2012).
  No propongas enviar datos reales a servicios externos sin autorización de la entidad.
- No automatizar ni extraer datos del SPOA u otros sistemas institucionales sin autorización expresa.
- Las decisiones jurídicas son del fiscal: el proyecto ayuda con organización y gestión, no da
  asesoría jurídica. Toda norma o término procesal citado lleva "verificar con la norma vigente".

## Convenciones
- Todo (código, comentarios, documentos, commits) en español.
- Commits cortos con el formato `tipo: descripción` (por ejemplo `feat: prompt de extracción`,
  `docs: diagnóstico inicial`).
- Los CSV usan punto y coma (`;`) como separador para que Excel en español los abra bien.
- Si cambias las columnas del prompt 2, actualiza también `plantillas/registro-documentos.csv`.
