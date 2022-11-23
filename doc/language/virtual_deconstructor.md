# [规 则] 实验18：为什么析构函数要声明为virtual？

析构函数声明为virtual，那么基于基类指针或者引用管理的对象，在析构的时候才会调用派生类的析构函数，否则会直接调用基类的析构函数，导致析构异常。

```cpp
#include <cstdio>

struct BaseA{
    ~BaseA(){ printf("~BaseA()\n"); }
};

struct DerivedA : public BaseA{
    ~DerivedA(){ printf("~DerivedA()\n"); }
};

struct BaseB{
    virtual ~BaseB(){ printf("~BaseB()\n"); }
};

struct DerivedB : public BaseB{
    ~DerivedB(){ printf("~DerivedB()\n"); }
};

int main(){
    BaseA *pa = new DerivedA();
    delete pa;
    BaseB *pb = new DerivedB();
    delete pb;
}
```

运行结果如下

```
~BaseA()
~DerivedB()
~BaseB()
```

显然，DerivedA的析构函数没有得到正确的执行。