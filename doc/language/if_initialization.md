[TODO][语法糖] if初始化语句

c++17 支持在 if 的判断语句之前增加一个初始化语句，将仅用于 if 语句内部的变量声明在 if 内，有助于提升代码的可读性。且对于 lock/iterator 等涉及并发/RAII 的类型更容易保证程序的正确性。

```cpp
// c++ 17
std::map<int, std::string> m;
std::mutex mx;
extern bool shared_flag; // guarded by mx
int demo()
{
    if (auto it = m.find(10); it != m.end()) { return it->second.size(); }
    if (char buf[10]; std::fgets(buf, 10, stdin)) { m[0] += buf; }
    if (std::lock_guard lock(mx); shared_flag) { unsafe_ping(); shared_flag = false; }
    if (int s; int count = ReadBytesWithSignal(&s)) { publish(count); raise(s); }
    if (const auto keywords = {"if", "for", "while"};
        std::ranges::any_of(keywords, [&tok](const char* kw) { return tok == kw; }))
    {
        std::cerr << "Token must not be a keyword\n";
    }
}
```