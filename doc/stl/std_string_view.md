[TODO][特 性]实验xx：std::string_view

std::string_view顾名思义是字符串的“视图”，类成员变量包含两个部分：字符串指针和字符串长度，std::string_view 涵盖了 std::string 的所有只读接口。std::string_view 对字符串不具有所有权，且兼容 std::string 和 const char*两种类型。

c++17 之前，我们处理只读字符串往往使用const std::string&，std::string有两点性能优势:

兼容两种字符串类型，减少类型转换和内存分配。如果传入的是明文字符串const char*, const std::string&需要进行一次内存分配，将字符串拷贝到堆上，而std::string_view则可以避免。
在处理子串时，std::string::substr也需要进行拷贝和分配内存，而std::string_view::substr则不需要，在处理大文件解析时，性能优势非常明显。


```cpp
// string_view的remove_prefix比const std::string&的快了15倍
string remove_prefix(const string &str) {
  return str.substr(3);
}
string_view remove_prefix(string_view str) {
  str.remove_prefix(3);
  return str;
}
static void BM_remove_prefix_string(benchmark::State& state) {
  std::string example{"asfaghdfgsghasfasg3423rfgasdg"};
  while (state.KeepRunning()) {
    auto res = remove_prefix(example);
    // auto res = remove_prefix(string_view(example)); for string_view
    if (res != "aghdfgsghasfasg3423rfgasdg") {
      throw std::runtime_error("bad op");
    }
  }
}
```