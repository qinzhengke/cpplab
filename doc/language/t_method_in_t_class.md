# [规 则] 实验15：模板类中的模板方法如何定义？

当类和方法有不同的模板参数时，在实现部分，模板参数顺序要正确，才能编译通过。
这本身不是啥很有价值的东西，但是如果不知道，编译出错时，可能会造成困惑。

```cpp
#include <iostream>

template<typename T1>
struct A {
    T1 x = 7;
    template<typename T2>
    void foo(T2 b); 
};

template<typename T2> 
template<typename T1>
void A<T1>::foo(T2 b) { 
    std::cout << b << "\n";
}

int main(void) {
    A<float> a;
    a.foo(1.2);
}

```
编译结果：

```
prog.cc:12:21: error: invalid use of incomplete type 'struct A<T1>'
   12 | void A<T1>::foo(T2 b) {
      |                     ^
prog.cc:4:8: note: declaration of 'struct A<T1>'
    4 | struct A {
      |        ^
```

但如果是以下顺序，就没有问题

```cpp
#include <iostream>

template<typename T1>
struct A {
    T1 x = 7;
    template<typename T2>
    void foo(T2 b); 
};

template<typename T1> 
template<typename T2>
void A<T1>::foo(T2 b) { 
    std::cout << b << "\n";
}

int main(void) {
    A<float> a;
    a.foo(1.2);
}
```

运行结果：

```
1.2
```