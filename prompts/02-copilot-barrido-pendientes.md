# Prompt para Copilot — Barrido de pendientes

**Para qué sirve:** que **Copilot** (en la pestaña **Trabajo**) revise el correo de los últimos 15 días,
encuentre las solicitudes enviadas y sus respuestas, y entregue las filas listas para pegar en la
[matriz de seguimiento](../plantillas/matriz-seguimiento.xlsx). Úselo los **lunes y jueves** si el
agente 4 no puede leer el correo directamente.

**Cómo usarlo:**
1. Abra Microsoft 365 Copilot, pestaña **Trabajo**.
2. Copie el bloque de abajo, cambie la fecha de hoy y envíelo.
3. Compare la tabla con la matriz:
   - **Solicitudes que no están en la matriz:** copie esas filas, haga clic en la **columna B** de la
     primera fila vacía y pegue.
   - **Solicitudes que ya están:** actualice a mano solo las celdas que cambiaron (estado, fecha de
     respuesta y observaciones). No pegue la fila completa encima, porque las celdas vacías borrarían
     datos.

> El resultado tiene datos de casos: úselo solo dentro de la entidad. **No lo pegue en Claude ni en
> ninguna herramienta externa.**

---

```text
Hoy es [DD/MM/AAAA]. Revisa mi correo de los últimos 15 días y encuentra todo lo que envié pidiendo algo a otros (solicitudes a entidades, órdenes a policía judicial, solicitudes o seguimientos de audiencia, citaciones y reiteraciones) y las respuestas que recibí a esas solicitudes.

Empareja cada respuesta con su solicitud por número de oficio o radicado, número de noticia criminal y remitente, o por el hilo del correo. Si el emparejamiento es dudoso, no lo hagas y avísame.

Clasifica cada solicitud en uno de estos estados:
- Pendiente: sin ninguna respuesta.
- Radicada: solo confirmaron el recibido o dieron un radicado (por ejemplo, "será atendida dentro de los términos"). No es respuesta.
- Respondida: llegó la respuesta de fondo con lo pedido.
- Programada: la audiencia o diligencia ya tiene fecha.

Entrega:
1. Resumen en una línea: cuántas solicitudes encontraste y cuántas hay en cada estado.
2. Una tabla con estas columnas, en este orden, para pegar en Excel: fecha_envio | tipo | destinatario | numero_noticia_criminal | asunto | fecha_respuesta_esperada | estado | fecha_ultima_reiteracion | num_reiteraciones | fecha_respuesta | observaciones. En tipo usa: Solicitud a entidad, Orden a policía judicial, Solicitud de audiencia, Citación u Otro. Fechas como DD/MM/AAAA. Deja vacías las celdas sin dato. En observaciones anota el radicado, la fecha de la audiencia programada o lo que falte de una respuesta incompleta.
3. Alertas: respuestas sin emparejar, respuestas incompletas y solicitudes con más de 15 días sin respuesta de fondo.
4. Cuántos correos enviados y recibidos revisaste. Advierte si la búsqueda pudo no traer todos.

No incluyas correos internos que no pidan nada a un tercero, boletines ni notificaciones del sistema. Una cadena de respuestas sobre la misma solicitud cuenta como una sola solicitud.
```
