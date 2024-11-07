questions = [
    {
        "tipo": "normalizacion",
        "enunciado": (
            "Determina cuál de las siguientes tablas está en 1NF pero NO en 2NF. La clave primaria es (A, B).<br><br>"
            "<table><pre>"
            "| A  | B  | C      |\n"
            "|----|----|--------|\n"
            "| a1 | b1 | c1, c2 |\n"
            "| a2 | b2 | c3     |"
            "</pre></table>"
        ),
        "opciones": [
            ("a", (
                "<table><pre>"
                "| A  | B  | C      |\n"
                "|----|----|--------|\n"
                "| a1 | b1 | c1, c2 |\n"
                "| a2 | b2 | c3     |"
                "</pre></table>"
            )),
            ("b", (
                "<table><pre>"
                "| A  | B  | C  |\n"
                "|----|----|----|\n"
                "| a1 | b1 | c1 |\n"
                "| a2 | b2 | c2 |"
                "</pre></table>"
            )),
            ("c", (
                "<table><pre>"
                "| A  | B  | C  |\n"
                "|----|----|----|\n"
                "| a1 | b1 | c1 |\n"
                "| a1 | b2 | c2 |"
                "</pre></table>"
            )),
            ("d", (
                "<table><pre>"
                "| A  | B  | C  |\n"
                "|----|----|----|\n"
                "| a1 | b1 | c1 |\n"
                "| a2 | b1 | c2 |"
                "</pre></table>"
            )),
        ],
        "correcta": "a",
        "feedback": {
            "a": "Correcto. La tabla está en 1NF porque hay valores múltiples en la columna C, por lo tanto, no puede estar en 2NF.",
            "b": "Incorrecto. La tabla está en 2NF ya que cumple con todas las reglas de 1NF y no tiene dependencias parciales.",
            "c": "Incorrecto. Esta tabla está en 2NF y también en 3NF.",
            "d": "Incorrecto. La tabla está en 2NF porque todas las dependencias funcionales se basan en la clave primaria.",
        }
    },
    {
        "tipo": "normalizacion",
        "enunciado": (
            "Considera la relación R(A, B, C, D) donde la clave primaria es (A, B). Las dependencias funcionales son:<br>"
            "1. A, B → C<br>"
            "2. C → D<br><br>"
            "¿Cuál de las siguientes tablas está en 2NF pero NO en 3NF?<br><br>"
            "<table><pre>"
            "| A  | B  | C  | D  |\n"
            "|----|----|----|----|\n"
            "| a1 | b1 | c1 | d1 |\n"
            "| a1 | b2 | c2 | d2 |\n"
            "| a2 | b1 | c3 | d3 |\n"
            "| a2 | b2 | c4 | d4 |"
            "</pre></table>"
        ),
        "opciones": [
            ("a", (
                "<table><pre>"
                "| A  | B  | C  | D  |\n"
                "|----|----|----|----|\n"
                "| a1 | b1 | c1 | d1 |\n"
                "| a1 | b2 | c2 | d2 |\n"
                "| a2 | b1 | c3 | d3 |\n"
                "| a2 | b2 | c4 | d4 |"
                "</pre></table>"
            )),
            ("b", (
                "<table><pre>"
                "| A  | B  | C  | D |\n"
                "|----|----|----|----|\n"
                "| a1 | b1 | c1 | d1 |\n"
                "| a1 | b1 | c1 | d2 |\n"
                "| a2 | b2 | c2 | d3 |\n"
                "| a2 | b2 | c2 | d4 |"
                "</pre></table>"
            )),
            ("c", (
                "<table><pre>"
                "| A  | B  | C  | D |\n"
                "|----|----|----|----|\n"
                "| a1 | b1 | c1 | d1 |\n"
                "| a1 | b1 | c2 | d1 |\n"
                "| a2 | b2 | c3 | d2 |\n"
                "| a2 | b2 | c4 | d2 |"
                "</pre></table>"
            )),
            ("d", (
                "<table><pre>"
                "| A  | B  | C  | D |\n"
                "|----|----|----|----|\n"
                "| a1 | b1 | c1 | d1 |\n"
                "| a2 | b1 | c1 | d2 |\n"
                "| a1 | b2 | c2 | d3 |\n"
                "| a2 | b2 | c2 | d4 |"
                "</pre></table>"
            )),
        ],
        "correcta": "a",
        "feedback": {
            "a": "Correcto. La tabla está en 2NF porque todos los atributos no clave (C y D) dependen de la clave primaria completa (A, B). Sin embargo, no está en 3NF debido a la dependencia transitiva C → D. Esto significa que D depende de C, y C depende de (A, B), creando una dependencia transitiva que viola la tercera forma normal.",
            "b": "Incorrecto. La tabla no está en 2NF porque existe una dependencia parcial de D en B. D cambia cuando B cambia, manteniéndose A constante, lo que viola la segunda forma normal.",
            "c": "Incorrecto. La tabla viola la 2NF debido a dependencias parciales. Aquí, D depende solo de A, ya que D permanece constante cuando A es constante, independientemente de B, violando así la segunda forma normal.",
            "d": "Incorrecto. La tabla está en 3NF y BCNF. No existen dependencias funcionales que violen estas formas normales, ya que todas las dependencias tienen claves candidatas en su lado izquierdo o los atributos derechos son primos.",
        }
    }

]

# questions = [
#     {
#         "tipo": "conceptos_generales",
#         "enunciado": "¿Qué es una base de datos?",
#         "opciones": [
#             ("a", "Un conjunto organizado de datos almacenados y accesibles electrónicamente."),
#             ("b", "Un programa que se usa para crear gráficos y tablas."),
#             ("c", "Una estructura de programación para manipular datos en memoria."),
#             ("d", "Una herramienta para diseñar interfaces de usuario."),
#         ],
#         "correcta": "a"
#     },
#     {
#         "tipo": "conceptos_generales",
#         "enunciado": "¿Cuál de las siguientes es una ventaja clave de usar bases de datos?",
#         "opciones": [
#             ("a", "Mayor redundancia de datos"),
#             ("b", "Menor integridad de datos"),
#             ("c", "Mayor integridad de datos y consistencia"),
#             ("d", "Almacenamiento en formato de texto plano"),
#         ],
#         "correcta": "c"
#     },
#     {
#         "tipo": "conceptos_generales",
#         "enunciado": "¿Qué es un sistema de gestión de bases de datos (DBMS)?",
#         "opciones": [
#             ("a", "Un conjunto de instrucciones para limpiar datos."),
#             ("b", "Un software que permite a los usuarios crear y gestionar bases de datos."),
#             ("c", "Una función que convierte datos en gráficos."),
#             ("d", "Una herramienta para sincronizar datos en tiempo real."),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "conceptos_generales",
#         "enunciado": "¿Qué es la atomicidad en una transacción de base de datos?",
#         "opciones": [
#             ("a", "La capacidad de una transacción para dividirse en partes más pequeñas."),
#             ("b", "La garantía de que cada transacción se ejecuta por completo o no se ejecuta en absoluto."),
#             ("c", "El proceso de asegurar la integridad de los datos durante una transacción."),
#             ("d", "La capacidad de realizar múltiples transacciones a la vez."),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "conceptos_generales",
#         "enunciado": "¿Cuál es el propósito principal de una base de datos relacional?",
#         "opciones": [
#             ("a", "Permitir el almacenamiento de datos no estructurados"),
#             ("b", "Mantener datos en estructuras de árbol"),
#             ("c", "Relacionar datos en tablas basadas en atributos comunes"),
#             ("d", "Crear gráficos dinámicos a partir de datos"),
#         ],
#         "correcta": "c"
#     },
#     {
#         "tipo": "conceptos_generales",
#         "enunciado": "¿Qué es una transacción en una base de datos?",
#         "opciones": [
#             ("a", "Una consulta SQL que actualiza datos en una tabla."),
#             ("b", "Una operación que implica una secuencia de cambios en la base de datos."),
#             ("c", "El proceso de eliminar datos de una base de datos."),
#             ("d", "Un gráfico que muestra las relaciones entre datos."),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "conceptos_generales",
#         "enunciado": "¿Cuál es una característica fundamental de una base de datos distribuida?",
#         "opciones": [
#             ("a", "Los datos se almacenan en una única ubicación."),
#             ("b", "Los datos se almacenan en múltiples ubicaciones interconectadas."),
#             ("c", "Los datos están en formato de texto plano."),
#             ("d", "Los datos no se pueden replicar."),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "conceptos_generales",
#         "enunciado": "¿Cuál es la principal función de un índice en una base de datos?",
#         "opciones": [
#             ("a", "Almacenar datos en un formato comprimido."),
#             ("b", "Facilitar el acceso rápido a datos específicos."),
#             ("c", "Resguardar datos en un archivo de respaldo."),
#             ("d", "Mejorar la integridad de los datos."),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "conceptos_generales",
#         "enunciado": "¿Qué tipo de datos suele manejar una base de datos relacional?",
#         "opciones": [
#             ("a", "Datos numéricos exclusivamente."),
#             ("b", "Datos no estructurados como imágenes y videos."),
#             ("c", "Datos estructurados organizados en tablas."),
#             ("d", "Datos en formato de texto sin estructura."),
#         ],
#         "correcta": "c"
#     },
#     {
#         "tipo": "conceptos_generales",
#         "enunciado": "¿Qué es la integridad referencial en una base de datos?",
#         "opciones": [
#             ("a", "La capacidad de mantener una copia de seguridad de los datos."),
#             ("b", "La necesidad de actualizar datos en múltiples tablas."),
#             ("c", "La restricción de que una relación de tabla debe ser válida."),
#             ("d", "La relación entre columnas que almacenan datos únicos."),
#         ],
#         "correcta": "c"
#     },
#     {
#         "tipo": "conceptos_generales",
#         "enunciado": "¿Qué es el modelo relacional de datos?",
#         "opciones": [
#             ("a", "Un modelo de datos donde se usan grafos para almacenar datos."),
#             ("b", "Un modelo de datos en donde los datos están organizados en tablas."),
#             ("c", "Un modelo basado en redes de nodos y relaciones."),
#             ("d", "Un modelo para manejar datos no estructurados."),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "conceptos_generales",
#         "enunciado": "¿Qué es una consulta en una base de datos?",
#         "opciones": [
#             ("a", "Una operación que elimina datos duplicados."),
#             ("b", "Un comando que permite recuperar o modificar datos."),
#             ("c", "Una estructura de datos utilizada para organizar atributos."),
#             ("d", "Un proceso para estructurar datos en tablas."),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "conceptos_generales",
#         "enunciado": "¿Qué significa la propiedad de aislamiento en una transacción?",
#         "opciones": [
#             ("a", "Las transacciones deben ejecutarse en el mismo orden en que se reciben."),
#             ("b", "Cada transacción debe ejecutarse de manera independiente, sin interferencia de otras."),
#             ("c", "Permite que múltiples transacciones accedan a los mismos datos."),
#             ("d", "Asegura que todos los datos están completos antes de la ejecución de una transacción."),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "conceptos_generales",
#         "enunciado": "¿Qué es la redundancia de datos en una base de datos?",
#         "opciones": [
#             ("a", "La eliminación de registros duplicados."),
#             ("b", "La presencia de datos duplicados en la base de datos."),
#             ("c", "El proceso de restaurar datos eliminados."),
#             ("d", "Un modelo de almacenamiento de datos en múltiples servidores."),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "conceptos_generales",
#         "enunciado": "¿Qué es una base de datos transaccional?",
#         "opciones": [
#             ("a", "Una base de datos diseñada para consultas de solo lectura."),
#             ("b", "Una base de datos que maneja operaciones en tiempo real y transacciones."),
#             ("c", "Una base de datos para almacenar datos multimedia."),
#             ("d", "Una base de datos utilizada solo para la exportación de datos."),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "ACID",
#         "enunciado": "¿Qué significa el principio de atomicidad en una transacción de base de datos?",
#         "opciones": [
#             ("a", "Una transacción debe completarse o revertirse completamente."),
#             ("b", "Una transacción puede dividirse en múltiples partes menores."),
#             ("c", "Permite que múltiples transacciones ocurran simultáneamente."),
#             ("d", "Los cambios en una transacción no necesitan ser permanentes."),
#         ],
#         "correcta": "a"
#     },
#     {
#         "tipo": "ACID",
#         "enunciado": "¿Cuál de las siguientes es una descripción correcta de la consistencia en ACID?",
#         "opciones": [
#             ("a", "La transacción puede ser revertida en cualquier momento."),
#             ("b", "El sistema permanece en un estado válido después de una transacción."),
#             ("c", "Los cambios realizados son visibles para todos los usuarios inmediatamente."),
#             ("d", "El sistema puede continuar funcionando aunque una transacción falle."),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "ACID",
#         "enunciado": "En el contexto de ACID, ¿qué representa el aislamiento?",
#         "opciones": [
#             ("a", "Las transacciones deben ejecutarse de manera secuencial."),
#             ("b", "Una transacción no puede interferir con otra en ejecución."),
#             ("c", "Cada transacción debe ejecutarse en un entorno completamente separado."),
#             ("d", "Solo una transacción puede ejecutarse en la base de datos a la vez."),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "ACID",
#         "enunciado": "¿Qué garantiza la durabilidad en una transacción de base de datos?",
#         "opciones": [
#             ("a", "Que la transacción pueda ser revertida después de ejecutarse."),
#             ("b", "Que los datos solo sean accesibles durante la transacción."),
#             ("c", "Que los cambios persistan incluso después de un fallo del sistema."),
#             ("d", "Que los datos se borren automáticamente después de la transacción."),
#         ],
#         "correcta": "c"
#     },
#     {
#         "tipo": "ACID",
#         "enunciado": "Si una transacción falla durante su ejecución, ¿qué aspecto de ACID asegura que la base de datos no queda en un estado inconsistente?",
#         "opciones": [
#             ("a", "Durabilidad"),
#             ("b", "Atomicidad"),
#             ("c", "Aislamiento"),
#             ("d", "Consistencia"),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "ACID",
#         "enunciado": "¿Qué se asegura con la propiedad de consistencia en ACID?",
#         "opciones": [
#             ("a", "Que cada transacción se ejecute por completo o no se ejecute."),
#             ("b", "Que los cambios de una transacción permanezcan en la base de datos."),
#             ("c", "Que la base de datos pase de un estado válido a otro válido."),
#             ("d", "Que los cambios se hagan visibles para otros usuarios de inmediato."),
#         ],
#         "correcta": "c"
#     },
#     {
#         "tipo": "ACID",
#         "enunciado": "¿Por qué es importante el aislamiento en las transacciones?",
#         "opciones": [
#             ("a", "Evita que las transacciones modifiquen datos temporalmente."),
#             ("b", "Permite que cada transacción tenga una copia de los datos."),
#             ("c", "Evita que los resultados intermedios sean visibles a otras transacciones."),
#             ("d", "Permite la ejecución paralela de múltiples transacciones."),
#         ],
#         "correcta": "c"
#     },
#     {
#         "tipo": "ACID",
#         "enunciado": "¿Qué significa que una base de datos es ACID-compliant?",
#         "opciones": [
#             ("a", "Que soporta consultas de solo lectura."),
#             ("b", "Que implementa las propiedades de atomicidad, consistencia, aislamiento y durabilidad."),
#             ("c", "Que puede ejecutar solo una transacción a la vez."),
#             ("d", "Que permite almacenar datos en formatos no estructurados."),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "ACID",
#         "enunciado": "¿Cuál es la diferencia principal entre durabilidad y consistencia en ACID?",
#         "opciones": [
#             ("a", "Durabilidad garantiza que los cambios se mantengan, consistencia asegura la validez de los datos."),
#             ("b", "Consistencia garantiza la permanencia de los cambios, durabilidad valida los datos."),
#             ("c", "Durabilidad permite múltiples transacciones, consistencia asegura la integridad de datos."),
#             ("d", "No hay diferencia; ambas se refieren a la validez de la transacción."),
#         ],
#         "correcta": "a"
#     },
#     {
#         "tipo": "ACID",
#         "enunciado": "¿Qué propiedad de ACID asegura que los cambios de una transacción completada no se pierdan en caso de un fallo?",
#         "opciones": [
#             ("a", "Atomicidad"),
#             ("b", "Consistencia"),
#             ("c", "Aislamiento"),
#             ("d", "Durabilidad"),
#         ],
#         "correcta": "d"
#     },
#     {
#         "tipo": "ACID",
#         "enunciado": "¿Qué sucede si una transacción no cumple con el principio de aislamiento?",
#         "opciones": [
#             ("a", "La base de datos se corrompe de inmediato."),
#             ("b", "La base de datos no puede ejecutar transacciones concurrentes."),
#             ("c", "Los resultados intermedios pueden afectar a otras transacciones."),
#             ("d", "No puede completarse la transacción."),
#         ],
#         "correcta": "c"
#     },
#     {
#         "tipo": "ACID",
#         "enunciado": "¿Por qué es importante la propiedad de atomicidad en ACID?",
#         "opciones": [
#             ("a", "Permite la concurrencia en las transacciones."),
#             ("b", "Asegura que una transacción sea completamente reversible."),
#             ("c", "Previene errores en la integridad referencial."),
#             ("d", "Permite realizar solo operaciones de consulta."),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "ACID",
#         "enunciado": "¿Cuál de las siguientes afirma algo incorrecto sobre las propiedades ACID?",
#         "opciones": [
#             ("a", "La consistencia asegura que cada transacción mantenga un estado válido."),
#             ("b", "El aislamiento permite que las transacciones se ejecuten simultáneamente sin interferir."),
#             ("c", "La durabilidad garantiza que los cambios de una transacción se mantengan después de un fallo."),
#             ("d", "La atomicidad asegura que una transacción pueda ejecutarse parcialmente."),
#         ],
#         "correcta": "d"
#     },
#     {
#         "tipo": "ACID",
#         "enunciado": "¿Qué propiedad ACID es especialmente importante en un sistema que maneja múltiples usuarios?",
#         "opciones": [
#             ("a", "Atomicidad"),
#             ("b", "Aislamiento"),
#             ("c", "Durabilidad"),
#             ("d", "Consistencia"),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "ACID",
#         "enunciado": "¿Qué aspecto de ACID asegura que una base de datos nunca quede en un estado inválido después de una transacción?",
#         "opciones": [
#             ("a", "Atomicidad"),
#             ("b", "Aislamiento"),
#             ("c", "Consistencia"),
#             ("d", "Durabilidad"),
#         ],
#         "correcta": "c"
#     },
#     {
#         "tipo": "modelo_er",
#         "enunciado": "En el modelo E-R, ¿qué representa un rectángulo?",
#         "opciones": [
#             ("a", "Una entidad"),
#             ("b", "Un atributo"),
#             ("c", "Una relación"),
#             ("d", "Una superllave"),
#         ],
#         "correcta": "a"
#     },
#     {
#         "tipo": "modelo_er",
#         "enunciado": "¿Qué símbolo se utiliza para representar una relación en un diagrama E-R?",
#         "opciones": [
#             ("a", "Rectángulo"),
#             ("b", "Círculo"),
#             ("c", "Rombo"),
#             ("d", "Elipse"),
#         ],
#         "correcta": "c"
#     },
#     {
#         "tipo": "modelo_er",
#         "enunciado": "En un diagrama E-R, ¿qué representa un elipse?",
#         "opciones": [
#             ("a", "Un atributo"),
#             ("b", "Una entidad"),
#             ("c", "Una relación"),
#             ("d", "Una clave primaria"),
#         ],
#         "correcta": "a"
#     },
#     {
#         "tipo": "modelo_er",
#         "enunciado": "¿Cómo se llama el atributo que identifica de manera única a cada entidad en una tabla?",
#         "opciones": [
#             ("a", "Atributo derivado"),
#             ("b", "Clave foránea"),
#             ("c", "Clave primaria"),
#             ("d", "Atributo compuesto"),
#         ],
#         "correcta": "c"
#     },
#     {
#         "tipo": "modelo_er",
#         "enunciado": "¿Qué tipo de relación describe una conexión entre una entidad y sí misma?",
#         "opciones": [
#             ("a", "Relación binaria"),
#             ("b", "Relación unaria"),
#             ("c", "Relación ternaria"),
#             ("d", "Relación secundaria"),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "modelo_er",
#         "enunciado": "¿Cuál es el propósito principal de un diagrama E-R?",
#         "opciones": [
#             ("a", "Describir el flujo de datos en un sistema."),
#             ("b", "Identificar claves primarias y foráneas."),
#             ("c", "Representar visualmente las entidades y relaciones en una base de datos."),
#             ("d", "Diseñar la interfaz de usuario de una aplicación de base de datos."),
#         ],
#         "correcta": "c"
#     },
#     {
#         "tipo": "modelo_er",
#         "enunciado": "¿Qué tipo de relación se representa entre dos entidades en un diagrama E-R?",
#         "opciones": [
#             ("a", "Relación de uno a uno (1:1)"),
#             ("b", "Relación de muchos a uno (M:1)"),
#             ("c", "Relación de uno a muchos (1:M)"),
#             ("d", "Todas las anteriores"),
#         ],
#         "correcta": "d"
#     },
#     {
#         "tipo": "modelo_er",
#         "enunciado": "¿Cómo se representa una relación de muchos a muchos (M:N) en un diagrama E-R?",
#         "opciones": [
#             ("a", "Mediante una sola línea entre dos entidades"),
#             ("b", "Con un rombo conectado a ambas entidades con líneas de cardinalidad M:N"),
#             ("c", "Con un círculo alrededor de ambas entidades"),
#             ("d", "Con un atributo compuesto entre las entidades"),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "modelo_er",
#         "enunciado": "¿Cuál de los siguientes NO es un componente básico de un diagrama E-R?",
#         "opciones": [
#             ("a", "Entidad"),
#             ("b", "Relación"),
#             ("c", "Proceso"),
#             ("d", "Atributo"),
#         ],
#         "correcta": "c"
#     },
#     {
#         "tipo": "modelo_er",
#         "enunciado": "En un diagrama E-R, ¿cómo se indica una clave primaria en un atributo?",
#         "opciones": [
#             ("a", "Con un subrayado"),
#             ("b", "Con un círculo alrededor"),
#             ("c", "Con un asterisco al final"),
#             ("d", "Con un color diferente"),
#         ],
#         "correcta": "a"
#     },
#     {
#         "tipo": "modelo_er",
#         "enunciado": "¿Qué tipo de atributo se calcula a partir de otros atributos en el modelo E-R?",
#         "opciones": [
#             ("a", "Atributo simple"),
#             ("b", "Atributo derivado"),
#             ("c", "Atributo compuesto"),
#             ("d", "Atributo multi-valorado"),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "modelo_er",
#         "enunciado": "¿Qué tipo de relación en un diagrama E-R conecta tres entidades?",
#         "opciones": [
#             ("a", "Relación binaria"),
#             ("b", "Relación unaria"),
#             ("c", "Relación ternaria"),
#             ("d", "Relación de composición"),
#         ],
#         "correcta": "c"
#     },
#     {
#         "tipo": "modelo_er",
#         "enunciado": "¿Qué se entiende por cardinalidad en un diagrama E-R?",
#         "opciones": [
#             ("a", "El número de atributos de una entidad"),
#             ("b", "El número de relaciones posibles entre dos entidades"),
#             ("c", "La cantidad de tablas en la base de datos"),
#             ("d", "La jerarquía entre entidades"),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "modelo_er",
#         "enunciado": "¿Cuál es el propósito de un atributo multi-valorado en un diagrama E-R?",
#         "opciones": [
#             ("a", "Almacenar múltiples valores para una sola entidad"),
#             ("b", "Permitir cálculos derivados de otros atributos"),
#             ("c", "Representar claves foráneas en la entidad"),
#             ("d", "Relacionar la entidad con sí misma"),
#         ],
#         "correcta": "a"
#     },
#     {
#         "tipo": "modelo_er",
#         "enunciado": "En el modelo E-R, una entidad débil se identifica porque:",
#         "opciones": [
#             ("a", "No tiene atributos propios."),
#             ("b", "Depende de una entidad fuerte para su existencia."),
#             ("c", "No puede tener relaciones con otras entidades."),
#             ("d", "Es siempre una clave primaria."),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "normalizacion",
#         "enunciado": "¿Cuál es el propósito principal de la normalización en una base de datos?",
#         "opciones": [
#             ("a", "Reducir la redundancia de datos y mejorar la integridad de los datos."),
#             ("b", "Permitir la duplicación de datos para mejorar la velocidad de consulta."),
#             ("c", "Incrementar el número de tablas en la base de datos."),
#             ("d", "Eliminar las relaciones entre tablas para simplificar el diseño."),
#         ],
#         "correcta": "a"
#     },
#     {
#         "tipo": "normalizacion",
#         "enunciado": "¿Qué se logra al aplicar la primera forma normal (1NF)?",
#         "opciones": [
#             ("a", "Eliminar los datos duplicados."),
#             ("b", "Eliminar los atributos multi-valorados."),
#             ("c", "Asegurar que cada columna contenga valores únicos."),
#             ("d", "Reducir las dependencias funcionales."),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "normalizacion",
#         "enunciado": "Para cumplir con la segunda forma normal (2NF), ¿qué debe eliminarse de la tabla?",
#         "opciones": [
#             ("a", "Las dependencias de clave compuesta."),
#             ("b", "Las dependencias parciales."),
#             ("c", "Los atributos redundantes."),
#             ("d", "Las dependencias transitivas."),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "normalizacion",
#         "enunciado": "¿Cuál es la característica principal de una tabla en tercera forma normal (3NF)?",
#         "opciones": [
#             ("a", "Elimina todas las dependencias transitivas."),
#             ("b", "No tiene dependencias parciales."),
#             ("c", "No tiene dependencias funcionales."),
#             ("d", "Permite datos multi-valorados."),
#         ],
#         "correcta": "a"
#     },
#     {
#         "tipo": "normalizacion",
#         "enunciado": "¿Qué tipo de dependencias elimina la forma normal Boyce-Codd (BCNF)?",
#         "opciones": [
#             ("a", "Dependencias parciales."),
#             ("b", "Dependencias transitivas."),
#             ("c", "Dependencias de superclave."),
#             ("d", "Dependencias funcionales que no son de clave."),
#         ],
#         "correcta": "d"
#     },
#     {
#         "tipo": "normalizacion",
#         "enunciado": "¿Qué es una dependencia transitoria en una base de datos?",
#         "opciones": [
#             ("a", "Cuando un atributo depende de otro que no es clave primaria."),
#             ("b", "Cuando un atributo depende de una combinación de atributos."),
#             ("c", "Cuando un atributo depende directamente de la clave primaria."),
#             ("d", "Cuando un atributo depende de un atributo no clave a través de otro atributo."),
#         ],
#         "correcta": "d"
#     },
#     {
#         "tipo": "normalizacion",
#         "enunciado": "¿Cuál de las siguientes afirmaciones es verdadera sobre la cuarta forma normal (4NF)?",
#         "opciones": [
#             ("a", "4NF elimina las dependencias multi-valoradas."),
#             ("b", "4NF es lo mismo que 3NF."),
#             ("c", "4NF elimina las dependencias transitivas."),
#             ("d", "4NF asegura que no haya dependencias de clave externa."),
#         ],
#         "correcta": "a"
#     },
#     {
#         "tipo": "normalizacion",
#         "enunciado": "¿Qué forma normal se enfoca en eliminar las dependencias multi-valoradas?",
#         "opciones": [
#             ("a", "1NF"),
#             ("b", "2NF"),
#             ("c", "3NF"),
#             ("d", "4NF"),
#         ],
#         "correcta": "d"
#     },
#     {
#         "tipo": "normalizacion",
#         "enunciado": "Para que una tabla esté en 2NF, ¿cuál de las siguientes condiciones debe cumplirse?",
#         "opciones": [
#             ("a", "Debe estar en 1NF y no tener dependencias parciales."),
#             ("b", "Debe estar en 1NF y no tener dependencias transitivas."),
#             ("c", "Debe estar en BCNF y no tener dependencias parciales."),
#             ("d", "Debe estar en 3NF y no tener dependencias multi-valoradas."),
#         ],
#         "correcta": "a"
#     },
#     {
#         "tipo": "normalizacion",
#         "enunciado": "¿Qué se elimina en la tercera forma normal (3NF) que no se elimina en la segunda forma normal (2NF)?",
#         "opciones": [
#             ("a", "Dependencias multi-valoradas"),
#             ("b", "Dependencias parciales"),
#             ("c", "Dependencias transitivas"),
#             ("d", "Atributos compuestos"),
#         ],
#         "correcta": "c"
#     },
#     {
#         "tipo": "normalizacion",
#         "enunciado": "¿Cuál de las siguientes afirmaciones es correcta sobre la forma normal BCNF?",
#         "opciones": [
#             ("a", "BCNF es una versión más estricta de 2NF."),
#             ("b", "BCNF es una versión más estricta de 3NF."),
#             ("c", "BCNF solo se aplica a tablas con una clave primaria simple."),
#             ("d", "BCNF elimina todas las dependencias de clave externa."),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "normalizacion",
#         "enunciado": "¿Qué es una dependencia parcial en el contexto de la normalización?",
#         "opciones": [
#             ("a", "Cuando un atributo depende de una parte de una clave compuesta."),
#             ("b", "Cuando un atributo depende de otro atributo que no es clave."),
#             ("c", "Cuando un atributo depende de múltiples claves primarias."),
#             ("d", "Cuando un atributo depende de una clave primaria simple."),
#         ],
#         "correcta": "a"
#     },
#     {
#         "tipo": "normalizacion",
#         "enunciado": "Si una tabla está en BCNF, ¿cuáles de las siguientes formas normales ha alcanzado también?",
#         "opciones": [
#             ("a", "1NF y 2NF solamente"),
#             ("b", "1NF, 2NF y 3NF"),
#             ("c", "2NF y 3NF solamente"),
#             ("d", "1NF y BCNF solamente"),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "normalizacion",
#         "enunciado": "¿Qué hace que una tabla esté en quinta forma normal (5NF)?",
#         "opciones": [
#             ("a", "Elimina dependencias transitivas."),
#             ("b", "Elimina todas las dependencias parciales."),
#             ("c", "Elimina dependencias de unión complejas."),
#             ("d", "Elimina dependencias multi-valoradas."),
#         ],
#         "correcta": "c"
#     },
#     {
#         "tipo": "normalizacion",
#         "enunciado": "¿Cuál de las siguientes es una razón para no aplicar la normalización hasta 4NF o 5NF?",
#         "opciones": [
#             ("a", "Es posible que se incrementen las consultas complejas debido a la fragmentación de tablas."),
#             ("b", "Aumenta la redundancia de datos en las tablas."),
#             ("c", "Reduce la consistencia de los datos almacenados."),
#             ("d", "Permite más datos duplicados en el sistema."),
#         ],
#         "correcta": "a"
#     },
#     {
#         "tipo": "normalizacion",
#         "enunciado": "¿Cuál de las siguientes tablas está en 3NF pero NO en BCNF? La clave primaria es (A, B).",
#         "opciones": [
#             ("a", """
#             | A  | B  | C  |
#             |----|----|----|
#             | a1 | b1 | c1 |
#             | a2 | b1 | c2 |
#             """),
#             ("b", """
#             | A  | B  | C  |
#             |----|----|----|
#             | a1 | b1 | c1 |
#             | a1 | b2 | c2 |
#             """),
#             ("c", """
#             | A  | B  | C  |
#             |----|----|----|
#             | a1 | b1 | c1 |
#             | a1 | b1 | c2 |
#             """),
#             ("d", """
#             | A  | B  | C  |
#             |----|----|----|
#             | a1 | b1 | c1 |
#             | a2 | b2 | c2 |
#             """),
#         ],
#         "correcta": "c"
#     },
#     {
#         "tipo": "normalizacion",
#         "enunciado": "Una tabla está en BCNF si:",
#         "opciones": [
#             ("a", "Está en 1NF y 2NF"),
#             ("b", "No contiene dependencias transitivas"),
#             ("c", "Cada dependencia funcional en la tabla es una dependencia de superclave"),
#             ("d", "Cada dependencia funcional en la tabla es una dependencia parcial"),
#         ],
#         "correcta": "c"
#     },
#     {
#         "tipo": "normalizacion",
#         "enunciado": "Dada la tabla siguiente, ¿en qué forma normal se encuentra? La clave primaria es (A, B).\n\n"
#                     "| A  | B  | C  | D  |\n"
#                     "|----|----|----|----|\n"
#                     "| a1 | b1 | c1 | d1 |\n"
#                     "| a1 | b2 | c2 | d1 |\n"
#                     "Dependencias: A &#8594; D, B &#8594; C.",
#         "opciones": [
#             ("a", "1NF"),
#             ("b", "2NF"),
#             ("c", "3NF"),
#             ("d", "BCNF"),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "normalizacion",
#         "enunciado": "En una tabla con clave primaria (X, Y), ¿cuál de las siguientes dependencias funcionales haría que la tabla esté en 3NF pero no en BCNF?",
#         "opciones": [
#             ("a", "X &#8594; Z"),
#             ("b", "Y &#8594; Z"),
#             ("c", "X, Y &#8594; Z"),
#             ("d", "Z &#8594; Y"),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "normalizacion",
#         "enunciado": "¿Cuál es una de las principales diferencias entre 3NF y BCNF?",
#         "opciones": [
#             ("a", "3NF elimina todas las dependencias transitivas, mientras que BCNF elimina todas las dependencias parciales."),
#             ("b", "3NF permite algunas dependencias funcionales que BCNF no permite."),
#             ("c", "3NF elimina todas las dependencias parciales, mientras que BCNF permite dependencias transitivas."),
#             ("d", "BCNF y 3NF son equivalentes en todos los casos."),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "normalizacion",
#         "enunciado": "Observa la tabla siguiente. ¿Está en BCNF?\n\n"
#                     "| A  | B  | C  |\n"
#                     "|----|----|----|\n"
#                     "| a1 | b1 | c1 |\n"
#                     "| a2 | b1 | c2 |\n"
#                     "| a3 | b2 | c1 |\n"
#                     "Dependencias: A &#8594; C, B &#8594; C.",
#         "opciones": [
#             ("a", "Sí, está en BCNF."),
#             ("b", "No, tiene dependencias que no son de superclave."),
#             ("c", "Sí, porque no tiene dependencias transitivas."),
#             ("d", "No, porque A y B no forman una clave compuesta."),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "normalizacion",
#         "enunciado": "Dada la siguiente tabla y dependencias, ¿qué forma normal se cumple? Clave primaria: (X, Y)\n\n"
#                     "| X  | Y  | Z  |\n"
#                     "|----|----|----|\n"
#                     "| x1 | y1 | z1 |\n"
#                     "| x1 | y2 | z1 |\n"
#                     "Dependencias: X &#8594; Z.",
#         "opciones": [
#             ("a", "1NF"),
#             ("b", "2NF"),
#             ("c", "3NF"),
#             ("d", "BCNF"),
#         ],
#         "correcta": "c"
#     },
#     {
#         "tipo": "normalizacion",
#         "enunciado": "¿Cuál de las siguientes condiciones es necesaria para que una tabla esté en BCNF?",
#         "opciones": [
#             ("a", "Cada dependencia funcional involucra una clave primaria completa."),
#             ("b", "No tiene dependencias transitivas."),
#             ("c", "No tiene dependencias parciales."),
#             ("d", "Cada dependencia funcional no trivial tiene una superclave como determinante."),
#         ],
#         "correcta": "d"
#     },
#     {
#         "tipo": "normalizacion",
#         "enunciado": "¿Cuál de las siguientes afirmaciones es correcta sobre BCNF y 3NF?",
#         "opciones": [
#             ("a", "Todas las tablas en 3NF están también en BCNF."),
#             ("b", "BCNF elimina dependencias de claves externas, mientras que 3NF no."),
#             ("c", "Todas las tablas en BCNF están en 3NF, pero no todas las tablas en 3NF están en BCNF."),
#             ("d", "BCNF y 3NF eliminan únicamente dependencias multi-valoradas."),
#         ],
#         "correcta": "c"
#     },
#     {
#         "tipo": "normalizacion",
#         "enunciado": "Dada la tabla siguiente, ¿qué forma normal se cumple?\n\n"
#                     "| A  | B  | C  | D  |\n"
#                     "|----|----|----|----|\n"
#                     "| a1 | b1 | c1 | d1 |\n"
#                     "| a2 | b1 | c2 | d1 |\n"
#                     "Clave primaria: (A, B). Dependencias: A &#8594; D, B &#8594; C.",
#         "opciones": [
#             ("a", "1NF"),
#             ("b", "2NF"),
#             ("c", "3NF"),
#             ("d", "BCNF"),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "normalizacion",
#         "enunciado": "Si una tabla en BCNF tiene una dependencia funcional de un atributo no clave, ¿qué acción se debería tomar?",
#         "opciones": [
#             ("a", "Eliminar el atributo no clave."),
#             ("b", "Dividir la tabla en dos para eliminar la dependencia."),
#             ("c", "Renombrar el atributo para que sea una clave secundaria."),
#             ("d", "Eliminar la clave primaria."),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "normalizacion",
#         "enunciado": "¿Qué situación en una tabla significa que cumple con 3NF pero no con BCNF?",
#         "opciones": [
#             ("a", "Tiene dependencias parciales de la clave primaria."),
#             ("b", "Contiene dependencias transitivas."),
#             ("c", "Tiene una dependencia funcional en la que el determinante no es una superclave."),
#             ("d", "Cumple con todas las dependencias funcionales."),
#         ],
#         "correcta": "c"
#     },
#     {
#         "tipo": "normalizacion",
#         "enunciado": "Dada una tabla que contiene la clave compuesta (X, Y), si la dependencia funcional X &#8594; Z existe, ¿en qué forma normal está?",
#         "opciones": [
#             ("a", "1NF"),
#             ("b", "2NF"),
#             ("c", "3NF"),
#             ("d", "No puede estar en 3NF debido a una dependencia parcial."),
#         ],
#         "correcta": "d"
#     },
#     {
#         "tipo": "normalizacion",
#         "enunciado": "Observa la tabla siguiente. ¿Está en BCNF?\n\n"
#                     "| X  | Y  | Z  |\n"
#                     "|----|----|----|\n"
#                     "| x1 | y1 | z1 |\n"
#                     "| x2 | y1 | z2 |\n"
#                     "Dependencias: Y &#8594; Z.",
#         "opciones": [
#             ("a", "Sí, porque cumple con 1NF."),
#             ("b", "No, porque Y no es una superclave y depende de Z."),
#             ("c", "Sí, porque todas las dependencias funcionales son de superclave."),
#             ("d", "No, porque contiene una dependencia parcial."),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "normalizacion",
#         "enunciado": "¿Cuál es la principal diferencia entre BCNF y 3NF en la normalización?",
#         "opciones": [
#             ("a", "BCNF solo aplica a dependencias transitivas."),
#             ("b", "3NF elimina dependencias parciales, BCNF elimina dependencias no triviales de clave."),
#             ("c", "BCNF aplica solo a tablas sin claves compuestas."),
#             ("d", "BCNF es más estricta en cuanto a dependencias funcionales de superclave."),
#         ],
#         "correcta": "d"
#     },
#     {
#         "tipo": "normalizacion",
#         "enunciado": "En una tabla con clave primaria (P, Q), ¿qué dependencia funcional violaría la forma normal BCNF?",
#         "opciones": [
#             ("a", "P &#8594; R"),
#             ("b", "Q &#8594; R"),
#             ("c", "P, Q &#8594; R"),
#             ("d", "R &#8594; Q"),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "dependencias_funcionales",
#         "enunciado": "¿Qué significa que exista una dependencia funcional A &#8594; B en una tabla?",
#         "opciones": [
#             ("a", "B determina el valor de A."),
#             ("b", "Para cada valor de A, existe un valor único de B."),
#             ("c", "A y B son claves candidatas."),
#             ("d", "A y B son independientes."),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "dependencias_funcionales",
#         "enunciado": "Si existe una dependencia funcional A &#8594; B y una dependencia funcional B &#8594; C, ¿qué se puede decir sobre A &#8594; C?",
#         "opciones": [
#             ("a", "A &#8594; C es una dependencia transitiva."),
#             ("b", "A &#8594; C no es una dependencia funcional válida."),
#             ("c", "A &#8594; C es una dependencia parcial."),
#             ("d", "A &#8594; C es una dependencia multi-valorada."),
#         ],
#         "correcta": "a"
#     },
#     {
#         "tipo": "dependencias_funcionales",
#         "enunciado": "En una tabla, si X &#8594; Y y Y &#8594; X, ¿qué se puede concluir sobre X e Y?",
#         "opciones": [
#             ("a", "X e Y son mutuamente excluyentes."),
#             ("b", "X e Y son determinantes mutuos."),
#             ("c", "X e Y son equivalentes en la tabla."),
#             ("d", "X e Y no tienen relación."),
#         ],
#         "correcta": "c"
#     },
#     {
#         "tipo": "dependencias_funcionales",
#         "enunciado": "En la tabla siguiente, ¿cuál es una dependencia funcional?\n\n"
#                     "| A  | B  | C  |\n"
#                     "|----|----|----|\n"
#                     "| a1 | b1 | c1 |\n"
#                     "| a2 | b1 | c2 |\n"
#                     "| a3 | b2 | c3 |\n",
#         "opciones": [
#             ("a", "A &#8594; B"),
#             ("b", "B &#8594; C"),
#             ("c", "A &#8594; C"),
#             ("d", "C &#8594; A"),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "dependencias_funcionales",
#         "enunciado": "Si una clave compuesta (A, B) determina C, ¿cómo se clasifica la dependencia funcional?",
#         "opciones": [
#             ("a", "Dependencia parcial"),
#             ("b", "Dependencia compuesta"),
#             ("c", "Dependencia funcional completa"),
#             ("d", "Dependencia transitiva"),
#         ],
#         "correcta": "c"
#     },
#     {
#         "tipo": "dependencias_funcionales",
#         "enunciado": "En una tabla con clave primaria (X, Y), si existe una dependencia X &#8594; Z, ¿qué se puede inferir?",
#         "opciones": [
#             ("a", "Es una dependencia funcional completa."),
#             ("b", "Es una dependencia parcial."),
#             ("c", "Es una dependencia transitiva."),
#             ("d", "Es una dependencia multi-valorada."),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "dependencias_funcionales",
#         "enunciado": "Dada una tabla con dependencias A &#8594; B y B &#8594; C, ¿cuál de las siguientes es una dependencia transitiva?",
#         "opciones": [
#             ("a", "A &#8594; C"),
#             ("b", "B &#8594; A"),
#             ("c", "C &#8594; A"),
#             ("d", "A &#8594; B"),
#         ],
#         "correcta": "a"
#     },
#     {
#         "tipo": "dependencias_funcionales",
#         "enunciado": "Si un atributo depende funcionalmente de un conjunto de atributos que no es la clave completa, ¿cómo se clasifica esta dependencia?",
#         "opciones": [
#             ("a", "Dependencia multi-valorada"),
#             ("b", "Dependencia parcial"),
#             ("c", "Dependencia transitiva"),
#             ("d", "Dependencia trivial"),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "dependencias_funcionales",
#         "enunciado": "¿Qué tipo de dependencia funcional existe si para cada valor de un atributo A, existen múltiples valores de un atributo B?",
#         "opciones": [
#             ("a", "Dependencia funcional"),
#             ("b", "Dependencia transitiva"),
#             ("c", "Dependencia multi-valorada"),
#             ("d", "Dependencia parcial"),
#         ],
#         "correcta": "c"
#     },
#     {
#         "tipo": "dependencias_funcionales",
#         "enunciado": "¿Cuál de las siguientes NO es una dependencia funcional en la tabla siguiente?\n\n"
#                     "| X  | Y  | Z  |\n"
#                     "|----|----|----|\n"
#                     "| x1 | y1 | z1 |\n"
#                     "| x1 | y1 | z2 |\n"
#                     "| x2 | y2 | z1 |\n",
#         "opciones": [
#             ("a", "X &#8594; Y"),
#             ("b", "Y &#8594; Z"),
#             ("c", "X &#8594; Z"),
#             ("d", "Z &#8594; X"),
#         ],
#         "correcta": "c"
#     },
#     {
#         "tipo": "dependencias_funcionales",
#         "enunciado": "En una tabla con clave primaria compuesta (P, Q), ¿qué indica que P &#8594; R sea una dependencia funcional?",
#         "opciones": [
#             ("a", "Es una dependencia completa de la clave primaria."),
#             ("b", "Es una dependencia parcial de la clave primaria."),
#             ("c", "Es una dependencia transitiva."),
#             ("d", "Es una dependencia multi-valorada."),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "dependencias_funcionales",
#         "enunciado": "Dada la tabla siguiente, ¿cuál es la dependencia funcional más probable?\n\n"
#                     "| A  | B  | C  |\n"
#                     "|----|----|----|\n"
#                     "| a1 | b1 | c1 |\n"
#                     "| a2 | b1 | c2 |\n"
#                     "| a2 | b2 | c3 |\n",
#         "opciones": [
#             ("a", "A &#8594; B"),
#             ("b", "B &#8594; A"),
#             ("c", "A &#8594; C"),
#             ("d", "C &#8594; A"),
#         ],
#         "correcta": "a"
#     },
#     {
#         "tipo": "dependencias_funcionales",
#         "enunciado": "Si una tabla tiene clave primaria compuesta (A, B) y existe una dependencia B &#8594; C, ¿qué indica esto sobre la tabla?",
#         "opciones": [
#             ("a", "Está en 2NF pero no en 3NF."),
#             ("b", "Cumple con BCNF."),
#             ("c", "Está en 3NF pero no en BCNF."),
#             ("d", "Cumple con 1NF pero no con 2NF."),
#         ],
#         "correcta": "a"
#     },
#     {
#         "tipo": "dependencias_funcionales",
#         "enunciado": "En una tabla donde se cumple X &#8594; Y y Y &#8594; Z, ¿qué se puede inferir sobre X y Z?",
#         "opciones": [
#             ("a", "X y Z son mutuamente dependientes."),
#             ("b", "X &#8594; Z es una dependencia transitiva."),
#             ("c", "Z &#8594; X también debe cumplirse."),
#             ("d", "X y Z son determinantes mutuos."),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "dependencias_funcionales",
#         "enunciado": "¿Cuál de las siguientes opciones describe correctamente una dependencia funcional trivial?",
#         "opciones": [
#             ("a", "Una dependencia en la que el atributo de la derecha es un subconjunto del de la izquierda."),
#             ("b", "Una dependencia en la que el atributo de la izquierda depende de un atributo externo."),
#             ("c", "Una dependencia que solo involucra la clave primaria."),
#             ("d", "Una dependencia multi-valorada entre dos atributos."),
#         ],
#         "correcta": "a"
#     },
#     {
#         "tipo": "llaves_candidatas",
#         "enunciado": "¿Qué es una llave candidata en una tabla de base de datos?",
#         "opciones": [
#             ("a", "Un atributo que puede contener valores duplicados."),
#             ("b", "Un atributo o conjunto de atributos que puede identificar de forma única una fila."),
#             ("c", "Una combinación de todas las columnas de una tabla."),
#             ("d", "Una clave primaria secundaria."),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "llaves_candidatas",
#         "enunciado": "¿Cuál de las siguientes es siempre una superllave en una tabla?",
#         "opciones": [
#             ("a", "La clave primaria"),
#             ("b", "Cualquier columna única"),
#             ("c", "Una combinación de atributos que contiene la clave primaria"),
#             ("d", "Un atributo único en la tabla"),
#         ],
#         "correcta": "c"
#     },
#     {
#         "tipo": "llaves_candidatas",
#         "enunciado": "Dada una tabla con las columnas A, B y C, y la clave primaria (A, B), ¿cuál de las siguientes es una superllave?",
#         "opciones": [
#             ("a", "A"),
#             ("b", "(A, B)"),
#             ("c", "(A, C)"),
#             ("d", "(B, C)"),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "llaves_candidatas",
#         "enunciado": "¿Qué característica debe cumplir una llave candidata?",
#         "opciones": [
#             ("a", "Debe ser una combinación de todas las columnas."),
#             ("b", "Debe ser única y minimal, sin atributos extra."),
#             ("c", "Debe incluir atributos multi-valorados."),
#             ("d", "Debe depender funcionalmente de la clave primaria."),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "llaves_candidatas",
#         "enunciado": "¿Cuál de las siguientes afirmaciones es correcta sobre superllaves?",
#         "opciones": [
#             ("a", "Cada superllave contiene al menos una llave candidata."),
#             ("b", "Una superllave no puede contener ninguna llave candidata."),
#             ("c", "Cada llave candidata contiene varias superllaves."),
#             ("d", "Las superllaves no incluyen la clave primaria."),
#         ],
#         "correcta": "a"
#     },
#     {
#         "tipo": "llaves_candidatas",
#         "enunciado": "¿Qué diferencia hay entre una llave candidata y una superllave?",
#         "opciones": [
#             ("a", "Una superllave siempre es minimal, una llave candidata no."),
#             ("b", "Una llave candidata es minimal y única, una superllave puede tener atributos adicionales."),
#             ("c", "Una llave candidata no puede usarse como clave primaria."),
#             ("d", "No hay diferencia entre una llave candidata y una superllave."),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "llaves_candidatas",
#         "enunciado": "Dada la tabla siguiente, ¿cuál es una llave candidata?\n\n"
#                     "| A  | B  | C  |\n"
#                     "|----|----|----|\n"
#                     "| a1 | b1 | c1 |\n"
#                     "| a2 | b2 | c2 |\n"
#                     "Dependencias: A &#8594; B, C &#8594; A.",
#         "opciones": [
#             ("a", "A"),
#             ("b", "B"),
#             ("c", "C"),
#             ("d", "(A, B)"),
#         ],
#         "correcta": "c"
#     },
#     {
#         "tipo": "llaves_candidatas",
#         "enunciado": "En una tabla con clave primaria (X, Y), ¿cuál de las siguientes combinaciones es también una superllave?",
#         "opciones": [
#             ("a", "(X, Y, Z)"),
#             ("b", "(Y, Z)"),
#             ("c", "Z"),
#             ("d", "(X, Z)"),
#         ],
#         "correcta": "a"
#     },
#     {
#         "tipo": "llaves_candidatas",
#         "enunciado": "Si una tabla tiene una única llave candidata, ¿qué puedes inferir sobre las superllaves?",
#         "opciones": [
#             ("a", "No hay superllaves adicionales."),
#             ("b", "La llave candidata es también la única superllave minimal."),
#             ("c", "Todas las combinaciones de atributos son superllaves."),
#             ("d", "Solo los atributos de la clave primaria pueden formar superllaves."),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "llaves_candidatas",
#         "enunciado": "Dada una tabla con las columnas A, B y C, y la clave primaria A, ¿cuál de las siguientes es una superllave pero no una llave candidata?",
#         "opciones": [
#             ("a", "A"),
#             ("b", "(A, B)"),
#             ("c", "B"),
#             ("d", "(A, C)"),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "llaves_candidatas",
#         "enunciado": "Si una tabla tiene clave primaria (P, Q), ¿cuál de las siguientes combinaciones es una llave candidata adicional?",
#         "opciones": [
#             ("a", "(P, Q)"),
#             ("b", "P"),
#             ("c", "(Q, R)"),
#             ("d", "(P, Q, R)"),
#         ],
#         "correcta": "a"
#     },
#     {
#         "tipo": "llaves_candidatas",
#         "enunciado": "¿Cuál de las siguientes opciones es siempre verdadera para una llave candidata?",
#         "opciones": [
#             ("a", "Debe ser una superllave y minimal."),
#             ("b", "Debe ser única pero no necesariamente minimal."),
#             ("c", "No puede usarse como clave primaria."),
#             ("d", "Siempre contiene todos los atributos de la tabla."),
#         ],
#         "correcta": "a"
#     },
#     {
#         "tipo": "llaves_candidatas",
#         "enunciado": "En una tabla con clave primaria A, ¿cuál de las siguientes opciones representa una superllave?",
#         "opciones": [
#             ("a", "A"),
#             ("b", "(A, B)"),
#             ("c", "B"),
#             ("d", "Ninguna de las anteriores"),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "llaves_candidatas",
#         "enunciado": "En una tabla, una superllave se caracteriza porque:",
#         "opciones": [
#             ("a", "Identifica de forma única cada fila y puede contener atributos adicionales."),
#             ("b", "Es siempre una combinación minimal de atributos."),
#             ("c", "No puede incluir la clave primaria."),
#             ("d", "No debe ser única en la tabla."),
#         ],
#         "correcta": "a"
#     },
#     {
#         "tipo": "llaves_candidatas",
#         "enunciado": "En una tabla con los atributos X, Y y Z, ¿cuál de las siguientes combinaciones sería una superllave si X es la clave primaria?",
#         "opciones": [
#             ("a", "(X, Y)"),
#             ("b", "Y"),
#             ("c", "Z"),
#             ("d", "(X, Z)"),
#         ],
#         "correcta": "a"
#     },
#     {
#         "tipo": "diseno_bd",
#         "enunciado": "¿Cuál de las siguientes es una característica de una arquitectura cliente-servidor en bases de datos?",
#         "opciones": [
#             ("a", "Los datos se almacenan en el cliente y se procesan en el servidor."),
#             ("b", "El cliente solicita y procesa datos, mientras el servidor gestiona el almacenamiento y acceso."),
#             ("c", "Todos los datos se almacenan y procesan exclusivamente en el cliente."),
#             ("d", "El cliente solo almacena datos, mientras que el servidor los procesa."),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "diseno_bd",
#         "enunciado": "En una arquitectura de base de datos distribuida, ¿qué ventaja ofrece sobre una centralizada?",
#         "opciones": [
#             ("a", "Mejor control de integridad en un único punto."),
#             ("b", "Mayor redundancia y resiliencia en múltiples ubicaciones."),
#             ("c", "Menor tiempo de respuesta debido a la centralización."),
#             ("d", "Mayor facilidad para realizar copias de seguridad en un único sitio."),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "diseno_bd",
#         "enunciado": "¿Cuál es la función de una base de datos replicada?",
#         "opciones": [
#             ("a", "Permitir que diferentes usuarios modifiquen el mismo registro simultáneamente."),
#             ("b", "Mantener copias idénticas de los datos en múltiples ubicaciones para redundancia y disponibilidad."),
#             ("c", "Dividir datos en fragmentos para almacenamiento distribuido."),
#             ("d", "Restringir el acceso a un único usuario a la vez."),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "diseno_bd",
#         "enunciado": "¿Qué es la fragmentación en bases de datos distribuidas?",
#         "opciones": [
#             ("a", "Dividir la base de datos en fragmentos para almacenarla en diferentes ubicaciones."),
#             ("b", "Replicar la misma base de datos en múltiples servidores."),
#             ("c", "Consolidar múltiples bases de datos en un solo servidor."),
#             ("d", "Segmentar las transacciones en pequeñas operaciones."),
#         ],
#         "correcta": "a"
#     },
#     {
#         "tipo": "diseno_bd",
#         "enunciado": "¿Cuál es la principal ventaja de la normalización en el diseño de una base de datos?",
#         "opciones": [
#             ("a", "Mejorar el rendimiento al duplicar los datos en varias tablas."),
#             ("b", "Reducir la redundancia de datos y mejorar la consistencia."),
#             ("c", "Aumentar la redundancia de datos para mejorar la recuperación."),
#             ("d", "Asegurar que todos los datos estén en un solo lugar."),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "diseno_bd",
#         "enunciado": "En un diseño de base de datos, ¿qué es una relación de 'uno a muchos'?",
#         "opciones": [
#             ("a", "Cada registro en una tabla está relacionado con un único registro en otra tabla."),
#             ("b", "Cada registro en una tabla está relacionado con múltiples registros en otra tabla."),
#             ("c", "Cada registro en una tabla tiene una relación bidireccional con varios registros."),
#             ("d", "Cada registro en una tabla está relacionado con múltiples registros de sí mismo."),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "diseno_bd",
#         "enunciado": "¿Qué es una base de datos NoSQL?",
#         "opciones": [
#             ("a", "Una base de datos que utiliza exclusivamente relaciones y claves foráneas."),
#             ("b", "Una base de datos que no utiliza el lenguaje SQL y almacena datos de forma no relacional."),
#             ("c", "Una base de datos solo para operaciones de lectura y escritura básica."),
#             ("d", "Una base de datos que solo permite operaciones transaccionales."),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "diseno_bd",
#         "enunciado": "En un sistema de bases de datos distribuidas, ¿qué es la fragmentación horizontal?",
#         "opciones": [
#             ("a", "Dividir los atributos de una tabla en diferentes ubicaciones."),
#             ("b", "Dividir las filas de una tabla en diferentes ubicaciones."),
#             ("c", "Replicar la misma tabla en múltiples ubicaciones."),
#             ("d", "Consolidar datos de diferentes tablas en una sola tabla."),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "diseno_bd",
#         "enunciado": "¿Cuál es un riesgo de una arquitectura de base de datos centralizada?",
#         "opciones": [
#             ("a", "Baja redundancia de datos."),
#             ("b", "Mayor tiempo de acceso debido a la fragmentación."),
#             ("c", "Complejidad en el control de integridad en múltiples ubicaciones."),
#             ("d", "Mayor dificultad en la administración de transacciones simultáneas."),
#         ],
#         "correcta": "a"
#     },
#     {
#         "tipo": "diseno_bd",
#         "enunciado": "¿Cuál es una ventaja de usar una arquitectura de base de datos orientada a microservicios?",
#         "opciones": [
#             ("a", "Permite que cada microservicio tenga su propia base de datos, mejorando la independencia y escalabilidad."),
#             ("b", "Aumenta la dependencia entre microservicios mediante una base de datos compartida."),
#             ("c", "Facilita la migración de datos a sistemas centralizados."),
#             ("d", "Reduce la complejidad del sistema al unificar todas las bases de datos."),
#         ],
#         "correcta": "a"
#     },
#     {
#         "tipo": "diseno_bd",
#         "enunciado": "En una base de datos distribuida, ¿qué significa la consistencia eventual?",
#         "opciones": [
#             ("a", "Todos los nodos siempre tienen los mismos datos en todo momento."),
#             ("b", "Los datos en los nodos pueden estar temporalmente desactualizados, pero finalmente se sincronizan."),
#             ("c", "Los datos se actualizan de forma sincrónica en todos los nodos."),
#             ("d", "Los datos solo están disponibles en un nodo principal."),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "diseno_bd",
#         "enunciado": "¿Qué enfoque de diseño de base de datos es ideal para aplicaciones que requieren alta disponibilidad y baja latencia?",
#         "opciones": [
#             ("a", "Base de datos centralizada."),
#             ("b", "Base de datos distribuida."),
#             ("c", "Base de datos orientada a archivos."),
#             ("d", "Base de datos transaccional."),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "diseno_bd",
#         "enunciado": "¿Qué tipo de diseño es preferible para manejar grandes volúmenes de datos no estructurados?",
#         "opciones": [
#             ("a", "Base de datos relacional."),
#             ("b", "Base de datos jerárquica."),
#             ("c", "Base de datos NoSQL."),
#             ("d", "Base de datos orientada a transacciones."),
#         ],
#         "correcta": "c"
#     },
#     {
#         "tipo": "diseno_bd",
#         "enunciado": "En una base de datos distribuida, ¿cuál es el principal desafío al replicar datos en múltiples ubicaciones?",
#         "opciones": [
#             ("a", "Asegurar la consistencia y resolución de conflictos entre réplicas."),
#             ("b", "Permitir la modificación simultánea de datos en todos los nodos."),
#             ("c", "Limitar el acceso a la base de datos solo al nodo principal."),
#             ("d", "Reducir el rendimiento general del sistema."),
#         ],
#         "correcta": "a"
#     },
#     {
#         "tipo": "diseno_bd",
#         "enunciado": "¿Cuál de las siguientes opciones describe mejor un sistema de base de datos OLAP?",
#         "opciones": [
#             ("a", "Optimizado para transacciones de lectura y escritura frecuentes."),
#             ("b", "Optimizado para análisis de grandes volúmenes de datos, como consultas complejas y reportes."),
#             ("c", "Diseñado exclusivamente para almacenar datos no estructurados."),
#             ("d", "Limitado a un solo tipo de transacción a la vez."),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "olap",
#         "enunciado": "¿Cuál es el propósito principal de un sistema OLAP?",
#         "opciones": [
#             ("a", "Facilitar transacciones de alta frecuencia y baja latencia."),
#             ("b", "Soportar consultas analíticas complejas para la toma de decisiones."),
#             ("c", "Gestionar y procesar datos no estructurados."),
#             ("d", "Proporcionar almacenamiento en la nube a gran escala."),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "olap",
#         "enunciado": "¿Qué es un cubo OLAP?",
#         "opciones": [
#             ("a", "Un contenedor de almacenamiento de datos no estructurados."),
#             ("b", "Una estructura de datos que permite el análisis multidimensional."),
#             ("c", "Un método de almacenamiento de datos en archivos planos."),
#             ("d", "Un sistema para gestionar transacciones concurrentes."),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "olap",
#         "enunciado": "¿Qué tipo de operaciones se suelen realizar en un cubo OLAP?",
#         "opciones": [
#             ("a", "Operaciones CRUD básicas"),
#             ("b", "Roll-up, Drill-down, Slice y Dice"),
#             ("c", "Actualización de registros en tiempo real"),
#             ("d", "Indexación y fragmentación de datos"),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "olap",
#         "enunciado": "¿Qué significa 'Roll-up' en el contexto de OLAP?",
#         "opciones": [
#             ("a", "Un proceso de agregar datos en un nivel superior de jerarquía."),
#             ("b", "Una operación para dividir los datos en múltiples dimensiones."),
#             ("c", "Una técnica para cambiar la orientación de los datos."),
#             ("d", "Un proceso para reducir el tamaño de los datos."),
#         ],
#         "correcta": "a"
#     },
#     {
#         "tipo": "olap",
#         "enunciado": "¿Cuál de las siguientes es una característica clave de los sistemas OLAP?",
#         "opciones": [
#             ("a", "Optimización para consultas transaccionales de alta frecuencia."),
#             ("b", "Capacidad de análisis multidimensional y consultas complejas."),
#             ("c", "Almacenamiento de datos en archivos no relacionales."),
#             ("d", "Facilidad para gestionar grandes volúmenes de datos no estructurados."),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "olap",
#         "enunciado": "En OLAP, ¿qué significa 'Drill-down'?",
#         "opciones": [
#             ("a", "Resumen de datos en un nivel más alto."),
#             ("b", "Navegar hacia un nivel más detallado de los datos."),
#             ("c", "Filtrar los datos para incluir solo ciertas dimensiones."),
#             ("d", "Cambiar la orientación de los datos para analizar otra dimensión."),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "olap",
#         "enunciado": "¿Cuál de los siguientes es un ejemplo de operación 'Slice' en un cubo OLAP?",
#         "opciones": [
#             ("a", "Agregar todos los datos en una dimensión."),
#             ("b", "Seleccionar un subconjunto de datos de una dimensión específica."),
#             ("c", "Navegar hacia niveles de datos más detallados."),
#             ("d", "Rotar el cubo para ver diferentes dimensiones."),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "olap",
#         "enunciado": "En un sistema OLAP, ¿qué permite la operación 'Dice'?",
#         "opciones": [
#             ("a", "Seleccionar un subconjunto de datos en varias dimensiones."),
#             ("b", "Filtrar los datos para incluir solo una dimensión específica."),
#             ("c", "Resumir datos a un nivel jerárquico superior."),
#             ("d", "Combinar datos de diferentes cubos OLAP."),
#         ],
#         "correcta": "a"
#     },
#     {
#         "tipo": "olap",
#         "enunciado": "¿Cuál de las siguientes opciones NO es una operación típica en OLAP?",
#         "opciones": [
#             ("a", "Roll-up"),
#             ("b", "Drill-down"),
#             ("c", "Replicación"),
#             ("d", "Slice"),
#         ],
#         "correcta": "c"
#     },
#     {
#         "tipo": "olap",
#         "enunciado": "¿Qué tipo de consultas suelen ser las más comunes en sistemas OLAP?",
#         "opciones": [
#             ("a", "Consultas de solo lectura y análisis de datos."),
#             ("b", "Actualización frecuente de registros."),
#             ("c", "Consultas para inserciones masivas de datos."),
#             ("d", "Consultas concurrentes de alta frecuencia."),
#         ],
#         "correcta": "a"
#     },
#     {
#         "tipo": "olap",
#         "enunciado": "¿Cuál de las siguientes opciones describe mejor un sistema OLTP en comparación con un sistema OLAP?",
#         "opciones": [
#             ("a", "Optimizado para consultas analíticas y reportes."),
#             ("b", "Optimizado para transacciones de alta frecuencia y actualizaciones concurrentes."),
#             ("c", "Diseñado exclusivamente para consultas de solo lectura."),
#             ("d", "Ideal para análisis de grandes volúmenes de datos."),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "olap",
#         "enunciado": "¿Qué significa el término 'tiempo de respuesta rápido' en un sistema OLAP?",
#         "opciones": [
#             ("a", "Las consultas se completan en menos de 1 segundo."),
#             ("b", "El sistema optimiza los datos para procesar consultas analíticas rápidamente."),
#             ("c", "El sistema solo permite consultas básicas sin análisis complejo."),
#             ("d", "El sistema actualiza los datos de forma inmediata."),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "olap",
#         "enunciado": "¿Qué modelo de almacenamiento suele utilizarse en OLAP para soportar análisis de grandes volúmenes de datos?",
#         "opciones": [
#             ("a", "Modelo relacional con tablas normalizadas."),
#             ("b", "Modelo multidimensional o en forma de cubo."),
#             ("c", "Modelo jerárquico basado en registros."),
#             ("d", "Modelo de grafo para redes de datos."),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "olap",
#         "enunciado": "¿Cuál es una ventaja de un sistema OLAP en comparación con un sistema OLTP?",
#         "opciones": [
#             ("a", "Mayor capacidad para manejar transacciones en tiempo real."),
#             ("b", "Soporte para consultas complejas y análisis multidimensional."),
#             ("c", "Actualización constante de registros en tiempo real."),
#             ("d", "Menor tiempo de respuesta en consultas concurrentes."),
#         ],
#         "correcta": "b"
#     },
#     {
#         "tipo": "olap",
#         "enunciado": "¿Qué arquitectura OLAP permite el procesamiento en un sistema centralizado de grandes volúmenes de datos?",
#         "opciones": [
#             ("a", "ROLAP (Relational OLAP)"),
#             ("b", "MOLAP (Multidimensional OLAP)"),
#             ("c", "HOLAP (Hybrid OLAP)"),
#             ("d", "EOLAP (Enterprise OLAP)"),
#         ],
#         "correcta": "a"
#     },
# ]

