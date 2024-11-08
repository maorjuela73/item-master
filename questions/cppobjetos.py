questions = [
    {
        "categoria": "Programación Orientada a Objetos",
        "dificultad": "IT'S A DOOM",
        "enunciado": "¿Cuál de los siguientes es uno de los cuatro pilares de la programación orientada a objetos?",
        "opciones": [
            ["a", "Iteración"],
            ["b", "Recursión"],
            ["c", "Herencia"],
            ["d", "Compilación"]
        ],
        "correcta": "c",
        "feedback": {
            "a": "Incorrecto. La iteración es una estructura de control, no un pilar de la POO.",
            "b": "Incorrecto. La recursión es una técnica de programación, no un pilar de la POO.",
            "c": "Correcto. La herencia es uno de los cuatro pilares de la POO.",
            "d": "Incorrecto. La compilación es un proceso de traducción de código, no un pilar de la POO."
        }
    },
    {
        "categoria": "Encapsulación",
        "dificultad": "HURT ME PLENTY",
        "enunciado": "En C++, ¿cuál es la palabra clave utilizada para especificar que los miembros de una clase son accesibles solo dentro de la clase misma?",
        "opciones": [
            ["a", "public"],
            ["b", "private"],
            ["c", "protected"],
            ["d", "friend"]
        ],
        "correcta": "b",
        "feedback": {
            "a": "Incorrecto. 'public' permite acceso desde cualquier lugar.",
            "b": "Correcto. 'private' restringe el acceso solo a la clase misma.",
            "c": "Incorrecto. 'protected' permite acceso desde clases derivadas.",
            "d": "Incorrecto. 'friend' es una declaración que permite acceso privado a otra clase o función."
        }
    },
    {
        "categoria": "Abstracción",
        "dificultad": "ULTRA-VIOLENCE",
        "enunciado": "¿Cómo se declara una clase abstracta en C++?",
        "opciones": [
            ["a", "Definiendo al menos un método virtual puro."],
            ["b", "Usando la palabra clave 'abstract' antes de la clase."],
            ["c", "Heredando de la clase 'Abstract'."],
            ["d", "No es posible crear clases abstractas en C++."]
        ],
        "correcta": "a",
        "feedback": {
            "a": "Correcto. Un método virtual puro se declara con '= 0'.",
            "b": "Incorrecto. C++ no tiene una palabra clave 'abstract'.",
            "c": "Incorrecto. No existe una clase 'Abstract' por defecto en C++.",
            "d": "Incorrecto. Sí es posible mediante métodos virtuales puros."
        }
    },
    {
        "categoria": "Herencia",
        "dificultad": "NIGHTMARE",
        "enunciado": "¿Cuál es la sintaxis correcta para indicar que una clase 'Perro' hereda públicamente de una clase 'Animal' en C++?",
        "opciones": [
            ["a", "`class Perro : Animal { };`"],
            ["b", "`class Perro -> public Animal { };`"],
            ["c", "`class Perro : public Animal { };`"],
            ["d", "`class Perro(Animal) { };`"]
        ],
        "correcta": "c",
        "feedback": {
            "a": "Incorrecto. Falta especificar el modo de herencia 'public'.",
            "b": "Incorrecto. La sintaxis de herencia no utiliza '->'.",
            "c": "Correcto. Esta es la sintaxis correcta para herencia pública.",
            "d": "Incorrecto. Esta no es la sintaxis correcta en C++."
        }
    },
    {
        "categoria": "Polimorfismo",
        "dificultad": "ULTRANIGHTMARE",
        "enunciado": "En C++, ¿cómo se logra el polimorfismo en tiempo de ejecución?",
        "opciones": [
            ["a", "Usando funciones sobrecargadas."],
            ["b", "Usando plantillas (templates)."],
            ["c", "Usando métodos virtuales y punteros o referencias a clases base."],
            ["d", "Usando macros preprocesador."]
        ],
        "correcta": "c",
        "feedback": {
            "a": "Incorrecto. La sobrecarga es polimorfismo en tiempo de compilación.",
            "b": "Incorrecto. Las plantillas también son polimorfismo en tiempo de compilación.",
            "c": "Correcto. Los métodos virtuales permiten polimorfismo dinámico.",
            "d": "Incorrecto. Los macros no proporcionan polimorfismo."
        }
    },
    {
        "categoria": "Visibilidad",
        "dificultad": "IT'S A DOOM",
        "enunciado": "¿Cuál es el modificador de acceso predeterminado para los miembros de una clase en C++?",
        "opciones": [
            ["a", "public"],
            ["b", "private"],
            ["c", "protected"],
            ["d", "internal"]
        ],
        "correcta": "b",
        "feedback": {
            "a": "Incorrecto. 'public' es el modificador predeterminado en 'struct', no en 'class'.",
            "b": "Correcto. En 'class', los miembros son 'private' por defecto.",
            "c": "Incorrecto. 'protected' no es el modificador predeterminado.",
            "d": "Incorrecto. 'internal' no es un modificador de acceso en C++."
        }
    },
    {
        "categoria": "Atributos y Métodos",
        "dificultad": "HURT ME PLENTY",
        "enunciado": "En C++, ¿cómo se declara un método constante que no modifica los miembros de la clase?",
        "opciones": [
            ["a", "`void metodo() const { }`"],
            ["b", "`const void metodo() { }`"],
            ["c", "`void const metodo() { }`"],
            ["d", "`void metodo() { } const`"]
        ],
        "correcta": "a",
        "feedback": {
            "a": "Correcto. El 'const' después de los paréntesis indica un método constante.",
            "b": "Incorrecto. 'const' antes del tipo de retorno no hace el método constante.",
            "c": "Incorrecto. El orden es incorrecto y no hace el método constante.",
            "d": "Incorrecto. La posición de 'const' es incorrecta."
        }
    },
    {
        "categoria": "Encapsulación",
        "dificultad": "ULTRA-VIOLENCE",
        "enunciado": "¿Qué mecanismo en C++ se utiliza para restringir el acceso directo a los datos de una clase?",
        "opciones": [
            ["a", "Herencia múltiple"],
            ["b", "Constructores"],
            ["c", "Modificadores de acceso (public, private, protected)"],
            ["d", "Sobrecarga de operadores"]
        ],
        "correcta": "c",
        "feedback": {
            "a": "Incorrecto. La herencia múltiple no se utiliza para restringir acceso.",
            "b": "Incorrecto. Los constructores inicializan objetos pero no restringen acceso.",
            "c": "Correcto. Los modificadores de acceso controlan la visibilidad de los miembros.",
            "d": "Incorrecto. La sobrecarga de operadores modifica el comportamiento de operadores."
        }
    },
    {
        "categoria": "Herencia",
        "dificultad": "ULTRANIGHTMARE",
        "enunciado": "En C++, si una clase derivada necesita llamar al constructor de su clase base que toma argumentos, ¿cómo se hace?",
        "opciones": [
            ["a", "No es posible llamar al constructor de la clase base con argumentos."],
            ["b", "En el cuerpo del constructor de la clase derivada, llamando `Base( argumentos );`"],
            ["c", "Usando una lista de inicialización: `Derivada( args ) : Base( args ) { }`"],
            ["d", "Usando la palabra clave `super`: `super( args );`"]
        ],
        "correcta": "c",
        "feedback": {
            "a": "Incorrecto. Sí es posible llamar al constructor de la clase base con argumentos.",
            "b": "Incorrecto. La sintaxis es incorrecta para llamar al constructor base.",
            "c": "Correcto. La lista de inicialización permite llamar al constructor base con argumentos.",
            "d": "Incorrecto. 'super' no es una palabra clave en C++."
        }
    },
    {
        "categoria": "Polimorfismo",
        "dificultad": "NIGHTMARE",
        "enunciado": "¿Qué palabra clave se utiliza en C++ para evitar que una clase sea heredada?",
        "opciones": [
            ["a", "sealed"],
            ["b", "final"],
            ["c", "override"],
            ["d", "static"]
        ],
        "correcta": "b",
        "feedback": {
            "a": "Incorrecto. 'sealed' es usado en otros lenguajes como C#, no en C++.",
            "b": "Correcto. 'final' previene la herencia de una clase o método.",
            "c": "Incorrecto. 'override' se utiliza para sobreescribir métodos virtuales.",
            "d": "Incorrecto. 'static' indica un miembro de clase compartido, no afecta la herencia."
        }
    }
]
