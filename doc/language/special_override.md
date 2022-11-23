# [特 性] 实验7：重写（override）操作一定要虚函数形参和返回值完全一样吗？

不一定的，如果派生类虚函数的参数或者返回值包含派生类本身的指针，则同样视为重写。

```cpp
#include <iostream>
#include <cstdio>

struct Base { virtual Base * clone() = 0; };

struct Derived : Base{
    Derived(){ printf("Derived()\n");}
    Derived * clone() override { return new Derived();} //确实是override
};

int main() {
    Derived d;
    d.clone();
}
```

运行结果

```
Derived()
Derived()
```

这样的好处是：派生类重写成员函数的时候，不在需要内部一个强行的指针转换，在重写的成员函数数量比较多的时候，还是挺能节省时间的。

遗憾的是，如果这些指针被shared_ptr封装，就不能这样写了。