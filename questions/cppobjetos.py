questions = [
    {
        "categoria": "Programación Orientada a Objetos",
        "dificultad": "IT'S A DOOM",
        "enunciado": "¿Cuál de los siguientes es uno de los cuatro pilares de la programación orientada a objetos?",
        "opciones": [
            ["a", "Iteración"],
            ["b", "Recursión"],
            ["c", "Herencia"],
            ["d", "Compilación"],
        ],
        "correcta": "c",
        "feedback": {
            "a": "Incorrecto. La iteración es una estructura de control, no un pilar de la POO.",
            "b": "Incorrecto. La recursión es una técnica de programación, no un pilar de la POO.",
            "c": "Correcto. La herencia es uno de los cuatro pilares de la POO.",
            "d": "Incorrecto. La compilación es un proceso de traducción de código, no un pilar de la POO.",
        },
    },
    {
        "categoria": "Encapsulación",
        "dificultad": "HURT ME PLENTY",
        "enunciado": "En C++, ¿cuál es la palabra clave utilizada para especificar que los miembros de una clase son accesibles solo dentro de la clase misma?",
        "opciones": [
            ["a", "public"],
            ["b", "private"],
            ["c", "protected"],
            ["d", "friend"],
        ],
        "correcta": "b",
        "feedback": {
            "a": "Incorrecto. 'public' permite acceso desde cualquier lugar.",
            "b": "Correcto. 'private' restringe el acceso solo a la clase misma.",
            "c": "Incorrecto. 'protected' permite acceso desde clases derivadas.",
            "d": "Incorrecto. 'friend' es una declaración que permite acceso privado a otra clase o función.",
        },
    },
    {
        "categoria": "Abstracción",
        "dificultad": "ULTRA-VIOLENCE",
        "enunciado": "¿Cómo se declara una clase abstracta en C++?",
        "opciones": [
            ["a", "Definiendo al menos un método virtual puro."],
            ["b", "Usando la palabra clave 'abstract' antes de la clase."],
            ["c", "Heredando de la clase 'Abstract'."],
            ["d", "No es posible crear clases abstractas en C++."],
        ],
        "correcta": "a",
        "feedback": {
            "a": "Correcto. Un método virtual puro se declara con '= 0'.",
            "b": "Incorrecto. C++ no tiene una palabra clave 'abstract'.",
            "c": "Incorrecto. No existe una clase 'Abstract' por defecto en C++.",
            "d": "Incorrecto. Sí es posible mediante métodos virtuales puros.",
        },
    },
    {
        "categoria": "Herencia",
        "dificultad": "NIGHTMARE",
        "enunciado": "¿Cuál es la sintaxis correcta para indicar que una clase 'Perro' hereda públicamente de una clase 'Animal' en C++?",
        "opciones": [
            ["a", "`class Perro : Animal { };`"],
            ["b", "`class Perro -> public Animal { };`"],
            ["c", "`class Perro : public Animal { };`"],
            ["d", "`class Perro(Animal) { };`"],
        ],
        "correcta": "c",
        "feedback": {
            "a": "Incorrecto. Falta especificar el modo de herencia 'public'.",
            "b": "Incorrecto. La sintaxis de herencia no utiliza '->'.",
            "c": "Correcto. Esta es la sintaxis correcta para herencia pública.",
            "d": "Incorrecto. Esta no es la sintaxis correcta en C++.",
        },
    },
    {
        "categoria": "Polimorfismo",
        "dificultad": "ULTRANIGHTMARE",
        "enunciado": "En C++, ¿cómo se logra el polimorfismo en tiempo de ejecución?",
        "opciones": [
            ["a", "Usando funciones sobrecargadas."],
            ["b", "Usando plantillas (templates)."],
            [
                "c",
                "Usando métodos virtuales y punteros o referencias a clases base.",
            ],
            ["d", "Usando macros preprocesador."],
        ],
        "correcta": "c",
        "feedback": {
            "a": "Incorrecto. La sobrecarga es polimorfismo en tiempo de compilación.",
            "b": "Incorrecto. Las plantillas también son polimorfismo en tiempo de compilación.",
            "c": "Correcto. Los métodos virtuales permiten polimorfismo dinámico.",
            "d": "Incorrecto. Los macros no proporcionan polimorfismo.",
        },
    },
    {
        "categoria": "Visibilidad",
        "dificultad": "IT'S A DOOM",
        "enunciado": "¿Cuál es el modificador de acceso predeterminado para los miembros de una clase en C++?",
        "opciones": [
            ["a", "public"],
            ["b", "private"],
            ["c", "protected"],
            ["d", "internal"],
        ],
        "correcta": "b",
        "feedback": {
            "a": "Incorrecto. 'public' es el modificador predeterminado en 'struct', no en 'class'.",
            "b": "Correcto. En 'class', los miembros son 'private' por defecto.",
            "c": "Incorrecto. 'protected' no es el modificador predeterminado.",
            "d": "Incorrecto. 'internal' no es un modificador de acceso en C++.",
        },
    },
    {
        "categoria": "Atributos y Métodos",
        "dificultad": "HURT ME PLENTY",
        "enunciado": "En C++, ¿cómo se declara un método constante que no modifica los miembros de la clase?",
        "opciones": [
            ["a", "`void metodo() const { }`"],
            ["b", "`const void metodo() { }`"],
            ["c", "`void const metodo() { }`"],
            ["d", "`void metodo() { } const`"],
        ],
        "correcta": "a",
        "feedback": {
            "a": "Correcto. El 'const' después de los paréntesis indica un método constante.",
            "b": "Incorrecto. 'const' antes del tipo de retorno no hace el método constante.",
            "c": "Incorrecto. El orden es incorrecto y no hace el método constante.",
            "d": "Incorrecto. La posición de 'const' es incorrecta.",
        },
    },
    {
        "categoria": "Encapsulación",
        "dificultad": "ULTRA-VIOLENCE",
        "enunciado": "¿Qué mecanismo en C++ se utiliza para restringir el acceso directo a los datos de una clase?",
        "opciones": [
            ["a", "Herencia múltiple"],
            ["b", "Constructores"],
            ["c", "Modificadores de acceso (public, private, protected)"],
            ["d", "Sobrecarga de operadores"],
        ],
        "correcta": "c",
        "feedback": {
            "a": "Incorrecto. La herencia múltiple no se utiliza para restringir acceso.",
            "b": "Incorrecto. Los constructores inicializan objetos pero no restringen acceso.",
            "c": "Correcto. Los modificadores de acceso controlan la visibilidad de los miembros.",
            "d": "Incorrecto. La sobrecarga de operadores modifica el comportamiento de operadores.",
        },
    },
    {
        "categoria": "Herencia",
        "dificultad": "ULTRANIGHTMARE",
        "enunciado": "En C++, si una clase derivada necesita llamar al constructor de su clase base que toma argumentos, ¿cómo se hace?",
        "opciones": [
            [
                "a",
                "No es posible llamar al constructor de la clase base con argumentos.",
            ],
            [
                "b",
                "En el cuerpo del constructor de la clase derivada, llamando `Base( argumentos );`",
            ],
            [
                "c",
                "Usando una lista de inicialización: `Derivada( args ) : Base( args ) { }`",
            ],
            ["d", "Usando la palabra clave `super`: `super( args );`"],
        ],
        "correcta": "c",
        "feedback": {
            "a": "Incorrecto. Sí es posible llamar al constructor de la clase base con argumentos.",
            "b": "Incorrecto. La sintaxis es incorrecta para llamar al constructor base.",
            "c": "Correcto. La lista de inicialización permite llamar al constructor base con argumentos.",
            "d": "Incorrecto. 'super' no es una palabra clave en C++.",
        },
    },
    {
        "categoria": "Polimorfismo",
        "dificultad": "NIGHTMARE",
        "enunciado": "¿Qué palabra clave se utiliza en C++ para evitar que una clase sea heredada?",
        "opciones": [
            ["a", "sealed"],
            ["b", "final"],
            ["c", "override"],
            ["d", "static"],
        ],
        "correcta": "b",
        "feedback": {
            "a": "Incorrecto. 'sealed' es usado en otros lenguajes como C#, no en C++.",
            "b": "Correcto. 'final' previene la herencia de una clase o método.",
            "c": "Incorrecto. 'override' se utiliza para sobreescribir métodos virtuales.",
            "d": "Incorrecto. 'static' indica un miembro de clase compartido, no afecta la herencia.",
        },
    },
]

questions.extend(
    [
        {
            "categoria": "Encapsulación",
            "dificultad": "IT'S A DOOM",
            "enunciado": (
                "En C++, ¿cuál es la palabra clave utilizada para declarar miembros de clase que solo son accesibles desde dentro de la misma clase?<br><br>"
                "<code>"
                "class MiClase {<br>"
                "    /* Completar */<br>"
                "    int datoPrivado;<br>"
                "};"
                "</code>"
            ),
            "opciones": [
                ["a", "public"],
                ["b", "private"],
                ["c", "protected"],
                ["d", "friend"],
            ],
            "correcta": "b",
            "feedback": {
                "a": "Incorrecto. 'public' permite acceso desde cualquier parte.",
                "b": "Correcto. 'private' restringe el acceso solo a la clase misma.",
                "c": "Incorrecto. 'protected' permite acceso desde clases derivadas.",
                "d": "Incorrecto. 'friend' es una declaración especial que otorga acceso.",
            },
        },
        {
            "categoria": "Herencia",
            "dificultad": "HURT ME PLENTY",
            "enunciado": (
                "En C++, ¿cómo se declara correctamente que una clase 'Coche' hereda públicamente de una clase 'Vehículo'?<br><br>"
                "<code>"
                "class Coche /* Completar */ {<br>"
                "    // Implementación<br>"
                "};"
                "</code>"
            ),
            "opciones": [
                ["a", ": Vehículo"],
                ["b", ": public Vehículo"],
                ["c", "-> Vehículo"],
                ["d", "(Vehículo)"],
            ],
            "correcta": "b",
            "feedback": {
                "a": "Incorrecto. Falta especificar el tipo de herencia 'public'.",
                "b": "Correcto. Esta es la sintaxis correcta para herencia pública.",
                "c": "Incorrecto. Esta sintaxis no es válida en C++ para herencia.",
                "d": "Incorrecto. Esta sintaxis no es correcta en C++.",
            },
        },
        {
            "categoria": "Polimorfismo",
            "dificultad": "NIGHTMARE",
            "enunciado": (
                "En C++, ¿qué especificador se utiliza para indicar que un método sobrescribe uno virtual de la clase base?<br><br>"
                "<code>"
                "class Base {<br>"
                "public:<br>"
                "    virtual void mostrar();<br>"
                "};<br><br>"
                "class Derivada : public Base {<br>"
                "public:<br>"
                "    void mostrar() /* Completar */;<br>"
                "};"
                "</code>"
            ),
            "opciones": [
                ["a", "virtual"],
                ["b", "override"],
                ["c", "final"],
                ["d", "static"],
            ],
            "correcta": "b",
            "feedback": {
                "a": "Incorrecto. 'virtual' se usa en la declaración del método en la clase base.",
                "b": "Correcto. 'override' indica que el método sobrescribe uno virtual de la base.",
                "c": "Incorrecto. 'final' se usa para evitar más sobrescrituras.",
                "d": "Incorrecto. 'static' define un método estático, no relacionado con sobrescritura.",
            },
        },
        {
            "categoria": "Abstracción",
            "dificultad": "ULTRA-VIOLENCE",
            "enunciado": (
                "En C++, ¿cómo se declara un método virtual puro en una clase abstracta?<br><br>"
                "<code>"
                "class Figura {<br>"
                "public:<br>"
                "    virtual void dibujar() /* Completar */;<br>"
                "};"
                "</code>"
            ),
            "opciones": [
                ["a", "= 0;"],
                ["b", "{}"],
                ["c", "= default;"],
                ["d", "= delete;"],
            ],
            "correcta": "a",
            "feedback": {
                "a": "Correcto. '= 0;' indica un método virtual puro.",
                "b": "Incorrecto. '{}' sería una implementación vacía, no un método puro.",
                "c": "Incorrecto. '= default;' solicita la implementación por defecto.",
                "d": "Incorrecto. '= delete;' elimina el método, impidiendo su uso.",
            },
        },
        {
            "categoria": "Constructores",
            "dificultad": "ULTRANIGHTMARE",
            "enunciado": (
                "En C++, ¿cómo se llama al constructor de la clase base 'Base' desde el constructor de la clase derivada 'Derivada'?<br><br>"
                "<code>"
                "class Derivada : public Base {<br>"
                "public:<br>"
                "    Derivada() /* Completar */ {<br>"
                "        // Cuerpo del constructor<br>"
                "    }<br>"
                "};"
                "</code>"
            ),
            "opciones": [
                ["a", "Base();"],
                ["b", ": Base()"],
                ["c", "{ Base(); }"],
                ["d", "-> Base()"],
            ],
            "correcta": "b",
            "feedback": {
                "a": "Incorrecto. Esta sintaxis no llama al constructor base correctamente.",
                "b": "Correcto. La lista de inicialización llama al constructor de 'Base'.",
                "c": "Incorrecto. Llamar al constructor dentro del cuerpo no es adecuado.",
                "d": "Incorrecto. Esta sintaxis no es válida en C++.",
            },
        },
        {
            "categoria": "Visibilidad",
            "dificultad": "IT'S A DOOM",
            "enunciado": (
                "En C++, ¿qué modificador de acceso permite que los miembros sean accesibles en la clase y sus derivadas, pero no desde fuera?<br><br>"
                "<code>"
                "class MiClase {<br>"
                "protected:<br>"
                "    int datoProtegido;<br>"
                "};"
                "</code>"
            ),
            "opciones": [
                ["a", "public"],
                ["b", "private"],
                ["c", "protected"],
                ["d", "friend"],
            ],
            "correcta": "c",
            "feedback": {
                "a": "Incorrecto. 'public' permite acceso desde cualquier parte.",
                "b": "Incorrecto. 'private' restringe el acceso solo a la clase misma.",
                "c": "Correcto. 'protected' permite acceso desde la clase y sus derivadas.",
                "d": "Incorrecto. 'friend' otorga acceso a clases o funciones específicas.",
            },
        },
        {
            "categoria": "Métodos Constantes",
            "dificultad": "HURT ME PLENTY",
            "enunciado": (
                "En C++, ¿cómo se declara un método constante que no modifica los miembros de la clase?<br><br>"
                "<code>"
                "class MiClase {<br>"
                "public:<br>"
                "    int obtenerValor() /* Completar */ {<br>"
                "        return valor;<br>"
                "    }<br>"
                "private:<br>"
                "    int valor;<br>"
                "};"
                "</code>"
            ),
            "opciones": [
                ["a", "const;"],
                ["b", "const {}"],
                ["c", "const { }"],
                ["d", "const"],
            ],
            "correcta": "d",
            "feedback": {
                "a": "Incorrecto. La sintaxis correcta es colocar 'const' después de los paréntesis.",
                "b": "Incorrecto. La posición de 'const' y las llaves son incorrectas.",
                "c": "Incorrecto. Las llaves no son necesarias aquí.",
                "d": "Correcto. 'const' después de los paréntesis declara el método como constante.",
            },
        },
        {
            "categoria": "Sobrecarga de Operadores",
            "dificultad": "NIGHTMARE",
            "enunciado": (
                "En C++, ¿cómo se declara correctamente la sobrecarga del operador '+' en una clase 'Complejo'?<br><br>"
                "<code>"
                "class Complejo {<br>"
                "public:<br>"
                "    Complejo operator+ (const Complejo& otro) /* Completar */ {<br>"
                "        // Implementación<br>"
                "    }<br>"
                "};"
                "</code>"
            ),
            "opciones": [
                ["a", "virtual"],
                ["b", "const"],
                ["c", "override"],
                ["d", ""],
            ],
            "correcta": "d",
            "feedback": {
                "a": "Incorrecto. No se necesita 'virtual' para sobrecargar operadores.",
                "b": "Incorrecto. 'const' no es necesario aquí.",
                "c": "Incorrecto. 'override' se usa al sobrescribir métodos virtuales.",
                "d": "Correcto. No se requiere ningún especificador adicional.",
            },
        },
        {
            "categoria": "Polimorfismo",
            "dificultad": "ULTRA-VIOLENCE",
            "enunciado": (
                "En C++, ¿cómo se declara una clase para que no pueda ser heredada?<br><br>"
                "<code>"
                "class ClaseFinal /* Completar */ {<br>"
                "    // Implementación<br>"
                "};"
                "</code>"
            ),
            "opciones": [
                ["a", "final"],
                ["b", ": final"],
                ["c", "class ClaseFinal final"],
                ["d", "sealed"],
            ],
            "correcta": "c",
            "feedback": {
                "a": "Incorrecto. 'final' debe colocarse después del nombre de la clase.",
                "b": "Incorrecto. La sintaxis correcta es colocar 'final' después del nombre.",
                "c": "Correcto. 'final' después del nombre impide la herencia.",
                "d": "Incorrecto. 'sealed' no es una palabra clave en C++.",
            },
        },
        {
            "categoria": "Herencia Múltiple",
            "dificultad": "ULTRANIGHTMARE",
            "enunciado": (
                "En C++, ¿cómo se declara una clase 'Híbrido' que hereda públicamente de 'ClaseA' y 'ClaseB'?<br><br>"
                "<code>"
                "class Híbrido : /* Completar */ {<br>"
                "    // Implementación<br>"
                "};"
                "</code>"
            ),
            "opciones": [
                ["a", "public ClaseA, public ClaseB"],
                ["b", "ClaseA, ClaseB"],
                ["c", "public ClaseA & ClaseB"],
                ["d", "ClaseA + ClaseB"],
            ],
            "correcta": "a",
            "feedback": {
                "a": "Correcto. Esta es la sintaxis para herencia múltiple pública.",
                "b": "Incorrecto. Falta especificar el tipo de herencia 'public'.",
                "c": "Incorrecto. '&' no se usa para indicar herencia.",
                "d": "Incorrecto. '+' no es válido para herencia múltiple.",
            },
        },
    ]
)

questions.extend(
    [
        {
            "categoria": "Lectura y Escritura de Archivos",
            "dificultad": "HURT ME PLENTY",
            "enunciado": (
                "¿Cuál es la salida esperada del siguiente código?<br><br>"
                "<code>"
                "#include &lt;fstream&gt;<br>"
                "#include &lt;iostream&gt;<br>"
                "#include &lt;string&gt;<br><br>"
                "int main() {<br>"
                '    std::ofstream archivo("salida.txt");<br>'
                '    archivo << "Hola, mundo" << std::endl;<br>'
                "    archivo.close();<br>"
                '    std::ifstream entrada("salida.txt");<br>'
                "    std::string linea;<br>"
                "    std::getline(entrada, linea);<br>"
                "    std::cout << linea << std::endl;<br>"
                "    entrada.close();<br>"
                "    return 0;<br>"
                "}"
                "</code>"
            ),
            "opciones": [
                ["a", "Imprime 'Hola, mundo' en la consola"],
                ["b", "Escribe 'Hola, mundo' en el archivo 'salida.txt'"],
                [
                    "c",
                    "Imprime 'Hola, mundo' en la consola y escribe 'Hola, mundo' en el archivo",
                ],
                ["d", "No produce salida y no escribe en el archivo"],
            ],
            "correcta": "a",
            "feedback": {
                "a": "Correcto. El programa escribe en el archivo y luego lee e imprime el contenido.",
                "b": "Incorrecto. Además de escribir en el archivo, también imprime en la consola.",
                "c": "Incorrecto. Solo se imprime en la consola después de leer del archivo.",
                "d": "Incorrecto. El programa realiza operaciones de E/S correctamente.",
            },
        },
        {
            "categoria": "Lectura y Escritura de Archivos",
            "dificultad": "NIGHTMARE",
            "enunciado": (
                "¿Qué hace el siguiente código en C++?<br><br>"
                "<code>"
                "#include &lt;fstream&gt;<br>"
                "#include &lt;iostream&gt;<br><br>"
                "int main() {<br>"
                '    std::ifstream archivo("datos.txt");<br>'
                "    if (!archivo) {<br>"
                '        std::cerr << "No se pudo abrir el archivo" << std::endl;<br>'
                "        return 1;<br>"
                "    }<br>"
                "    int suma = 0, numero;<br>"
                "    while (archivo >> numero) {<br>"
                "        suma += numero;<br>"
                "    }<br>"
                '    std::cout << "La suma es: " << suma << std::endl;<br>'
                "    archivo.close();<br>"
                "    return 0;<br>"
                "}"
                "</code>"
            ),
            "opciones": [
                ["a", "Lee números de 'datos.txt' y calcula su suma"],
                ["b", "Escribe números en 'datos.txt'"],
                ["c", "Genera un error de compilación"],
                ["d", "No hace nada"],
            ],
            "correcta": "a",
            "feedback": {
                "a": "Correcto. El programa lee números desde el archivo y calcula la suma.",
                "b": "Incorrecto. El programa solo lee del archivo, no escribe en él.",
                "c": "Incorrecto. El código compila correctamente.",
                "d": "Incorrecto. El programa realiza operaciones de lectura y cálculo.",
            },
        },
        {
            "categoria": "Lectura y Escritura de Archivos",
            "dificultad": "ULTRA-VIOLENCE",
            "enunciado": (
                "Considerando el siguiente código, ¿qué contenido tendrá el archivo 'output.txt' después de ejecutarlo?<br><br>"
                "<code>"
                "#include &lt;fstream&gt;<br>"
                "#include &lt;string&gt;<br><br>"
                "int main() {<br>"
                '    std::ofstream archivo("output.txt", std::ios::app);<br>'
                '    archivo << "Línea 1" << std::endl;<br>'
                "    archivo.close();<br>"
                "    return 0;<br>"
                "}"
                "</code>"
            ),
            "opciones": [
                ["a", "El archivo contendrá solo 'Línea 1'"],
                [
                    "b",
                    "El archivo contendrá 'Línea 1' al final, preservando el contenido previo",
                ],
                ["c", "El archivo estará vacío"],
                ["d", "El código genera un error y no modifica el archivo"],
            ],
            "correcta": "b",
            "feedback": {
                "a": "Incorrecto. El modo 'std::ios::app' añade al final sin borrar el contenido previo.",
                "b": "Correcto. El texto se añade al final del archivo existente.",
                "c": "Incorrecto. El archivo no estará vacío después de escribir.",
                "d": "Incorrecto. El código funciona y escribe en el archivo.",
            },
        },
        {
            "categoria": "Lectura y Escritura de Archivos",
            "dificultad": "ULTRANIGHTMARE",
            "enunciado": (
                "Analiza el siguiente código y determina su funcionalidad:<br><br>"
                "<code>"
                "#include &lt;fstream&gt;<br>"
                "#include &lt;iostream&gt;<br>"
                "#include &lt;vector&gt;<br><br>"
                "int main() {<br>"
                '    std::ifstream entrada("datos.txt");<br>'
                "    std::vector&lt;int&gt; numeros;<br>"
                "    int num;<br>"
                "    while (entrada >> num) {<br>"
                "        numeros.push_back(num);<br>"
                "    }<br>"
                "    entrada.close();<br>"
                '    std::ofstream salida("resultado.txt");<br>'
                "    for (auto it = numeros.rbegin(); it != numeros.rend(); ++it) {<br>"
                "        salida << *it << std::endl;<br>"
                "    }<br>"
                "    salida.close();<br>"
                "    return 0;<br>"
                "}"
                "</code>"
            ),
            "opciones": [
                [
                    "a",
                    "Copia los números de 'datos.txt' a 'resultado.txt' en orden inverso",
                ],
                [
                    "b",
                    "Ordena los números de 'datos.txt' y los guarda en 'resultado.txt'",
                ],
                [
                    "c",
                    "Calcula la suma de los números y la escribe en 'resultado.txt'",
                ],
                ["d", "Genera un error en tiempo de ejecución"],
            ],
            "correcta": "a",
            "feedback": {
                "a": "Correcto. El programa almacena los números y los escribe en orden inverso.",
                "b": "Incorrecto. No se realiza ninguna operación de ordenamiento.",
                "c": "Incorrecto. No se calcula la suma de los números.",
                "d": "Incorrecto. El código funciona correctamente si los archivos existen.",
            },
        },
        {
            "categoria": "Lectura y Escritura de Archivos",
            "dificultad": "IT'S A DOOM",
            "enunciado": (
                "¿Qué hace el siguiente fragmento de código?<br><br>"
                "<code>"
                "#include &lt;fstream&gt;<br>"
                "#include &lt;iostream&gt;<br>"
                "#include &lt;string&gt;<br><br>"
                "int main() {<br>"
                "    std::fstream archivo;<br>"
                '    archivo.open("miarchivo.txt", std::ios::in | std::ios::out | std::ios::trunc);<br>'
                '    archivo << "Texto inicial" << std::endl;<br>'
                "    archivo.seekg(0, std::ios::beg);<br>"
                "    std::string linea;<br>"
                "    std::getline(archivo, linea);<br>"
                "    std::cout << linea << std::endl;<br>"
                "    archivo.close();<br>"
                "    return 0;<br>"
                "}"
                "</code>"
            ),
            "opciones": [
                [
                    "a",
                    "Escribe 'Texto inicial' en 'miarchivo.txt' y lo imprime en la consola",
                ],
                ["b", "Solo escribe 'Texto inicial' en 'miarchivo.txt'"],
                ["c", "Solo imprime 'Texto inicial' en la consola"],
                [
                    "d",
                    "Genera un error porque 'seekg' no es válido en 'fstream'",
                ],
            ],
            "correcta": "a",
            "feedback": {
                "a": "Correcto. El programa escribe en el archivo, mueve el puntero al inicio y lee para imprimir.",
                "b": "Incorrecto. Además de escribir, también lee e imprime el contenido.",
                "c": "Incorrecto. El contenido proviene del archivo, no de una variable en memoria.",
                "d": "Incorrecto. 'seekg' es válido y utilizado correctamente en este contexto.",
            },
        },
    ]
)

questions.extend(
    [
        {
            "categoria": "Programación Orientada a Objetos",
            "dificultad": "NIGHTMARE",
            "enunciado": (
                "¿Cuál es la salida esperada del siguiente código?<br><br>"
                "<code>"
                "class Animal {<br>"
                "public:<br>"
                '    virtual void hacerSonido() { cout << "Sonido genérico" << endl; }<br>'
                "};<br><br>"
                "class Perro : public Animal {<br>"
                "public:<br>"
                '    void hacerSonido() override { cout << "Guau" << endl; }<br>'
                "};<br><br>"
                "int main() {<br>"
                "    Animal* animal = new Perro();<br>"
                "    animal->hacerSonido();<br>"
                "    delete animal;<br>"
                "    return 0;<br>"
                "}"
                "</code>"
            ),
            "opciones": [
                ["a", "Sonido genérico"],
                ["b", "Guau"],
                ["c", "Error de compilación"],
                ["d", "Sonido genérico\nGuau"],
            ],
            "correcta": "b",
            "feedback": {
                "a": "Incorrecto. La clase 'Perro' sobrescribe el método 'hacerSonido' de 'Animal'.",
                "b": "Correcto. 'animal' es un puntero a 'Perro', y se invoca el método sobrescrito 'Guau'.",
                "c": "Incorrecto. El código compila correctamente.",
                "d": "Incorrecto. Solo se llama una vez a 'hacerSonido' en este ejemplo.",
            },
        },
        {
            "categoria": "Programación Orientada a Objetos",
            "dificultad": "HURT ME PLENTY",
            "enunciado": (
                "¿Cuál es la salida esperada del siguiente código?<br><br>"
                "<code>"
                "class Base {<br>"
                "public:<br>"
                '    Base() { cout << "Constructor Base" << endl; }<br>'
                '    virtual ~Base() { cout << "Destructor Base" << endl; }<br>'
                "};<br><br>"
                "class Derivada : public Base {<br>"
                "public:<br>"
                '    Derivada() { cout << "Constructor Derivada" << endl; }<br>'
                '    ~Derivada() { cout << "Destructor Derivada" << endl; }<br>'
                "};<br><br>"
                "int main() {<br>"
                "    Base* obj = new Derivada();<br>"
                "    delete obj;<br>"
                "    return 0;<br>"
                "}"
                "</code>"
            ),
            "opciones": [
                [
                    "a",
                    "Constructor Base\nConstructor Derivada\nDestructor Base",
                ],
                [
                    "b",
                    "Constructor Derivada\nDestructor Derivada\nDestructor Base",
                ],
                [
                    "c",
                    "Constructor Base\nConstructor Derivada\nDestructor Derivada\nDestructor Base",
                ],
                [
                    "d",
                    "Constructor Base\nDestructor Derivada\nDestructor Base",
                ],
            ],
            "correcta": "c",
            "feedback": {
                "a": "Incorrecto. Falta el 'Destructor Derivada'. El destructor virtual asegura la llamada al destructor derivado.",
                "b": "Incorrecto. El 'Constructor Base' debería ejecutarse primero.",
                "c": "Correcto. Primero se construye 'Base' y luego 'Derivada'. Los destructores se llaman en orden inverso.",
                "d": "Incorrecto. El orden de construcción y destrucción no coincide con la salida esperada.",
            },
        },
        {
            "categoria": "Programación Orientada a Objetos",
            "dificultad": "ULTRA-VIOLENCE",
            "enunciado": (
                "¿Cuál es la salida esperada del siguiente código?<br><br>"
                "<code>"
                "class A {<br>"
                "public:<br>"
                '    void mostrar() { cout << "Clase A" << endl; }<br>'
                "};<br><br>"
                "class B : public A {<br>"
                "public:<br>"
                '    void mostrar() { cout << "Clase B" << endl; }<br>'
                "};<br><br>"
                "int main() {<br>"
                "    A* obj = new B();<br>"
                "    obj->mostrar();<br>"
                "    delete obj;<br>"
                "    return 0;<br>"
                "}"
                "</code>"
            ),
            "opciones": [
                ["a", "Clase A"],
                ["b", "Clase B"],
                ["c", "Error de compilación"],
                ["d", "Clase A\nClase B"],
            ],
            "correcta": "a",
            "feedback": {
                "a": "Correcto. La función 'mostrar' no es virtual, por lo que se llama la versión de 'A'.",
                "b": "Incorrecto. 'mostrar' no es virtual, por lo que no se produce polimorfismo.",
                "c": "Incorrecto. El código compila correctamente.",
                "d": "Incorrecto. Solo se llama a 'mostrar' una vez, desde 'obj' de tipo 'A*'.",
            },
        },
        {
            "categoria": "Programación Orientada a Objetos",
            "dificultad": "ULTRANIGHTMARE",
            "enunciado": (
                "¿Cuál es la salida esperada del siguiente código?<br><br>"
                "<code>"
                "class Base {<br>"
                "public:<br>"
                '    Base() { cout << "Base construida" << endl; }<br>'
                "    virtual void saludo() = 0;<br>"
                "};<br><br>"
                "class Derivada : public Base {<br>"
                "public:<br>"
                '    Derivada() { cout << "Derivada construida" << endl; }<br>'
                '    void saludo() override { cout << "Hola desde Derivada" << endl; }<br>'
                "};<br><br>"
                "int main() {<br>"
                "    Base* obj = new Derivada();<br>"
                "    obj->saludo();<br>"
                "    delete obj;<br>"
                "    return 0;<br>"
                "}"
                "</code>"
            ),
            "opciones": [
                ["a", "Error de compilación"],
                ["b", "Base construida\nDerivada construida"],
                [
                    "c",
                    "Base construida\nDerivada construida\nHola desde Derivada",
                ],
                ["d", "Hola desde Derivada"],
            ],
            "correcta": "c",
            "feedback": {
                "a": "Incorrecto. La clase 'Derivada' implementa el método virtual puro 'saludo'.",
                "b": "Incorrecto. Falta la salida de la llamada a 'saludo'.",
                "c": "Correcto. Se construyen ambas clases, y luego se invoca 'saludo' en 'Derivada'.",
                "d": "Incorrecto. La construcción de objetos imprime mensajes también.",
            },
        },
        {
            "categoria": "Programación Orientada a Objetos",
            "dificultad": "IT'S A DOOM",
            "enunciado": (
                "¿Cuál es la salida esperada del siguiente código?<br><br>"
                "<code>"
                "class Base {<br>"
                "public:<br>"
                '    Base() { cout << "Base" << endl; }<br>'
                "};<br><br>"
                "class Derivada : public Base {<br>"
                "public:<br>"
                '    Derivada() { cout << "Derivada" << endl; }<br>'
                "};<br><br>"
                "int main() {<br>"
                "    Derivada obj;<br>"
                "    return 0;<br>"
                "}"
                "</code>"
            ),
            "opciones": [
                ["a", "Base"],
                ["b", "Derivada"],
                ["c", "Base\nDerivada"],
                ["d", "Error de compilación"],
            ],
            "correcta": "c",
            "feedback": {
                "a": "Incorrecto. También se ejecuta el constructor de 'Derivada'.",
                "b": "Incorrecto. Primero se llama al constructor de 'Base'.",
                "c": "Correcto. El constructor de 'Base' se llama antes que el de 'Derivada'.",
                "d": "Incorrecto. El código compila correctamente.",
            },
        },
    ]
)

questions.extend(
    [
        {
            "categoria": "Archivos .h y .cpp",
            "dificultad": "IT'S A DOOM",
            "enunciado": (
                "En C++, ¿cuál es la extensión estándar para un archivo de encabezado?<br><br>"
                "<code>"
                "/* Completar */"
                "</code>"
            ),
            "opciones": [
                ["a", ".cpp"],
                ["b", ".h"],
                ["c", ".exe"],
                ["d", ".txt"],
            ],
            "correcta": "b",
            "feedback": {
                "a": "Incorrecto. '.cpp' es la extensión para archivos de código fuente.",
                "b": "Correcto. '.h' es la extensión estándar para archivos de encabezado.",
                "c": "Incorrecto. '.exe' es la extensión para archivos ejecutables.",
                "d": "Incorrecto. '.txt' es la extensión para archivos de texto plano.",
            },
        },
        {
            "categoria": "Archivos .h y .cpp",
            "dificultad": "HURT ME PLENTY",
            "enunciado": (
                "En C++, ¿qué directiva de preprocesador se utiliza para incluir el contenido de un archivo de encabezado?<br><br>"
                "<code>"
                '/* Completar */ "miarchivo.h"'
                "</code>"
            ),
            "opciones": [
                ["a", "#include"],
                ["b", "#define"],
                ["c", "#ifndef"],
                ["d", "#pragma"],
            ],
            "correcta": "a",
            "feedback": {
                "a": "Correcto. '#include' se utiliza para incluir archivos de encabezado.",
                "b": "Incorrecto. '#define' se usa para definir macros.",
                "c": "Incorrecto. '#ifndef' se usa en guardas de inclusión.",
                "d": "Incorrecto. '#pragma' se usa para directivas específicas del compilador.",
            },
        },
        {
            "categoria": "Archivos .h y .cpp",
            "dificultad": "NIGHTMARE",
            "enunciado": (
                "En C++, ¿cuál es la razón principal para separar las declaraciones en archivos '.h' y las definiciones en archivos '.cpp'?<br><br>"
                "<code>"
                "// miarchivo.h<br>"
                "void funcion();<br><br>"
                "// miarchivo.cpp<br>"
                "/* Completar */<br>"
                "void funcion() {<br>"
                "    // Implementación<br>"
                "}"
                "</code>"
            ),
            "opciones": [
                ["a", "Mejorar la seguridad del código"],
                ["b", "Facilitar la compilación separada y modularidad"],
                ["c", "Reducir el uso de memoria en tiempo de ejecución"],
                ["d", "Permitir múltiples definiciones de funciones"],
            ],
            "correcta": "b",
            "feedback": {
                "a": "Incorrecto. La separación no está directamente relacionada con la seguridad.",
                "b": "Correcto. Separar declaraciones y definiciones mejora la modularidad y compilación.",
                "c": "Incorrecto. No afecta el uso de memoria en tiempo de ejecución.",
                "d": "Incorrecto. Las múltiples definiciones causan errores de enlace.",
            },
        },
        {
            "categoria": "Archivos .h y .cpp",
            "dificultad": "ULTRA-VIOLENCE",
            "enunciado": (
                "En C++, ¿cómo se previene la inclusión múltiple de un mismo archivo de encabezado?<br><br>"
                "<code>"
                "/* Completar */<br>"
                "#define MIARCHIVO_H<br>"
                "// Declaraciones<br>"
                "#endif"
                "</code>"
            ),
            "opciones": [
                ["a", "Usando directivas '#pragma once'"],
                ["b", "Usando guardas de inclusión con '#ifndef'"],
                ["c", "No es posible prevenir inclusiones múltiples"],
                ["d", "Usando comentarios para deshabilitar código"],
            ],
            "correcta": "b",
            "feedback": {
                "a": "Incorrecto. '#pragma once' es una opción, pero el ejemplo muestra guardas tradicionales.",
                "b": "Correcto. '#ifndef' se utiliza para crear guardas de inclusión.",
                "c": "Incorrecto. Sí es posible mediante guardas de inclusión.",
                "d": "Incorrecto. Los comentarios no previenen inclusiones múltiples.",
            },
        },
        {
            "categoria": "Archivos .h y .cpp",
            "dificultad": "ULTRANIGHTMARE",
            "enunciado": (
                "En C++, considerando buenas prácticas, ¿qué tipo de contenido debe ir en un archivo '.h'?<br><br>"
                "<code>"
                "// Opciones:<br>"
                "A. Implementaciones de funciones<br>"
                "B. Declaraciones de clases y funciones<br>"
                "C. Variables globales con definición<br>"
                "D. Código de la función 'main()'<br><br>"
                "/* Completar con la opción correcta */"
                "</code>"
            ),
            "opciones": [
                ["a", "Solo A y C"],
                ["b", "Solo B"],
                ["c", "B y D"],
                ["d", "Todas las anteriores"],
            ],
            "correcta": "b",
            "feedback": {
                "a": "Incorrecto. Las implementaciones y variables globales no deben estar en el '.h'.",
                "b": "Correcto. Las declaraciones de clases y funciones van en el archivo '.h'.",
                "c": "Incorrecto. 'main()' debe estar en un archivo '.cpp'.",
                "d": "Incorrecto. No es buena práctica incluir todas en el '.h'.",
            },
        },
        {
            "categoria": "Archivos .h y .cpp",
            "dificultad": "IT'S A DOOM",
            "enunciado": (
                "En C++, ¿qué sucede si incluyes una definición de función en un archivo '.h' y lo incluyes en múltiples archivos '.cpp'?<br><br>"
                "<code>"
                "// miarchivo.h<br>"
                "void funcion() { /* Implementación */ }<br><br>"
                "// archivo1.cpp<br>"
                '#include "miarchivo.h"<br><br>'
                "// archivo2.cpp<br>"
                '#include "miarchivo.h"<br><br>'
                "/* Completar con la consecuencia */"
                "</code>"
            ),
            "opciones": [
                ["a", "El programa funciona sin problemas"],
                ["b", "El compilador genera un error de sintaxis"],
                [
                    "c",
                    "El enlazador genera un error por definiciones múltiples",
                ],
                ["d", "Las funciones se sobrescriben y solo una es usada"],
            ],
            "correcta": "c",
            "feedback": {
                "a": "Incorrecto. Habrá problemas en la etapa de enlace.",
                "b": "Incorrecto. El error ocurre en el enlazador, no en el compilador.",
                "c": "Correcto. El enlazador detecta múltiples definiciones de la misma función.",
                "d": "Incorrecto. No se sobrescriben; el enlazador reporta el conflicto.",
            },
        },
        {
            "categoria": "Archivos .h y .cpp",
            "dificultad": "HURT ME PLENTY",
            "enunciado": (
                "En C++, ¿cómo se declaran las funciones inline correctamente en archivos de encabezado?<br><br>"
                "<code>"
                "/* Completar */ void funcion() {<br>"
                "    // Implementación<br>"
                "}"
                "</code>"
            ),
            "opciones": [
                [
                    "a",
                    "Usando la palabra clave 'inline' antes de la definición",
                ],
                [
                    "b",
                    "Declarando la función en el '.h' y definiéndola en el '.cpp'",
                ],
                ["c", "Colocando la función dentro de una clase"],
                [
                    "d",
                    "No es posible tener funciones inline en archivos '.h'",
                ],
            ],
            "correcta": "a",
            "feedback": {
                "a": "Correcto. 'inline' permite definir funciones en el encabezado sin errores de enlace.",
                "b": "Incorrecto. Esto no garantiza que la función sea inline.",
                "c": "Incorrecto. Esto define una función miembro, no necesariamente inline.",
                "d": "Incorrecto. Sí es posible utilizando 'inline'.",
            },
        },
        {
            "categoria": "Archivos .h y .cpp",
            "dificultad": "NIGHTMARE",
            "enunciado": (
                "En C++, al usar plantillas (templates), ¿por qué se suelen implementar en el archivo '.h' en lugar del '.cpp'?<br><br>"
                "<code>"
                "template &lt;typename T&gt;<br>"
                "/* Completar */<br>"
                "void funcionTemplate(T param) {<br>"
                "    // Implementación<br>"
                "}"
                "</code>"
            ),
            "opciones": [
                [
                    "a",
                    "Porque el compilador necesita ver la implementación para instanciar la plantilla",
                ],
                ["b", "Para mejorar la seguridad del código"],
                ["c", "Para separar claramente declaraciones y definiciones"],
                [
                    "d",
                    "No es necesario; las plantillas siempre van en el '.cpp'",
                ],
            ],
            "correcta": "a",
            "feedback": {
                "a": "Correcto. Las plantillas deben ser visibles al compilador para generar el código necesario.",
                "b": "Incorrecto. No está relacionado con la seguridad del código.",
                "c": "Incorrecto. En plantillas, las definiciones suelen ir en el '.h'.",
                "d": "Incorrecto. Las plantillas no funcionan correctamente si solo están en el '.cpp'.",
            },
        },
        {
            "categoria": "Archivos .h y .cpp",
            "dificultad": "ULTRA-VIOLENCE",
            "enunciado": (
                "En C++, ¿cuál es el propósito de utilizar '#pragma once' en un archivo de encabezado?<br><br>"
                "<code>"
                "/* Completar */<br>"
                "// Declaraciones<br>"
                "</code>"
            ),
            "opciones": [
                ["a", "Incluir el archivo una vez por proyecto"],
                [
                    "b",
                    "Prevenir múltiples inclusiones del mismo archivo durante la compilación",
                ],
                ["c", "Optimizar el código para mayor velocidad"],
                [
                    "d",
                    "Indicar al compilador que el archivo es dependiente de plataforma",
                ],
            ],
            "correcta": "b",
            "feedback": {
                "a": "Incorrecto. Se refiere a cada unidad de compilación, no al proyecto completo.",
                "b": "Correcto. '#pragma once' previene inclusiones múltiples del archivo.",
                "c": "Incorrecto. No está relacionado con la optimización de velocidad.",
                "d": "Incorrecto. No indica dependencias de plataforma.",
            },
        },
        {
            "categoria": "Archivos .h y .cpp",
            "dificultad": "ULTRANIGHTMARE",
            "enunciado": (
                "En C++, si una clase es declarada en un archivo '.h', ¿cómo se evita que los cambios en su implementación requieran recompilar todos los archivos que la incluyen?<br><br>"
                "<code>"
                "// miClase.h<br>"
                "class MiClase {<br>"
                "public:<br>"
                "    void metodoPublico();<br>"
                "private:<br>"
                "    /* Completar */<br>"
                "};"
                "</code>"
            ),
            "opciones": [
                ["a", "Usando el patrón Pimpl (Pointer to Implementation)"],
                ["b", "Declarando todos los miembros en 'public'"],
                ["c", "Es imposible evitar la recompilación en este caso"],
                ["d", "Usando macros para aislar cambios"],
            ],
            "correcta": "a",
            "feedback": {
                "a": "Correcto. El patrón Pimpl oculta la implementación y reduce dependencias.",
                "b": "Incorrecto. No afecta la necesidad de recompilación y es mala práctica.",
                "c": "Incorrecto. El patrón Pimpl puede ayudar a evitar recompilaciones innecesarias.",
                "d": "Incorrecto. Las macros no son la solución adecuada para este problema.",
            },
        },
    ]
)
