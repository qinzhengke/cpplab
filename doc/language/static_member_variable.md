# [规 则] 实验14：如何定义静态成员变量？

```cpp
#include <cstdio>

class A{
    public:
    A(){}
    static int count;
};
int A::count = 0;

int main(void){
    A a;
    printf("%d\n",a.count);
    return 0;
}
```

运行结果：

```
0
```