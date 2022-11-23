# [规 则] 实验10：什么是名字隐藏（name hiding）？

如果派生类重载了（注意不是重写）基类的成员函数，那么该基类成员函数就无法被调用派生类对象调用，这称为名字隐藏。

意义：目前作者也不太了解名字隐藏的作用，但是如果不了解这个设计，写代码时可能会产生困惑。

```cpp
#include <iostream>

struct A { int x = 7; };

struct Base {
    void foo(int x) { std::cout << x << "\n"; }
};

struct Derived : public Base { 
    void foo(A& p) { std::cout<< p.x << "\n";}
};

int main(void) {
    Derived obj;
    
    Base base;
    base.foo("7");
    
    A a;
    obj.foo(a);
    // obj.foo(7);  // 编译报错，子对象无法调用父类方法foo(int x)
    obj.Base::foo(7);  // 正确用法
}
```