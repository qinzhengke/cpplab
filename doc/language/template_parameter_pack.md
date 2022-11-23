# [特 性] 实验8：模板参数包（template paramter pack，可变长模板参数）的使用场景是什么？

一个非常典型的案例就是std::vector::emplace_back()，这个函数为了减少向容器插入对象时的构造次数，可以不接受对象本身，而是接受对象构造所需的参数，在内部再进行构造。

而vector是容器，它所存储的类型是无法预先知道的，当然其构造函数的形参个数和类型也是无法知道。

在完全抽象的前提下，我们需要完成emplace_back的逻辑，就必须借助模板参数包。

我们在这里实现一个简单的MyVector，固定容量大小为5，实现一个简单的emplace_back和at接口。

```cpp
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>

template<typename T>
struct MyVector {
    int size = 0;
    T* data = nullptr;
    MyVector() { data = (T*)malloc(5 * sizeof(T)); }

    template<typename ... Args>
    void emplace_back(Args ... args) { new (data + (size++)) T(args...); }

    T* at(int idx) { return data + idx; }
    
};

struct A {
    int x = 7;
    A(int _x) : x(_x) { }
};

struct B {
    float x = 7.0;
    std::string y = "seven";
    B(float _x, std::string _y) : x(_x), y(_y) { }
};

int main(void) {
    MyVector<A> va;
    va.emplace_back(5);
    va.emplace_back(8);
    for(int i=0; i<va.size; i++) std::cout<<va.at(i)->x << "\n";

    std::cout<<"====\n";
    
    MyVector<B> vb;
    vb.emplace_back(1, "one");
    vb.emplace_back(4, "four");
    vb.emplace_back(9, "nine");
    for(int i=0; i<vb.size; i++) std::cout<<vb.at(i)->x << "," << vb.at(i)->y << "\n";
}

```

运行结果：

```
5
8
====
1,one
4,four
9,nine
```

显然，我们实现了我们想要的功能，容器能够装在不同的类型，内存是连续的，并且每次emplace_back，对象也只构造了一次。