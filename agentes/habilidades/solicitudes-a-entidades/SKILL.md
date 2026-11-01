---
name: solicitudes-a-entidades
description: "Invocar para redactar solicitudes de información a entidades públicas y privadas dentro de una investigación penal en Colombia, como organismos de tránsito, RUNT, patios, Registraduría y notarías, seguridad social, entidades financieras, operadores de telecomunicaciones, cámaras de comercio, oficinas de registro, juzgados, centros de servicios judiciales y establecimientos privados con cámaras. Indica qué se puede pedir a cada una, qué datos necesita la entidad para buscar, cómo estructurar el oficio y cuándo advertir que la información es reservada y puede requerir autorización judicial."
---

# Solicitudes de información a entidades

> Guía orientativa. Usa las plantillas institucionales cuando existan. **No inventes plazos legales:**
> usa el plazo que indique el despacho o la plantilla. Las alertas de reserva son para **verificar**:
> la decisión es del fiscal.

## Reglas generales

1. **Una solicitud por entidad.** Si hay que pedir a varias, haz una pieza para cada una.
2. **Pide solo lo necesario**, en una lista numerada. Evita "toda la información que repose".
3. **Incluye los datos que la entidad necesita para buscar** (placa, número de documento, número de
   cuenta, periodo, número de comparendo) y solo esos.
4. **Indica el formato de entrega:** copia digital, copia certificada, imágenes, archivos de video u
   hojas de cálculo.
5. **Indica el canal y el plazo de respuesta** que te dé el despacho.
6. **No describas los hechos del caso** ni nombres a la víctima si la entidad no lo necesita.
7. **Alerta de reserva.** Si se pide información reservada sobre el indiciado o sobre un tercero
   (financiera, de telecomunicaciones, tributaria, de salud o de seguridad social con datos sensibles),
   escribe en la verificación: *"Verificar si requiere autorización previa del juez de control de
   garantías (búsqueda selectiva en bases de datos, art. 244 Ley 906)"*. Si la víctima pide su propia
   información y lo autoriza, déjalo anotado.

## Catálogo por entidad

### Tránsito y vehículos (grupo muy frecuente en el despacho)
| Entidad | Qué se suele pedir | Datos para buscar | Reserva |
|---|---|---|---|
| **RUNT** | Historial del vehículo: propietarios y traspasos, matrícula, características, limitaciones a la propiedad (prendas, embargos), SOAT y revisión técnico-mecánica; licencias de conducción de una persona | Placa; VIN, número de motor o chasis; número de documento para licencias | Verificar si los datos personales del propietario requieren autorización |
| **Organismo de tránsito o secretaría de movilidad** | Carpeta del vehículo (trámites y documentos soporte de traspasos), comparendos, fotodetecciones con sus imágenes | Placa, número de comparendo, fechas o periodo | Administrativa; verificar si incluye datos sensibles |
| **Patios** | Fecha y causa de ingreso, inventario y estado del vehículo, autoridad que lo dejó a disposición, situación actual | Placa, fecha aproximada de ingreso, número de inventario | — |

**Oficios de ingreso o puesta a disposición en patios:** usa la plantilla institucional. Deben incluir
placa y características del vehículo, autoridad que lo pone a disposición, motivo, a disposición de
quién queda y las indicaciones del despacho sobre su entrega. **La decisión sobre la entrega del
vehículo es del fiscal:** nunca la redactes sin que te la indiquen.

### Identificación y estado civil
| Entidad | Qué se suele pedir | Datos para buscar |
|---|---|---|
| **Registraduría** | Información de identificación, registros civiles de nacimiento, matrimonio o defunción | Número de documento, nombre completo, fecha de nacimiento aproximada |
| **Notarías** | Copias de registros civiles o de escrituras | Serial o indicativo, nombre, fecha |

### Seguridad social
| Entidad | Qué se suele pedir | Datos para buscar | Reserva |
|---|---|---|---|
| **Colpensiones y fondos de pensiones** | Afiliación, empleador reportado, datos de contacto registrados | Número de documento | Verificar (información de terceros) |
| **EPS** | Afiliación y datos de contacto | Número de documento | Verificar. **Las historias clínicas tienen reserva especial:** requieren autorización del titular o judicial (verificar) |

### Entidades financieras y billeteras digitales
| Qué se suele pedir | Datos para buscar | Reserva |
|---|---|---|
| Titular de una cuenta o producto, extractos y movimientos, trazabilidad de transferencias, registros de acceso (IP, dispositivo), videos de cajeros u oficinas, reclamaciones de la víctima | Número de cuenta o producto, fecha, hora y valor de la transacción, número de documento | Información de terceros: control previo (verificar). Información de la víctima: con su autorización |

### Operadores de telecomunicaciones
Titular de una línea, datos del abonado, IMEI y registros de comunicaciones. **Todo lo que no sea del
propio usuario que lo autoriza: control previo (verificar).**

### Comercio y registro
| Entidad | Qué se suele pedir | Reserva |
|---|---|---|
| **Cámara de comercio** | Certificado de existencia y representación legal | Pública |
| **Oficina de registro de instrumentos públicos** | Certificado de tradición y libertad | Pública |
| **DIAN** | Información tributaria | Reservada: verificar |

### Juzgados y centros de servicios judiciales
Programación o estado de audiencias, copias de actas o registros. **Datos para buscar:** radicado o
noticia criminal, tipo de audiencia y fecha de radicación de la solicitud.

### Establecimientos privados con cámaras
- Videos: fecha, franja horaria amplia y ubicación de la cámara.
- **URGENTE:** muchos sistemas sobrescriben las grabaciones en pocos días.
- Si es posible, la recolección debe hacerla policía judicial con cadena de custodia. Sugiere también
  la orden a policía judicial (habilidad `ordenes-policia-judicial`).

## Estructura del oficio (solo si no hay plantilla)

1. Ciudad y fecha; número de oficio `[COMPLETAR]`.
2. Destinatario: entidad, dependencia y correo (del directorio de entidades, si existe).
3. Asunto: `Solicitud de información – NC [número]`.
4. Primer párrafo: referencia a la investigación y a que la información se requiere con fines
   investigativos.
5. Lista numerada de lo que se solicita.
6. Datos para la búsqueda.
7. Formato, plazo y canal de respuesta.
8. `[FIRMA]`.

## Errores frecuentes

- Pedir "toda la información" sin precisar qué.
- Omitir la placa, el documento o el periodo de búsqueda.
- Incluir datos de la víctima que la entidad no necesita.
- Mezclar varias entidades en un mismo oficio.
- Enviar a un correo general cuando la entidad tiene uno para requerimientos judiciales.
- Olvidar registrar la solicitud en la matriz de seguimiento.
