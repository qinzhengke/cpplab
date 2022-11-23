# [特 性] 实验1：如何优雅地拷贝基类指针指向的派生类对象？

```cpp
#include <iostream>

struct Base {
    virtual Base* clone() const = 0;
};

struct Derived : public Base {
    int y = 7;
    Derived* clone() const {
        Derived* that = new Derived(*this);
        *that = *this;
        return that;
    }

};

void foo(const Base* p) {
    Derived* dp = static_cast<Derived*>(p->clone());
    dp->y = 8;
    printf("%d\n", dp->y);
}

int main(){
    Base *p = new Derived();
    foo(p);
}
```

显然传进来的是一个const Base*指针，我们不能改变其内容，由于算法需要，我们拷贝一份对象，然后再进行写操作。

运行结果如下：

```
8
```