# Diagnóstico — octubre de 2026

**Fuente:** informe generado por Copilot con `prompts/01-copilot-radiografia-trabajo.md`
(periodo solicitado: 4 al 31 de octubre de 2026). El informe ya venía anonimizado: no incluye
nombres, números de noticia criminal ni detalles de casos.

**Limitación importante:** Copilot solo pudo revisar el historial de conversaciones con Copilot
(6 al 26 de octubre). **No accedió** a Outlook, calendario, Teams, OneDrive ni SharePoint. Por eso
los hallazgos son **cualitativos**: sabemos *qué* hace y *dónde se traba*, pero todavía no
*cuánto tiempo* le toma cada cosa. Esa medición está en la sección 6.

---

## 1. Qué hace: cuatro frentes de trabajo

| Frente | Ejemplos | ¿Repetitivo? |
|---|---|---|
| **Comunicaciones** | Citaciones, solicitudes de información a entidades, correos de remisión de órdenes y oficios, respuestas a usuarios, comunicaciones internas | Muy repetitivo |
| **Seguimiento procesal** | Solicitudes de audiencia sin programar, respuestas pendientes de entidades, actividades de policía judicial | Repetitivo |
| **Gestión documental** | Revisar expedientes en PDF para sacar datos, preparar oficios y órdenes, matrices en Excel | Parcialmente |
| **Apoyo jurídico y estudio** | Análisis de actuaciones; estudio de delitos contra el patrimonio económico y la fe pública por el cambio a una nueva unidad | No |

## 2. Hallazgos principales

1. **La mayor parte del trabajo visible son comunicaciones casi iguales.** Citaciones, solicitudes a
   entidades y correos de remisión cambian muy poco entre un caso y otro: destinatario, entidad,
   fecha, finalidad y anexos. Hoy se rehacen cada vez.
2. **Copilot ayuda, pero se pierde tiempo en idas y vueltas.** Las instrucciones que más repite son:
   "más breve", "más formal", "que suene natural", "no agregues información", "corrige solo
   ortografía" y "déjalo listo para enviar". Copilot también agrega información que nadie pidió,
   mezcla el oficio con el correo de remisión y no muestra claramente el texto final.
3. **Los pendientes que dependen de otros no tienen un control único.** Ejemplos: audiencias
   solicitadas que no se han programado y entidades que no responden. La información está
   repartida entre correo, PDF, Word, Excel, OneDrive y SharePoint, así que hay que buscar varias
   veces el estado de lo mismo.
4. **Cada envío son dos piezas: el documento y el correo.** Eso duplica trabajo y crea riesgo de
   inconsistencias (asunto, destinatario, anexo, fecha) o de que queden **datos de un expediente
   anterior** al reutilizar un texto.
5. **Hay mucho cambio de contexto.** En la misma jornada pasa de revisar un expediente a citar, pedir
   información, controlar audiencias, atender temas administrativos y estudiar la nueva unidad.
   Eso aumenta los errores de nombres, fechas y adjuntos.

## 3. Lectura crítica del informe de Copilot

- **Acierta** en que el cuello de botella no es solo redactar: buscar el dato, verificar, adjuntar,
  registrar y hacer seguimiento pesan tanto o más.
- **Hay que matizar su recomendación principal.** Copilot propone un agente que lea el correo,
  registre los envíos y avise solo cuando no haya respuesta. Un agente normal de Copilot no hace eso:
  responde cuando se le pide, pero no vigila el correo por su cuenta. Eso requiere Power Automate o
  Copilot Studio y autorización de TI, así que queda para la **fase 3**. Mientras tanto, la matriz
  de seguimiento con el agente 4 cubre lo esencial con un paso manual pequeño.
- **Hay que confirmar por qué Copilot no vio el correo.** Puede que su licencia no incluya Copilot con
  datos de trabajo, o que el prompt se haya usado fuera de la pestaña *Trabajo*. Esto cambia la
  forma de usar los agentes: sin esa licencia, ella tendrá que pegar o adjuntar los documentos.

## 4. Problema → solución

| # | Problema | Solución | Tipo | Impacto | Esfuerzo | Cuándo |
|---|---|---|---|---|---|---|
| 1 | Idas y vueltas de tono con Copilot | [Agente 2 — Redactor del despacho](../agentes/02-redactor-despacho.md) | Agente | Alto | Bajo | Semana 1 |
| 2 | Búsqueda manual de datos en expedientes | [Agente 1 — Lector de documentos](../agentes/01-lector-documentos.md) (modo "buscar un dato") | Agente | Medio | Bajo | Semana 1 |
| 3 | Cambio constante de contexto | Trabajar por bloques: citaciones juntas, correo en 3 momentos fijos del día, seguimiento los lunes y jueves | Hábito | Medio | Bajo | Semana 1 |
| 4 | Citaciones y solicitudes repetidas, documento y correo por separado | [Agente 3 — Citaciones y solicitudes](../agentes/03-citaciones-solicitudes.md) con las plantillas institucionales | Agente + plantillas | Alto | Medio | Semana 2 |
| 5 | Inconsistencias entre correo, documento y anexo; restos de otro caso | [Agente 5 — Revisor antes de enviar](../agentes/05-revisor-antes-de-enviar.md) | Agente | Alto (evita errores) | Bajo | Semana 2 |
| 6 | Pendientes con terceros dispersos | [Matriz de seguimiento](../plantillas/matriz-seguimiento.csv) + [Agente 4 — Control de pendientes](../agentes/04-control-pendientes.md) | Plantilla + agente + hábito | Alto | Medio | Semana 3 |
| 7 | Estudio de la nueva unidad y apoyo jurídico | [Agente 6 — Análisis de noticia criminal](../agentes/06-analisis-noticia-criminal.md). Ella ya lo había creado; se revisaron sus instrucciones. | Agente | Medio | Bajo | Ya existe |
| 8 | Registro y alertas automáticas desde el correo | Power Automate o Copilot Studio, con autorización de TI | Automatización | Alto | Alto | Fase 3 |

## 5. Plan de 30 días

**Semana 1: medir y primeras mejoras**
- Medir la línea base (sección 6).
- Crear el **agente 2 (Redactor)** y usarlo en lugar del chat normal de Copilot para todo texto.
- Usar el **agente 1** para sacar datos de los expedientes.
- Empezar a trabajar por bloques de tiempo.

**Semana 2: comunicaciones**
- Conseguir las **plantillas institucionales vacías** de citación y de oficio de solicitud.
- Crear el **agente 3 (Citaciones y solicitudes)** y subir esas plantillas como conocimiento.
- Crear el **agente 5 (Revisor)**. Regla: todo envío importante pasa por el revisor antes de salir.

**Semana 3: control de pendientes**
- Crear la matriz de seguimiento en Excel, en OneDrive, a partir de `plantillas/matriz-seguimiento.csv`.
- Cargar los pendientes actuales, empezando por las **solicitudes de audiencia sin programar**.
- Crear el **agente 4 (Control de pendientes)** y revisarlo cada lunes y jueves.

**Semana 4: evaluar**
- Repetir la medición y comparar con la semana 1.
- Ajustar las instrucciones de los agentes según lo que no funcionó.
- Decidir si se pasa a la fase 2 (agente de consulta de la unidad) y si se pide apoyo a TI para la fase 3.

## 6. Cómo medir si mejoró

**Línea base (semana 1).** Son los datos que Copilot no pudo calcular. Basta con una aproximación:
1. Correos recibidos y enviados por semana (se ven en Outlook).
2. Horas por semana en audiencias y reuniones (se ven en el calendario).
3. Correos o solicitudes pendientes de respuesta hoy.
4. Oficios, citaciones, órdenes y respuestas elaborados en una semana.
5. Si ya lleva alguna matriz en Excel o SharePoint.
6. **Tiempo para preparar una citación con su correo:** cronometrar 3 casos.
7. **Ajustes que pide a Copilot por texto:** contarlos en 10 textos.

| Indicador | Cómo medirlo | Meta sugerida a 30 días |
|---|---|---|
| Ajustes pedidos a Copilot por texto | Contar en 10 textos | 1 o menos |
| Tiempo de citación + correo | Cronometrar 3 casos | La mitad del tiempo inicial |
| Pendientes vencidos sin reiterar | Tablero del agente 4 | 0 |
| Errores detectados antes de enviar | Semáforo del agente 5 | Registrar cuántos: es la prueba de que el revisor sirve |
| Horas semanales en comunicaciones | Estimación propia | Bajar respecto a la semana 1 |

## 7. Pendiente por confirmar

- [x] ¿Puede crear agentes? **Sí.** Ya creó el agente "ANALISIS NOTICIA CRIMINAL" (1 de noviembre de 2026).
- [ ] ¿Su licencia incluye Copilot con datos de trabajo (correo, calendario)? En el informe, Copilot no pudo verlos.
- [ ] ¿La Fiscalía **autoriza** usar Copilot con documentos de casos?
- [ ] ¿Existen **plantillas oficiales** de citación y de oficio de solicitud?
- [ ] Los datos de la línea base (sección 6).
