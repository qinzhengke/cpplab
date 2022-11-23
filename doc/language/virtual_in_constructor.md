# [规 则] 实验19：为什么不要在构造和析构函数中调用虚函数？

在里面调用虚函数，是无法实现多态的目的，这可能导致和代码和预期不符，如下代码所示：

```cpp
#include <cstdio>

struct Base {
    Base() { foo(); }
    ~Base() { bar(); }
    virtual void foo() { printf("Base::foo()\n"); }
    virtual void bar() { printf("Base::bar()\n"); }
};

struct Derived : public Base {
    Derived() { foo(); }
    ~Derived() { bar(); }
    void foo() override { printf("Derived::foo()\n"); }
    void bar() override { printf("Derived::bar()\n"); }
};

int main(){
    Derived obj;
}
```

运行结果

```
Base::foo()
Derived::foo()
Derived::bar()
Base::bar()
```

可以看到，foo()和bar()的基类版本和派生类版本都被调用了一遍，并没有表现出我们所希望的多态特性。
这是因为对象在构造时，基类和派生类的构造函数会先后被调用，自然会各自调用foo()函数。
同样，派生类和基类的析构函数也会先后被调用，同样会各自调用bar()函数。

因为基类构造函数先执行，此时派生类的构造还未执行，如果调用了派生类的虚函数，访问派生类的未初始化的成员，是未定义的。
所以，不管从什么角度，在构造函数中，我们不应该，实际上也不能调用派生类虚函数。

同样的，基类析构时，派生类已经析构，如果再调用派生类的虚函数，访问已析构成员，那么访问也是非法的。