[特 性] 实验xx：std::any

std::any是一个可以存储任何可拷贝类型的容器，C 语言中通常使用void*实现类似的功能，与void*相比，std::any具有两点优势：

- std::any更安全：在类型 T 被转换成void*时，T 的类型信息就已经丢失了，在转换回具体类型时程序无法判断当前的void*的类型是否真的是 T，容易带来安全隐患。而std::any会存储类型信息，std::any_cast是一个安全的类型转换。
- std::any管理了对象的生命周期，在std::any析构时，会将存储的对象析构，而void*则需要手动管理内存。

std::any应当很少是程序员的第一选择，在已知类型的情况下，std::optional, std::variant和继承都是比它更高效、更合理的选择。只有当对类型完全未知的情况下，才应当使用std::any，比如动态类型文本的解析或者业务逻辑的中间层信息传递。


```cpp
#include <any>
#include <iostream>
 
int main()
{
    std::cout << std::boolalpha;
 
    // any type
    std::any a = 1;
    std::cout << a.type().name() << ": " << std::any_cast<int>(a) << '\n';
    a = 3.14;
    std::cout << a.type().name() << ": " << std::any_cast<double>(a) << '\n';
    a = true;
    std::cout << a.type().name() << ": " << std::any_cast<bool>(a) << '\n';
 
    // bad cast
    try
    {
        a = 1;
        std::cout << std::any_cast<float>(a) << '\n';
    }
    catch (const std::bad_any_cast& e)
    {
        std::cout << e.what() << '\n';
    }
 
    // has value
    a = 2;
    if (a.has_value())
        std::cout << a.type().name() << ": " << std::any_cast<int>(a) << '\n';
 
    // reset
    a.reset();
    if (!a.has_value())
        std::cout << "no value\n";
 
    // pointer to contained data
    a = 3;
    int* i = std::any_cast<int>(&a);
    std::cout << *i << '\n';
}
```

```
int: 1
double: 3.14
bool: true
bad any_cast
int: 2
no value
3
```