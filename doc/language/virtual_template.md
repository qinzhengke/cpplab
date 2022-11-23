# [规 则] 实验20：模板函数能够声明为virtual吗？

从语言的角度上说，没有什么毛病，但是实际上GCC上是做不到的，其他编译器没有测试过，下面是一条比较合理的说法：

> Templates are all about the compiler generating code at compile-time. Virtual functions are all about the run-time system figuring out which function to call at run-time.
> Once the run-time system figured out it would need to call a templatized virtual function, compilation is all done and the compiler cannot generate the appropriate instance anymore. Therefore you cannot have virtual member function templates.
> However, there are a few powerful and interesting techniques stemming from combining polymorphism and templates, notably so-called type erasure.


让我们来做实验

```cpp
#include<iostream>

struct Base {
    template<typename T>
    virtual void foo(T x) { std::cout<<"Base::foo", << x << "\n"; }
};

struct Derived {
    template<typename T>
    void foo(T x) override { std::cout<<"Derived::foo, " << x << "\n"; }
};

int main(){
    Derived obj;
    obj.foo(10.2f);
}
```

编译结果如下：

```
prog.cc:5:5: error: templates may not be 'virtual'
    5 |     virtual void foo(T x) { std::cout<<"Base::foo", << x << "\n"; }
      |     ^~~~~~~
prog.cc: In member function 'void Base::foo(T)':
prog.cc:5:53: error: expected primary-expression before '<<' token
    5 |     virtual void foo(T x) { std::cout<<"Base::foo", << x << "\n"; }
      |                                                     ^~
prog.cc: At global scope:
prog.cc:10:19: error: member template 'void Derived::foo(T)' may not have virt-specifiers
   10 |     void foo(T x) override { std::cout<<"Derived::foo, " << x << "\n"; }
      |                   ^~~~~~~~
```

GCC输出说的很明白了，template不支持virtual。

然而，我们可以有两种方法绕开。

方法一，将整个类作为模板。

```cpp
#include<iostream>

template<typename T>
struct Base {
    virtual void foo(T x) = 0;
};

template<typename T>
struct Derived : public Base<T>{
    void foo(T x) { std::cout<<"Derived::foo, " << x << "\n"; }
};

int main(){
    Base<float>* fobj = new Derived<float>();
    fobj->foo(7.1);
    
    Base<std::string>* sobj = new Derived<std::string>();
    sobj->foo("seven_dot_one");
}
```

运行结果：
```
Derived::foo, 7.1
Derived::foo, seven_dot_one
```

这种方法有一点不好，如果类很大，而需要模板化的方法，只有少数时，那么类里的所有方法都必须带有模板参数，在分离编译时很痛苦。

举个极端例子，一个类10个方法，只有1个需要模板化，那么其他9个方法也必须“陪着”模板化，分离编译时全都得加上模板参数，并且都得手动实例化，实际编码起来很麻烦。

所以我们引入方法二。

方法二，将成员函数不再定义为虚，新增虚的、非模板的接口，里面调用原来的方法。

由于新增的接口是非模板的，所以需要枚举出各种类型的接口，虽然需要手枚举，但是这也是没有办法的办法，接口函数尽量简单，这样倒也能够凑合用。

```cpp
#include<iostream>

struct Base {
    virtual void wrap_foo(float x) = 0;
    virtual void wrap_foo(std::string x) = 0;
};

struct Derived : public Base{
    template<typename T>
    void foo(T x) { std::cout<<"Derived::foo, " << x << "\n"; }
    void wrap_foo(float x) override { foo(x); }         // 尽量简单调用
    void wrap_foo(std::string x) override { foo(x); }   // 尽量简单调用
};

int main(){
    Base* obj = new Derived();
    obj->wrap_foo(7.1);
    obj->wrap_foo("seven_dot_one");
}
```

运行结果：

```
Derived::foo, 7.1
Derived::foo, seven_dot_one
```