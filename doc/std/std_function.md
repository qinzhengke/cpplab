# [特 性] 实验28：有了函数指针，为什么还需要std::function？


```cpp
#include <functional>
#include <vector>
#include <cstdio>

// 传统C函数
int c_function(int a, int b) { return a + b; }

// 仿函数
struct Functor {
    int operator()(int a, int b) { return a + b; }
};

int main(void)
{
    Functor functor;
    std::vector<std::function<int(int, int)>> callables;

    callables.push_back(c_function);
    callables.push_back(functor);
    callables.push_back([](int x, int y)->int{ return x + y; });

    // 最关键的地方，可以把不同形式的函数抽象成数组进行调用，和函数指针功能一样。
    for (const auto& e : callables) printf("%d\n", e(3,4));
}
```