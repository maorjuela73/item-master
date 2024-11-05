questions = [
    {
        'code': '''#include &lt;iostream&gt;
#include &lt;vector&gt;

int main() {
    std::vector&lt;int&gt; numeros = {1, 2, 3, 4, 5};

    // Insertar el número 10 al inicio del vector
    numeros.insert(numeros.begin(), 10);

    // Eliminar el último elemento del vector
    numeros.pop_back();

    // Mostrar los elementos del vector
    for (int num : numeros) {
        std::cout &lt;&lt; num &lt;&lt; " ";
    }
    std::cout &lt;&lt; std::endl;

    return 0;
}''',
        'options': [
            {'letter': 'A', 'text': '1 2 3 4 5 10'},
            {'letter': 'B', 'text': '10 1 2 3 4 5'},
            {'letter': 'C', 'text': '10 1 2 3 4'},
            {'letter': 'D', 'text': '1 2 3 4'},
        ],
        'correct_option': 'C',
    },
    {
        'code': '''#include &lt;iostream&gt;

int fibonacci(int n) {
    if (n &lt;= 1)
        return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}

int main() {
    std::cout &lt;&lt; fibonacci(5) &lt;&lt; std::endl;
    return 0;
}''',
        'options': [
            {'letter': 'A', 'text': '5'},
            {'letter': 'B', 'text': '8'},
            {'letter': 'C', 'text': '13'},
            {'letter': 'D', 'text': 'Error de compilación'},
        ],
        'correct_option': 'A',
    },
    {
        'code': '''#include &lt;iostream&gt;

int main() {
    int arr[] = {10, 20, 30, 40, 50};
    int *ptr = arr;
    *(ptr + 2) = 100;
    for (int i = 0; i &lt; 5; ++i) {
        std::cout &lt;&lt; arr[i] &lt;&lt; " ";
    }
    std::cout &lt;&lt; std::endl;
    return 0;
}''',
        'options': [
            {'letter': 'A', 'text': '10 20 30 40 50'},
            {'letter': 'B', 'text': '10 20 100 40 50'},
            {'letter': 'C', 'text': '10 100 30 40 50'},
            {'letter': 'D', 'text': 'Error de compilación'},
        ],
        'correct_option': 'B',
    },
    {
        'code': '''#include &lt;iostream&gt;

int main() {
    int x = 5;
    {
        int x = 10;
        std::cout &lt;&lt; x &lt;&lt; " ";
    }
    std::cout &lt;&lt; x &lt;&lt; std::endl;
    return 0;
}''',
        'options': [
            {'letter': 'A', 'text': '5 10'},
            {'letter': 'B', 'text': '10 5'},
            {'letter': 'C', 'text': '10 10'},
            {'letter': 'D', 'text': '5 5'},
        ],
        'correct_option': 'B',
    },
    {
        'code': '''#include &lt;iostream&gt;

void func(int n) {
    if (n &lt;= 0)
        return;
    std::cout &lt;&lt; n &lt;&lt; " ";
    func(n - 2);
}

int main() {
    func(5);
    std::cout &lt;&lt; std::endl;
    return 0;
}''',
        'options': [
            {'letter': 'A', 'text': '5 3 1'},
            {'letter': 'B', 'text': '1 3 5'},
            {'letter': 'C', 'text': '5 4 3 2 1'},
            {'letter': 'D', 'text': 'Error de compilación'},
        ],
        'correct_option': 'A',
    },
    {
        'code': '''#include &lt;iostream&gt;

int main() {
    for (int i = 0; i &lt; 5; ++i) {
        if (i == 2)
            continue;
        std::cout &lt;&lt; i &lt;&lt; " ";
    }
    std::cout &lt;&lt; std::endl;
    return 0;
}''',
        'options': [
            {'letter': 'A', 'text': '0 1 2 3 4'},
            {'letter': 'B', 'text': '0 1 3 4'},
            {'letter': 'C', 'text': '2'},
            {'letter': 'D', 'text': '0 1 2 3'},
        ],
        'correct_option': 'B',
    },
    {
        'code': '''#include &lt;iostream&gt;

int factorial(int n) {
    int result = 1;
    for (int i = 2; i &lt;= n; ++i) {
        result *= i;
    }
    return result;
}

int main() {
    std::cout &lt;&lt; factorial(4) &lt;&lt; std::endl;
    return 0;
}''',
        'options': [
            {'letter': 'A', 'text': '6'},
            {'letter': 'B', 'text': '24'},
            {'letter': 'C', 'text': '120'},
            {'letter': 'D', 'text': 'Error de compilación'},
        ],
        'correct_option': 'B',
    },
    {
        'code': '''#include &lt;iostream&gt;

int main() {
    int a = 5;
    int &amp;ref = a;
    ref = 10;
    std::cout &lt;&lt; a &lt;&lt; std::endl;
    return 0;
}''',
        'options': [
            {'letter': 'A', 'text': '5'},
            {'letter': 'B', 'text': '10'},
            {'letter': 'C', 'text': '0'},
            {'letter': 'D', 'text': 'Error de compilación'},
        ],
        'correct_option': 'B',
    },
    {
        'code': '''#include &lt;iostream&gt;

void increment(int *ptr) {
    (*ptr)++;
}

int main() {
    int x = 5;
    increment(&amp;x);
    std::cout &lt;&lt; x &lt;&lt; std::endl;
    return 0;
}''',
        'options': [
            {'letter': 'A', 'text': '5'},
            {'letter': 'B', 'text': '6'},
            {'letter': 'C', 'text': 'Error de compilación'},
            {'letter': 'D', 'text': 'Comportamiento indefinido'},
        ],
        'correct_option': 'B',
    },
    {
        'code': '''#include &lt;iostream&gt;

int main() {
    int a = 2, b = 3;
    std::cout &lt;&lt; (a &amp; b) &lt;&lt; std::endl;
    return 0;
}''',
        'options': [
            {'letter': 'A', 'text': '0'},
            {'letter': 'B', 'text': '1'},
            {'letter': 'C', 'text': '2'},
            {'letter': 'D', 'text': '3'},
        ],
        'correct_option': 'C',
    },
    {
        'code': '''#include &lt;iostream&gt;

int main() {
    int arr[5] = {0};
    for (int i = 0; i &lt; 5; ++i) {
        arr[i] = i * i;
    }
    std::cout &lt;&lt; arr[3] &lt;&lt; std::endl;
    return 0;
}''',
        'options': [
            {'letter': 'A', 'text': '3'},
            {'letter': 'B', 'text': '6'},
            {'letter': 'C', 'text': '9'},
            {'letter': 'D', 'text': 'Error de compilación'},
        ],
        'correct_option': 'C',
    },
]
