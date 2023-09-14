[规 则] Union能够存储非POD数据吗？

不能，非POD对象的析构函数不会被执行

```cpp
#include <iostream>

class A {
 public:
    A() { std::cout<<"A()\n"; }
    ~A() { std::cout<<"~A()\n"; }
};

union U {
    A a;
    int b;
};
 
int main()
{
    U u;
}
``` 