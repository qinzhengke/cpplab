# [规 则] 实验11：有了编译器返回值优化（RVO），为何还需要右值引用？

返回值优化（Return Value Optimization，简称RVO）是编译器优化的一种技术，它可以在函数返回一个临时对象时，将临时对象的构造和拷贝过程省略掉，直接将临时对象构造在调用者的栈空间中。

至少有以下几种情况不工作

- 返回的局部对象存在分支判断。
- 如果在编译时显式地禁用了优化，RVO 将不会发生。
- 调用的时候不是初始化，而是赋值。
- 被调用的函数已经编译为so文件，调用者和被调用者无法在代码层面交互，只能在更底层的链接层面交互。
- 返回的时候带有std::move()

```cpp
#include <cstdio>
#include <utility>
struct A {
    int *pointer;
    A():pointer(new int(1)) { printf("A()\n"); }

    A(A& a):pointer(new int(*a.pointer)) {
        printf("Copy A() pointer:%p\n", pointer);
    }

    A& operator=(const A&) {
        printf("A::operator=()\n");
        return *this;
    }

    A(A&& a):pointer(a.pointer) {
        a.pointer = nullptr;
        printf(" Move A()\n");
    }

    ~A(){ delete pointer; }
};

A foo() {
    A a;
    return a;
}

A foo2(bool test) {
    A a,b;
    return test ? a : b;
}

A foo3() {
    A a;
    return std::move(a);
}

int main() {
    
    {
        printf("==== RVO work ====\n");
        A obj = foo();
    }
    {
        printf("==== RVO fail #1 ====\n");
        A obj = foo2(false);
    }
    {
        printf("==== RVO fail #2 ====\n");
        A obj;
        obj = foo();
    }
    {
        printf("==== RVO fail #3 ====\n");
        A obj = foo3();
    }
}
```

编译警告如下：

```
prog.cc: In function 'A foo3()':
prog.cc:39:21: warning: moving a local object in a return statement prevents copy elision [-Wpessimizing-move]
   39 |     return std::move(a);
      |            ~~~~~~~~~^~~
prog.cc:39:21: note: remove 'std::move' call
```

运行结果如下：

```
==== RVO work ====
A()
==== RVO fail #1 ====
A()
A()
Copy A() pointer:0x23ddab0
==== RVO fail #2 ====
A()
A()
A::operator=()
==== RVO fail #3 ====
A()
 Move A()
```

显然，情况1和情况2都产生两次拷贝构造，情况3产生一次移动构造。