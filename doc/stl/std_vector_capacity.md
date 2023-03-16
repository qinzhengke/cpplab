# [特 性] 实验xx：std::vector.capacity()

vector a在赋值的时候，哪怕被赋值的vector b容量和size更小，a本身的容量是不会变小的，而且数据地址，即data()是不会变的。
但vector在构造赋值的时候，注意赋值和构造赋值是不一样的，a的容量可能会变小。data()有可能会改变。

```cpp
#include <iostream>
#include <vector>
#include <cstdio>

using std::vector;
using std::cout;
 
int main() {
    vector<int> a(100);
    vector<int> b(10);
    printf("%p,%3lu,%3lu\n", b.data(), b.capacity(), b.size());
    printf("%p,%3lu,%3lu\n", a.data(), a.capacity(), a.size());
  
    a = b;  // 赋值，data(), capcacity()不会减小。
    printf("%p,%3lu,%3lu\n", a.data(), a.capacity(), a.size());
  
    a = vector<int>(10);  // 构造， data()，capacity()可能会减小。
    printf("%p,%3lu,%3lu\n", a.data(), a.capacity(), a.size());
}
```

运行结果：
```
0x5011b0, 10, 10
0x501018,100,100
0x501018,100, 10
0x5011e0, 10, 10
```
