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
| [`agentes/01-lector-documentos.md`](agentes/01-lector-documentos.md) | Agente que lee un documento y saca los datos clave, fechas, tareas, alertas y una fila para Excel. |
| [`agentes/plantilla-agente.md`](agentes/plantilla-agente.md) | Plantilla para diseñar los siguientes agentes. |
| [`plantillas/registro-documentos.csv`](plantillas/registro-documentos.csv) | Encabezados de la hoja de control en Excel donde se pegan las filas del agente 1. |
| `analisis/` | Diagnóstico y plan de mejora, construidos con el informe de Copilot. |

## ⚠️ Privacidad — leer antes de usar

- La información de las investigaciones penales tiene **reserva** y contiene **datos personales
  sensibles** (Ley 1581 de 2012).
- El informe de Copilot que se comparte fuera de la entidad debe ir **sin nombres, números de
  noticia criminal ni detalles de casos**. Revísalo antes de pegarlo en cualquier otro lugar.
- Usa los agentes con documentos reales **solo si la Fiscalía autoriza Copilot** para eso.
- **Nunca subas documentos reales a este repositorio.** La carpeta `datos/` está excluida para eso.
- Los agentes ayudan a organizar; las decisiones jurídicas son del fiscal.
