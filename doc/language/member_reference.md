# [特 性] 实验3：如何定义类成员引用？

```cpp
#include <cstdio>

struct A {
    int& x;
    A(int& _x) : x(_x) { }
};

int main(void){
    int x = 7;
    A a(x);
    printf("%d\n",a.x);
}
```

运行结果：
```
7
```