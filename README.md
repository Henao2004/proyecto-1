# proyecto-1 — Agentes de Copilot para una asistente de fiscal

Analizar el trabajo diario de una asistente de fiscal con ayuda de **Microsoft Copilot** y crearle
**agentes de Copilot** que le ahorren tiempo.

## Cómo funciona

```
1. Radiografía           2. Análisis                 3. Agentes
Copilot revisa su    →   Claude y tú analizan    →   Se crean agentes en
trabajo y entrega        el informe y priorizan      Copilot, listos para
un informe anónimo       qué mejorar                 copiar y pegar
```

> **Uso diario:** [`GUIA-USO-DIARIO.md`](GUIA-USO-DIARIO.md) dice qué agente usar en cada momento del día, con las frases para empezar.

## ¿Qué hay aquí?

| Archivo | Para qué sirve |
|---|---|
| [`prompts/02-copilot-barrido-pendientes.md`](prompts/02-copilot-barrido-pendientes.md) | Prompt para Copilot (lunes y jueves): revisa el correo de 15 días y entrega las filas de pendientes para la matriz. |
| [`prompts/01-copilot-radiografia-trabajo.md`](prompts/01-copilot-radiografia-trabajo.md) | **Empieza aquí.** Prompt para Copilot que resume, de forma anonimizada, las tareas, correos, reuniones y documentos de la asistente, y lo que ella le pide a Copilot. |
| [`agentes/COMO-CREAR-AGENTES.md`](agentes/COMO-CREAR-AGENTES.md) | Paso a paso para crear un agente en Microsoft 365 Copilot. |
| [`analisis/01-diagnostico-octubre-2026.md`](analisis/01-diagnostico-octubre-2026.md) | **Diagnóstico** a partir del informe de Copilot: hallazgos, qué agente resuelve cada problema, plan de 30 días y cómo medir. |

### Agentes

| # | Agente | Para qué | Cuándo crearlo |
|---|---|---|---|
| 1 | [Lector de documentos y respuestas](agentes/01-lector-documentos.md) | Analiza las respuestas que llegan (a qué responden, constancia o fondo, completitud, anexos, datos útiles, actualización de la matriz y resumen para el fiscal); fichas, búsquedas, cronología e intervinientes de expedientes. Versión completa con 2 habilidades | Semana 1 |
| 2 | [Redactor del despacho](agentes/02-redactor-despacho.md) | Corrige y ajusta textos con su estilo desde el primer intento; correos de remisión, respuestas, reiteraciones y lenguaje claro. Versión completa con 3 habilidades | Semana 1 |
| 3 | [Citaciones y solicitudes](agentes/03-citaciones-solicitudes.md) | Citaciones (también virtuales), solicitudes a entidades (vehículos, RUNT, patios), órdenes a policía judicial y reiteraciones: documento, correo, evento para el calendario y fila para la matriz. Versión completa con 3 habilidades | Semana 2 |
| 5 | [Revisor antes de enviar](agentes/05-revisor-antes-de-enviar.md) | Semáforo 🔴🟡🟢 antes de enviar: datos de otro caso, anexos, destinatario, fechas, formatos (NC de 21 dígitos, placas), datos personales y restos de Copilot. Versión completa con 2 habilidades | Semana 2 |
| 4 | [Control de pendientes](agentes/04-control-pendientes.md) | Barrido del correo, pendientes por etapas (radicada ≠ respondida), tablero por urgencia, reiteraciones, informe semanal para el fiscal y filas para la matriz. Versión completa con 2 habilidades | Semana 3 |
| 6 | [Análisis de noticia criminal](agentes/06-analisis-noticia-criminal.md) | Diagnóstico jurídico-penal preliminar en 5 bloques (patrimonio económico y fe pública), como borrador para el fiscal | Ya existe: actualizar con la versión revisada |

### Plantillas

| Archivo | Para qué sirve |
|---|---|
| [`plantillas/medicion-carga-trabajo.xlsx`](plantillas/medicion-carga-trabajo.xlsx) | Medición de la carga de trabajo (semana 1 y semana 4): datos de Outlook, registro diario, mediciones puntuales y resumen automático |
| [`plantillas/directorio-entidades.csv`](plantillas/directorio-entidades.csv) | Directorio de correos institucionales de entidades, para el conocimiento del agente 3 |
| [`plantillas/matriz-seguimiento.xlsx`](plantillas/matriz-seguimiento.xlsx) | Matriz de pendientes con estados por etapas y alertas automáticas (vencida, escalar, reiterar, por vencer, incorporar). La alimentan los agentes 3 y 4 |
| [`plantillas/registro-documentos.csv`](plantillas/registro-documentos.csv) | Hoja de control donde se pegan las filas del agente 1 |
| [`agentes/plantilla-agente.md`](agentes/plantilla-agente.md) | Plantilla para diseñar nuevos agentes |

### Habilidades de Copilot

[`agentes/habilidades/`](agentes/habilidades/) tiene las habilidades (`SKILL.md`) que se cargan en
Agent Builder:

| Agente | Habilidades |
|---|---|
| [1 — Lector de documentos y respuestas](agentes/01-lector-documentos.md#habilidades) | `lectura-de-respuestas`, `analisis-de-expedientes` |
| [2 — Redactor del despacho](agentes/02-redactor-despacho.md#habilidades) | `estilo-institucional`, `correccion-ortografica`, `correos-del-despacho` |
| [3 — Citaciones y solicitudes](agentes/03-citaciones-solicitudes.md#habilidades) | `citaciones-y-entrevistas`, `solicitudes-a-entidades`, `ordenes-policia-judicial` |
| [4 — Control de pendientes](agentes/04-control-pendientes.md#habilidades) | `seguimiento-por-etapas`, `barrido-de-correo` |
| [5 — Revisor antes de enviar](agentes/05-revisor-antes-de-enviar.md#habilidades) | `verificacion-de-envios`, `proteccion-de-datos-en-envios` |
| [6 — Análisis de noticia criminal](agentes/06-analisis-noticia-criminal.md#habilidades) | `diagnostico-penal-preliminar`, `calificacion-patrimonio-economico`, `calificacion-fe-publica`, `aspectos-procesales`, `programa-metodologico` |

## ⚠️ Privacidad — leer antes de usar

- La información de las investigaciones penales tiene **reserva** y contiene **datos personales
  sensibles** (Ley 1581 de 2012).
- El informe de Copilot que se comparte fuera de la entidad debe ir **sin nombres, números de
  noticia criminal ni detalles de casos**. Revísalo antes de pegarlo en cualquier otro lugar.
- Usa los agentes con documentos reales **solo si la Fiscalía autoriza Copilot** para eso.
- **Nunca subas documentos reales a este repositorio.** La carpeta `datos/` está excluida para eso.
- Los agentes ayudan a organizar; las decisiones jurídicas son del fiscal.
