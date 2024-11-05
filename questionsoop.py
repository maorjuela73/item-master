questions = [
    {
        'code': '''#include &lt;iostream&gt;

class Animal {
public:
    void speak() {
        std::cout &lt;&lt; "Animal speaks" &lt;&lt; std::endl;
    }
};

int main() {
    Animal a;
    a.speak();
    return 0;
}''',
        'options': [
            {'letter': 'A', 'text': 'No output'},
            {'letter': 'B', 'text': 'Animal speaks'},
            {'letter': 'C', 'text': 'Error at compile time'},
            {'letter': 'D', 'text': 'Animal'},
        ],
        'correct_option': 'B',
    },
    {
        'code': '''#include &lt;iostream&gt;

class Animal {
public:
    void speak() {
        std::cout &lt;&lt; "Animal speaks" &lt;&lt; std::endl;
    }
};

class Dog : public Animal {
public:
    void speak() {
        std::cout &lt;&lt; "Dog barks" &lt;&lt; std::endl;
    }
};

int main() {
    Dog d;
    d.speak();
    return 0;
}''',
        'options': [
            {'letter': 'A', 'text': 'Animal speaks'},
            {'letter': 'B', 'text': 'Dog barks'},
            {'letter': 'C', 'text': 'Error at compile time'},
            {'letter': 'D', 'text': 'No output'},
        ],
        'correct_option': 'B',
    },
    {
        'code': '''#include &lt;iostream&gt;

class Animal {
public:
    virtual void speak() {
        std::cout &lt;&lt; "Animal speaks" &lt;&lt; std::endl;
    }
};

class Dog : public Animal {
public:
    void speak() override {
        std::cout &lt;&lt; "Dog barks" &lt;&lt; std::endl;
    }
};

int main() {
    Animal* a = new Dog();
    a-&gt;speak();
    delete a;
    return 0;
}''',
        'options': [
            {'letter': 'A', 'text': 'Animal speaks'},
            {'letter': 'B', 'text': 'Dog barks'},
            {'letter': 'C', 'text': 'Error at compile time'},
            {'letter': 'D', 'text': 'No output'},
        ],
        'correct_option': 'B',
    },
    {
        'code': '''#include &lt;iostream&gt;

class Shape {
public:
    virtual double area() = 0;
};

class Circle : public Shape {
    double radius;
public:
    Circle(double r) : radius(r) {}
    double area() override {
        return 3.14 * radius * radius;
    }
};

int main() {
    Shape* s = new Circle(5.0);
    std::cout &lt;&lt; s-&gt;area() &lt;&lt; std::endl;
    delete s;
    return 0;
}''',
        'options': [
            {'letter': 'A', 'text': '78.5'},
            {'letter': 'B', 'text': 'Error at compile time'},
            {'letter': 'C', 'text': '0'},
            {'letter': 'D', 'text': 'Undefined behavior'},
        ],
        'correct_option': 'A',
    },
    {
        'code': '''#include &lt;iostream&gt;

class Base {
public:
    Base() {
        std::cout &lt;&lt; "Base constructor" &lt;&lt; std::endl;
    }
    ~Base() {
        std::cout &lt;&lt; "Base destructor" &lt;&lt; std::endl;
    }
};

class Derived : public Base {
public:
    Derived() {
        std::cout &lt;&lt; "Derived constructor" &lt;&lt; std::endl;
    }
    ~Derived() {
        std::cout &lt;&lt; "Derived destructor" &lt;&lt; std::endl;
    }
};

int main() {
    Derived d;
    return 0;
}''',
        'options': [
            {'letter': 'A', 'text': 'Base constructor\nDerived constructor\nDerived destructor\nBase destructor'},
            {'letter': 'B', 'text': 'Derived constructor\nBase constructor\nDerived destructor\nBase destructor'},
            {'letter': 'C', 'text': 'Base constructor\nDerived constructor\nBase destructor\nDerived destructor'},
            {'letter': 'D', 'text': 'Base constructor\nDerived constructor\nBase destructor'},
        ],
        'correct_option': 'A',
    },
    {
        'code': '''#include &lt;iostream&gt;

class Number {
    int value;
public:
    Number(int v) : value(v) {}
    Number(const Number&amp; other) {
        value = other.value;
        std::cout &lt;&lt; "Copy constructor called" &lt;&lt; std::endl;
    }
    int getValue() { return value; }
};

int main() {
    Number n1(5);
    Number n2 = n1;
    std::cout &lt;&lt; n2.getValue() &lt;&lt; std::endl;
    return 0;
}''',
        'options': [
            {'letter': 'A', 'text': '5'},
            {'letter': 'B', 'text': 'Copy constructor called\n5'},
            {'letter': 'C', 'text': 'Copy constructor called\nError at runtime'},
            {'letter': 'D', 'text': 'Error at compile time'},
        ],
        'correct_option': 'B',
    },
    {
        'code': '''#include &lt;iostream&gt;

class Complex {
    double real, imag;
public:
    Complex(double r, double i) : real(r), imag(i) {}
    Complex operator+(const Complex&amp; c) {
        return Complex(real + c.real, imag + c.imag);
    }
    void display() {
        std::cout &lt;&lt; real &lt;&lt; " + " &lt;&lt; imag &lt;&lt; "i" &lt;&lt; std::endl;
    }
};

int main() {
    Complex c1(1.0, 2.0);
    Complex c2(3.0, 4.0);
    Complex c3 = c1 + c2;
    c3.display();
    return 0;
}''',
        'options': [
            {'letter': 'A', 'text': '4.0 + 6.0i'},
            {'letter': 'B', 'text': '1.0 + 2.0i'},
            {'letter': 'C', 'text': 'Error at compile time'},
            {'letter': 'D', 'text': '3.0 + 4.0i'},
        ],
        'correct_option': 'A',
    },
    {
        'code': '''#include &lt;iostream&gt;

class Box {
    double width;
public:
    Box(double w) : width(w) {}
    friend void printWidth(Box b);
};

void printWidth(Box b) {
    std::cout &lt;&lt; "Width: " &lt;&lt; b.width &lt;&lt; std::endl;
}

int main() {
    Box box(10.5);
    printWidth(box);
    return 0;
}''',
        'options': [
            {'letter': 'A', 'text': 'Width: 10.5'},
            {'letter': 'B', 'text': 'Width: 0'},
            {'letter': 'C', 'text': 'Error at compile time'},
            {'letter': 'D', 'text': 'Width: Undefined'},
        ],
        'correct_option': 'A',
    },
    {
        'code': '''#include &lt;iostream&gt;

class PrintData {
public:
    void print(int i) {
        std::cout &lt;&lt; "Printing int: " &lt;&lt; i &lt;&lt; std::endl;
    }
    void print(double f) {
        std::cout &lt;&lt; "Printing float: " &lt;&lt; f &lt;&lt; std::endl;
    }
    void print(const char* c) {
        std::cout &lt;&lt; "Printing character: " &lt;&lt; c &lt;&lt; std::endl;
    }
};

int main() {
    PrintData pd;
    pd.print(5);
    pd.print(500.263);
    pd.print("Hello C++");
    return 0;
}''',
        'options': [
            {'letter': 'A', 'text': 'Error at compile time'},
            {'letter': 'B', 'text': 'Printing int: 5\nPrinting float: 500.263\nPrinting character: Hello C++'},
            {'letter': 'C', 'text': 'Printing int: 5\nPrinting float: 500.263\nPrinting string: Hello C++'},
            {'letter': 'D', 'text': 'Printing int: 5\nPrinting double: 500.263\nPrinting character: H'},
        ],
        'correct_option': 'B',
    },
    {
        'code': '''#include &lt;iostream&gt;

class Count {
public:
    static int counter;
    Count() {
        counter++;
    }
};

int Count::counter = 0;

int main() {
    Count c1;
    Count c2;
    Count c3;
    std::cout &lt;&lt; "Total objects: " &lt;&lt; Count::counter &lt;&lt; std::endl;
    return 0;
}''',
        'options': [
            {'letter': 'A', 'text': 'Total objects: 1'},
            {'letter': 'B', 'text': 'Total objects: 2'},
            {'letter': 'C', 'text': 'Total objects: 3'},
            {'letter': 'D', 'text': 'Error at compile time'},
        ],
        'correct_option': 'C',
    },
    {
        'code': '''#include &lt;iostream&gt;

class A {
public:
    void display() {
        std::cout &lt;&lt; "Class A" &lt;&lt; std::endl;
    }
};

class B {
public:
    void display() {
        std::cout &lt;&lt; "Class B" &lt;&lt; std::endl;
    }
};

class C : public A, public B {
};

int main() {
    C obj;
    obj.display();
    return 0;
}''',
        'options': [
            {'letter': 'A', 'text': 'Class A'},
            {'letter': 'B', 'text': 'Class B'},
            {'letter': 'C', 'text': 'Error at compile time'},
            {'letter': 'D', 'text': 'No output'},
        ],
        'correct_option': 'C',
    },
    {
        'code': '''#include &lt;iostream&gt;

namespace First {
    void fun() {
        std::cout &lt;&lt; "First namespace" &lt;&lt; std::endl;
    }
}

namespace Second {
    void fun() {
        std::cout &lt;&lt; "Second namespace" &lt;&lt; std::endl;
    }
}

int main() {
    using namespace First;
    fun();
    return 0;
}''',
        'options': [
            {'letter': 'A', 'text': 'First namespace'},
            {'letter': 'B', 'text': 'Second namespace'},
            {'letter': 'C', 'text': 'Error at compile time'},
            {'letter': 'D', 'text': 'No output'},
        ],
        'correct_option': 'A',
    },
    {
        'code': '''#include &lt;iostream&gt;

template &lt;typename T&gt;
T max(T a, T b) {
    return (a &gt; b) ? a : b;
}

int main() {
    std::cout &lt;&lt; max(3, 7) &lt;&lt; std::endl;
    std::cout &lt;&lt; max(3.0, 7.0) &lt;&lt; std::endl;
    std::cout &lt;&lt; max('g', 'e') &lt;&lt; std::endl;
    return 0;
}''',
        'options': [
            {'letter': 'A', 'text': '7\n7\ng'},
            {'letter': 'B', 'text': '7\n7\ne'},
            {'letter': 'C', 'text': 'Error at compile time'},
            {'letter': 'D', 'text': '3\n3\ne'},
        ],
        'correct_option': 'A',
    },
    {
        'code': '''#include &lt;iostream&gt;

int main() {
    try {
        throw 20;
    } catch (int e) {
        std::cout &lt;&lt; "An exception occurred. Exception Nr. " &lt;&lt; e &lt;&lt; std::endl;
    }
    return 0;
}''',
        'options': [
            {'letter': 'A', 'text': 'An exception occurred. Exception Nr. 20'},
            {'letter': 'B', 'text': 'Error at compile time'},
            {'letter': 'C', 'text': 'No output'},
            {'letter': 'D', 'text': 'Program crashes'},
        ],
        'correct_option': 'A',
    },
    {
        'code': '''#include &lt;iostream&gt;

class Base {
private:
    int x;
protected:
    int y;
public:
    int z;
};

class Derived : public Base {
public:
    void display() {
        // x = 1; // Line A
        y = 2; // Line B
        z = 3; // Line C
        std::cout &lt;&lt; y &lt;&lt; " " &lt;&lt; z &lt;&lt; std::endl;
    }
};

int main() {
    Derived d;
    d.display();
    return 0;
}''',
        'options': [
            {'letter': 'A', 'text': 'Error at Line A'},
            {'letter': 'B', 'text': 'Error at Line B'},
            {'letter': 'C', 'text': 'Error at Line C'},
            {'letter': 'D', 'text': '2 3'},
        ],
        'correct_option': 'D',
    },
]
