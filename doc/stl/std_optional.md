# [特 性] 实验xx：为什么需要std::optional

std::optional 是一个容器，它除了提供原始类型的值外，还提供一个是否为空的状态，在以往常常会使用另外一个标志变量来表达值是否为空或者是否合法，这里将两者进行了二合一。
在一个变量中就能知道变量是否为空。

```cpp
#include <iostream>
#include <optional>
#include <string>
 
// optional can be used as the return type of a factory that may fail
std::optional<std::string> create(bool b)
{
    if (b)
        return "Godzilla";
    return {};
}
 
// std::nullopt can be used to create any (empty) std::optional
auto create2(bool b)
{
    return b ? std::optional<std::string>{"Godzilla"} : std::nullopt;
}
 
int main()
{
    std::cout << "create(false) returned "
              << create(false).value_or("empty") << '\n';
 
    // optional-returning factory functions are usable as conditions of while and if
    if (auto str = create2(true))
        std::cout << "create2(true) returned " << *str << '\n';
}
```

以往的增加一个标志会有什么问题呢？
其实问题也不大，主要是引入了不必要的复杂性：
使用额外的状态变量会使代码变得更加复杂，因为开发者需要在获取状态和使用结果之间保持一致。

容易遗忘更新状态变量：
如果开发者忘记在获取状态的同时更新状态变量，就可能导致错误的行为。

```cpp
bool status = false; // 初始状态为非空
int value = getValue(status);

// ... 一段时间后

if (status) {
    // 这里可能会出现错误，因为 status 没有被更新
    // 变量 value 可能是一个无效的值
}
```

本人认为，为了减少这种维护和更C++化，引入一个std::optional新概念，变量平白无故多了一层封装，反而代码看起来更复杂。