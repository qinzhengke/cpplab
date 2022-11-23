# [特 性] 实验5：基于引用来调用虚函数

所有人都知道基于指针来调用虚函数，实现多态。
但实际上使用引用也可以达到相同的目的。

```cpp
#include <cstdio>

struct Base {int x = 7; };

struct Derived : public Base { int y = 8; };

void foo(Base & obj) {
    printf("%d, %d\n", obj.x, static_cast<Derived&>(obj).y);;
}
 
int main(void) {
    Derived obj;
    foo(obj);
}
```

```
7, 8
```