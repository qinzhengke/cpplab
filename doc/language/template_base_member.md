# [规 则] 实验16：如何访问模板基类成员？

如果在派生类中直接访问模板基类的成员，那么编译会报错，如下所示。

```cpp
#include <iostream>

template<typename T>
struct Base {
    T x = 7;
    int y = 8;
    void foo() { std::cout << "foo()\n"; }
};

template<typename T>
struct Derived : public Base<T> { 
    Derived() {
        std::cout << y << "\n";
        foo();
    }
};

int main(void) { Derived<float> a; }
```

编译结果：
```
prog.cc: In constructor 'Derived<T>::Derived()':
prog.cc:13:22: error: 'y' was not declared in this scope
   13 |         std::cout << y << "\n";
      |                      ^
prog.cc:14:9: error: there are no arguments to 'foo' that depend on a template parameter, so a declaration of 'foo' must be available [-fpermissive]
   14 |         foo();
      |         ^~~
prog.cc:14:9: note: (if you use '-fpermissive', G++ will accept your code, but allowing the use of an undeclared name is deprecated)
```

具体为什么会这样，尚未考证（咱也不知道，咱也不敢问）。具体的解决办法是在访问时加入this指针。

```cpp
#include <iostream>

template<typename T>
struct Base {
    T x = 7;
    int y = 8;
    void foo() { std::cout << "foo()\n"; }
};

template<typename T>
struct Derived : public Base<T> { 
    Derived() {
        std::cout << this->y << "\n";
        this->foo();
    }
};

int main(void) { Derived<float> a; }
```

运行结果如下：

```
8
foo()
```