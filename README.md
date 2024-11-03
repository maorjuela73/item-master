# Item Master

Este código implementa un modelo ORM (Object-Relational Mapping) usando SQLAlchemy para una base de datos SQLite que gestiona ítems de evaluación, opciones de respuesta y usuarios evaluadores/evaluados. A continuación se explica la estructura y funcionalidades principales de este código:

## Estructura del Código

1. **Base de Datos y Sesión**
   - Se crea una conexión a una base de datos SQLite (`item_master.db`) y se inicializa una sesión para gestionar las operaciones CRUD.
   - `Base` es la clase base que permite definir los modelos de las tablas.

2. **Modelos (Tablas)**
   - **Item**: Representa un ítem de evaluación, con los atributos:
     - `contenido`: Descripción del ítem.
     - `dificultad`: Grado de dificultad (parámetro `a`).
     - `discriminacion`: Capacidad para discriminar entre individuos (parámetro `b`).
     - `adivinacion`: Probabilidad de adivinar correctamente (parámetro `c`).
   - **OpcionDeRespuesta**: Cada opción de respuesta para un ítem, con los atributos:
     - `clave`: La opción de respuesta.
     - `es_correcta`: Indica si es la opción correcta.
     - `item_id`: ForeignKey que enlaza la opción con el `Item`.
   - **Evaluador**: Representa al usuario evaluador, que puede crear, editar y eliminar ítems.
     - Métodos como `crear_item`, `editar_item`, y `eliminar_item` permiten manipular ítems.
   - **Evaluado**: Representa a la persona evaluada.

3. **Operaciones CRUD y Relaciones**
   - La relación entre `Item` y `OpcionDeRespuesta` es de uno a muchos, donde un ítem puede tener varias opciones de respuesta, gestionada con `relationship`.
   - Métodos de `Evaluador` permiten:
     - Crear ítems con `crear_item`.
     - Editar un ítem específico usando `editar_item` al pasar el `item_id` y atributos a modificar.
     - Eliminar ítems mediante `eliminar_item`.

4. **Carga de Datos desde CSV**
   - El código carga datos iniciales de `items.csv` y `opciones_items.csv`, donde:
     - `items.csv` define los ítems de evaluación.
     - `opciones_items.csv` define las opciones de respuesta, incluyendo si cada opción es correcta.

## Ejecución

Para ejecutar este código:

1. Asegúrate de tener instaladas las librerías necesarias, especialmente `SQLAlchemy`.
2. Los archivos `items.csv` y `opciones_items.csv` deben existir en el directorio actual, con los atributos correspondientes para importar correctamente los datos.
3. Al finalizar, el código cierra la sesión de base de datos con `session.close()`.

## Mejora y Pruebas

Para una cobertura de pruebas, puedes implementar una clase `unittest` para validar:

- Creación de ítems y opciones.
- Funcionalidad CRUD completa en los métodos del `Evaluador`.
- Integridad referencial entre `Item` y `OpcionDeRespuesta`.

Esta estructura es ideal para sistemas de evaluación y exámenes en línea.
