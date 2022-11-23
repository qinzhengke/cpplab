# [特 性] 实验26：什么场景需要std::bind？

我们都知道std::bind可以实例化部分形参，将函数转变为参数更少的另一个函数，但是什么时候需要使用这样的特性呢？

这里举一个具体的例子，通常我们实现一个回调函数时，需要将一些参数传入回调函数，而回调函数的形参是固定的，我们无法修改，那么怎么传入呢？
C语言的做法是，库作者设计回调函数时，设计一个固定的void指针，用户将自己所需要的数据通过void指针进行匿名转换，在回调函数内部再转换回来。

如果库作者没有预留void指针接口，那么除了全局变量，就没有办法传入数据。

如果基于std::bind，则就不需要这些设计，定义一个函数，将非回调所需要的用户参数作为形参，并且在绑定的时候定下具体的值。
由于绑定机制，绑定后生成一个满足回调形参的新函数，传入回调，那么在实际调用中，函数会使用当初被绑定的值。

```cpp
#include <functional>
#include <vector>
#include <cstdio>

struct A {
    std::function<void(int)> foo_;
    void registCallBack(std::function<void(int)> foo) { foo_ = foo; }
    void run() { foo_(7); }
};

int main(void) {
    // 希望把y作为参数传入回调函数。
    auto foo = [](int x, int y) { printf("%d,%d\n", x, y); };
    auto bfoo = std::bind(foo, std::placeholders::_1, 8);
    A a;
    // a.registCallBack(foo);   // 编译失败，参数列表不一致
    a.registCallBack(bfoo);     // 编译成功
    a.run();
}
```

运行结果如下：

```
7,8
```

除了普通函数外，bind还可以绑定类方法，并且可以具体绑定某一个对象，使得回调过程中可以使用对象内部的变量，这样会大大方便编程。

```cpp
#include <cstdio>
#include <string>
#include <functional>

struct A {      
    void sayHello() {  
        printf("Hello: %s!\n", name.c_str());
    }           
private:  
    std::string name = "bob";  
};

void foo(std::function<void(void)> callback) {
    callback();
}

int main(void) {  
    A a;
    auto sayHello = std::bind(&A::sayHello, a);  
    foo(sayHello);
}
```

运行结果：

```
Hello: bob!
```


网上有一篇文章讲解得很好，链接：https://www.jianshu.com/p/e396c1aab4b0

将函数、成员函数和闭包转成function函数对象 将多元(n>1)函数转成一元函数或者(n-1)元函数。 bind是一种机制，可以预先把指定的可调用的实体的某些参数绑定到已有的变量，产生一个新的可调用实体。 它作为一个通用函数适配器，接收一个可调用对象，生成一个新的可调用对象来适应原对象的参数列表。

比如，存在一个这样的函数check_size，因为这是一个二元函数，当我们要将它作为find_if的参数，会出错。因为find_if只接受一元函数，那么如何解决呢？ 一个方法是Lambda表达式，还有一个方法就是使用std::bind

下面这个bind的函数只有一个占位符，即只需要传入一个参数。它将check_size的第二个参数绑定在sz上，sz的值就是check_size的第二个参数的值，而check_size第一个参数需要传入