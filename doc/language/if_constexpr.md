[TODO][特 性]实验：if_constexpr

if constexpr 语句是编译期的 if 判断语句，在 C++17 以前做编译期的条件判断往往通过复杂SFINAE机制或模版重载实现，甚至嫌麻烦的时候直接放到运行时用 if 判断，造成性能损耗，if constexpr 大大缓解了这个问题。比如我想实现一个函数将不同类型的输入转化为字符串，在 c++17 之前需要写三个函数去实现，而 c++17 只需要一个函数。

```cpp
// pre c++17
template <typename T>
std::string convert(T input){
    return std::to_string(input);
}
// const char*和string进行特殊处理
std::string convert(const char* input){
    return input;
}
std::string convert(std::string input){
    return input;
}
// c++17
template <typename T>
std::string convert(T input) {
    if constexpr (std::is_same_v<T, const char*> ||
                  std::is_same_v<T, std::string>) {
        return input;
    } else {
        return std::to_string(input);
    }
}
```