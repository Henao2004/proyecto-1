---
name: lectura-de-respuestas
description: "Invocar cuando llegue la respuesta de una entidad, un juzgado, policía judicial o un perito a una solicitud del despacho, para identificar a qué solicitud responde, distinguir una constancia de radicación de una respuesta de fondo o de una programación, verificar si está completa, inventariar los anexos, extraer los datos útiles según el tipo de remitente (RUNT, tránsito, patios, Registraduría, seguridad social, bancos, operadores, juzgados, informes de policía judicial y experticias) y sugerir el siguiente paso."
---

# Lectura de respuestas recibidas

Una respuesta no se da por recibida porque llegó un correo. Hay que saber **qué** responde, **si está
completa** y **qué aporta**.

## 1. ¿A qué solicitud responde?

Busca, en este orden:
1. Número de oficio, orden o radicado citado en la respuesta.
2. Número de noticia criminal.
3. Asunto del hilo ("RE:", "RV:") y remitente.
4. Fecha de la solicitud que menciona la respuesta.

Si no puedes identificarla con seguridad, dilo: "Solicitud de origen: por verificar".

## 2. Clasificación

| Clasificación | Señales | Estado en la matriz |
|---|---|---|
| **Constancia** | "Acuso recibo", "radicado No.", "será atendida dentro de los términos", respuesta automática o de mesa de ayuda | Radicada |
| **Respuesta de fondo** | Entrega la información o los documentos pedidos | Respondida |
| **Programación** | Fija fecha, hora y sala o enlace de una audiencia o diligencia | Programada |
| **Respuesta negativa** | "No reposa información", "no es de nuestra competencia", "no es posible atender" | Respondida, con alerta y siguiente paso |
| **Traslado** | "Se remitió por competencia a…" | Radicada, anotando la nueva entidad en observaciones |

## 3. ¿Está completa?

- Si tienes la solicitud original o la lista de lo pedido, compara punto por punto con una tabla:
  `Lo pedido | ¿Llegó? (Sí / Parcial / No) | Dónde está (anexo o página)`.
- Si no la tienes, pregunta qué se pidió o escribe "Completitud: por verificar".
- **No asumas que un anexo contiene lo que dice el correo:** revisa el anexo. Si no puedes abrirlo o
  está ilegible, dilo.

## 4. Qué extraer según el remitente

| Remitente | Datos útiles que suele aportar |
|---|---|
| **RUNT** | Propietarios actuales y anteriores, fechas de traspaso, organismo de tránsito donde está matriculado, limitaciones a la propiedad (prenda, embargo), estado del registro, vigencia de SOAT y revisión técnico-mecánica |
| **Organismo de tránsito** | Trámites con fechas, documentos soporte de traspasos (quién firmó y ante quién), comparendos (fecha, lugar, conductor si consta), fotodetecciones (fecha, hora, lugar e imagen) |
| **Patios** | Fecha y causa de ingreso, autoridad que lo dejó, a disposición de quién está, inventario y estado del vehículo |
| **Registraduría o notarías** | Datos de identificación y filiación, estado de la cédula, fechas de nacimiento, matrimonio o defunción |
| **Seguridad social** | Afiliación, empleador, dirección y teléfono reportados (útiles para ubicar a una persona y verificar su arraigo) |
| **Bancos** | Titular, movimientos relevantes (fecha, valor, origen y destino), registros de acceso |
| **Operadores** | Titular de la línea, fecha de activación, IMEI |
| **Juzgados y centros de servicios** | Fecha, hora, sala o enlace de la audiencia, o el estado de la solicitud |
| **Informe de policía judicial** | Por cada actividad ordenada: cumplida, parcial o no realizada (y por qué); EMP y EF recaudados con cadena de custodia; personas identificadas; hallazgos clave; recomendaciones del investigador |
| **Experticia o peritaje** | Objeto del estudio, conclusión textual (cítala entre comillas) y limitaciones que señale el perito |

Cita la página o el fragmento de cada dato útil. **No interpretes jurídicamente los hallazgos:** di qué
aportan, no qué prueban.

**Señales de alerta que vale la pena destacar:**
- Una persona que no aparecía antes en el caso (nuevo propietario, nuevo titular).
- Fechas que no cuadran con los hechos denunciados.
- Diferencias entre el documento recibido y lo que dice el expediente (nombres, números, placas).
- Información que parece reservada y llegó sin que conste la autorización.

## 5. Anexos

Tabla: `Anexo | Qué contiene | Páginas | Nombre sugerido para guardarlo`.

Formato del nombre sugerido: `AAAA-MM-DD_Tipo_NC-[últimos 4 dígitos]_Remitente.pdf`. Por ejemplo:
`2026-11-03_Respuesta-RUNT_NC-1234_RUNT.pdf`. Nunca pongas nombres de personas en el nombre del archivo.

## 6. Siguiente paso sugerido

Elige uno o varios y explica por qué:
- **Incorporar:** guardar los anexos en la carpeta del caso.
- **Informar al fiscal:** si el dato es relevante para una decisión.
- **Solicitar complemento:** si la respuesta está incompleta.
- **Redirigir:** si la entidad no tenía la información o no era competente.
- **Nueva actuación derivada:** por ejemplo, un nuevo propietario lleva a una entrevista o citación,
  y un vehículo en patios lleva a una experticia (se preparan con el agente 3).
- **Agendar:** si fija una audiencia o diligencia, registrarla en el calendario de Outlook.
- **Cerrar:** si la respuesta resuelve completamente la solicitud y ya se incorporó.

## 7. Resumen para el fiscal (máximo 4 líneas, ficticio)

> Doctor(a), llegó la respuesta del RUNT a nuestra solicitud del [fecha] (NC [número]). Reporta
> [n] propietarios; el último traspaso fue el [fecha]. Está completa. Sugiero [siguiente paso].

## Errores frecuentes

- Confundir una constancia de radicación con una respuesta.
- Dar por completa una respuesta sin revisar los anexos.
- Omitir lo que falta.
- Copiar en el resumen datos personales que no se necesitan.
- Interpretar jurídicamente un hallazgo en lugar de describirlo.
