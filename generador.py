import csv
import random

# Define el número de ítems y el archivo CSV
num_items = 29
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
        "distractores": ["/* Comentario */", "<!-- Comentario -->", "# Comentario"]
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
        "clave_correcta": "std::cout << valor << std::endl;",
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
    {
        "contenido": "¿Cómo se convierte un número entero a flotante en C++?",
        "clave_correcta": "static_cast<float>(numero)",
        "distractores": ["float(numero)", "toFloat(numero)", "(float)numero", "convert<float>(numero)"]
    },
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
    {
        "contenido": "¿Para qué sirve el comando 'make' en C++?",
        "clave_correcta": "Automatizar la compilación del programa",
        "distractores": ["Ejecutar el programa", "Depurar el código", "Instalar bibliotecas"]
    },
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
        "contenido": "¿Qué hace el operador '&&' en una expresión lógica?",
        "clave_correcta": "Realiza una operación AND lógica",
        "distractores": ["Realiza una operación OR lógica", "Realiza una operación NOT lógica", "Concatena cadenas"]
    },
    {
        "contenido": "¿Cómo se define un puntero en C++ y qué representa?",
        "clave_correcta": "tipo* nombrePuntero; representa la dirección de una variable",
        "distractores": ["tipo& nombrePuntero; representa una referencia", "tipo nombrePuntero; representa una copia de la variable", "tipo** nombrePuntero; representa un puntero doble"]
    }
]

# A cada elemento agregar un serial item_id
contents = [ { "item_id": i+1, **content } for i, content in enumerate(contents) ]


# Genera el archivo CSV con datos realistas de programación en C++
with open(filename, mode='w', newline='') as csvfile:
    fieldnames = ['item_id', 'contenido', 'dificultad', 'discriminacion', 'adivinacion']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
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

# Genera el archivo CSV con datos de cada Items con su contenido, la clave correcta y los distractores
with open(filename_opciones, mode='w', newline='') as csvfile:
    fieldnames = ['item_id', 'texto', 'clave', 'es_correcta']	
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Escribe la cabecera
    writer.writeheader()

    # Genera ítems de prueba con contenido específico
    for i in range(num_items):
        writer.writerow({
            'item_id': contents[i]['item_id'],
            'texto': contents[i]['contenido'],
            'clave': contents[i]['clave_correcta'],
            'es_correcta': True
        })
        for distractor in contents[i]['distractores']:
            writer.writerow({
                'item_id': contents[i]['item_id'],
                'texto': contents[i]['contenido'],
                'clave': distractor,
                'es_correcta': False
            })


print(f"Archivo '{filename_opciones}' creado con éxito con 30 ítems sobre preguntas de programación en C++.")
