# Prompt para Claude — Productividad con Microsoft 365

**Para qué sirve:** que **Claude** (en claude.ai) entregue, de una sola vez, el plan de productividad
con las herramientas de Microsoft 365 que la asistente ya tiene. Incluye las 10 funciones que más tiempo
ahorran, el material listo para usar (plantillas, reglas y abreviaturas), la organización de OneNote
para estudiar, un plan de 4 semanas y 5 atajos de teclado.

**Cómo usarlo:** abra un chat nuevo en claude.ai, pegue el bloque completo y envíelo.

> La red de la Fiscalía bloquea claude.ai, así que este prompt se usa desde otro computador. Si el
> resultado le sirve, pídale a Claude que lo convierta en un documento (PDF o Word) y lléveselo a la
> asistente.
>
> **No pegue información de casos en Claude.** Este prompt no la necesita.

## Qué corrige respecto a la primera respuesta (de Copilot)

| En la primera respuesta | Corrección en este prompt |
|---|---|
| "Ctrl + Shift + N crea un correo nuevo en Outlook" | Ese atajo no crea un correo. Ahora pide decir si no está seguro de un atajo y dónde funciona cada uno |
| Acaparamiento y especulación como delitos contra el patrimonio económico | Son delitos contra el orden económico y social. Ahora trae la lista de delitos de la unidad y los excluye |
| "Abrir PDF escaneados en Word los vuelve texto buscable" | No siempre: un PDF escaneado puede quedar como imagen. Ahora pide advertirlo |
| "Ahorro de 30 a 60 minutos diarios" | Era una cifra sin respaldo. Ahora pide no inventar cifras o marcarlas "aprox." |
| Los pasos de Outlook sin distinguir versión | Ahora pide los caminos para Outlook clásico y para el nuevo Outlook |
| Solo la lista de plantillas | Ahora pide el texto completo de 3 plantillas, 4 reglas concretas y las abreviaturas |

---

```text
Eres un experto en productividad con Microsoft 365 para entidades públicas de Colombia. Necesito un plan práctico para mi trabajo. Usa lenguaje sencillo, sin tecnicismos.

<contexto>
Soy asistente de fiscal en una unidad de patrimonio económico y fe pública de la Fiscalía General de la Nación (Colombia). En octubre recibí unos 155 correos y envié unos 78. Mi trabajo:
- Citaciones a entrevistas y declaraciones, también virtuales.
- Solicitudes de información a entidades (tránsito, RUNT, patios, bancos, seguridad social) y a juzgados.
- Seguimiento de respuestas y de audiencias sin programar.
- Órdenes a policía judicial y documentos jurídicos (análisis, archivos, acusaciones).
- Revisión de expedientes largos en PDF.
- Estudio de los delitos de la nueva unidad.
Ya uso Word, Excel, PowerPoint, Outlook y Copilot Chat con agentes.
</contexto>

<herramientas_disponibles>
- Computador de la entidad con Windows.
- En el iniciador de aplicaciones de Microsoft 365 veo Outlook, Teams, OneDrive y OneNote. No sé si tengo To Do, Planner, Lists, Forms, Power Automate, Loop ni SharePoint.
- No veo el botón de Copilot dentro de Word, Excel ni Outlook (probablemente mi licencia no lo incluye).
- No puedo instalar programas sin autorización de TI, y la red de la entidad bloquea algunos sitios externos.
</herramientas_disponibles>

<tarea>
1. Una tabla con las 10 funciones que más tiempo me ahorrarían, priorizando las que no requieren instalar nada, con estas columnas: # | Tarea mía | Herramienta y función | Qué me resuelve | Cómo configurarla (pasos cortos) | Minutos para configurarla | ¿Necesito a TI?
   Evalúa: plantillas y pasos rápidos de Outlook; marcas de seguimiento y To Do; reglas y carpetas; deshacer envío; autocorrección y elementos rápidos de Word; combinar correspondencia de Word con Excel; abrir un PDF en Word; anotar PDF en Edge; historial del portapapeles (Windows + V); dictado por voz (Windows + H); OneNote para estudiar.

2. Para las 3 funciones de mayor impacto, el material listo para usar:
   - Plantillas de Outlook: la lista de plantillas que debo crear y el texto completo de 3 (citación a entrevista virtual, solicitud de información a una entidad y reiteración de una solicitud sin respuesta), en español institucional colombiano y con [CAMPOS] para lo que cambia.
   - Reglas de Outlook: 4 reglas, cada una con su condición, su acción y su carpeta.
   - Autocorrección: una tabla de 6 abreviaturas (Escribo | Se convierte en) y cuándo conviene más usar elementos rápidos para textos largos.

3. OneNote para estudiar: un cuaderno con una sección de patrimonio económico (hurto, estafa, abuso de confianza, emisión ilegal de cheque, extorsión, daño en bien ajeno, receptación y fraudes informáticos) y una de fe pública (falsedad material e ideológica en documento público, falsedad en documento privado, uso de documento falso y falsedad personal). Una página por delito y una plantilla de página con: elementos del delito, preguntas clave para la entrevista, pruebas típicas y dudas para el fiscal.

4. Un plan de 4 semanas, con máximo 3 funciones por semana y el tiempo total de cada semana.

5. Los 5 atajos de teclado que más me servirían, en una tabla: Atajo | Para qué | Dónde funciona.
</tarea>

<reglas>
- No recomiendes instalar programas ni herramientas externas sin autorización de TI.
- No te voy a compartir información de casos. No me recomiendes usar inteligencias artificiales externas con esa información.
- Si una función depende de mi licencia, de la versión de Outlook (clásico o nuevo) o de la configuración de la entidad, dilo.
- Los menús de Outlook clásico y del nuevo Outlook son distintos: da los dos caminos cuando cambien.
- Si no estás seguro del nombre exacto de un menú o de un atajo, dilo en lugar de adivinar.
- Advierte que un PDF escaneado puede quedar como imagen al abrirlo en Word.
- No inventes cifras de ahorro de tiempo; si estimas, márcalas "aprox.".
- No incluyas delitos del orden económico y social, como el acaparamiento o la especulación: no son de mi unidad. Si mencionas artículos del Código Penal, márcalos "verificar con la norma vigente".
- En las plantillas usa [CAMPOS], nunca datos reales.
</reglas>

Al final, ofréceme convertir todo en un documento para imprimir.
```
