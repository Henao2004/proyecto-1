---
name: verificacion-de-envios
description: "Invocar para revisar un correo y sus documentos adjuntos antes de enviarlos: coherencia de números de caso, nombres, placas, fechas y horas entre correo, documento y anexos; restos de otro caso; campos sin llenar; anexos faltantes o equivocados; destinatario correcto; formatos (número de noticia criminal, placas, fechas) y contenido mínimo según el tipo de documento (citación, solicitud a entidad, orden a policía judicial, reiteración, correo de remisión, respuesta a usuario). Define qué es grave (no enviar) y qué es menor."
---

# Verificación de envíos

El objetivo es atajar **antes de enviar** los errores que obligan a rehacer, confunden al destinatario o
exponen información. **No se corrige el estilo** (eso lo hace el Redactor): solo se señalan errores.

## 1. Cómo leer el envío

Arma primero una tabla de **datos clave por pieza** (correo, documento 1, documento 2…):
`Dato | Correo | Documento | Anexo`, con número de noticia criminal, destinatario, nombres, placas,
fechas, horas, lugar o enlace, y número de oficio u orden. Las diferencias saltan a la vista.

## 2. Revisiones generales

| Revisión | Qué buscar |
|---|---|
| **Coherencia** | El mismo número de caso, nombres, destinatario, fechas, horas, lugares, placas y valores en todas las piezas |
| **Restos de otro caso** | Datos que aparecen una sola vez o no encajan con el resto; nombres de archivos adjuntos con otro número de caso; un género o un rol que no corresponden ("la señora" cuando el resto habla de un hombre) |
| **Campos sin llenar** | `[COMPLETAR]`, `XXX`, `___`, "nombre", `00/00/0000`, textos de ejemplo de la plantilla |
| **Anexos** | Lo mencionado está adjunto; lo adjunto está mencionado; el correo dice "adjunto" pero no hay anexo |
| **Destinatario** | El correo del campo "Para" corresponde a la entidad o persona del documento (compáralo con el directorio de entidades si lo tienes) |
| **Fechas y horas** | Fechas pasadas en una citación; fin de semana o festivo; el día de la semana no coincide con la fecha; hora fuera del horario laboral; palabras relativas ("mañana", "el próximo lunes") sin fecha exacta |
| **Nombres propios** | La misma persona escrita de formas distintas |

## 3. Formatos que se pueden verificar

| Dato | Formato habitual | Si no cumple |
|---|---|---|
| Número de noticia criminal | Normalmente **21 dígitos**: departamento (2), municipio (3), entidad (2), unidad receptora (5), **año (dígitos 13 a 16)** y consecutivo (5) | Otro largo, o un año posterior al actual o incoherente con los hechos: "verificar" |
| Placa de carro | 3 letras y 3 números (ABC123) | "Verificar placa" |
| Placa de moto | 3 letras, 2 números y 1 letra (ABC12D) | "Verificar placa" |
| Fechas | Día, mes y año completos | Una fecha sin año o ambigua: "verificar" |
| Horas | Con a. m. o p. m. (o formato de 24 horas) | Una hora ambigua ("a las 8"): "verificar" |

Estos formatos son referencias. Cuando no se cumplan, marca "verificar"; no los des por error seguro.

## 4. Contenido mínimo por tipo de documento

| Tipo | Debe tener |
|---|---|
| **Citación** | Fecha, hora, lugar exacto o enlace, qué debe traer y cómo confirmar o reprogramar. Si la persona es menor de edad, se cita a través de su representante legal |
| **Solicitud a entidad** | Una sola entidad, lo que se pide en concreto, los datos para buscar (placa, documento, periodo), el plazo y el canal de respuesta |
| **Orden a policía judicial** | La finalidad de cada actividad y el término para el informe. Ninguna actividad que requiera control previo presentada como autorizada |
| **Reiteración** | La fecha y el número de la solicitud original, y qué se pidió |
| **Correo de remisión** | Asunto claro; dice qué se remite; no repite el contenido del documento |
| **Respuesta a un usuario** | Lenguaje claro; sin información reservada de la investigación; sin promesas de plazos o resultados |
| **Oficio a patios** | Placa y características del vehículo, y la indicación del despacho sobre su entrega (la decide el fiscal) |

## 5. Gravedad

**🔴 NO ENVIAR TODAVÍA** cuando el error puede causar un daño o un reproceso:
- Número de caso, nombre o placa de otro caso.
- Destinatario equivocado.
- Anexo faltante o equivocado.
- Fecha, hora o lugar incorrectos en una citación.
- Datos personales o reservados enviados a quien no debe recibirlos.
- Una actividad que requiere autorización judicial presentada como autorizada.

**🟡 REVISAR** cuando son detalles menores:
- Campo sin llenar que no es esencial.
- Formato por verificar (día de la semana, placa, número de caso).
- Asunto poco claro.
- Nombre escrito de forma distinta en dos lugares.

**🟢 LISTO PARA ENVIAR** si no encontraste problemas. **No inventes problemas** para tener algo que decir.

## 6. Si te piden "corrígelo"

Entrega el texto completo de cada pieza **cambiando solo lo señalado**. No mejores el estilo ni agregues
información. Lo que no se pueda corregir sin datos (por ejemplo, el número correcto) déjalo como
`[COMPLETAR: dato]`.
