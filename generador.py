import csv
import random

# Define el número de ítems y el archivo CSV
filename = 'items.csv'
filename_opciones = 'opciones_items.csv'

# Contenidos de preguntas de ejemplo en C++
contents = [
    {
        "contenido": "¿Cómo se declara una variable de tipo flotante en C++?",
        "clave_correcta": "float numero;",
        "distractores": ["int numero;", "double numero;", "char numero;"]
    },
    {
        "contenido": "¿Qué comando se usa para compilar un archivo en C++ usando g++?",
        "clave_correcta": "g++ archivo.cpp -o ejecutable",
        "distractores": ["gcc archivo.cpp -o ejecutable", "compile archivo.cpp", "build archivo.cpp"]
    },
    {
        "contenido": "¿Cuál es el propósito de la función 'main' en un programa C++?",
        "clave_correcta": "Es el punto de entrada del programa",
        "distractores": ["Es una función de utilidad", "Gestiona la memoria", "No tiene un propósito específico"]
    },
    {
        "contenido": "¿Cómo se escribe un bucle 'for' para iterar de 0 a 10 en C++?",
        "clave_correcta": "for(int i = 0; i <= 10; i++) { }",
        "distractores": ["for(int i = 0; i < 10; i++) { }", "for(i = 0; i <= 10; i++) { }", "for(int i = 1; i <= 10; i++) { }"]
    },
    {
        "contenido": "¿Qué hace el operador '++' en una variable?",
        "clave_correcta": "Incrementa el valor de la variable en 1",
        "distractores": ["Decrementa el valor de la variable en 1", "Multiplica el valor por 2", "No realiza ninguna operación"]
    },
    {
        "contenido": "¿Cómo se define una constante en C++?",
        "clave_correcta": "const tipo nombre = valor;",
        "distractores": ["constant tipo nombre = valor;", "final tipo nombre = valor;", "tipo nombre = valor;"]
    },
    {
        "contenido": "¿Para qué sirve el comando 'g++ -o' en la compilación?",
        "clave_correcta": "Especifica el nombre del ejecutable generado",
        "distractores": ["Optimiza el código", "Incluye bibliotecas adicionales", "Muestra advertencias durante la compilación"]
    },
    {
        "contenido": "¿Qué es una variable global en C++?",
        "clave_correcta": "Una variable declarada fuera de todas las funciones",
        "distractores": ["Una variable dentro de una función", "Una variable constante", "Una variable estática"]
    },
    {
        "contenido": "¿Cómo se crea un comentario de una línea en C++?",
        "clave_correcta": "// Comentario",
        "distractores": ["/* Comentario */", "<!-- Comentario -->", "# Comentario", "-- Comentario"]
    },
    {
        "contenido": "¿Qué es una referencia en C++ y cómo se declara?",
        "clave_correcta": "Un alias para una variable, se declara usando &",
        "distractores": ["Un puntero, se declara usando *", "Una copia de una variable, se declara usando =", "No existe en C++"]
    },
    {
        "contenido": "¿Cuál es la diferencia entre '==' y '=' en C++?",
        "clave_correcta": "'==' compara igualdad, '=' asigna un valor",
        "distractores": ["'==' asigna un valor, '=' compara igualdad", "'==' y '=' son equivalentes", "'==' es para números y '=' para cadenas"]
    },
    {
        "contenido": "¿Cómo se imprime un valor en consola usando cout?",
        "clave_correcta": "std::cout &lt;&lt; valor &lt;&lt; std::endl;",
        "distractores": ["print(valor);", "System.out.println(valor);", "printf(\"%d\", valor);"]
    },
    {
        "contenido": "¿Qué es el 'if' en C++ y cómo se usa?",
        "clave_correcta": "Una estructura condicional para ejecutar código basado en una condición",
        "distractores": ["Un bucle para iterar sobre elementos", "Una función para imprimir en pantalla", "Una variable para almacenar valores booleanos"]
    },
    {
        "contenido": "¿Cómo se declara una función en C++?",
        "clave_correcta": "tipo_de_retorno nombreFuncion(parámetros) { /* cuerpo */ }",
        "distractores": ["nombreFuncion tipo_de_retorno(parámetros) { }", "function nombreFuncion(parámetros) : tipo_de_retorno { }", "def nombreFuncion(parámetros) -> tipo_de_retorno { }"]
    },
    {
        "contenido": "¿Cuál es el uso de la palabra clave 'return' en una función?",
        "clave_correcta": "Devuelve un valor al llamador de la función",
        "distractores": ["Inicia la función", "Finaliza el programa", "Declara una variable"]
    },
    # {
    #     "contenido": "¿Cómo se convierte un número entero a flotante en C++?",
    #     "clave_correcta": "static_cast<float>(numero)",
    #     "distractores": ["float(numero)", "toFloat(numero)", "(float)numero", "convert<float>(numero)"]
    # }, TOFIX: No explicado
    {
        "contenido": "¿Qué comando se usa para ejecutar un archivo compilado?",
        "clave_correcta": "./ejecutable",
        "distractores": ["run ejecutable", "execute ejecutable", "start ejecutable"]
    },
    {
        "contenido": "¿Cómo se usa la estructura 'switch' en C++?",
        "clave_correcta": "switch(variable) { case valor1: /* código */ break; ... }",
        "distractores": ["switch(variable) { if(valor1) { } }", "switch { case valor1: /* código */ }", "switch(variable) => { case valor1: /* código */ }"]
    },
    {
        "contenido": "¿Qué es una biblioteca y cómo se incluye en C++?",
        "clave_correcta": "Un conjunto de funciones y se incluye usando #include",
        "distractores": ["Un tipo de variable y se declara con var", "Un comentario y se escribe con //", "Una clase y se define con class"]
    },
    {
        "contenido": "¿Qué tipo de datos se usa para almacenar texto en C++?",
        "clave_correcta": "std::string",
        "distractores": ["char", "int", "float"]
    },
    {
        "contenido": "¿Cómo se define un arreglo en C++?",
        "clave_correcta": "tipo nombreArreglo[tamaño];",
        "distractores": ["tipo nombreArreglo();", "arreglo tipo nombreArreglo[tamaño];", "tipo[] nombreArreglo = {};" ]
    },
    {
        "contenido": "¿Qué es el 'heap' y el 'stack' en la memoria de C++?",
        "clave_correcta": "Áreas de memoria para almacenamiento dinámico y automático, respectivamente",
        "distractores": ["Dos tipos de variables", "Funciones especiales para gestionar memoria", "Nombres alternativos para punteros y referencias"]
    },
    # {
    #     "contenido": "¿Para qué sirve el comando 'make' en C++?",
    #     "clave_correcta": "Automatizar la compilación del programa",
    #     "distractores": ["Ejecutar el programa", "Depurar el código", "Instalar bibliotecas"]
    # }, TOFIX: No explicado
    {
        "contenido": "¿Cómo se inicializa una variable con un valor en su declaración?",
        "clave_correcta": "tipo nombre = valor;",
        "distractores": ["tipo nombre;", "nombre = valor;", "tipo = valor;"]
    },
    {
        "contenido": "¿Qué es una clase en C++?",
        "clave_correcta": "Una plantilla para crear objetos que encapsula datos y funciones",
        "distractores": ["Una función especial", "Una variable global", "Una biblioteca estándar"]
    },
    {
        "contenido": "¿Cómo se crea un objeto de una clase en C++?",
        "clave_correcta": "Clase nombreObjeto;",
        "distractores": ["new Clase();", "Clase::crearObjeto();", "crear Clase nombreObjeto;"]
    },
    {
        "contenido": "¿Qué es una función recursiva y cómo se declara en C++?",
        "clave_correcta": "Una función que se llama a sí misma, declarada como cualquier otra función",
        "distractores": ["Una función que nunca termina, declarada con while", "Una función que retorna múltiples valores, declarada con array", "Una función interna, declarada dentro de otra función"]
    },
    {
        "contenido": "¿Qué hace el operador '&amp;&amp;' en una expresión lógica?",
        "clave_correcta": "Realiza una operación AND lógica",
        "distractores": ["Realiza una operación OR lógica", "Realiza una operación NOT lógica", "Concatena cadenas"]
    },
    {
        "contenido": "¿Cómo se define un puntero en C++ y qué representa?",
        "clave_correcta": "tipo* nombrePuntero; representa la dirección de una variable",
        "distractores": ["tipo& nombrePuntero; representa una referencia", "tipo nombrePuntero; representa una copia de la variable", "tipo** nombrePuntero; representa un puntero doble"]
    }
]

contents.extend([
    {
        "contenido": "¿Cómo se crea un objeto de una clase en C++?",
        "clave_correcta": "Clase nombreObjeto;",
        "distractores": [
            "new Clase();",
            "Clase::crearObjeto();",
            "crear Clase nombreObjeto;"
        ]
    },
    {
        "contenido": "¿Qué es una función recursiva y cómo se declara en C++?",
        "clave_correcta": "Una función que se llama a sí misma, declarada como cualquier otra función",
        "distractores": [
            "Una función que nunca termina, declarada con while",
            "Una función que retorna múltiples valores, declarada con array",
            "Una función interna, declarada dentro de otra función"
        ]
    },
    {
        "contenido": "¿Qué hace el operador &amp;&amp; en una expresión lógica?",
        "clave_correcta": "Realiza una operación AND lógica",
        "distractores": [
            "Realiza una operación OR lógica",
            "Realiza una operación NOT lógica",
            "Concatena cadenas"
        ]
    },
    {
        "contenido": "¿Cómo se define un puntero en C++ y qué representa?",
        "clave_correcta": "tipo* nombrePuntero; representa la dirección de una variable",
        "distractores": [
            "tipo& nombrePuntero; representa una referencia",
            "tipo nombrePuntero; representa una copia de la variable",
            "tipo** nombrePuntero; representa un puntero doble"
        ]
    },
    {
        "contenido": "¿Cuál es la sintaxis correcta para incluir una librería estándar en C++?",
        "clave_correcta": "#include &lt;iostream&gt;",
        "distractores": [
            "#include iostream",
            "import &lt;iostream&gt;",
            "include iostream.h"
        ]
    }
])

# 10 preguntas más avanzadas para poner a prueba conocimientos en C++
contents.extend([
    {
        "contenido": "¿Cuál es la diferencia entre '++i' y 'i++' en C++?",
        "clave_correcta": "'++i' incrementa antes de evaluar, 'i++' incrementa después de evaluar",
        "distractores": ["Ambos incrementan antes de evaluar", "Ambos incrementan después de evaluar", "'i++' es más rápido que '++i'"]
    },
    {
        "contenido": "¿Qué sucede si no se libera memoria dinámica asignada con 'new'?",
        "clave_correcta": "Produce una fuga de memoria",
        "distractores": ["Lanza una excepción automáticamente", "Reduce el rendimiento temporalmente", "No tiene ningún efecto negativo"]
    },
    # {
    #     "contenido": "¿Cuál es el propósito del 'virtual destructor' en una clase base?",
    #     "clave_correcta": "Permitir la eliminación correcta de objetos derivados",
    #     "distractores": ["Prevenir la creación de objetos de la clase base", "Optimizar el rendimiento del programa", "Evitar el uso de punteros en la clase"]
    # }, TOFIX: No explicado
    {
        "contenido": "¿Cuál es el propósito del operador '->*' en C++?",
        "clave_correcta": "Acceder a un miembro apuntado por un puntero a miembro",
        "distractores": ["Multiplicar un puntero por un miembro", "Comparar dos punteros a miembros", "Asignar un valor a un puntero"]
    },
    # {
    #     "contenido": "¿Qué especifica la palabra clave 'explicit' cuando se usa en un constructor?",
    #     "clave_correcta": "Evita conversiones implícitas",
    #     "distractores": ["Permite herencia múltiple", "Hace el constructor accesible solo dentro de la clase", "Permite inicialización automática"]
    # }, TOFIX: No explicado
    # {
    #     "contenido": "¿Cómo se declara un método constante en una clase C++?",
    #     "clave_correcta": "añadiendo 'const' al final de la declaración del método",
    #     "distractores": ["usando 'static' antes del tipo de retorno", "usando 'const' antes del tipo de retorno", "añadiendo '&' al final de la declaración"]
    # }, TOFIX: No explicado
    # {
    #     "contenido": "¿Qué significa la palabra clave 'mutable' en un atributo de clase?",
    #     "clave_correcta": "Permite modificar el atributo incluso en un objeto constante",
    #     "distractores": ["Hace el atributo constante", "Permite múltiples tipos para el atributo", "Optimiza el acceso al atributo"]
    # }, TOFIX: No explicado
    # {
    #     "contenido": "¿Qué función de C++ se usa para lanzar una excepción personalizada?",
    #     "clave_correcta": "throw",
    #     "distractores": ["try", "catch", "raise"]
    # }, TOFIX: No explicado
    {
        "contenido": "¿Qué representa el operador '::' en C++?",
        "clave_correcta": "El operador de resolución de ámbito",
        "distractores": ["El operador de apuntador a miembro", "El operador de flujo de entrada", "El operador de asignación múltiple"]
    }
    # ,
    # {
    #     "contenido": "¿Qué librería se debe incluir para utilizar la clase 'std::unique_ptr'?",
    #     "clave_correcta": "<memory>",
    #     "distractores": ["<unique>", "<iostream>", "<vector>"]
    # } TOFIX: No se muestran las opciones bien
])

# 10 preguntas sobre el propósito de ciertas funciones en C++
contents.extend([
    {
        "contenido": "¿Qué hace la función 'std::getline()' en C++?",
        "clave_correcta": "Lee una línea completa de texto de una entrada hasta encontrar un salto de línea",
        "distractores": ["Lee un solo carácter de la entrada", "Lee varios caracteres sin detenerse en el salto de línea", "Devuelve la longitud de la línea leída"]
    },
    {
        "contenido": "¿Cuál es el propósito de la función 'std::stoi()' en C++?",
        "clave_correcta": "Convierte una cadena a un número entero",
        "distractores": ["Convierte un número entero a cadena", "Convierte una cadena a un número decimal", "Extrae caracteres de una cadena"]
    },
    {
        "contenido": "¿Qué hace la función 'std::to_string()' en C++?",
        "clave_correcta": "Convierte un número a una cadena",
        "distractores": ["Convierte una cadena a un número", "Concatena dos cadenas", "Devuelve el tamaño de una cadena"]
    },
    {
        "contenido": "¿Para qué se utiliza la función 'std::sort()' en C++?",
        "clave_correcta": "Ordena los elementos de un contenedor en un rango específico",
        "distractores": ["Invierte los elementos de un contenedor", "Encuentra el máximo elemento en un contenedor", "Devuelve la posición de un elemento en un contenedor"]
    },
    {
        "contenido": "¿Qué hace la función 'std::reverse()' en C++?",
        "clave_correcta": "Invierte el orden de los elementos en un rango",
        "distractores": ["Ordena el rango en orden ascendente", "Devuelve el tamaño del rango", "Concatena el rango con otro"]
    },
    {
        "contenido": "¿Cuál es el propósito de la función 'std::find()' en C++?",
        "clave_correcta": "Busca el primer elemento en un rango que coincide con un valor específico",
        "distractores": ["Cuenta cuántas veces aparece un valor", "Elimina un elemento en un rango", "Encuentra el último elemento que coincide con el valor"]
    },
    {
        "contenido": "¿Qué realiza la función 'std::unique()' en C++?",
        "clave_correcta": "Elimina elementos duplicados contiguos en un rango",
        "distractores": ["Ordena los elementos en orden único", "Cuenta los elementos únicos en un rango", "Convierte todos los elementos a valores únicos"]
    },
    # {
    #     "contenido": "¿Para qué se utiliza la función 'std::accumulate()' en C++?",
    #     "clave_correcta": "Suma o acumula los elementos en un rango, con un valor inicial opcional",
    #     "distractores": ["Multiplica los elementos en un rango", "Devuelve el valor máximo en un rango", "Cuenta el número de elementos en un rango"]
    # }, TOFIX: No explicado
    {
        "contenido": "¿Qué hace la función 'std::remove()' en C++?",
        "clave_correcta": "Elimina todas las apariciones de un valor específico en un rango",
        "distractores": ["Elimina todos los elementos de un rango", "Reemplaza los elementos de un rango", "Devuelve el tamaño de un rango"]
    }
    # ,
    # {
    #     "contenido": "¿Cuál es el propósito de la función 'std::copy()' en C++?",
    #     "clave_correcta": "Copia un rango de elementos a otra ubicación",
    #     "distractores": ["Corta un rango de elementos", "Elimina duplicados en un rango", "Invierte el orden de los elementos en un rango"]
    # } TOFIX: No explicado aún
])

# 10 preguntas sobre condicionales en C++
contents.extend([
    {
        "contenido": "¿Qué significa un condicional 'if' anidado en C++?",
        "clave_correcta": "Un 'if' dentro de otro 'if' para verificar condiciones adicionales",
        "distractores": ["Un 'if' que se repite varias veces", "Un 'if' dentro de un bucle", "Un 'if' que depende de un 'else'"]
    },
    {
        "contenido": "¿Cuál es el propósito de un condicional 'else if' en una estructura encadenada?",
        "clave_correcta": "Proporciona una condición alternativa si la condición anterior es falsa",
        "distractores": ["Cierra el bloque 'if'", "Ejecuta un bloque de código al final", "Es lo mismo que 'else' pero con varias líneas"]
    },
    {
        "contenido": "¿Qué sucede si ninguna condición es verdadera en una estructura encadenada 'if-else if-else'?",
        "clave_correcta": "Se ejecuta el bloque de 'else', si está presente",
        "distractores": ["Se vuelve al primer 'if'", "El programa se detiene", "No se ejecuta ningún código"]
    },
    {
        "contenido": "¿Es posible usar múltiples condicionales 'if' encadenados sin un bloque 'else' final?",
        "clave_correcta": "Sí, se ejecutarán en orden y se evaluarán independientemente",
        "distractores": ["No, siempre se requiere un 'else'", "Sí, pero el 'else' se ejecuta automáticamente al final", "No, porque no se puede encadenar más de dos 'if'"]
    },
    {
        "contenido": "¿Qué ventaja tienen los condicionales 'else if' sobre condicionales 'if' independientes?",
        "clave_correcta": "Permiten evaluar condiciones de manera excluyente y evitar evaluaciones innecesarias",
        "distractores": ["Permiten ejecutar todos los bloques 'if' al mismo tiempo", "Optimizan solo los 'if' con bucles", "Obligan a ejecutar siempre un bloque de código"]
    },
    # {
    #     "contenido": "¿Qué sucede en una estructura anidada si el primer 'if' es falso?",
    #     "clave_correcta": "Se omite el bloque 'if' interno y se pasa al siguiente código",
    #     "distractores": ["Se ejecuta el 'else' del bloque interno", "Se reinicia el bloque 'if' desde el principio", "Se ejecuta el 'else' del bloque externo"]
    # }, TOFIX: Agregar imagen de codigo
    {
        "contenido": "¿Qué permite lograr una estructura de 'if-else' encadenado?",
        "clave_correcta": "Evaluar múltiples condiciones en un solo flujo de control",
        "distractores": ["Usar bucles de forma más efectiva", "Simplificar la lectura de código eliminando todos los 'if'", "Crear estructuras de datos más eficientes"]
    },
    {
        "contenido": "¿Qué se debe considerar al escribir 'if' anidados?",
        "clave_correcta": "La lógica debe ser clara y los niveles de anidación deben evitarse en exceso",
        "distractores": ["Siempre se debe agregar un 'else' final", "Cada 'if' debe ser independiente del siguiente", "No se puede usar más de dos niveles de anidación"]
    },
    {
        "contenido": "¿Cuál es la mejor práctica al tener múltiples condiciones que evaluar?",
        "clave_correcta": "Usar 'else if' encadenados para evitar evaluaciones innecesarias",
        "distractores": ["Anidar todos los 'if' dentro de bucles", "Agregar 'if' independientes en lugar de encadenar", "Usar únicamente 'if' y 'else' sin encadenar"]
    },
    {
        "contenido": "¿Qué tipo de errores se pueden producir con condicionales anidados mal estructurados?",
        "clave_correcta": "Errores de lógica difíciles de depurar",
        "distractores": ["Errores de sintaxis ineludibles", "Errores de memoria", "Ningún error si compila"]
    }
])

# 10 preguntas sobre el uso de los bucles for y while en C++
contents.extend([
    {
        "contenido": "¿Cuál es la diferencia principal entre un bucle 'for' y un bucle 'while' en C++?",
        "clave_correcta": "El bucle 'for' se usa cuando el número de iteraciones es conocido, mientras que 'while' se usa cuando no lo es",
        "distractores": ["'for' es más rápido que 'while'", "'while' solo se usa en estructuras anidadas", "'for' se usa solo para valores enteros"]
    },
    {
        "contenido": "¿Qué sucede si la condición de un bucle 'while' es siempre verdadera?",
        "clave_correcta": "El bucle se ejecuta indefinidamente, creando un bucle infinito",
        "distractores": ["El bucle se detiene automáticamente", "El programa da error de compilación", "Se ejecuta una sola vez"]
    },
    {
        "contenido": "¿Qué parte de la estructura 'for' controla el incremento de la variable en cada iteración?",
        "clave_correcta": "La tercera parte, que define el incremento o decremento",
        "distractores": ["La primera parte, que inicializa la variable", "La segunda parte, que evalúa la condición", "La cuarta parte, que reinicia el bucle"]
    },
    {
        "contenido": "¿Qué sucede si olvidas actualizar la condición en un bucle 'while'?",
        "clave_correcta": "Es posible que el bucle entre en un ciclo infinito",
        "distractores": ["El bucle se detiene automáticamente", "Se ejecuta solo la primera iteración", "El programa no compila"]
    },
    {
        "contenido": "¿Para qué se utiliza la palabra clave 'break' en un bucle?",
        "clave_correcta": "Para salir del bucle antes de que se complete",
        "distractores": ["Para pausar el bucle temporalmente", "Para repetir la última iteración", "Para ir al comienzo del bucle"]
    },
    {
        "contenido": "¿Cuál es el propósito de la palabra clave 'continue' en un bucle?",
        "clave_correcta": "Hace que el bucle salte a la siguiente iteración",
        "distractores": ["Termina el bucle", "Pausa el bucle indefinidamente", "Reinicia el bucle desde el principio"]
    },
    {
        "contenido": "¿Qué sucede si omites la parte de inicialización en un bucle 'for'?",
        "clave_correcta": "El bucle se ejecuta sin una variable de inicio, pero puede fallar sin inicialización previa",
        "distractores": ["El bucle no compila", "El bucle se ejecuta una sola vez", "El bucle ejecuta la condición siempre como verdadera"]
    },
    {
        "contenido": "¿Cuál es la sintaxis correcta para un bucle 'for' que cuenta de 0 a 9?",
        "clave_correcta": "for (int i = 0; i < 10; i++)",
        "distractores": ["for (int i = 1; i <= 10; i++)", "for (int i = 0; i <= 9; i+1)", "for (int i = 10; i > 0; i--)"]
    },
    {
        "contenido": "¿Cómo puedes crear un bucle infinito utilizando 'for'?",
        "clave_correcta": "for (;;) { }",
        "distractores": ["for (int i = 0; i < ∞; i++)", "for (i < 0; i++)", "for (i = 0; ; i++)"]
    },
    {
        "contenido": "¿Cuándo es preferible usar un bucle 'while' en lugar de un 'for'?",
        "clave_correcta": "Cuando el número de iteraciones no se conoce de antemano",
        "distractores": ["Cuando se necesita un bucle infinito", "Cuando se quiere mayor eficiencia", "Cuando solo se quiere ejecutar el bucle una vez"]
    }
])

# 15 preguntas sobre cin y cout con ejemplos de código en C++:
contents.extend([
    {
        "contenido": "¿Qué hace la línea de código 'cout &lt;&lt; \"Hola, Mundo!\";'?",
        "clave_correcta": "Imprime 'Hola, Mundo!' en la consola",
        "distractores": ["Lee 'Hola, Mundo!' desde la consola", "Guarda 'Hola, Mundo!' en una variable", "Imprime el valor de una variable 'Hola, Mundo!'"]
    },
    {
        "contenido": "¿Cuál es el resultado de ejecutar 'int x = 5; cout &lt;&lt; \"x = \" &lt;&lt; x;'?",
        "clave_correcta": "Imprime 'x = 5' en la consola",
        "distractores": ["Imprime '5 = x'", "Imprime solo 'x'", "Imprime solo '5'"]
    },
    {
        "contenido": "¿Qué hace el siguiente código? 'int edad; cin &gt;&gt; edad;'",
        "clave_correcta": "Solicita al usuario que ingrese un valor para la variable 'edad'",
        "distractores": ["Imprime el valor de 'edad'", "Inicializa 'edad' en 0", "Imprime 'edad' con un valor predeterminado"]
    },
    {
        "contenido": "¿Cuál es el propósito de 'cout' en C++?",
        "clave_correcta": "Enviar datos a la consola para mostrarlos",
        "distractores": ["Leer datos desde la consola", "Pausar la ejecución del programa", "Declarar variables en C++"]
    },
    {
        "contenido": "¿Qué hace el siguiente código? 'cout &lt;&lt; \"Ingrese su nombre: \";'",
        "clave_correcta": "Imprime 'Ingrese su nombre: ' en la consola",
        "distractores": ["Lee el nombre del usuario", "Almacena el nombre en una variable", "Cambia el nombre del usuario"]
    },
    {
        "contenido": "Si se ejecuta 'int a, b; cin &gt;&gt; a &gt;&gt; b;', ¿qué se espera del usuario?",
        "clave_correcta": "Que ingrese dos valores separados por un espacio",
        "distractores": ["Que ingrese un solo valor", "Que ingrese dos valores en líneas separadas", "Que ingrese solo letras"]
    },
    {
        "contenido": "¿Qué sucede si el usuario ingresa un valor no numérico en 'int x; cin &gt;&gt; x;'?",
        "clave_correcta": "El programa detecta un error y 'x' no cambia",
        "distractores": ["El programa convierte el valor a 0", "El programa ignora el error y sigue", "El programa se detiene indefinidamente"]
    },
    {
        "contenido": "¿Qué hace el siguiente código? 'cout &lt;&lt; \"Resultado: \" &lt;&lt; 5 + 3;'",
        "clave_correcta": "Imprime 'Resultado: 8' en la consola",
        "distractores": ["Imprime 'Resultado: 5 + 3'", "Imprime 'Resultado: ' seguido de un error", "Imprime solo '8'"]
    },
    {
        "contenido": "¿Cuál es el propósito de 'cin' en C++?",
        "clave_correcta": "Leer datos de la entrada estándar (teclado)",
        "distractores": ["Imprimir datos en la consola", "Pausar la ejecución", "Cerrar el programa"]
    },
    {
        "contenido": "¿Qué hace el siguiente código? 'int x; cout &lt;&lt; \"Ingrese un número: \"; cin &gt;&gt; x;'",
        "clave_correcta": "Solicita al usuario un número y lo almacena en 'x'",
        "distractores": ["Imprime el número de 'x'", "Declara una variable 'x' sin valor", "Imprime 'x' con valor predeterminado"]
    },
    {
        "contenido": "Si 'cout &lt;&lt; \"a\" &lt;&lt; \"b\" &lt;&lt; \"c\";' se ejecuta, ¿qué se muestra en la consola?",
        "clave_correcta": "abc",
        "distractores": ["a b c", "cba", "abc con saltos de línea entre letras"]
    },
    {
        "contenido": "¿Qué sucede si se omite '&lt;&lt;' en una instrucción 'cout'?",
        "clave_correcta": "Causa un error de compilación",
        "distractores": ["Imprime un valor vacío", "No produce ningún efecto", "Concatena los valores automáticamente"]
    },
    {
        "contenido": "¿Qué hace 'cout &lt;&lt; \"Resultado: \" &lt;&lt; (10 > 5);'?",
        "clave_correcta": "Imprime 'Resultado: 1' ya que 10 es mayor que 5",
        "distractores": ["Imprime 'Resultado: verdadero'", "Imprime 'Resultado: 10'", "Imprime solo 'Resultado:'"]
    },
    {
        "contenido": "¿Qué hace el siguiente código? 'int num; cout &lt;&lt; \"Ingrese un número:\"; cin &gt;&gt; num; cout &lt;&lt; \"Número ingresado:\" &lt;&lt; num;'",
        "clave_correcta": "Solicita un número al usuario y luego lo imprime",
        "distractores": ["Imprime el número ingresado dos veces", "Solicita dos números y los imprime", "Imprime 'Número ingresado' sin el número"]
    }
    # ,
    # {
    #     "contenido": "¿Qué pasa si se usa 'cin' para leer una cadena con espacios sin 'std::getline'?",
    #     "clave_correcta": "Solo lee hasta el primer espacio",
    #     "distractores": ["Lee toda la línea", "Genera un error", "Ignora cualquier entrada con espacios"]
    # } TOFIX: No explicado
])

# 10 preguntas sobre el uso de fstream en C++
contents.extend([
    {
        "contenido": "¿Para qué se utiliza la librería 'fstream' en C++?",
        "clave_correcta": "Para manipular archivos, permitiendo leer y escribir datos",
        "distractores": ["Para manejar flujos de entrada estándar", "Para manejar solo archivos de texto", "Para manipular bases de datos"]
    },
    {
        "contenido": "¿Qué clase de 'fstream' se utiliza específicamente para leer desde un archivo?",
        "clave_correcta": "ifstream",
        "distractores": ["ofstream", "fstream", "infile"]
    },
    {
        "contenido": "¿Qué clase de 'fstream' se usa para escribir en un archivo?",
        "clave_correcta": "ofstream",
        "distractores": ["ifstream", "fstream", "outfile"]
    },
    {
        "contenido": "¿Qué modo de apertura se debe utilizar para agregar datos al final de un archivo existente en C++?",
        "clave_correcta": "ios::app",
        "distractores": ["ios::end", "ios::trunc", "ios::open"]
    },
    {
        "contenido": "¿Qué hace el siguiente código? 'ofstream archivo(\"datos.txt\");'",
        "clave_correcta": "Abre o crea el archivo 'datos.txt' para escritura",
        "distractores": ["Abre 'datos.txt' para lectura", "Cierra el archivo 'datos.txt'", "Elimina el contenido de 'datos.txt' sin abrirlo"]
    },
    {
        "contenido": "¿Qué sucede si intentas abrir un archivo inexistente con 'ifstream'?",
        "clave_correcta": "El archivo no se abre, y el objeto 'ifstream' indica un error",
        "distractores": ["Se crea un nuevo archivo automáticamente", "Lanza una excepción", "El programa se detiene inmediatamente"]
    },
    {
        "contenido": "¿Cómo se verifica si un archivo fue abierto correctamente con 'fstream'?",
        "clave_correcta": "Usando el método 'is_open()' en el objeto de archivo",
        "distractores": ["Usando 'file_exists()'", "Verificando si el objeto no es NULL", "Usando 'check()' en el archivo"]
    },
    {
        "contenido": "¿Qué hace el operador '&lt;&lt;' cuando se utiliza con 'ofstream'?",
        "clave_correcta": "Escribe datos en el archivo",
        "distractores": ["Lee datos del archivo", "Borra datos del archivo", "Cierra el archivo"]
    },
    {
        "contenido": "¿Cuál es el propósito de 'archivo.close()' en el uso de 'fstream'?",
        "clave_correcta": "Cerrar el archivo abierto para liberar los recursos",
        "distractores": ["Abrir un archivo en modo lectura", "Guardar automáticamente los cambios en el archivo", "Reiniciar el archivo desde el principio"]
    }
    # ,
    # {
    #     "contenido": "¿Qué hace 'ios::trunc' al abrir un archivo en C++?",
    #     "clave_correcta": "Elimina el contenido del archivo si ya existe",
    #     "distractores": ["Agrega datos al final del archivo", "Abre el archivo solo en modo lectura", "Cierra el archivo después de escribir"]
    # } TOFIX: No explicado
])

contents = [
    {
        "contenido": "¿Qué imprime el siguiente código?&#92;n&#92;nint x = 5;&#92;nint y = 10;&#92;ncout &lt;&lt; x + y &lt;&lt; endl;",
        "clave_correcta": "15",
        "distractores": ["5", "10", "50"]
    }    ,
    {
        "contenido": "¿Qué imprime el siguiente código?&#92;n&#92;nint x = 8;&#92;nx += 2;&#92;ncout &lt;&lt; x &lt;&lt; endl;",
        "clave_correcta": "10",
        "distractores": ["8", "2", "12"]
    },
    {
        "contenido": "¿Qué imprime el siguiente código?&#92;n&#92;nint a = 3;&#92;nint b = 4;&#92;ncout &lt;&lt; a * b &lt;&lt; endl;",
        "clave_correcta": "12",
        "distractores": ["7", "1", "34"]
    }
    # {
    #     "contenido": "¿Qué imprime el siguiente código?&#92;n&#92;nint num = 7;&#92;ncout &lt;&lt; num % 3 &lt;&lt; endl;",
    #     "clave_correcta": "1",
    #     "distractores": ["3", "2", "0"]
    # },
    # {
    #     "contenido": "¿Qué imprime el siguiente código?&#92;n&#92;nint a = 5;&#92;nint b = 2;&#92;ncout &lt;&lt; a / b &lt;&lt; endl;",
    #     "clave_correcta": "2",
    #     "distractores": ["2.5", "3", "1"]
    # },
    # {
    #     "contenido": "¿Qué imprime el siguiente código?&#92;n&#92;nint x = 5;&#92;nint y = 3;&#92;ncout &lt;&lt; (x > y) &lt;&lt; endl;",
    #     "clave_correcta": "1",
    #     "distractores": ["0", "5", "3"]
    # },
    # {
    #     "contenido": "¿Qué imprime el siguiente código?&#92;n&#92;nint x = 5;&#92;nint y = 10;&#92;ncout &lt;&lt; (x < y &amp;&amp; y > 5) &lt;&lt; endl;",
    #     "clave_correcta": "1",
    #     "distractores": ["0", "10", "5"]
    # },
    # {
    #     "contenido": "¿Qué imprime el siguiente código?&#92;n&#92;nint x = 10;&#92;nint y = 5;&#92;ncout &lt;&lt; (x == y) &lt;&lt; endl;",
    #     "clave_correcta": "0",
    #     "distractores": ["10", "5", "1"]
    # },
    # {
    #     "contenido": "¿Qué imprime el siguiente código?&#92;n&#92;nint x = 1;&#92;nx++;&#92;ncout &lt;&lt; x &lt;&lt; endl;",
    #     "clave_correcta": "2",
    #     "distractores": ["1", "0", "3"]
    # },
    # {
    #     "contenido": "¿Qué imprime el siguiente código?&#92;n&#92;nint x = 2;&#92;nx--;&#92;ncout &lt;&lt; x &lt;&lt; endl;",
    #     "clave_correcta": "1",
    #     "distractores": ["2", "0", "-1"]
    # },
    # {
    #     "contenido": "¿Qué imprime el siguiente código?&#92;n&#92;nint a = 5;&#92;nint b = 3;&#92;ncout &lt;&lt; (a >= b) &lt;&lt; endl;",
    #     "clave_correcta": "1",
    #     "distractores": ["0", "8", "5"]
    # },
    # {
    #     "contenido": "¿Qué imprime el siguiente código?&#92;n&#92;nint a = 4;&#92;nint b = 2;&#92;ncout &lt;&lt; (a != b) &lt;&lt; endl;",
    #     "clave_correcta": "1",
    #     "distractores": ["0", "4", "2"]
    # },
    # {
    #     "contenido": "¿Qué imprime el siguiente código?&#92;n&#92;nint num = 10;&#92;ncout &lt;&lt; num / 3 &lt;&lt; endl;",
    #     "clave_correcta": "3",
    #     "distractores": ["3.33", "2", "10"]
    # },
    # {
    #     "contenido": "¿Qué imprime el siguiente código?&#92;n&#92;nint x = 7;&#92;nint y = 2;&#92;ncout &lt;&lt; x % y &lt;&lt; endl;",
    #     "clave_correcta": "1",
    #     "distractores": ["2", "0", "3"]
    # }
]

num_items = len(contents)

# A cada elemento agregar un serial item_id
contents = [ { "item_id": i+1, **content } for i, content in enumerate(contents) ]


# Genera el archivo CSV con datos realistas de programación en C++
with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['item_id', 'contenido', 'dificultad', 'discriminacion', 'adivinacion']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    # Configura el delimitador de strings para evitar problemas con las comillas
    writer._string_delimiter = '"'
    
    # Escribe la cabecera
    writer.writeheader()
    
    # Genera ítems de prueba con contenido específico
    for i in range(num_items):
        writer.writerow({
            'item_id': contents[i]['item_id'],
            'contenido': contents[i],
            'dificultad': round(random.uniform(0.1, 1.0), 2),
            'discriminacion': round(random.uniform(0.2, 1.0), 2),
            'adivinacion': round(random.uniform(0.0, 0.25), 2)
        })

# # Genera el archivo CSV con datos de cada Items con su contenido, la clave correcta y los distractores
# with open(filename_opciones, mode='w', newline='') as csvfile:
#     fieldnames = ['item_id', 'texto', 'clave', 'es_correcta']	
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#     # Escribe la cabecera
#     writer.writeheader()

#     # Genera ítems de prueba con contenido específico
#     for i in range(num_items):
#         writer.writerow({
#             'item_id': contents[i]['item_id'],
#             'texto': contents[i]['contenido'],
#             'clave': contents[i]['clave_correcta'],
#             'es_correcta': True
#         })
#         for distractor in contents[i]['distractores']:
#             writer.writerow({
#                 'item_id': contents[i]['item_id'],
#                 'texto': contents[i]['contenido'],
#                 'clave': distractor,
#                 'es_correcta': False
#             })


# print(f"Archivo '{filename_opciones}' creado con éxito con {num_items} ítems sobre preguntas de programación en C++.")
