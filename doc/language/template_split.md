# [规 则] 实验17：如何实现模板分离编译？

分离编译是指将想普通函数那样，将声明放到头文件，将实现放到cpp文件。
那么模板函数可以这样编译吗？

```cpp
// lib.hh
template<typename T>
void foo(T x);

// lib.cc
#include "lib.hh"
#include <cstdio>
template<typename T>
void foo(T x) { printf("%f\n", x); }

// main.cc
#include "lib.hh"
int main(){
    foo(1.0);
    foo(2.0f);
}
```

编译结果：

```
/usr/bin/ld: /tmp/ccEoyiDS.o: in function `main':
/home/jail/prog.cc:4: undefined reference to `void foo<double>(double)'
/usr/bin/ld: /home/jail/prog.cc:5: undefined reference to `void foo<float>(float)'
collect2: error: ld returned 1 exit status
```

结果是编译出错，这是因为函数目标并非函数，它只有实例化的时候，才会依据具体的类型，展开为具体的函数。
显然，这里将lib.cc编译为lib.obj时，lib.obj实际上是空的，所以链接时才会提示找不到。

那么能否分离式编译呢？

回答：对于可以预先枚举的类型，例如int，float，string等，以及不允许调用端扩展的自定义模板参数，例如类或者枚举，是可以做到的。

对于不可枚举的，并且支持调用端扩展的，是无法做到的，例如vector<T>中，无法知道、也无法限制用户使用的T是什么类型。

对于第一种情况，根据以下代码来进行分离式的编译

```cpp
// lib.hh
#pragma once
template<typename T>
void foo(T x);

// lib.cc
#include "lib.hh"
#include <cstdio>

template<typename T>
void foo(T x) { printf("%f\n", x); }

template void foo(float x);
template void foo(double x);

// main.cc
#include "lib.hh"
int main(){
    foo(1.0);
    foo(2.0f);
}
```

运行结果

```
1.000000
2.000000
```