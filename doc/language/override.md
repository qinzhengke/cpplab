# [特 性] 实验4：override关键字有什么作用？

override关键字在派生类中使用，告诉编译器，它所修饰的函数必需重写（override）基类的某个虚函数，否则编译器要报错。 这样强制有什么用呢？一个很大的作用（唯一的作用？）就是能在编译阶段防止拼写错误导致的重写失败问题，举个例子，如下代码所示，故意拼错派生类的函数名。

```cpp
#include <iostream>
using namespace std;
class Base{
public:
    virtual void print(){ cout<<"Base::print()"<<endl;}
};

class Derived : public Base{
public:
    // 注意下面的函数名拼写错误
    void pirnt() override { cout<<"Derived::print()"<<endl;}　// 编译器报错
};

int main(){
    Base *p = new Derived();
    p->print();
}
```

编译结果：

```
prog.cc:14:61: error: extended character 　 is not valid in an identifier
   14 |     void pirnt() override { cout<<"Derived::print()"<<endl;}　// 情况二：编译器报错
      |         
```