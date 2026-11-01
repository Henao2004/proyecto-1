# Guía diaria de los agentes

Seis ayudantes en Copilot, cada uno para una tarea. Aquí está para qué sirve cada uno, cómo funciona,
qué hace y en qué momento usarlo.

**Cómo usar cualquier agente:** copie la frase para empezar, péguela en el agente y agregue después el
documento o los datos. Cambie lo que va entre corchetes.

## ¿Qué está haciendo?

| Si… | Use |
|---|---|
| Llegó algo | **1** · Lector de documentos y respuestas |
| Voy a escribir | **2** · Redactor del despacho |
| Voy a citar o a pedir algo | **3** · Citaciones y solicitudes |
| Voy a enviar | **5** · Revisor antes de enviar |
| ¿Qué tengo pendiente? | **4** · Control de pendientes |
| Analizar un caso | **6** · ANALISIS NOTICIA CRIMINAL |

---

## 1 · Lector de documentos y respuestas

**Para qué sirve:** leer por usted lo que llega al despacho y decirle qué es, qué trae y qué hacer con
eso. Le ahorra leer documentos largos completos y buscar datos a mano.

**Cómo funciona**
1. Usted pega el texto o adjunta el documento: una respuesta, una denuncia, un informe o un expediente en PDF.
2. El agente lo lee, identifica qué tipo de documento es y saca lo importante, indicando la página o el fragmento de donde lo tomó.
3. Le devuelve una ficha con lo esencial y el siguiente paso. Si es una respuesta, le dice si está completa y qué cambiar en la matriz.

**Qué hace**
- Dice a qué solicitud responde una respuesta y si es solo una constancia o la respuesta de fondo.
- Revisa si llegó todo lo pedido, qué anexos trae y cómo nombrarlos.
- Hace la ficha de una denuncia o un informe: datos, fechas, tareas y alertas.
- Busca un dato en un expediente largo y le dice en qué página está.
- Arma la cronología y la ficha del caso para una audiencia.
- Prepara un resumen de 4 líneas para el fiscal.

**Cuándo usarlo**
- Al llegar, con las respuestas que entraron al correo.
- Cuando llega una denuncia, un informe de policía judicial o un documento nuevo.
- Cuando necesita una dirección, una fecha o una placa de un expediente largo.
- Antes de una audiencia.

**Qué no hace:** no interpreta jurídicamente los hallazgos ni inventa datos que no estén en el documento.

> **Ejemplo:** llega un correo del RUNT con un PDF. Usted lo pega con "Llegó esta respuesta. Analízala:".
> El agente le dice que es la respuesta de fondo a la solicitud del 15 de octubre, que reporta dos
> propietarios, que está completa, cómo nombrar el PDF y que cambie el estado a "Respondida".

**Frases para empezar:** `Llegó esta respuesta. Analízala:` · `Haz la ficha de este documento:` ·
`En este expediente, busca:` · `Arma la cronología de este expediente:`

---

## 2 · Redactor del despacho

**Para qué sirve:** escribir y corregir textos con su estilo (breve, formal y natural) desde el primer
intento, sin tener que pedir cambios una y otra vez.

**Cómo funciona**
1. Usted pega su texto o sus ideas y dice qué quiere: corregir, mejorar, acortar, responder o remitir.
2. El agente aplica sus preferencias de estilo y el tono que corresponde a quien va dirigido (juzgado, entidad, usuario).
3. Le devuelve primero el texto listo para copiar. Abajo, solo si cambió algo de fondo, una nota corta.

**Qué hace**
- Corrige ortografía y puntuación sin cambiar su estilo.
- Mejora o acorta textos y quita las frases de relleno.
- Redacta el correo para enviar un oficio, una orden o una citación.
- Responde correos con las ideas que usted le dé.
- Explica textos técnicos en lenguaje claro para un usuario.
- Marca con `[COMPLETAR]` lo que falta en lugar de inventarlo.

**Cuándo usarlo**
- Cada vez que vaya a escribir un correo, una respuesta o un oficio.
- Cuando un texto le quedó largo o muy rígido.
- Cuando tiene que responderle a un usuario o a una víctima.
- Cuando necesita el correo que acompaña un documento.

**Qué no hace:** no decide qué se responde ni agrega datos. Tampoco revisa si el número de caso es el
correcto: eso lo hace el agente 5.

> **Ejemplo:** usted escribe "Mejora este texto:" y pega un párrafo largo para un juzgado. El agente le
> devuelve un correo de cuatro líneas, con asunto y cierre "Respetuosamente". Si le dice "más breve",
> cambia solo eso.

**Frases para empezar:** `Mejora este texto:` · `Corrige solo ortografía y puntuación de este texto:` ·
`Redacta el correo para remitir este documento:` · `Explica este texto en lenguaje claro para un usuario:`

---

## 3 · Citaciones y solicitudes

**Para qué sirve:** preparar todo lo que el despacho envía para citar a una persona o pedir
información, con el documento y el correo de envío coherentes entre sí.

**Cómo funciona**
1. Usted le dice qué necesita (una citación, una solicitud o una orden) y le da los datos, o adjunta el expediente.
2. Si falta un dato obligatorio, por ejemplo la hora, el agente se lo pregunta. Todo de una vez, nunca lo inventa.
3. Le devuelve el documento, el correo para enviarlo, el evento para el calendario, la fila para la matriz y una verificación final.

**Qué hace**
- Citaciones a entrevistas, declaraciones juradas (también virtuales) e interrogatorios.
- Solicitudes de información a tránsito, RUNT, patios, Registraduría, seguridad social, bancos y juzgados.
- Órdenes a policía judicial, incluidas las experticias técnicas de vehículos.
- Convierte el programa metodológico del agente 6 en órdenes listas para firma.
- Seguimiento de audiencias sin programar y reiteraciones formales.
- Avisa si lo que se pide puede requerir autorización del juez.

**Cuándo usarlo**
- En el bloque de la mañana, cuando prepara lo que va a enviar.
- Cuando hay que citar a alguien o reprogramar una cita.
- Cuando hay que pedir información a una entidad o sobre un vehículo.
- Cuando el fiscal aprueba un programa metodológico y hay que hacer las órdenes.

**Qué no hace:** no decide qué se pide ni a quién (eso lo decide el despacho) y no inventa números de
oficio.

> **Ejemplo:** usted escribe "Prepara las solicitudes sobre este vehículo (RUNT, tránsito o patios):" y
> la placa. El agente propone las tres solicitudes, le pregunta cuáles hacer y le entrega cada una con su
> correo y su fila para la matriz.

**Frases para empezar:** `Necesito una citación. Pregúntame los datos que falten.` ·
`Necesito una solicitud de información a una entidad. Pregúntame los datos que falten.` ·
`Prepara las solicitudes sobre este vehículo (RUNT, tránsito o patios):` ·
`Convierte este programa metodológico en órdenes a policía judicial:`

---

## 4 · Control de pendientes

**Para qué sirve:** saber en todo momento qué solicitudes siguen sin respuesta, cuáles hay que reiterar
y qué respuestas falta incorporar, para que nada se olvide.

**Cómo funciona**
1. Usted le pide el barrido del correo, o le adjunta la matriz de pendientes, y le da la fecha de hoy.
2. El agente busca lo que se envió y lo que llegó, y pone cada solicitud en su etapa: Pendiente, Radicada, Respondida…
3. Le devuelve la lista ordenada por urgencia, los correos de reiteración que hagan falta y las filas para actualizar la matriz.

**Qué hace**
- Revisa el correo de los últimos días y empareja solicitudes con respuestas.
- Distingue una constancia de radicación de una respuesta de fondo.
- Ordena los pendientes por urgencia: escalar, vencido, reiterar, por vencer.
- Redacta las reiteraciones y sugiere escalar al fiscal después de dos.
- Avisa de las diligencias próximas que hay que confirmar.
- Prepara el informe semanal para el fiscal.

**Cuándo usarlo**
- Los lunes y jueves, 15 minutos, para revisar los pendientes.
- Los viernes, para el informe al fiscal.
- Cuando quiere saber en qué va una solicitud.

**Qué no hace:** no da por respondido algo que no consta en el correo ni en la matriz, y no envía
correos por usted.

> **Ejemplo:** el lunes escribe "Hoy es 03/11/2026. Haz el barrido de correo de los últimos 15 días." El
> agente encuentra 12 solicitudes: 2 vencidas, 1 para escalar al fiscal y 3 respuestas por incorporar, y
> le entrega los borradores de reiteración.

**Frases para empezar:** `Hoy es [DD/MM/AAAA]. Haz el barrido de correo de los últimos 15 días.` ·
`Registra esta respuesta recibida:` ·
`Hoy es [DD/MM/AAAA]. Prepara el informe semanal de pendientes para el fiscal.`

---

## 5 · Revisor antes de enviar

**Para qué sirve:** revisar en segundos que un correo y sus adjuntos no salgan con errores antes de
enviarlos.

**Cómo funciona**
1. Usted copia del borrador de Outlook las líneas Para, CC y Asunto, más el cuerpo, y adjunta los documentos.
2. El agente compara los datos de cada pieza: número de caso, nombres, fechas, horas y anexos.
3. Le devuelve un semáforo (🔴 no enviar todavía · 🟡 revisar · 🟢 listo) y la lista de lo que hay que corregir.

**Qué hace**
- Detecta números o nombres que no coinciden entre el correo y el documento.
- Encuentra datos que quedaron de otro caso.
- Avisa si falta un anexo o si el adjunto es una versión equivocada.
- Revisa las fechas y los formatos del número de caso y de las placas.
- Señala datos personales enviados a quien no los necesita.
- Detecta `[FIRMA]` o notas de Copilot pegadas por error.

**Cuándo usarlo**
- Antes de enviar cualquier cosa a un juzgado, una entidad, policía judicial o una víctima.
- Siempre que haya reutilizado un documento de otro caso.
- Cuando envía varios documentos a la vez.

**Qué no hace:** no cambia el estilo ni opina sobre el fondo. Si le pide "corrígelo", cambia solo lo
que señaló.

> **Ejemplo:** una citación dice "lunes 15" en el correo y "martes 16" en el documento. El agente marca 🔴
> y le muestra las dos fechas para que escoja la correcta.

**Frases para empezar:** `Revisa este correo y sus adjuntos antes de enviarlos:` ·
`Revisa si este correo expone datos personales o reservados:`

---

## 6 · ANALISIS NOTICIA CRIMINAL

**Para qué sirve:** ayudar a analizar jurídicamente un caso de patrimonio económico o fe pública, como
borrador para el fiscal.

**Cómo funciona**
1. Usted pega o adjunta la noticia criminal, la denuncia o el informe policial.
2. El agente separa lo comprobado de lo que solo afirma el denunciante, y revisa los delitos posibles y los aspectos procesales.
3. Le devuelve un borrador en cinco partes, con lo que falta por investigar y las normas que hay que verificar.

**Qué hace**
- Identifica los hechos importantes y los vacíos de información.
- Propone los delitos posibles y revisa si se cumplen sus elementos.
- Revisa querella, conciliación, procedimiento y salidas posibles.
- Propone los actos de investigación urgentes y el programa metodológico.
- Advierte cuando el asunto parece civil y no penal.

**Cuándo usarlo**
- Cuando el fiscal le pide el análisis de una noticia criminal.
- Cuando hay que proponer los actos de investigación de un caso nuevo.
- Antes de hacer las órdenes con el agente 3.

**Qué no hace:** no decide ni cita sentencias que no haya verificado. **Es solo un borrador: el fiscal lo
revisa y decide.**

> **Ejemplo:** una denuncia por la venta de un carro que nunca se entregó. El agente plantea la estafa
> como hipótesis, advierte que podría ser un incumplimiento civil y lista qué pruebas faltan para
> distinguir una cosa de la otra.

**Frases para empezar:**
`Analiza esta noticia criminal y elabora el diagnóstico preliminar en los cinco bloques.` ·
`A partir de este informe policial, propone los actos urgentes y el programa metodológico inicial, con la finalidad y la prioridad de cada acto.`

---

## En qué momento usar cada uno

| Momento | Situación | Agente |
|---|---|---|
| Al llegar | Revisar las respuestas que entraron al correo | 1 Lector |
| En la mañana | Preparar citaciones, solicitudes y órdenes, y revisarlas antes de enviar | 3 Citaciones → 5 Revisor |
| Durante el día | Escribir o responder correos; buscar un dato en un expediente | 2 Redactor · 1 Lector |
| Cuando el fiscal lo pida | Analizar un caso y después hacer las órdenes | 6 Análisis → 3 Citaciones |
| Antes de una audiencia | Ficha del caso y cronología | 1 Lector |
| Lunes y jueves | Revisar los pendientes y reiterar lo vencido | 4 Pendientes |
| Viernes | Informe de pendientes para el fiscal | 4 Pendientes |

## Cuatro reglas

- Si ve `[COMPLETAR]` o `[FIRMA]`, complételo antes de enviar.
- Cada solicitud va a la matriz y cada diligencia, al calendario.
- El agente 6 hace borradores: decide el fiscal.
- **Los datos de los casos no salen de la entidad.**
