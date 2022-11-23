# [规 则] 实验9：构造与析构的执行顺序是什么？

- 构造顺序：派生类构造函数（系统生成部分）->基类构造函数->派生类构造函数（用户编写部分）
- 析构顺序：派生类析构函数（系统生成部分）->派生类析构函数（用户编写部分）->基类析构函数

```cpp
#include <cstdio>

class Base{
public:
    Base(){ printf("Base()\n"); }
    virtual ~Base(){ printf("~Base()\n"); }
};

class Derived : public Base{
public:
    Derived(){ printf("Derived()\n"); }
    virtual ~Derived(){ printf("~Derived()\n"); }
};

int main(){
    Derived a;
}
```

运行结果如下

```
Base()
Derived()
~Derived()
~Base()
```