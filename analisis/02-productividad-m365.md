# Productividad con Microsoft 365: lo que recomendó Copilot y correcciones

**Fuente:** respuesta de Copilot a un prompt de productividad (noviembre de 2026). Aquí queda el resumen y
lo que **hay que corregir o tener en cuenta** antes de aplicarlo. Sin datos de casos.

## Lo que se sabe de su equipo

- **Tiene:** Windows, Outlook, Teams, OneDrive, OneNote, Word, Excel, PowerPoint y Copilot Chat con
  agentes.
- **No ve** el botón de Copilot dentro de Word, Excel ni Outlook.
- **No sabe** si tiene To Do, Planner, Lists, Forms, Power Automate y Loop.
- **Ojo:** el 1 de noviembre, Copilot sí encontró sus correos y archivos. Eso sugiere que su cuenta tiene
  acceso a datos de trabajo. Que no aparezca el botón en las aplicaciones puede deberse a la licencia, a
  una configuración de TI o a una versión desactualizada de Office. **Hay que preguntarle a TI**, no
  suponer que no hay licencia.

## Las 10 funciones recomendadas

Plantillas de Outlook, pasos rápidos, marcas de seguimiento, To Do, reglas, deshacer envío, PDF en Word,
anotaciones de PDF en Edge, Windows + V y dictado con Windows + H. Además: autocorrección, combinar
correspondencia y OneNote para estudiar.

**Prioridad recomendada:** plantillas de Outlook, reglas de Outlook y Windows + V.

## Correcciones y precauciones

| # | Recomendación de Copilot | Corrección o precaución |
|---|---|---|
| 1 | Cuaderno de OneNote "Patrimonio económico" con **acaparamiento** y **especulación** | Esos delitos son del **orden económico social**, no del patrimonio económico (verificar con el Código Penal). **Administración desleal** sí va en patrimonio económico |
| 2 | Windows + V para guardar radicados, nombres y cuentas | Guarda datos de casos. **Desactivar "Sincronizar entre dispositivos"** y **borrar el historial** al final del día (Windows + V → "Borrar todo") |
| 3 | Dictado por voz (Windows + H) para redactar | El dictado de Windows suele procesar el audio en los servidores de Microsoft. **Para información de casos, confirmar con TI** si está permitido |
| 4 | "Deshacer envío" en Configuración | Existe en el **Outlook nuevo** y en el web (hasta 10 segundos). En el **Outlook clásico** se logra con una regla que retrasa el envío unos minutos |
| 5 | Pasos rápidos para "crear correos prediseñados" | Depende de la versión de Outlook. En el Outlook nuevo, las **plantillas ("Mis plantillas")** cumplen mejor esa función |
| 6 | "Abrir PDF en Word" para expedientes escaneados | Funciona bien con PDF de texto. **Con PDF escaneados la conversión suele salir mal.** Además crea una copia del expediente: guardarla solo en el OneDrive institucional |
| 7 | Reglas que mueven correos con "Respuesta", "Requerimiento" o "Informe" | Las reglas por palabras pueden esconder correos importantes en carpetas. **Mejor reglas por remitente o por dominio** y revisar las carpetas a diario |
| 8 | "Ahorro de 30 a 60 minutos diarios" | Es una estimación, no una medición. Se confirma con la hoja de medición (`plantillas/medicion-carga-trabajo.xlsx`) |
| 9 | Plantillas con SPOA, nombre, fecha y entidad | Las plantillas deben llevar **campos vacíos** (`[COMPLETAR]`), nunca datos de un caso real. Complementan a los agentes 2 y 3: la plantilla sirve para lo más repetido y el agente para lo que cambia |

## Siguiente paso

Usar [`prompts/03-copilot-apps-y-pc.md`](../prompts/03-copilot-apps-y-pc.md) para que Copilot recomiende
qué aplicaciones necesita y cómo personalizar su computador.
