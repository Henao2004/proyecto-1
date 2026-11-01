# proyecto-1 — Apoyo al trabajo de una asistente de fiscal

Herramientas para **entender, organizar y mejorar** el trabajo diario de una asistente de fiscal:
prompts para usar con IA, plantillas y, más adelante, automatizaciones sencillas.

## ¿Qué hay aquí?

| Archivo | Para qué sirve |
|---|---|
| [`prompts/01-diagnostico-trabajo.md`](prompts/01-diagnostico-trabajo.md) | Entrevista guiada que levanta todas las tareas, tiempos y problemas, y entrega un diagnóstico con mejoras priorizadas y un plan de 30 días. |
| [`prompts/02-extraccion-documentos.md`](prompts/02-extraccion-documentos.md) | Saca de un documento (denuncia, oficio, acta, correo…) los datos clave, fechas, tareas pendientes y alertas, y genera una fila lista para Excel. |
| [`plantillas/registro-documentos.csv`](plantillas/registro-documentos.csv) | Encabezados de la hoja de control. Ábrela en Excel y pega ahí las filas que genera el prompt 2. |

## Cómo empezar

1. **Diagnóstico (una vez):** abre `prompts/01-diagnostico-trabajo.md`, copia el bloque de texto en
   una conversación nueva con Claude y responde las preguntas. Guarda el resultado.
2. **Uso diario:** cada vez que llegue un documento, usa `prompts/02-extraccion-documentos.md` y
   pega la fila resultante en tu hoja de Excel de control.
3. **Mejora continua:** con el diagnóstico en mano, aplicamos las mejoras del plan de 30 días.

## ⚠️ Privacidad — leer antes de usar

- La información de las investigaciones penales tiene **reserva** y contiene **datos personales
  sensibles** (Ley 1581 de 2012).
- Pega documentos reales en una herramienta de IA **solo si la entidad lo autoriza**. Si no,
  anonimiza: cambia nombres por iniciales y reemplaza cédulas, direcciones y teléfonos por `[DATO]`.
- **Nunca subas documentos reales a este repositorio.** La carpeta `datos/` está excluida para eso.
- La IA ayuda a organizar; las decisiones jurídicas son del fiscal.
