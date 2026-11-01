---
name: barrido-de-correo
description: "Invocar cuando el usuario pida un barrido de correo, revisar el correo en busca de pendientes o conciliar la matriz de seguimiento con Outlook. Explica cómo buscar en un periodo los correos enviados que piden algo (solicitudes, órdenes, citaciones, solicitudes y seguimientos de audiencia, reiteraciones) y las respuestas recibidas, cómo emparejar cada respuesta con su solicitud, qué excluir y cómo informar los límites de la búsqueda."
---

# Barrido de correo

Objetivo: que ninguna solicitud enviada quede sin control y que cada respuesta recibida quede
registrada en la matriz.

## Paso 1. Definir el periodo

- Por defecto, **los últimos 15 días**. El usuario puede pedir otro periodo.
- Para las respuestas, busca desde el inicio del periodo hasta hoy.

## Paso 2. Buscar los correos enviados que piden algo

Busca en **Elementos enviados** correos que contengan expresiones como:

| Tipo | Expresiones frecuentes |
|---|---|
| Solicitud a entidad | "solicito", "solicitud de información", "requiero", "oficio No.", "agradezco remitir" |
| Orden a policía judicial | "orden a policía judicial", "OPJ", "remito orden", "programa metodológico" |
| Solicitud de audiencia | "solicitud de audiencia", "programación de audiencia", "fijar fecha" |
| Citación | "citación", "se le cita", "entrevista", "declaración jurada", "confirmar asistencia" |
| Reiteración | "reitero", "reiteración", "sin respuesta a la fecha" |

Para cada solicitud registra: fecha de envío, destinatario (entidad o rol), número de noticia criminal,
asunto, número de oficio u orden (si aparece) y qué se pidió, en pocas palabras.

## Paso 3. Buscar las respuestas recibidas

Busca en la **Bandeja de entrada** y sus subcarpetas:
- Correos con "RE:", "RV:" o "Respuesta" y el asunto de la solicitud.
- Correos del mismo destinatario (mismo dominio de correo) posteriores al envío.
- Correos que mencionen el número de noticia criminal, el número de oficio o un número de radicado
  dado por la entidad.
- Expresiones como "en atención a", "damos respuesta", "acuso recibo", "radicado", "se programa",
  "remito informe".

## Paso 4. Emparejar respuesta y solicitud

Orden de prioridad para decidir que una respuesta corresponde a una solicitud:
1. Mismo número de oficio, orden o radicado.
2. Mismo número de noticia criminal **y** mismo remitente o entidad.
3. Respuesta directa al hilo ("RE:" del mismo asunto).
4. Mismo remitente y fecha cercana, **solo si no hay otra solicitud abierta a esa entidad**.

Si el emparejamiento es dudoso, **no lo hagas**: repórtalo en Alertas como "Respuesta sin emparejar" o
"Solicitud con posible respuesta: verificar".

## Paso 5. Clasificar

Usa la habilidad `seguimiento-por-etapas` para asignar el estado: Pendiente, Radicada, Reiterada,
Respondida, Programada o Cerrada.

## Qué excluir

- Hilos repetidos: una cadena de "RE:" sobre la misma solicitud cuenta como **una** solicitud.
- Correos internos que no piden nada a un tercero (salvo que el usuario los pida).
- Boletines, notificaciones del sistema y publicidad.
- Correos administrativos personales (permisos, nómina, etc.).

## Conciliar con la matriz

Si además te dan la matriz:
- **Filas nuevas:** solicitudes encontradas en el correo que no están en la matriz.
- **Filas actualizadas:** filas de la matriz cuyo estado cambió según el correo (por ejemplo, de
  Pendiente a Radicada o a Respondida). Indica el id.
- **Sin rastro:** filas abiertas de la matriz de las que no encontraste ningún correo. Pueden haberse
  enviado por otro medio: repórtalas, pero no cambies su estado.

## Informar los límites

Al final, siempre:
- Cuántos correos enviados y recibidos revisaste y en qué fechas.
- Si la búsqueda pudo no traer todos los resultados (por ejemplo, si devolvió pocos correos para el
  periodo), dilo y sugiere verificar en Outlook.
- Nunca afirmes que "no hay más pendientes": solo que no encontraste otros.

## Privacidad

Dentro de Copilot institucional puedes usar los números de noticia criminal. Si el usuario dice que el
resultado se compartirá fuera de la entidad, omite números de caso y nombres de personas.
