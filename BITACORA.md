# Bitácora del proyecto

Memoria de trabajo entre sesiones. **Léela al empezar y actualízala al terminar.** No contiene datos de
casos: solo decisiones, estado y pendientes.

## Contexto

- El usuario (cuenta de GitHub `Henao2004`) apoya a una **asistente de fiscal** de una unidad de
  **patrimonio económico y fe pública** de la Fiscalía General de la Nación (Colombia). Ella cambió de
  unidad en octubre de 2026.
- Ella usa **Microsoft 365 Copilot** en Mac, con **Agent Builder**: instrucciones de hasta 8.000
  caracteres, **habilidades** cargadas como `SKILL.md` o `.zip`, conocimiento (sitios web y archivos) e
  indicaciones sugeridas. Su licencia **sí permite que Copilot busque en su correo y sus archivos**
  (confirmado el 1 de noviembre de 2026).
- Rama de trabajo: `claude/prompts-asistente-fiscal`. Todavía no se ha pasado a `main`. **El repositorio
  sigue público**: se le recomendó hacerlo privado.

## Sesión del 1 de noviembre de 2026: qué se hizo

1. Radiografía del trabajo con Copilot (`prompts/01`) y diagnóstico en `analisis/01-diagnostico-octubre-2026.md`.
2. Medición parcial con datos de Copilot (sección 8 y 9 del diagnóstico):
   - **Octubre (20 días hábiles):** 155 correos recibidos, 78 enviados, 2 eventos en el calendario
     (1 hora), 33 archivos y al menos 6 tipos de pendientes.
   - **Semana del 26 al 30 de octubre:** 46 recibidos, 39 enviados y 8 documentos. Inconsistencia con
     el mes, por verificar.
3. Hallazgos clave:
   - El centro del trabajo son las solicitudes a terceros (juzgados, tránsito, RUNT, Colpensiones,
     bancos) y su seguimiento.
   - Hay un grupo repetitivo de solicitudes sobre vehículos.
   - Las diligencias no están en el calendario.
   - No hay un control único de pendientes.
   - Tiene redacción jurídica sustancial: acusaciones, archivos y programas metodológicos.
4. **Los 6 agentes en versión completa**, cada uno con instrucciones, descripción, habilidades,
   conocimiento, indicaciones y pruebas.
5. Plantillas: matriz de pendientes en Excel con alertas (probada con LibreOffice), directorio de
   entidades, hoja de medición y registro de documentos.
6. Guía de uso diario (`GUIA-USO-DIARIO.md`), también publicada como página de Claude, compartida por
   enlace. Por cada agente explica para qué sirve, cómo funciona en 3 pasos, qué hace, qué no hace,
   cuándo usarlo, un ejemplo y frases para copiar (iguales a sus indicaciones de inicio). Al final trae
   los momentos del día y cuatro reglas.

## Estado de los agentes

| Agente | Instrucciones (conteo de Copilot) | Habilidades | ¿Creado en Copilot? |
|---|---|---|---|
| 1. Lector de documentos y respuestas | 6.914 | `lectura-de-respuestas`, `analisis-de-expedientes` | Por confirmar |
| 2. Redactor del despacho | 7.304 | `estilo-institucional`, `correccion-ortografica`, `correos-del-despacho` | Por confirmar |
| 3. Citaciones y solicitudes | 7.144 | `citaciones-y-entrevistas`, `solicitudes-a-entidades`, `ordenes-policia-judicial` | Por confirmar |
| 4. Control de pendientes | 6.858 | `seguimiento-por-etapas`, `barrido-de-correo` | Por confirmar |
| 5. Revisor antes de enviar | 6.465 | `verificacion-de-envios`, `proteccion-de-datos-en-envios` | Por confirmar |
| 6. ANALISIS NOTICIA CRIMINAL | 7.602 | `diagnostico-penal-preliminar`, `calificacion-patrimonio-economico`, `calificacion-fe-publica`, `aspectos-procesales`, `programa-metodologico` | **Sí.** Ya existía; se le entregaron las instrucciones, la descripción, las habilidades y el conocimiento revisados |

## Decisiones de diseño (respetarlas)

- **Copilot cuenta los caracteres sin los saltos de línea.** Las instrucciones deben quedar por debajo
  de 8.000 en ese conteo. Mídelo con `tr -d '\n' | wc -m`.
- **Las instrucciones** llevan las reglas y el formato. **Las habilidades** llevan el detalle (Copilot
  las carga cuando las necesita). **El conocimiento** lleva las fuentes oficiales para verificar.
- **Habilidades:** frontmatter YAML con `name` igual a la carpeta y `description` entre comillas de
  1.024 caracteres o menos. El `.zip` lleva el `SKILL.md` en la raíz:
  `cd agentes/habilidades/<nombre> && zip -X <ruta>/<nombre>.zip SKILL.md`. Los `.zip` no se versionan.
- **Matriz de pendientes:**
  - Estados: Pendiente, Radicada, Reiterada, Respondida, Programada y Cerrada.
  - Columnas B..L idénticas en los agentes 3 y 4, en el prompt 02 y en el Excel.
  - Las filas se entregan como **tabla** y se pegan **desde la columna B**. Nunca se pega una fila con
    celdas vacías encima de una existente.
- **"Una constancia de radicación no es una respuesta":** es una regla transversal.
- **Referencias normativas:** son orientativas y llevan la marca "verificar". Los agentes no citan
  sentencias que no hayan consultado.
- **Privacidad:** nunca se guardan números de noticia criminal ni datos de casos en el repo. El 1 de
  noviembre, el usuario pegó por error tres números de noticia criminal; no se guardaron.

## Guía de uso diario

- Página publicada: https://claude.ai/artifact/3AzuKhNgPunQ5svdQt2tbr (compartida por enlace).
- **La red de la Fiscalía bloquea claude.ai** (3 de noviembre de 2026). Por eso existe `guia/` con
  una versión HTML que se abre sin internet y un PDF. Se regeneran con `python3 guia/construir.py`.

## Herramientas

- `analisis/02-recomendaciones-herramientas.md`: las 10 funciones de Office y Windows que más tiempo
  ahorran, programas que pedir a TI (Acrobat Pro, PowerToys) y la regla de IA: información de casos
  solo en Copilot institucional.
- `prompts/03`: Copilot le pregunta qué aplicaciones tiene y le arma su propia lista con un plan de 4
  semanas. Pendiente: que ella lo use y comparta el resultado (no tiene datos de casos).

## Productividad con Microsoft 365 (3 de noviembre de 2026)

- Su computador del trabajo es **Windows**. No ve el botón de Copilot en Word, Excel ni Outlook, aunque
  Copilot sí pudo buscar en su correo: hay que preguntarle a TI.
- Recomendaciones de Copilot y correcciones en `analisis/02-productividad-m365.md`. Prompt siguiente:
  `prompts/03-copilot-apps-y-pc.md` (aplicaciones y personalización del computador).

## Pendientes

- [ ] Ella: estimaciones de horas por tarea, minutos por citación completa y ajustes a Copilot por texto.
- [ ] Ella: títulos de las columnas de su "base de control" y de su **radicador** en Excel, para
      adaptar los agentes 1 y 4.
- [ ] Crear los agentes en Copilot en orden: 2 y 1 → 3 y 5 → 4. Hacer las pruebas de cada ficha.
- [ ] El fiscal valida las habilidades jurídicas del agente 6 y las alertas de control judicial de los
      agentes 3 y 5.
- [ ] Hacer privado el repositorio y pasar la rama a `main`.
- [ ] Repetir la medición en la semana 4 (hacia el 30 de noviembre de 2026) y comparar.

## Ideas para después (no urgentes)

- Agregar al agente 6 un "modo estudio" para preguntas sobre delitos y no sobre casos.
- Habilidad de cuestionarios de entrevista para el agente 6.
- Prompt 03: informe de gestión mensual con Copilot (el informe de 30 días ya sirvió de modelo).
- Fase 3, con autorización de TI: Power Automate para registrar los envíos en la matriz y enviar
  alertas diarias.
