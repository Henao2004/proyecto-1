---
name: diagnostico-penal-preliminar
description: "Invocar cuando el usuario suministre una noticia criminal, denuncia, informe de policía judicial o crónica policial y solicite un diagnóstico jurídico-penal preliminar o un dictamen completo. Guía paso a paso la elaboración del dictamen en cinco bloques (hechos jurídicamente relevantes, calificación jurídica provisional, aspectos procesales, programa metodológico inicial y conclusiones con sus límites), con plantilla de salida, criterios de solidez y control de calidad final."
---

# Diagnóstico penal preliminar

Esta guía explica cómo elaborar el dictamen preliminar del agente y complementa sus instrucciones.
Si algo de esta guía contradice las instrucciones del agente, prevalecen las instrucciones.

> Las referencias normativas de esta guía son orientativas. Al citarlas en el dictamen, márcalas
> "Pendiente de verificar vigencia", salvo que hayas consultado el texto oficial en la conversación.

## Paso 1. Identificar la fuente

Registra:
- Tipo de documento: denuncia, noticia criminal, informe ejecutivo, informe de investigador de
  campo, crónica policial, entrevista u otro.
- Fecha del documento y fecha de los hechos.
- Quién informa: víctima, policía judicial, tercero o anónimo.
- Si hay una persona capturada, cuándo y dónde. En ese caso, el análisis de la captura es lo primero
  del bloque 3.

## Paso 2. Extraer y clasificar los hechos

Para cada hecho, identifica qué pasó, quién intervino (por su rol y sus iniciales), cuándo, dónde, cómo, qué bien o
documento se afectó y su valor.

Clasifica cada hecho:
- **Comprobable:** está respaldado por un EMP o EF que el documento menciona como existente (factura,
  video asegurado, documento original, informe pericial) o puede verificarse de forma objetiva.
- **Afirmación de la fuente:** lo dice el denunciante, un testigo o el informe, sin soporte
  independiente. En una denuncia, casi todo es afirmación de la fuente hasta que se corrobore.
- **Inferencia:** lo deduces a partir de otros hechos. Explica brevemente la deducción.

## Paso 3. Identificar los vacíos esenciales

Revisa como mínimo:
- ¿Está individualizado o identificado el presunto autor?
- ¿Cuál es el valor del bien y qué lo soporta?
- ¿Cuál es la fecha exacta de los hechos? Incide en la caducidad de la querella y en el SMLMV que se
  usa para la cuantía.
- ¿Había una relación previa entre la víctima y el indiciado (contrato, préstamo, trabajo, confianza)?
- ¿Cómo salió el bien del poder de la víctima?
- ¿Hay cámaras, transferencias, mensajes, testigos o documentos originales?
- ¿Hay víctimas en condición de vulnerabilidad (menores de edad, adultos mayores, personas con
  discapacidad)?

## Paso 4. Calificación jurídica (bloque 2)

- Usa la habilidad `calificacion-patrimonio-economico` o `calificacion-fe-publica`, según la materia.
- Formula una hipótesis principal y, cuando corresponda, hipótesis alternativas, incluida la de
  atipicidad o controversia civil.
- Contrasta cada elemento del tipo con los hechos en la tabla de elementos.

## Paso 5. Aspectos procesales (bloque 3)

Usa la habilidad `aspectos-procesales`. Revisa en este orden: captura (si la hay), querellabilidad y
caducidad, conciliación preprocesal, procedimiento aplicable, salidas posibles y, si corresponde,
medida de aseguramiento.

## Paso 6. Programa metodológico (bloque 4)

Usa la habilidad `programa-metodologico`. Prioriza lo que se puede perder: videos, rastros de
transferencias, evidencia digital y bienes recuperables.

## Paso 7. Conclusiones y nivel de solidez (bloque 5)

- **Alta:** los hechos relevantes son comprobables y los elementos del tipo se acreditan con lo
  aportado.
- **Media:** los elementos se apoyan sobre todo en afirmaciones de la fuente, pero se pueden
  corroborar con actos concretos.
- **Baja:** hay vacíos sobre elementos esenciales, no hay individualización del autor o es plausible
  una controversia civil.

El siguiente paso sugerido debe ser concreto, por ejemplo: "emitir orden a policía judicial para
asegurar los videos del establecimiento", "citar a conciliación preprocesal" o "solicitar avalúo".

## Paso 8. Control de calidad antes de entregar

- [ ] Están los cinco bloques, en orden.
- [ ] Cada hecho tiene su fragmento del documento entre comillas.
- [ ] Ninguna persona aparece con nombre completo, documento de identidad, dirección o teléfono.
- [ ] Cada norma citada tiene su estado: "Verificada en [fuente]" o "Pendiente de verificar vigencia".
- [ ] No hay números de sentencia ni radicados sin una fuente consultada.
- [ ] No hay expresiones de certeza sin soporte ("procede", "está demostrado").
- [ ] La cuantía aparece en pesos y en SMLMV, o se indica que falta su soporte.
- [ ] Hay al menos una hipótesis alternativa o de descargo, o se explica por qué no la hay.
- [ ] El dictamen termina con la frase de cierre fija.

## Plantilla de salida

```
# Diagnóstico jurídico-penal preliminar
Fuente analizada: [tipo de documento], [fecha]. Fecha de los hechos: [fecha o "No consta"].

## Bloque 1. Hechos jurídicamente relevantes
Resumen: [máximo 8 líneas]

| # | Hecho | Clase | Fragmento del documento |
|---|---|---|---|

Personas: [rol – iniciales]
Víctimas en condición de vulnerabilidad: [si constan]
Vacíos de información: [lista]

## Bloque 2. Calificación jurídica provisional
Hipótesis principal: [tipo penal – artículo]
Hipótesis alternativas: [incluida atipicidad o controversia civil, si aplica]

| Elemento | ¿Se acredita? | Soporte o faltante |
|---|---|---|

Agravantes, atenuantes, concursos, participación y cuantía: [...]

## Bloque 3. Aspectos procesales
Captura: [...] · Querella y caducidad: [...] · Conciliación: [...]
Procedimiento: [...] · Salidas posibles: [...] · Medida de aseguramiento: [...]

## Bloque 4. Programa metodológico inicial
Hipótesis delictiva: [...]
Hipótesis alternativas o de descargo: [...]

| # | Acto | Finalidad | Responsable | Prioridad | Control judicial |
|---|---|---|---|---|---|

## Bloque 5. Conclusiones provisionales y límites
Conclusión tentativa: [máximo 5 líneas]
Solidez: [baja / media / alta], porque [...]
Siguiente paso sugerido: [...]
Verificaciones pendientes: [...]
Normas citadas: [artículo – ley – estado]

Borrador de apoyo preliminar. No sustituye la valoración del fiscal del caso ni las decisiones de los jueces competentes.
```

## Errores frecuentes que debes evitar

- Tratar el relato del denunciante como un hecho probado.
- Calificar como estafa un incumplimiento contractual sin engaño previo.
- Calificar como abuso de confianza el no pago de un préstamo de dinero, porque el mutuo transfiere
  el dominio.
- Citar artículos o sentencias de memoria como si estuvieran verificados.
- Omitir la caducidad de la querella cuando el delito es querellable.
- Calcular la cuantía sin soporte del valor.
- Afirmar que "procede" el archivo, el principio de oportunidad o la medida de aseguramiento.
- Olvidar las hipótesis de descargo.
- Mezclar los hechos de distintos indiciados o de distintas conductas en un solo análisis.
