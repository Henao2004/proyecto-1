# Prompt para Copilot — Radiografía del trabajo

**Para qué sirve:** que **Microsoft Copilot** revise la información de trabajo de la asistente de
fiscal (correos, calendario, Teams, archivos y lo que ella le pide a Copilot) y entregue un informe
**anonimizado** de qué hace, qué le piden, cuánto tiempo le toma y dónde se pierde tiempo. Ese
informe es la base para analizar su trabajo y diseñar sus agentes de Copilot.

## Cómo usarlo

1. Abre **Microsoft 365 Copilot** (en Teams, Outlook, la app de Microsoft 365 o el navegador) y
   selecciona la pestaña **Trabajo** (*Work*), no **Web**. Así Copilot puede consultar su correo,
   calendario, chats y archivos.
2. Copia el bloque de texto de abajo, pégalo y envíalo.
3. Si Copilot se corta, escribe **continúa**.
4. Revisa el resultado: **no debe tener nombres, números de noticia criminal ni datos de casos.** Si
   aparece alguno, bórralo.
5. Pega el informe en la conversación con Claude para analizarlo.

> Si solo tiene el Copilot gratuito (sin la pestaña *Trabajo*), Copilot no puede ver su correo ni su
> calendario. El prompt ya contempla ese caso: Copilot le hará preguntas para completar el informe.
>
> Si Copilot no recuerda conversaciones anteriores, abre el historial de chats (panel izquierdo) y
> anota de forma genérica los 10 pedidos que más le haces. Por ejemplo: "resumir un informe de
> policía judicial", nunca el contenido real.

---

```text
Actúa como analista de productividad. Necesito una radiografía de mi trabajo como asistente de fiscal (Fiscalía General de la Nación, Colombia). Usa mi información de trabajo de las últimas 4 semanas: correos de Outlook, calendario y reuniones, chats de Teams, archivos de OneDrive y SharePoint, y lo que sepas de cómo te uso a ti (Copilot).

REGLA DE PRIVACIDAD (obligatoria): voy a compartir este informe fuera de la entidad para analizarlo. NO incluyas nombres de personas, números de noticia criminal o radicados, cédulas, direcciones, teléfonos, nombres de juzgados específicos ni detalles de ningún caso. Usa solo categorías, cantidades aproximadas y roles genéricos ("el fiscal", "policía judicial", "un juzgado", "una entidad externa"). Si tienes duda sobre un dato, omítelo.

Entrega el informe con estas secciones:

1. FUENTES: qué fuentes pudiste revisar, de qué fechas, y cuáles no pudiste consultar.

2. TAREAS: tabla con las columnas Tarea | Frecuencia aproximada | Dónde la ves (correo, calendario, Teams, archivos) | ¿Es repetitiva? (sí/no).

3. CORREO: correos recibidos y enviados por semana (aproximado); los 5 tipos de correo más comunes (por ejemplo: solicitudes del fiscal, respuestas de entidades, citaciones, solicitudes de usuarios); quién los envía según su rol; tiempo de respuesta típico si lo puedes estimar; cuántos siguen sin respuesta.

4. REUNIONES Y AUDIENCIAS: horas por semana en reuniones o audiencias, de qué tipo y en qué días hay picos.

5. DOCUMENTOS: los tipos de documento que más creo o edito (oficios, citaciones, órdenes, actas, informes, hojas de Excel); cuáles son casi iguales cada vez (candidatos a plantilla); cuánto tiempo pasa entre que se pide un documento y se envía.

6. USO DE COPILOT: qué tipo de cosas te pido con más frecuencia, con ejemplos escritos de forma genérica; qué te he pedido varias veces de forma parecida; en qué tus respuestas no me sirvieron o tuve que corregirlas.

7. CUELLOS DE BOTELLA: tareas que se acumulan, pendientes sin cerrar, trabajo que se repite, información que busco varias veces, días u horas de sobrecarga.

8. OPORTUNIDADES: las 5 tareas donde un agente de Copilot me ahorraría más tiempo. Para cada una indica qué haría el agente, cuánto tiempo estimas que ahorraría por semana y qué información necesitaría.

Reglas: no inventes datos ni cifras; si una cifra es estimada, márcala con "aprox.". Si no tienes acceso a una fuente o no recuerdas nuestras conversaciones anteriores, dilo en esa sección y hazme hasta 5 preguntas concretas para completarla. Si el informe es muy largo, entrega hasta la sección 4 y espera a que escriba "continúa".
```

## Después de usarlo

Revisa que el informe no tenga datos de casos y pégalo en la conversación con Claude. Con eso:

1. Analizamos juntos qué hace, qué le piden y en qué se le va el tiempo.
2. Priorizamos qué conviene resolver con un agente, con una plantilla o con un cambio de hábito.
3. Creamos los agentes en `agentes/`, listos para copiar en Copilot.
