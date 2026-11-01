# Cómo crear un agente en Microsoft 365 Copilot

Un **agente** es un Copilot especializado: tiene instrucciones fijas, sus propias fuentes de
conocimiento y botones de inicio rápido. Así la asistente no tiene que volver a escribir el mismo
prompt largo cada vez.

> Los nombres de los menús pueden cambiar un poco según la versión de Copilot y el idioma.
> Crear agentes depende de la licencia y de lo que permita el administrador de TI de la entidad.

## Pasos

1. Abre **Microsoft 365 Copilot** (app de Microsoft 365, Teams o navegador).
2. En el panel izquierdo busca **Agentes** y luego **Crear agente** (*New agent* / *Create agent*).
3. Elige la pestaña **Configurar** (*Configure*) en lugar de **Describir**. Así el agente queda
   exactamente como lo diseñamos.
4. Copia cada campo del archivo del agente (por ejemplo `01-lector-documentos.md`):
   - **Nombre**
   - **Descripción**
   - **Instrucciones**: el bloque completo
   - **Conocimiento**: solo si el archivo del agente lo sugiere
   - **Indicaciones iniciales** (*starter prompts*)
5. Pruébalo en el panel de vista previa con un documento **inventado**, siguiendo la lista
   *Cómo probarlo* del archivo del agente.
6. Pulsa **Crear**. Al compartir, elige **Solo yo** hasta que esté probado.
7. Para usarlo: panel izquierdo → **Agentes** → el nombre del agente. También se puede llamar
   escribiendo `@` y su nombre en el chat de Copilot.

## Si no aparece "Crear agente"

- Probablemente la licencia o la configuración de la entidad no lo permite. Pregunta al área de TI.
- Mientras tanto, se puede usar el bloque **Instrucciones** como prompt normal: pégalo al inicio de
  un chat y después adjunta o pega el documento. Si su Copilot permite **guardar indicaciones**
  (*prompts*), guárdalo para no copiarlo cada vez.

## Buenas prácticas

- **Un agente, un trabajo.** Es mejor tener tres agentes pequeños y precisos que uno que lo haga todo.
- **Instrucciones cortas y concretas.** El límite es de alrededor de 8.000 caracteres.
- **Probar siempre con datos inventados** antes de usar documentos reales.
- **No usar como conocimiento** carpetas con documentos de casos, salvo que la entidad lo autorice.
- **Revisar el resultado.** El agente ayuda a organizar, pero la asistente y el fiscal deciden.
