# Guía diaria de los agentes

Qué agente usar en cada momento, cómo pedírselo y la rutina para que ninguna solicitud se quede sin
respuesta.

**Los seis agentes en Copilot:** 1 Lector de documentos y respuestas · 2 Redactor del despacho ·
3 Citaciones y solicitudes · 4 Control de pendientes · 5 Revisor antes de enviar · 6 ANALISIS NOTICIA
CRIMINAL.

## ¿Qué necesito hacer?

| Situación | Agente | Frase para empezar | Después |
|---|---|---|---|
| **Llegó la respuesta** de una entidad, un juzgado o policía judicial | 1 | `Llegó esta respuesta. Analízala:` | Cambiar el estado en la matriz, guardar los anexos con el nombre sugerido y enviar el resumen al fiscal si es relevante |
| **Llegó una denuncia**, un informe o un documento nuevo | 1 | `Haz la ficha de este documento:` | Fechas clave al calendario y tareas a la lista del día |
| **Necesito un dato** de un expediente largo | 1 | `En este expediente, busca:` | Si aparece con valores distintos, confirmar cuál es el correcto |
| El fiscal pide el **análisis de una noticia criminal** | 6 | `Analiza esta noticia criminal y elabora el diagnóstico preliminar en los cinco bloques.` | Es un borrador: el fiscal lo revisa y decide |
| Hay que definir **actos investigativos y órdenes** | 6 → 3 | `A partir de este informe policial, propone los actos urgentes y el programa metodológico inicial, con la finalidad y la prioridad de cada acto.` · `Convierte este programa metodológico en órdenes a policía judicial:` | Primero el programa con el 6; después, las órdenes con el 3. Los actos con control previo van aparte, para el juez |
| **Preparar una audiencia** | 1 | `Prepara la ficha del caso con estos documentos:` · `Arma la cronología de este expediente:` | Llevar la ficha y la cronología a la audiencia |
| Hay que **citar a alguien** (también de forma virtual) | 3 | `Necesito una citación. Pregúntame los datos que falten.` | Revisar con el 5, enviar, crear el evento en el calendario y pegar la fila en la matriz |
| Hay que **pedir información** a una entidad o sobre un vehículo | 3 | `Necesito una solicitud de información a una entidad. Pregúntame los datos que falten.` · `Prepara las solicitudes sobre este vehículo (RUNT, tránsito o patios):` | Si avisa que puede requerir autorización del juez, consultarlo con el fiscal |
| **Escribir o corregir** un correo, una respuesta o un oficio | 2 | `Mejora este texto:` · `Corrige solo ortografía y puntuación de este texto:` · `Redacta el correo para remitir este documento:` | Si pide un ajuste, el agente cambia solo eso |
| Un **usuario pregunta** y hay que explicarle | 2 | `Explica este texto en lenguaje claro para un usuario:` | Si puede revelar información reservada, confirmar con el fiscal |
| **Voy a enviar** algo a un juzgado, una entidad, policía judicial o una víctima | 5 | `Revisa este correo y sus adjuntos antes de enviarlos:` | 🔴 no enviar todavía · 🟡 revisar · 🟢 listo |
| **¿Qué tengo pendiente?** (lunes y jueves) | 4 | `Hoy es [DD/MM/AAAA]. Haz el barrido de correo de los últimos 15 días.` | Pegar las filas nuevas desde la columna B de la matriz; en las que ya existen, cambiar a mano solo lo que cambió |
| **Informe semanal** para el fiscal (viernes) | 4 | `Hoy es [DD/MM/AAAA]. Prepara el informe semanal de pendientes para el fiscal.` | Adjuntar la matriz |

## El recorrido de una solicitud

1. **Preparar** (agente 3): el documento, el correo, el evento para el calendario y la fila para la matriz.
2. **Revisar** (agente 5): nada sale en 🔴.
3. **Enviar y registrar:** se pega la fila en la matriz → **Pendiente**.
4. **Llega la respuesta** (agente 1): si es solo una constancia queda **Radicada**; si es de fondo, **Respondida**.
5. **Si no responden** (agente 4): reiterar → **Reiterada**. Después de 2 reiteraciones, escalar al fiscal.
6. **Incorporar:** guardar los anexos, informar al fiscal → **Cerrada**.

> **Una constancia de radicación no es una respuesta.** Si la entidad solo dijo "será atendida dentro de
> los términos", el estado es Radicada y el plazo sigue contando. Las audiencias y diligencias con fecha
> pasan a **Programada** y van al calendario.

## Un día de trabajo

| Momento | Qué hacer |
|---|---|
| **Al llegar** (15 min) | Revisar el calendario del día. Primera ronda de correo: cada respuesta que llegó va al agente 1, y luego se actualiza la matriz |
| **Mañana** (bloque de producción) | Citaciones, solicitudes y órdenes con el agente 3; revisión con el agente 5; enviar; fila en la matriz y evento en el calendario |
| **Mediodía** | Segunda ronda de correo. Respuestas cortas con el agente 2 |
| **Tarde** | Expedientes y análisis con los agentes 1 y 6; estudio de la unidad |
| **Antes de salir** (10 min) | Tercera ronda de correo, matriz al día y lista de tareas para mañana |

## Cada semana

- **Lunes y jueves (15 min):** barrido de correo con el agente 4 (o con el
  [prompt de barrido](prompts/02-copilot-barrido-pendientes.md)), pegar las filas en la matriz y atender
  las alertas:
  - **ESCALAR:** ya se reiteró 2 veces; informar al fiscal.
  - **VENCIDA:** pasó la fecha esperada; reiterar.
  - **REITERAR:** 15 días o más sin respuesta de fondo.
  - **POR VENCER:** vence en los próximos 7 días.
  - **INCORPORAR:** llegó la respuesta; guardar e informar.
- **Viernes (10 min):** informe de pendientes para el fiscal con el agente 4.

## Reglas que no cambian

- **Nada sale con `[COMPLETAR]` o `[FIRMA]`.** Los agentes marcan lo que falta en lugar de inventarlo.
- **Todo envío importante pasa por el Revisor** (agente 5).
- **Cada diligencia va al calendario; cada solicitud, a la matriz.**
- **Los análisis jurídicos son borradores:** las decisiones son del fiscal.
- **Pedir un ajuste a la vez:** el agente cambia solo lo que se le pide.
- **Los datos de los casos no salen de la entidad:** solo en Copilot institucional y en el OneDrive de la
  entidad.
