# [规 则] 实验34：vector\<A>(n,A())中，A()会执行n次吗？

```cpp
#include <cstdio>
#include <vector>

int create(){
    printf("create()\n");
    static int x = 7;
    return x++;
}

int main() {
    std::vector<int> x(5,create());
    for(auto xx : x){
        printf("%d\n", xx);
    }
}

```

运行结果

```
create()
7
7
7
7
7
```

显然，答案是并没有执行n次，而是将第一次运行的结果，赋值给n个对象。