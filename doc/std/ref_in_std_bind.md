# [规 则] 实验30：为什么std::bind绑定引用必须需要std::ref()？

```cpp
#include <functional>
#include <vector>
#include <cstdio>

void bar(std::function<void(int)> callback) { callback(7); }

int main(void) {
    // 希望把y作为参数传入回调函数。
    auto foo = [](int x, int& y) { y += x; };
    int y = 8;
    auto bfoo = std::bind(foo, std::placeholders::_1, y);
    bar(bfoo);
    printf("y=%d\n", y);

    auto bfoo2 = std::bind(foo, std::placeholders::_1, std::ref(y));
    bar(bfoo2);
    printf("y=%d\n", y);
}
```

运行结果如下

```
y=8
y=15
```

可以看到，直接按照普通的方法传入，是无法实现引用的目的，必须使用std::ref()才能生效，至于为什么这样，并没有细究。