---
name: seguimiento-por-etapas
description: "Invocar para clasificar en qué etapa está cada solicitud, orden, solicitud de audiencia o citación del despacho (Pendiente, Radicada, Reiterada, Respondida, Programada o Cerrada), reconocer si un correo recibido es una constancia de radicación o una respuesta de fondo, detectar respuestas incompletas, decidir cuándo reiterar o escalar, incorporar respuestas y preparar el informe semanal de pendientes para el fiscal. Incluye modelos de reiteración, escalamiento, solicitud de complemento e informe."
---

# Seguimiento de pendientes por etapas

Una solicitud no está resuelta porque alguien contestó. Está resuelta cuando llegó la **respuesta de
fondo**, se **incorporó** y el fiscal **la conoce**.

## Ciclo de cada tipo

| Tipo | Ciclo normal | Desvíos |
|---|---|---|
| Solicitud a entidad | Pendiente → Radicada → Respondida → Cerrada | Reiterada (sin respuesta de fondo); Respondida con respuesta incompleta |
| Orden a policía judicial | Pendiente → Respondida (llegó el informe) → Cerrada | Reiterada si vence el término del informe |
| Solicitud de audiencia | Pendiente → Radicada → Programada (con fecha) → Cerrada (realizada) | Reiterada si no la programan; nueva fecha si la aplazan |
| Citación | Pendiente → Programada (confirmó) → Cerrada (asistió) | No confirmó: reiterar. No asistió: volver a Pendiente y anotarlo en observaciones |

## Cómo reconocer cada etapa en un correo

| Etapa | Señales típicas en el correo recibido |
|---|---|
| **Radicada** (no es respuesta) | "Acuso recibo", "su solicitud fue radicada con el número…", "será atendida dentro de los términos legales", "hemos recibido su requerimiento", respuestas automáticas, correos de mesa de ayuda con número de caso |
| **Respondida** | "En atención a su solicitud… remitimos", "damos respuesta al oficio…", adjuntos con la información pedida (certificados, historiales, extractos, videos, registros) |
| **Programada** | "Se fija/programa audiencia para el…", invitación con fecha y enlace, "confirmo mi asistencia el…" |
| **Sigue pendiente** (audiencias) | "Se informará oportunamente la fecha", "en espera de agenda", "se encuentra en reparto" |
| **Informe de policía judicial** | Informe de investigador adjunto o remisión de resultados de la orden |

Si una respuesta mezcla señales (por ejemplo, una constancia con un adjunto parcial), clasifícala por lo
que efectivamente entrega y explícalo en observaciones.

## Respuestas incompletas

Compara lo que se pidió (en la solicitud original) con lo que llegó:
- Si falta algo, el estado es **Respondida**, pero en Alertas escribe "Respuesta incompleta: falta
  [X]" y sugiere la acción **solicitar complemento**.
- Si la entidad dice que no tiene la información o que no es competente, anótalo en observaciones y
  sugiere al despacho evaluar a qué otra entidad dirigirse.

## Cuándo reiterar y cuándo escalar

- **Reiterar:** la solicitud está vencida, o no tiene fecha esperada y lleva 15 días o más (contados
  desde el envío o desde la última reiteración) sin respuesta de fondo. **Una constancia de radicación
  no detiene el reloj.**
- **Escalar:** ya se reiteró 2 o más veces. Opciones para proponer al despacho:
  1. Informar al fiscal con un resumen, para que decida.
  2. Usar otro canal: llamada, correo de requerimientos judiciales de la entidad o radicación física.
  3. Que la reiteración vaya firmada por el fiscal, si las anteriores fueron de la asistente.
  4. En juzgados: consultar a la secretaría o al centro de servicios.
- No menciones sanciones ni consecuencias legales en las reiteraciones, salvo que el despacho lo indique.

## Incorporar una respuesta (acción "Incorporar")

1. Descargar los anexos.
2. Guardarlos en la carpeta del caso con el nombre estándar del despacho.
3. Revisar si responden todo lo pedido.
4. Informar al fiscal con un correo interno breve, si la respuesta es relevante.
5. Cambiar el estado a **Cerrada** y anotar la fecha de respuesta.

## Modelos (ficticios)

**Reiteración**
> Asunto: Reiteración – [asunto original]
>
> Cordial saludo,
>
> Reitero la solicitud enviada el [fecha] mediante [oficio/correo] [número], relacionada con
> [qué se pidió]. A la fecha no hemos recibido respuesta de fondo. Agradezco su pronta gestión.
>
> Atentamente,
> [FIRMA]

**Escalamiento al fiscal (interno)**
> Asunto: Pendiente sin respuesta – NC [número] – [entidad]
>
> Doctor(a), la solicitud a [entidad] del [fecha] sobre [tema] sigue sin respuesta de fondo después de
> [n] reiteraciones (la última, el [fecha]). Propongo [opción de escalamiento]. Quedo atenta a su
> indicación.

**Solicitud de complemento**
> Asunto: Complemento de respuesta – [asunto original]
>
> Cordial saludo,
>
> Agradezco la respuesta del [fecha] a nuestra solicitud [número]. Para completarla, solicito
> [lo que falta].
>
> Atentamente,
> [FIRMA]

## Informe semanal para el fiscal (máximo 10 líneas)

```
Pendientes al [fecha]
- Abiertas: [n] (Pendiente [n] · Radicada [n] · Reiterada [n])
- Vencidas: [n] — las más antiguas: [NC – entidad – días]
- Audiencias sin programar: [n]
- Respuestas recibidas por incorporar: [n]
- Para su decisión: [escalamientos o respuestas que requieren su revisión]
```
