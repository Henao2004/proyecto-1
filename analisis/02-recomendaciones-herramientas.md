# Recomendaciones de herramientas, programas e inteligencia artificial

Para la asistente de fiscal, que ya cuenta con Office (Word, Excel, PowerPoint, Outlook) y Microsoft 365
Copilot con agentes. Basado en el diagnóstico de octubre de 2026.

## Tres criterios

1. **Primero lo que ya tiene.** Microsoft 365 trae muchas funciones que casi nadie usa. Ya están
   pagadas, autorizadas por la entidad y protegidas por su seguridad.
2. **Lo que requiere instalación pasa por TI.** En un computador institucional no se instalan programas
   por cuenta propia.
3. **Información de casos, solo en Copilot institucional.** Las IA externas (ChatGPT, Claude, Gemini y
   otras) solo sirven para contenido público o general, y solo si la política de la Fiscalía lo permite.

---

## 1. Las 10 que más tiempo le ahorrarían (ya las tiene)

| # | Problema del diagnóstico | Herramienta y función | Qué le resuelve |
|---|---|---|---|
| 1 | Escribe muchos correos casi iguales | **Outlook: Mis plantillas** (o Elementos rápidos en Outlook clásico) | Inserta con un clic el correo de remisión, la citación o la reiteración |
| 2 | Frases que escribe todo el tiempo | **Autocorrección de Word y Outlook** | Escribe un atajo, por ejemplo `nnc`, y aparece "noticia criminal". Sirve para fórmulas de saludo, cierres y nombres de entidades |
| 3 | Copiar y pegar los mismos datos varias veces | **Historial del portapapeles de Windows** (Windows + V) | Guarda lo último que copió (números, frases, correos) y lo pega cuando lo necesite |
| 4 | Solicitudes que se olvidan | **Marcar correos con seguimiento**, que aparecen solos en **Microsoft To Do** | Toda solicitud enviada queda como tarea con fecha de recordatorio |
| 5 | Correos que llegan mezclados | **Reglas de Outlook** | Los correos de juzgados, entidades y policía judicial van solos a su carpeta |
| 6 | Errores después de enviar | **Deshacer envío** (o una regla que retrase el envío 1 o 2 minutos en Outlook clásico) | Le da unos segundos para atajar un adjunto o un destinatario equivocado |
| 7 | Citar a varias personas | **Combinar correspondencia** (Word + Excel) | Genera todas las citaciones de una vez a partir de una lista |
| 8 | Diligencias fuera del calendario | **Calendario de Outlook con recordatorios** | Cada entrevista o audiencia con aviso un día antes y 30 minutos antes. Además, Copilot podrá ver su agenda |
| 9 | Expedientes largos en PDF | **Abrir el PDF en Word** para copiar o editar; **anotar el PDF en Edge** (resaltar, notas) | Trabaja el expediente sin imprimirlo ni volver a escribirlo |
| 10 | Estudio de la nueva unidad | **OneNote**, con un cuaderno "Unidad" y una sección por delito | Tiene en un solo lugar los conceptos, criterios y modelos, y puede buscar en ellos |

**Bonus: dictado por voz.** Con Windows + H, o con el botón **Dictar** de Word, habla y el texto se
escribe solo. Sirve para borradores largos. No lo use para grabar entrevistas: eso tiene reglas propias.

## 2. Otras aplicaciones de Microsoft 365 que vale la pena revisar

| Aplicación | Para qué le sirve | Cuándo |
|---|---|---|
| **Copilot dentro de Word, Excel y Outlook** | Resumir un hilo largo de correos, preguntarle a un documento, crear fórmulas en la matriz | Si ve el botón de Copilot dentro de esas aplicaciones |
| **Teams** | Chat rápido con el fiscal para aprobaciones y firmas, sin correos de ida y vuelta | Desde ya |
| **OneDrive o SharePoint** | Una carpeta por noticia criminal, con nombres de archivo estándar | Desde ya |
| **Microsoft Lists** | Una versión compartida de la matriz de pendientes, con avisos automáticos | Si el fiscal o un compañero también la necesitan |
| **Planner** | Tareas del despacho repartidas entre el fiscal y la asistente | Si el despacho tiene varias personas |
| **Power Automate** | Automatizar: correo marcado → fila en la matriz; resumen diario de vencidos | Fase 3, con TI |
| **PowerPoint** | Poco útil para su trabajo diario. Sirve si el fiscal pide apoyo visual para un juicio (línea de tiempo, mapa de los hechos) | Ocasional |

## 3. Programas que requieren TI (pedirlos, no instalarlos)

| Programa | Para qué | Por qué pedirlo |
|---|---|---|
| **Adobe Acrobat Pro** (o el lector de PDF que tenga la entidad) | Hacer buscable un PDF escaneado (OCR), unir y dividir PDF, numerar páginas | Muchos expedientes llegan escaneados y no se puede buscar en ellos |
| **Microsoft PowerToys** | Copiar texto de una imagen o de un PDF escaneado (Text Extractor), entre otras utilidades | Es gratuito y de Microsoft, pero necesita instalación |

## 4. Inteligencia artificial: cuál usar para qué

| Herramienta | ¿Con información de casos? | Para qué sí |
|---|---|---|
| **Microsoft 365 Copilot y sus 6 agentes** | **Sí**, si la Fiscalía lo autoriza: es la herramienta institucional | Todo el trabajo diario |
| **ChatGPT, Claude, Gemini** (personales) | **No, nunca** | Solo dudas generales de redacción o conceptos, sin datos de casos y si la política lo permite |
| **NotebookLM** (Google) | **No** | Estudiar a partir de documentos **públicos** (leyes, sentencias publicadas): les hace preguntas y le devuelve las citas |
| **Perplexity** u otros buscadores con IA | **No** | Encontrar normas o jurisprudencia, **siempre verificando** en la Secretaría del Senado o en las relatorías |

> La regla práctica: **si el texto tiene un nombre, un número de caso o un hecho de una
> investigación, va a Copilot institucional o a ninguna parte.**

## 5. Lo que no recomiendo

- Instalar programas o extensiones del navegador por su cuenta, sobre todo extensiones de IA que leen
  las páginas abiertas.
- Usar WhatsApp personal o el correo personal para información de casos.
- Usar aplicaciones externas para grabar o transcribir entrevistas.
- Probar muchas herramientas a la vez: es mejor adoptar 2 o 3 por semana.

## 6. Orden sugerido

| Semana | Qué configurar |
|---|---|
| 1 | Mis plantillas de Outlook, autocorrección y Windows + V |
| 2 | Seguimiento y To Do, reglas de correo y deshacer envío |
| 3 | Calendario con recordatorios, carpetas por caso en OneDrive y OneNote para el estudio |
| 4 | Combinar correspondencia y, con TI, la solicitud de Acrobat Pro o PowerToys |

Para confirmar qué tiene disponible en su licencia, use el
[prompt 03](../prompts/03-copilot-herramientas-productividad.md) en Copilot.
