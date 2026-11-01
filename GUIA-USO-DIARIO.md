# Guía diaria de los agentes

Seis ayudantes en Copilot, cada uno para una tarea. Elija según lo que esté haciendo, copie la frase y
pegue después el documento o los datos.

## ¿Qué está haciendo?

| Si… | Use |
|---|---|
| Llegó algo | **1** · Lector de documentos y respuestas |
| Voy a escribir | **2** · Redactor del despacho |
| Voy a citar o a pedir algo | **3** · Citaciones y solicitudes |
| Voy a enviar | **5** · Revisor antes de enviar |
| ¿Qué tengo pendiente? | **4** · Control de pendientes |
| Analizar un caso | **6** · ANALISIS NOTICIA CRIMINAL |

## Qué hace cada agente

### 1 · Lector de documentos y respuestas
Lee por usted lo que llega y le dice qué hacer con eso.
- **Úselo cuando:** llega la respuesta de una entidad, un juzgado o policía judicial; llega una denuncia o un informe; necesita un dato de un expediente largo.
- **Le entrega:** qué dice el documento, si la respuesta está completa, qué anexos trae y el siguiente paso.
- **Frases:** `Llegó esta respuesta. Analízala:` · `Haz la ficha de este documento:` · `En este expediente, busca:`

### 2 · Redactor del despacho
Escribe y corrige con su estilo: breve, formal y natural, sin inventar nada.
- **Úselo cuando:** tiene que escribir o corregir un correo, una respuesta o un oficio; necesita el correo para enviar un documento; debe explicarle algo a un usuario en palabras sencillas.
- **Le entrega:** el texto listo para copiar y enviar. Si le pide "más breve" o "más formal", cambia solo eso.
- **Frases:** `Mejora este texto:` · `Corrige solo ortografía y puntuación de este texto:` · `Redacta el correo para remitir este documento:`

### 3 · Citaciones y solicitudes
Prepara lo que el despacho envía para citar a alguien o pedir información.
- **Úselo cuando:** hay que citar a alguien (en persona o de forma virtual), pedir información a una entidad o sobre un vehículo, o hacer órdenes a policía judicial.
- **Le entrega:** el documento, el correo para enviarlo, el evento para el calendario y la fila para la matriz de pendientes.
- **Frases:** `Necesito una citación. Pregúntame los datos que falten.` · `Necesito una solicitud de información a una entidad. Pregúntame los datos que falten.` · `Prepara una orden a policía judicial con estas actividades:`

### 4 · Control de pendientes
Le dice qué falta por responder y qué hay que reiterar, para que nada se olvide.
- **Úselo:** los lunes y jueves, para revisar los pendientes; los viernes, para el informe al fiscal.
- **Le entrega:** la lista de pendientes ordenada por urgencia, los correos de reiteración y las filas para la matriz.
- **Frases:** `Hoy es [DD/MM/AAAA]. Haz el barrido de correo de los últimos 15 días.` · `Hoy es [DD/MM/AAAA]. Prepara el informe semanal de pendientes para el fiscal.`

### 5 · Revisor antes de enviar
Revisa que nada salga con errores: datos de otro caso, anexos que faltan o fechas equivocadas.
- **Úselo cuando:** va a enviar algo a un juzgado, una entidad, policía judicial o una víctima.
- **Le entrega:** un semáforo (🔴 no enviar todavía · 🟡 revisar · 🟢 listo) y qué corregir.
- **Frase:** `Revisa este correo y sus adjuntos antes de enviarlos:`

### 6 · ANALISIS NOTICIA CRIMINAL
Ayuda a analizar un caso de patrimonio económico o fe pública para el fiscal.
- **Úselo cuando:** el fiscal pide el análisis de una noticia criminal o hay que proponer los actos de investigación.
- **Le entrega:** un borrador del análisis en cinco partes y un plan de investigación. **Es solo un borrador: el fiscal lo revisa y decide.**
- **Frase:** `Analiza esta noticia criminal y elabora el diagnóstico preliminar en los cinco bloques.`

## La rutina

| Cuándo | Qué hacer |
|---|---|
| Cada día | Las respuestas que lleguen, al agente 1. Antes de enviar algo importante, al agente 5 |
| Lunes y jueves | Agente 4: revisar los pendientes y reiterar lo vencido |
| Viernes | Agente 4: informe de pendientes para el fiscal |

## Cuatro reglas

- Si ve `[COMPLETAR]` o `[FIRMA]`, complételo antes de enviar.
- Cada solicitud va a la matriz y cada diligencia, al calendario.
- El agente 6 hace borradores: decide el fiscal.
- **Los datos de los casos no salen de la entidad.**
