# [语法糖] 实验21：为什么要定义匿名结构体？

很多时候，当我们定义类型时，我们希望拥有多种方式对同一个地址的变量进行引用。 qq 举个例子，比如四元数，我们即希望能使用数组的方式来引用，这样方便内存拷贝以及循环操作，同时，我们也希望使用w,x,y,z方式引用它，这样更直观，因为w,x,y,z的名称有自解释能力。

uinon能够提供这个功能，union在C语言标准里是可以匿名的，这没什么问题。

匿名的好处是不需要在额外命名，父结构体直接引用子union的成员。

union要配合strcut使用，才能得到我们期望的效果，但是struct能否是匿名的呢？

这个问题似乎有不同的答案，stackoverflow上有一个回答，说是可以编译运行，但是编译器会警告，说是不兼容C语言。

stackoverflow提问: Why does C++ disallow anonymous structs?

但是我使用cpp.sh（c++98）进行了实验，是完全没有问题的，警告也没有。

```cpp
#include <cstdio>
union Vec {
    struct { float x,y,z; };
    float m[3];
};
int main(){
    Vec v;
    v.x = 10;
    v.y = 1.2;
    v.z = -2.5;
    printf("%f,%f,%f", v.m[0], v.m[1], v.m[2]);
}
```

运行结果如下

```
10.000000,1.200000,-2.500000
```