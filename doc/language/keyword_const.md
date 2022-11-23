# [特 性] 实验2：const关键字有什么作用？

1. 变量、指针、引用由const修饰时，它们相关的变量都无法被修改。

```cpp
#include <cstdio>
 
int main(void) {
    {
        const int a = 0;
        a = 1;
    }

    {
        int a = 0;
        const int& r = a;
        r = 1;
    }

    {
        int* a = new int[10];
        const int*p = a;
        p[0] = 1;
    }

}
```

编译结果：

```
prog.cc: In function 'int main()':
prog.cc:6:11: error: assignment of read-only variable 'a'
    6 |         a = 1;
      |         ~~^~~
prog.cc:12:11: error: assignment of read-only reference 'r'
   12 |         r = 1;
      |         ~~^~~
prog.cc:18:14: error: assignment of read-only location '* p'
   18 |         p[0] = 1;
      |         ~~~~~^~~
```

修饰指针时，const放在int前面，表示指向内容不能被修改，const放在类型后面，表示指针的指向不能被修改。

```cpp
#include <cstdio>
 
int main(void) {
    {
        int a[3] = {1,2,3}, b[3] = {4,5,6};
        const int* p = a;
        p = b;  // OK
        printf("%d\n", p[0]);
    }

    {
        int a[3] = {1,2,3}, b[3] = {4,5,6};
        const int* const p = a;
        p = b;  // Error
    }
}
```

编译结果

```
prog.cc: In function 'int main()':
prog.cc:14:11: error: assignment of read-only variable 'p'
   14 |         p = b;
      |         ~~^~~
```

2. 修饰方法时，方法内部不允许修改成员变量。

```cpp
#include <cstdio>

struct A {
    int x = 7;
    void foo () const { x = 8; }
};
 
int main(void) {
    A a;
    a.foo();
}
```

编译结果：

```
prog.cc: In member function 'void A::foo() const':
prog.cc:5:27: error: assignment of member 'A::x' in read-only object
    5 |     void foo () const { x = 8; }
      |                         ~~^~~
```

3. 修饰对象时，无法修改对象的成员变量，只能调用const修饰的方法。

```cpp
#include <cstdio>

struct A {
    int x = 7;
    void foo () { x = 8; }
    void bar () const { printf("%d\n", x); }
};
 
int main(void) {
    const A a;
    a.foo();    // Error
    a.bar();    // OK
}
```

编译结果

```
prog.cc: In function 'int main()':
prog.cc:11:10: error: passing 'const A' as 'this' argument discards qualifiers [-fpermissive]
   11 |     a.foo();    // Error
      |     ~~~~~^~
prog.cc:5:10: note:   in call to 'void A::foo()'
    5 |     void foo () { x = 8; }
      |          ^~~7
```