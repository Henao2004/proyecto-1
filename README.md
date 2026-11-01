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

## ¿Qué hay aquí?

| Archivo | Para qué sirve |
|---|---|
| [`prompts/01-copilot-radiografia-trabajo.md`](prompts/01-copilot-radiografia-trabajo.md) | **Empieza aquí.** Prompt para Copilot que resume, de forma anonimizada, las tareas, correos, reuniones y documentos de la asistente, y lo que ella le pide a Copilot. |
| [`agentes/COMO-CREAR-AGENTES.md`](agentes/COMO-CREAR-AGENTES.md) | Paso a paso para crear un agente en Microsoft 365 Copilot. |
| [`analisis/01-diagnostico-octubre-2026.md`](analisis/01-diagnostico-octubre-2026.md) | **Diagnóstico** a partir del informe de Copilot: hallazgos, qué agente resuelve cada problema, plan de 30 días y cómo medir. |

### Agentes

| # | Agente | Para qué | Cuándo crearlo |
|---|---|---|---|
| 1 | [Lector de documentos](agentes/01-lector-documentos.md) | Saca de un documento los datos clave, fechas, tareas y alertas, o busca un dato puntual en un expediente | Semana 1 |
| 2 | [Redactor del despacho](agentes/02-redactor-despacho.md) | Corrige y ajusta textos con su estilo desde el primer intento; correos de remisión y respuestas | Semana 1 |
| 3 | [Citaciones y solicitudes](agentes/03-citaciones-solicitudes.md) | Documento + correo de remisión + verificación, sin inventar datos | Semana 2 |
| 5 | [Revisor antes de enviar](agentes/05-revisor-antes-de-enviar.md) | Semáforo de errores antes de enviar: datos de otro caso, anexos, fechas | Semana 2 |
| 4 | [Control de pendientes](agentes/04-control-pendientes.md) | Tablero de solicitudes sin respuesta, reiteraciones y filas para el Excel | Semana 3 |
| 6 | [Análisis de noticia criminal](agentes/06-analisis-noticia-criminal.md) | Diagnóstico jurídico-penal preliminar en 5 bloques (patrimonio económico y fe pública), como borrador para el fiscal | Ya existe: actualizar con la versión revisada |

### Plantillas

| Archivo | Para qué sirve |
|---|---|
| [`plantillas/matriz-seguimiento.csv`](plantillas/matriz-seguimiento.csv) | Matriz de seguimiento de solicitudes enviadas, que usa el agente 4 |
| [`plantillas/registro-documentos.csv`](plantillas/registro-documentos.csv) | Hoja de control donde se pegan las filas del agente 1 |
| [`agentes/plantilla-agente.md`](agentes/plantilla-agente.md) | Plantilla para diseñar nuevos agentes |

### Habilidades de Copilot

[`agentes/habilidades/`](agentes/habilidades/) tiene cinco habilidades (`SKILL.md`) para el agente 6:
diagnóstico completo, calificación de patrimonio económico, calificación de fe pública, aspectos
procesales y programa metodológico. Los pasos para cargarlas están en la ficha del
[agente 6](agentes/06-analisis-noticia-criminal.md#habilidades).

## ⚠️ Privacidad — leer antes de usar

- La información de las investigaciones penales tiene **reserva** y contiene **datos personales
  sensibles** (Ley 1581 de 2012).
- El informe de Copilot que se comparte fuera de la entidad debe ir **sin nombres, números de
  noticia criminal ni detalles de casos**. Revísalo antes de pegarlo en cualquier otro lugar.
- Usa los agentes con documentos reales **solo si la Fiscalía autoriza Copilot** para eso.
- **Nunca subas documentos reales a este repositorio.** La carpeta `datos/` está excluida para eso.
- Los agentes ayudan a organizar; las decisiones jurídicas son del fiscal.
