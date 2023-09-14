# [特 性] 实验27：std::forward是什么，为什么需要它？

在泛型编程中，我们经常要写能处理不同引用类型的通用代码。这时候 std::forward 就变得非常有用了。它的作用是保持传递的参数的原始引用类型（左值引用或右值引用）。

```cpp
template <typename T>
void wrapper(T&& arg) {
    // 在这里我们希望将 arg 传递给其他函数
    // 但是我们想保持 arg 的原始引用类型
    other_function(std::forward<T>(arg));
}
```

在这个例子中，wrapper 是一个模板函数，它接受一个通用引用（universal reference） T&& 作为参数。我们希望将这个参数传递给 other_function，但是我们希望保持 arg 的原始引用类型（左值引用或右值引用）。

如果我们直接使用 arg，那么传递给 other_function 的将会是一个左值引用，即使 arg 本身是一个右值引用。这会导致不正确的行为。

相反，我们使用 std::forward<T>(arg)，它会根据 arg 的原始引用类型将其传递给 other_function，从而保持了参数的原始性质。

总的来说，std::forward 用于在泛型代码中正确地传递参数，以保持参数的原始引用类型，避免不必要的拷贝，并提升性能。

std::forward是怎么实现保持原有的引用类型的？

T& & 折叠成 T&
T&& & 折叠成 T&
T& && 折叠成 T&
T&& && 折叠成 T&&
现在让我们看看 std::forward 的一个简化实现：

```cpp
template <typename T>
T&& forward(typename std::remove_reference<T>::type& arg) noexcept {
    return static_cast<T&&>(arg);
}
```

这里的关键是 static_cast<T&&>(arg)。这个强制类型转换将 arg 强制转换成 T&& 类型，其中 T 是 std::forward 的模板参数。因为我们知道 arg 的原始类型是 T&&（通过模板参数 T 推导得到），所以这个类型转换会保持 arg 的原始引用类型。

这样，当你在调用 std::forward 时，它会将参数按照原始的引用类型传递给其他函数。

需要注意的是，std::remove_reference 是一个模板元编程工具，用于移除类型中的引用部分。这里用它来确保我们获得的 T 是没有引用的版本。

总的来说，std::forward 的实现基于类型转换和引用折叠的特性，通过正确的类型转换来保持参数的原始引用类型。