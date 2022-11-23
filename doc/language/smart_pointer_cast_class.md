# [规 则] 实验13：指向类的智能指针如何进行类型转换？

使用static_pointer_cast或者dynamic_pointer_cast，两者本身就功能而言是一致的，都可以用来做类型转换。
不知为何，偶尔会有人将static，dynamic和up cast或者down cast绑定起来，其实两者完全没有关系。
下面的实验的代码能够证明，这里举了一个稍微复杂的多重继承的例子。

注：up cast是将派生类指针转换成基类指针，在UML图中，基类一般在上方，两者契合。反过来down cast就是将基类指针转换为派生类指针。


```cpp
#include <cstdio>
#include <memory>

struct Base {
    int x = 7;
    virtual void foo() { printf("Base::foo, %d\n", x); }
};

struct Base2 {
    int z = 9;  
    virtual void bar() { printf("Base2::bar, %d\n", z); }
};

struct Derived : public Base, Base2 {
    int y = 8;
    void foo() override { printf("Derived::foo, x:%d,y:%d\n", x, y); }
    void bar() override { printf("Derived::bar, z:%d,y:%d\n", z, y); }
};

int main(){
    auto obj = std::make_shared<Derived>();
    std::shared_ptr<Base> bp;
    std::shared_ptr<Base> b2p;
    std::shared_ptr<Derived> dp;
    
    bp = std::dynamic_pointer_cast<Base>(obj);
    dp = std::dynamic_pointer_cast<Derived>(bp);
    dp->foo();
    dp->bar();

    bp = std::static_pointer_cast<Base>(obj);
    dp = std::dynamic_pointer_cast<Derived>(bp);
    dp->foo();
    dp->bar();

    bp = std::dynamic_pointer_cast<Base>(obj);
    dp = std::static_pointer_cast<Derived>(bp);
    dp->foo();
    dp->bar();

    bp = std::static_pointer_cast<Base>(obj);
    dp = std::static_pointer_cast<Derived>(bp);
    dp->foo();
    dp->bar();
}
```

运行结果：
```
Derived::foo, x:7,y:8
Derived::bar, z:9,y:8
Derived::foo, x:7,y:8
Derived::bar, z:9,y:8
Derived::foo, x:7,y:8
Derived::bar, z:9,y:8
Derived::foo, x:7,y:8
Derived::bar, z:9,y:8
```

但是dynamic_pointer_cast能够检查转换是否合法，如果不合法，就会返回nullptr，当然，会带来额外运行开销。

实验代码如下所示：

```cpp
#include <cstdio>
#include <memory>

struct Base {
    int x = 7;
    virtual void foo() { printf("Base::foo, %d\n", x); }
};

struct Derived : public Base{
    int y = 8;
    void foo() override { printf("Derived::foo, x:%d,y:%d\n", x, y); }
};

int main(){
    auto obj = std::make_shared<Base>();
    std::shared_ptr<Derived> dp;
    
    dp = std::dynamic_pointer_cast<Derived>(obj);
    printf("%p\n", dp.get());
    if (dp == nullptr) {
        printf("down cast fail!\n");
    } else {
        dp->foo();
    }

    dp = std::static_pointer_cast<Derived>(obj);
    printf("%p\n", dp.get());
    if (dp == nullptr) {
        printf("down cast fail!\n");
    } else {
        dp->foo();
    }
}
```

运行结果如下：

```
(nil)
down cast fail!
0x230aa90
Base::foo, 7
```

显然，用一个派生类指针指向基类对象，并调用虚函数，是不合法的，也并非我们想看到的。
dynamic_pointer_cast基于RTTI技术将转换结果设为nullptr，static_pointer_cast则不会。