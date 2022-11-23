# [特 性] 实验31：push_back vs emplace_back

一些初学者会简单的认为push_back()会产生一次拷贝构造，emplace_back()会产生一次移动构造，因而后者效率更高，这其实是不正确的。

push_back同样支持右值引入作为形参，也就是支持移动语义。

来看push_back的接口声明，显然它可以是以接受右值的，只要接受对象定义了移动构造，那么push_back就会调用移动构造。

```cpp
void push_back( const T& value );
constexpr void push_back( const T& value );
void push_back( T&& value );
constexpr void push_back( T&& value );
```

emplace_back的不同之处在于它并非接受对象作为形参，而是接受对象的构造参数，作为形参，然后在emplace_back内部进行对象的构造。
其核心作用在于能够省去一次拷贝构造或者移动构造。

这里做两个实验，实验一让push_back接收右值对象，结果确实触发了移动构造。
实验二比较push_back和emplace_back，显然，前者出现了两次构造，后者只出现一次构造。

```cpp
#include <string>
#include <vector>
#include <cstdio>

struct A {
    std::string name;
    size_t len;
    char* buf = NULL;
    A(std::string _name, int _len) : name(_name), len(_len) { 
        buf = new char[len];
        printf("A(%s)\n", name.c_str());
    }
    A(const A& a) { 
        name = a.name;
        len = a.len;
        buf = new char[len];
        memcpy(buf, a.buf, len);
        printf("A(%s) copy\n", name.c_str());
    }
    A(A&& a) {
        name  = a.name;
        len = a.len;
        buf = a.buf;
        a.buf = NULL;   // 这里很关键，需要修改旧对象的内容，完成资源管理权的移交
        printf("A(%s) move\n", name.c_str());
    }
    ~A() { if(buf) delete buf; }
};

int main() {
    printf("===[1]===\n");
    {
        A a("1", 100);
        printf("a.buf:%p\n", a.buf);
        std::vector<A> v;
        v.reserve(5);   // 预先申请足够的内存，否则插入时会因为内存重分配而触发额外的构造
        v.push_back(a);
        v.push_back(std::move(a));
        v.push_back(A("2", 200));
        printf("a.buf:%p, v[0].buf:%p, v[1].buf:%p\n", a.buf, v[0].buf, v[1].buf);
    }
    printf("===[2]===\n");
    {
        std::vector<A> v;
        v.reserve(5);
        v.push_back(A("1", 100));
        v.emplace_back("2", 200);
    }
}
```

运行结果如下

```
===[1]===
A(1)
a.buf:0x501138
A(1) copy
A(1) move
A(2)
A(2) move
a.buf:0, v[0].buf:0x501208, v[1].buf:0x501138
===[2]===
A(1)
A(1) move
A(2)
```