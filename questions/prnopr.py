preguntas_teoricas = [
    {
        "tipo": "teorica",
        "enunciado": "¿Qué método se usa en Python para obtener una representación textual de un objeto?",
        "opciones": [
            ("a", "__str__"),
            ("b", "__repr__"),
            ("c", "__format__"),
            ("d", "__call__")
        ],
        "correcta": "a"
    },
    {
        "tipo": "teorica",
        "enunciado": "¿Cuál es la principal ventaja de un diccionario sobre una lista?",
        "opciones": [
            ("a", "Permite valores duplicados"),
            ("b", "Es más rápido para búsquedas de clave"),
            ("c", "Es inmutable"),
            ("d", "Tiene menor complejidad de espacio")
        ],
        "correcta": "b"
    },
    {
        "tipo": "teorica",
        "enunciado": "¿Qué significa que un método esté decorado con @staticmethod?",
        "opciones": [
            ("a", "No recibe ni cls ni self"),
            ("b", "No puede modificar el estado de la clase"),
            ("c", "Puede acceder a otros métodos de instancia"),
            ("d", "Es una función fuera de la clase")
        ],
        "correcta": "a"
    },
    # Añade 12 preguntas más de tipo teórico
    {
        "tipo": "teorica",
        "enunciado": "¿Qué estructura de datos usarías en Python para implementar una cola (queue) de manera eficiente?",
        "opciones": [
            ("a", "Lista (list)"),
            ("b", "Tupla (tuple)"),
            ("c", "Deque de collections"),
            ("d", "Conjunto (set)")
        ],
        "correcta": "c"
    },
    {
        "tipo": "teorica",
        "enunciado": "¿Qué significa que una función sea de orden superior en Python?",
        "opciones": [
            ("a", "Que tiene mayor prioridad en las operaciones"),
            ("b", "Que acepta otras funciones como argumentos o devuelve funciones"),
            ("c", "Que está definida en un nivel superior del código"),
            ("d", "Que se ejecuta antes que otras funciones")
        ],
        "correcta": "b"
    },
    {
        "tipo": "teorica",
        "enunciado": "¿Cuál es el resultado de la expresión 5 // 2 en Python?",
        "opciones": [
            ("a", "2.5"),
            ("b", "2"),
            ("c", "3"),
            ("d", "Error de sintaxis")
        ],
        "correcta": "b"
    },
    {
        "tipo": "teorica",
        "enunciado": "¿Qué módulo estándar de Python usarías para manejar fechas y horas?",
        "opciones": [
            ("a", "datetime"),
            ("b", "time"),
            ("c", "calendar"),
            ("d", "date")
        ],
        "correcta": "a"
    },
    {
        "tipo": "teorica",
        "enunciado": "En Python, ¿qué es una comprensión de listas (list comprehension)?",
        "opciones": [
            ("a", "Una forma de crear listas a partir de otras listas usando una sintaxis concisa"),
            ("b", "Un método para entender mejor las listas"),
            ("c", "Una función que recorre una lista y devuelve otra lista"),
            ("d", "Una forma de ordenar listas al comprender su contenido")
        ],
        "correcta": "a"
    },
    {
        "tipo": "teorica",
        "enunciado": "¿Qué hace la función map(func, iterable) en Python?",
        "opciones": [
            ("a", "Aplica una función a cada elemento de un iterable y devuelve un nuevo iterable"),
            ("b", "Crea un diccionario a partir de dos iterables"),
            ("c", "Filtra elementos de un iterable basándose en una función"),
            ("d", "Devuelve un mapa geográfico de datos")
        ],
        "correcta": "a"
    },
    {
        "tipo": "teorica",
        "enunciado": "¿Cuál es la diferencia entre los operadores 'is' y '==' en Python?",
        "opciones": [
            ("a", "'is' compara identidades, '==' compara valores"),
            ("b", "'is' compara valores, '==' compara identidades"),
            ("c", "No hay diferencia, son equivalentes"),
            ("d", "'is' se usa para tipos numéricos, '==' para cadenas")
        ],
        "correcta": "a"
    },
    {
        "tipo": "teorica",
        "enunciado": "¿Qué tipo de excepción se lanza al intentar acceder a una clave inexistente en un diccionario?",
        "opciones": [
            ("a", "KeyError"),
            ("b", "IndexError"),
            ("c", "ValueError"),
            ("d", "TypeError")
        ],
        "correcta": "a"
    },
    {
        "tipo": "teorica",
        "enunciado": "¿Cuál es la salida de print('Hola' * 3) en Python?",
        "opciones": [
            ("a", "HolaHolaHola"),
            ("b", "Hola Hola Hola"),
            ("c", "Error de tipo"),
            ("d", "3")
        ],
        "correcta": "a"
    },
    {
        "tipo": "teorica",
        "enunciado": "¿Qué significa que una variable tenga un valor None en Python?",
        "opciones": [
            ("a", "Que es equivalente a cero"),
            ("b", "Que no ha sido inicializada"),
            ("c", "Que no tiene valor o ausencia de valor"),
            ("d", "Que es una cadena vacía")
        ],
        "correcta": "c"
    },
    {
        "tipo": "teorica",
        "enunciado": "¿Cuál es la función de la declaración 'with' en Python?",
        "opciones": [
            ("a", "Importar módulos"),
            ("b", "Crear bucles de iteración"),
            ("c", "Manejar contextos y asegurar liberación de recursos"),
            ("d", "Definir funciones anidadas")
        ],
        "correcta": "c"
    },
    {
        "tipo": "teorica",
        "enunciado": "¿Qué significa que una función en Python sea un generador?",
        "opciones": [
            ("a", "Que puede generar números aleatorios"),
            ("b", "Que devuelve un iterador y usa la palabra clave 'yield'"),
            ("c", "Que es una función recursiva"),
            ("d", "Que es una función anónima")
        ],
        "correcta": "b"
    }
]

preguntas_salida_codigo = [
    {
        "tipo": "codigo",
        "enunciado": """
class Person:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return f"Hello, {self.name}!"

p = Person("Alice")
print(p.greet())
        """,
        "opciones": [
            ("a", "Hello, Alice!"),
            ("b", "Hello, Person!"),
            ("c", "Hello, None!"),
            ("d", "Error")
        ],
        "correcta": "a"
    },
    {
        "tipo": "codigo",
        "enunciado": """
numbers = [1, 2, 3, 4, 5]
print(numbers[::-1][2])
        """,
        "opciones": [
            ("a", "2"),
            ("b", "3"),
            ("c", "4"),
            ("d", "1")
        ],
        "correcta": "c"
    },
    {
        "tipo": "codigo",
        "enunciado": """
a = [1, 2, 3]
b = a
b.append(4)
print(a)
        """,
        "opciones": [
            ("a", "[1, 2, 3]"),
            ("b", "[1, 2, 3, 4]"),
            ("c", "[4, 3, 2, 1]"),
            ("d", "Error")
        ],
        "correcta": "b"
    },
    {
        "tipo": "codigo",
        "enunciado": """
def func(x, y=5):
    return x + y

print(func(2))
        """,
        "opciones": [
            ("a", "7"),
            ("b", "2"),
            ("c", "Error"),
            ("d", "5")
        ],
        "correcta": "a"
    },
    {
        "tipo": "codigo",
        "enunciado": """
for i in range(3):
    print(i)
else:
    print("Done")
        """,
        "opciones": [
            ("a", "0\\n1\\n2\\nDone"),
            ("b", "0\\n1\\n2"),
            ("c", "Done"),
            ("d", "Error")
        ],
        "correcta": "a"
    },
    {
        "tipo": "codigo",
        "enunciado": """
try:
    print(1 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero")
        """,
        "opciones": [
            ("a", "Cannot divide by zero"),
            ("b", "1 / 0"),
            ("c", "ZeroDivisionError"),
            ("d", "Error")
        ],
        "correcta": "a"
    },
    {
        "tipo": "codigo",
        "enunciado": """
x = [i * 2 for i in range(3)]
print(x)
        """,
        "opciones": [
            ("a", "[0, 2, 4]"),
            ("b", "[1, 2, 3]"),
            ("c", "[2, 4, 6]"),
            ("d", "[0, 1, 2]")
        ],
        "correcta": "a"
    },
    {
        "tipo": "codigo",
        "enunciado": """
def func(a, b):
    return a if a > b else b

print(func(5, 3))
        """,
        "opciones": [
            ("a", "5"),
            ("b", "3"),
            ("c", "True"),
            ("d", "False")
        ],
        "correcta": "a"
    },
    {
        "tipo": "codigo",
        "enunciado": """
x = {'a': 1, 'b': 2}
print(x.get('c', 3))
        """,
        "opciones": [
            ("a", "3"),
            ("b", "1"),
            ("c", "2"),
            ("d", "None")
        ],
        "correcta": "a"
    },
    {
        "tipo": "codigo",
        "enunciado": """
print(bool('False'))
        """,
        "opciones": [
            ("a", "True"),
            ("b", "False"),
            ("c", "0"),
            ("d", "Error")
        ],
        "correcta": "a"
    },
    {
        "tipo": "codigo",
        "enunciado": """
def outer():
    x = 'local'
    def inner():
        nonlocal x
        x = 'nonlocal'
    inner()
    print(x)

outer()
        """,
        "opciones": [
            ("a", "nonlocal"),
            ("b", "local"),
            ("c", "Error"),
            ("d", "inner")
        ],
        "correcta": "a"
    },
    {
        "tipo": "codigo",
        "enunciado": """
import math
print(math.ceil(4.2))
        """,
        "opciones": [
            ("a", "5"),
            ("b", "4"),
            ("c", "4.2"),
            ("d", "Error")
        ],
        "correcta": "a"
    },
    {
        "tipo": "codigo",
        "enunciado": """
x = [1, 2, 3]
y = x.copy()
y.append(4)
print(len(x))
        """,
        "opciones": [
            ("a", "3"),
            ("b", "4"),
            ("c", "Error"),
            ("d", "0")
        ],
        "correcta": "a"
    },
    {
        "tipo": "codigo",
        "enunciado": """
print("Hello {0}".format("World"))
        """,
        "opciones": [
            ("a", "Hello World"),
            ("b", "Hello {0}"),
            ("c", "Hello"),
            ("d", "Error")
        ],
        "correcta": "a"
    },
    {
        "tipo": "codigo",
        "enunciado": """
a = set([1, 2, 3])
b = set([3, 4, 5])
print(a & b)
        """,
        "opciones": [
            ("a", "{3}"),
            ("b", "{1, 2, 3, 4, 5}"),
            ("c", "{}"),
            ("d", "{1, 2}")
        ],
        "correcta": "a"
    },
    {
        "tipo": "codigo",
        "enunciado": """
def func(a, L=[]):
    L.append(a)
    return L

print(func(1))
print(func(2))
        """,
        "opciones": [
            ("a", "[1]\\n[1, 2]"),
            ("b", "[1]\\n[2]"),
            ("c", "[1]\\n[1]"),
            ("d", "Error")
        ],
        "correcta": "a"
    }
]

preguntas_error = [
    {
        "tipo": "error",
        "enunciado": """
def calculate(x, y):
    return x / y

print(calculate(10, 0))
        """,
        "opciones": [
            ("a", "Línea 2: return x / y"),
            ("b", "Línea 3: print(calculate(10, 0))"),
            ("c", "Línea 1: def calculate(x, y):"),
            ("d", "No hay error")
        ],
        "correcta": "a"
    },
    {
        "tipo": "error",
        "enunciado": """
my_dict = {"a": 1, "b": 2}
print(my_dict["c"])
        """,
        "opciones": [
            ("a", 'Línea 1: my_dict = {"a": 1, "b": 2}'),
            ("b", 'Línea 2: print(my_dict["c"])'),
            ("c", "No hay error"),
            ("d", "Línea 1 y 2")
        ],
        "correcta": "b"
    },
    {
        "tipo": "error",
        "enunciado": """
def add_item(list=[]):
    list.append("new item")
    return list

print(add_item())
print(add_item())
        """,
        "opciones": [
            ("a", "Línea 1: def add_item(list=[])"),
            ("b", 'Línea 2: list.append("new item")'),
            ("c", "Línea 4: print(add_item())"),
            ("d", "No hay error")
        ],
        "correcta": "a"
    },
    {
        "tipo": "error",
        "enunciado": """
x = 10
if x = 5:
    print("x es 5")
        """,
        "opciones": [
            ("a", "Línea 2: if x = 5:"),
            ("b", 'Línea 1: x = 10'),
            ("c", 'Línea 3: print("x es 5")'),
            ("d", "No hay error")
        ],
        "correcta": "a"
    },
    {
        "tipo": "error",
        "enunciado": """
def func():
    print(message)
    message = "Hola"
func()
        """,
        "opciones": [
            ("a", "Línea 2: print(message)"),
            ("b", 'Línea 3: message = "Hola"'),
            ("c", "Línea 4: func()"),
            ("d", "No hay error")
        ],
        "correcta": "a"
    },
    {
        "tipo": "error",
        "enunciado": """
for i in range(5)
    print(i)
        """,
        "opciones": [
            ("a", "Línea 1: for i in range(5)"),
            ("b", "Línea 2: print(i)"),
            ("c", "Línea 1 y 2"),
            ("d", "No hay error")
        ],
        "correcta": "a"
    },
    {
        "tipo": "error",
        "enunciado": """
my_list = [1, 2, 3]
print(my_list[3])
        """,
        "opciones": [
            ("a", "Línea 1: my_list = [1, 2, 3]"),
            ("b", "Línea 2: print(my_list[3])"),
            ("c", "No hay error"),
            ("d", "Línea 1 y 2")
        ],
        "correcta": "b"
    },
    {
        "tipo": "error",
        "enunciado": """
import math
print(math.sine(30))
        """,
        "opciones": [
            ("a", "Línea 2: print(math.sine(30))"),
            ("b", "Línea 1: import math"),
            ("c", "Línea 1 y 2"),
            ("d", "No hay error")
        ],
        "correcta": "a"
    },
    {
        "tipo": "error",
        "enunciado": """
class MyClass:
    def __init__(self):
        self.value = 10

    def get_value(self):
        return self.vale

obj = MyClass()
print(obj.get_value())
        """,
        "opciones": [
            ("a", "Línea 5: return self.vale"),
            ("b", "Línea 2: def __init__(self):"),
            ("c", "Línea 8: print(obj.get_value())"),
            ("d", "No hay error")
        ],
        "correcta": "a"
    },
    {
        "tipo": "error",
        "enunciado": """
with open('file.txt', 'r') as f:
    content = f.read()
print(content)
        """,
        "opciones": [
            ("a", "Línea 1: with open('file.txt', 'r') as f:"),
            ("b", "Línea 2: content = f.read()"),
            ("c", "Línea 3: print(content)"),
            ("d", "No hay error")
        ],
        "correcta": "a"
    },
    {
        "tipo": "error",
        "enunciado": """
print("Hola Mundo"
        """,
        "opciones": [
            ("a", 'Línea 1: print("Hola Mundo"'),
            ("b", "No hay error"),
            ("c", "Error en tiempo de ejecución"),
            ("d", "Línea 1 y 2")
        ],
        "correcta": "a"
    },
    {
        "tipo": "error",
        "enunciado": """
def suma(a, b):
    return a + b

print(suma(5))
        """,
        "opciones": [
            ("a", "Línea 4: print(suma(5))"),
            ("b", "Línea 2: return a + b"),
            ("c", "Línea 1: def suma(a, b):"),
            ("d", "No hay error")
        ],
        "correcta": "a"
    },
    {
        "tipo": "error",
        "enunciado": """
x = "10"
y = x + 5
print(y)
        """,
        "opciones": [
            ("a", "Línea 2: y = x + 5"),
            ("b", 'Línea 1: x = "10"'),
            ("c", "Línea 3: print(y)"),
            ("d", "No hay error")
        ],
        "correcta": "a"
    },
    {
        "tipo": "error",
        "enunciado": """
lambda x: x * 2
print(x(5))
        """,
        "opciones": [
            ("a", "Línea 2: print(x(5))"),
            ("b", "Línea 1: lambda x: x * 2"),
            ("c", "Línea 1 y 2"),
            ("d", "No hay error")
        ],
        "correcta": "a"
    },
    {
        "tipo": "error",
        "enunciado": """
import random
print(random.randInt(1, 10))
        """,
        "opciones": [
            ("a", "Línea 2: print(random.randInt(1, 10))"),
            ("b", "Línea 1: import random"),
            ("c", "No hay error"),
            ("d", "Línea 1 y 2")
        ],
        "correcta": "a"
    },
    {
        "tipo": "error",
        "enunciado": """
mi_tupla = (1, 2, 3)
mi_tupla[0] = 4
        """,
        "opciones": [
            ("a", "Línea 2: mi_tupla[0] = 4"),
            ("b", "Línea 1: mi_tupla = (1, 2, 3)"),
            ("c", "No hay error"),
            ("d", "Línea 1 y 2")
        ],
        "correcta": "a"
    }
]

preguntas_pandas = [
    {
        "tipo": "pandas",
        "enunciado": "¿Cuál de las siguientes opciones se usa para filtrar un DataFrame basado en una condición en la columna 'age'?",
        "opciones": [
            ("a", "df[df['age'] > 20]"),
            ("b", "df['age' > 20]"),
            ("c", "df.loc[df['age'] > 20]"),
            ("d", "Solo a y c son correctas")
        ],
        "correcta": "d"
    },
    {
        "tipo": "pandas",
        "enunciado": "¿Cuál es el método para eliminar columnas en un DataFrame?",
        "opciones": [
            ("a", "df.drop(columns='columna')"),
            ("b", "df.remove('columna')"),
            ("c", "df.pop('columna')"),
            ("d", "a y c")
        ],
        "correcta": "a"
    },
    {
        "tipo": "pandas",
        "enunciado": "¿Qué función se usa para renombrar columnas en un DataFrame?",
        "opciones": [
            ("a", "df.rename(columns={'columna_antigua': 'columna_nueva'})"),
            ("b", "df.columns.rename({'columna_antigua': 'columna_nueva'})"),
            ("c", "df.columns = {'columna_antigua': 'columna_nueva'}"),
            ("d", "df.rename(columns='columna_antigua', name='columna_nueva')")
        ],
        "correcta": "a"
    },
    # Añade 12 preguntas más de tipo pandas
    {
        "tipo": "pandas",
        "enunciado": "¿Qué método se utiliza para eliminar filas con valores NaN en un DataFrame?",
        "opciones": [
            ("a", "df.dropna()"),
            ("b", "df.remove_na()"),
            ("c", "df.delete_na()"),
            ("d", "df.clean_na()")
        ],
        "correcta": "a"
    },
    {
        "tipo": "pandas",
        "enunciado": "¿Cómo se concatenan dos DataFrames verticalmente?",
        "opciones": [
            ("a", "pd.concat([df1, df2])"),
            ("b", "pd.concat([df1, df2], axis=1)"),
            ("c", "df1.append(df2)"),
            ("d", "a y c")
        ],
        "correcta": "d"
    },
    {
        "tipo": "pandas",
        "enunciado": "¿Qué método se usa para resetear el índice de un DataFrame?",
        "opciones": [
            ("a", "df.reset_index()"),
            ("b", "df.set_index()"),
            ("c", "df.index_reset()"),
            ("d", "df.index = 0")
        ],
        "correcta": "a"
    },
    {
        "tipo": "pandas",
        "enunciado": "¿Cómo se puede aplicar una función a cada fila de un DataFrame?",
        "opciones": [
            ("a", "df.apply(func, axis=1)"),
            ("b", "df.apply(func)"),
            ("c", "df.applymap(func)"),
            ("d", "df.map(func)")
        ],
        "correcta": "a"
    },
    {
        "tipo": "pandas",
        "enunciado": "¿Qué método permite agrupar datos en un DataFrame?",
        "opciones": [
            ("a", "df.groupby('columna')"),
            ("b", "df.aggregate('columna')"),
            ("c", "df.group('columna')"),
            ("d", "df.sort_values('columna')")
        ],
        "correcta": "a"
    },
    {
        "tipo": "pandas",
        "enunciado": "¿Cómo se calcula la media de una columna en un DataFrame?",
        "opciones": [
            ("a", "df['columna'].mean()"),
            ("b", "df.mean('columna')"),
            ("c", "df['columna'].average()"),
            ("d", "mean(df['columna'])")
        ],
        "correcta": "a"
    },
    {
        "tipo": "pandas",
        "enunciado": "¿Cuál es la forma correcta de leer un archivo CSV en pandas?",
        "opciones": [
            ("a", "pd.read_csv('archivo.csv')"),
            ("b", "pd.load_csv('archivo.csv')"),
            ("c", "pd.open_csv('archivo.csv')"),
            ("d", "pd.DataFrame('archivo.csv')")
        ],
        "correcta": "a"
    },
    {
        "tipo": "pandas",
        "enunciado": "¿Cómo se accede a las primeras 5 filas de un DataFrame?",
        "opciones": [
            ("a", "df.head()"),
            ("b", "df.tail()"),
            ("c", "df.first(5)"),
            ("d", "df.top(5)")
        ],
        "correcta": "a"
    },
    {
        "tipo": "pandas",
        "enunciado": "¿Qué método se utiliza para fusionar dos DataFrames en función de una clave común?",
        "opciones": [
            ("a", "pd.merge(df1, df2, on='clave')"),
            ("b", "df1.join(df2)"),
            ("c", "pd.concat([df1, df2])"),
            ("d", "df1.append(df2)")
        ],
        "correcta": "a"
    },
    {
        "tipo": "pandas",
        "enunciado": "¿Cómo se crea una copia independiente de un DataFrame?",
        "opciones": [
            ("a", "df.copy()"),
            ("b", "df.deepcopy()"),
            ("c", "df.clone()"),
            ("d", "df.duplicate()")
        ],
        "correcta": "a"
    },
    {
        "tipo": "pandas",
        "enunciado": "¿Cuál es el método para ordenar un DataFrame por valores de una columna?",
        "opciones": [
            ("a", "df.sort_values('columna')"),
            ("b", "df.order_by('columna')"),
            ("c", "df.sort('columna')"),
            ("d", "df.arrange('columna')")
        ],
        "correcta": "a"
    },
    {
        "tipo": "pandas",
        "enunciado": "¿Cómo se seleccionan múltiples columnas 'A' y 'B' de un DataFrame?",
        "opciones": [
            ("a", "df[['A', 'B']]"),
            ("b", "df['A', 'B']"),
            ("c", "df.loc[:, ['A', 'B']]"),
            ("d", "a y c")
        ],
        "correcta": "d"
    },
    {
        "tipo": "pandas",
        "enunciado": "¿Qué método se utiliza para transponer un DataFrame?",
        "opciones": [
            ("a", "df.T"),
            ("b", "df.transpose()"),
            ("c", "df.pivot()"),
            ("d", "a y b")
        ],
        "correcta": "d"
    }
]

questions = preguntas_teoricas + preguntas_salida_codigo + preguntas_error + preguntas_pandas
