# [规 则] 实验12：指向内置类型的智能指针如何进行类型转换？

内置类型，是指int、float这种基本数据类型。

如果按照类的方法，使用static_pointer_cast或者dynamic_pointer_cast，是编译不通过的。

```cpp
#include <memory>
int main(){
    std::shared_ptr<int> a;
    std::shared_ptr<char> b = std::static_pointer_cast<char>(a);
    std::shared_ptr<char> c = std::dynamic_pointer_cast<char>(a);
}
```

编译结果如下：

```
In file included from /opt/wandbox/gcc-12.1.0/include/c++/12.1.0/memory:77,
                 from prog.cc:1:
/opt/wandbox/gcc-12.1.0/include/c++/12.1.0/bits/shared_ptr.h: In instantiation of 'std::shared_ptr<_Tp> std::static_pointer_cast(const shared_ptr<_Tp>&) [with _Tp = char; _Up = int]':
prog.cc:4:61:   required from here
/opt/wandbox/gcc-12.1.0/include/c++/12.1.0/bits/shared_ptr.h:703:23: error: invalid 'static_cast' from type 'std::__shared_ptr<int, __gnu_cxx::_S_atomic>::element_type*' {aka 'int*'} to type 'std::shared_ptr<char>::element_type*' {aka 'char*'}
  703 |       return _Sp(__r, static_cast<typename _Sp::element_type*>(__r.get()));
      |                       ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/opt/wandbox/gcc-12.1.0/include/c++/12.1.0/bits/shared_ptr.h: In instantiation of 'std::shared_ptr<_Tp> std::dynamic_pointer_cast(const shared_ptr<_Tp>&) [with _Tp = char; _Up = int]':
prog.cc:5:62:   required from here
/opt/wandbox/gcc-12.1.0/include/c++/12.1.0/bits/shared_ptr.h:721:23: error: cannot 'dynamic_cast' '(& __r)->std::shared_ptr<int>::<anonymous>.std::__shared_ptr<int, __gnu_cxx::_S_atomic>::get()' (of type 'using element_type = std::remove_extent<int>::type*' {aka 'int*'}) to type 'using element_type = using element_type = std::remove_extent<char>::type*' {aka 'char*'} (target is not pointer or reference to class)
  721 |       if (auto* __p = dynamic_cast<typename _Sp::element_type*>(__r.get()))
      |                       ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

正确的方法是使用reinterpret_pointer_cast

```cpp
#include <memory>
#include <cstring>
#include <cstdio>
int main(){
    std::shared_ptr<char> a = std::shared_ptr<char>(new char[8]);
    memset(a.get(), 0xff, 8);
    std::shared_ptr<int> b = std::reinterpret_pointer_cast<int>(a);
    printf("%p,%p,%d\n", a.get(), b.get(), b.get()[0]);
}
```

运行结果如下：

```
0xb168f0,0xb168f0,-1
```