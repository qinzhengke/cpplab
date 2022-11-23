# cpplab

- cpplab是一个教程，试图基于实验的方式来理清C++的各种知识点。
- 本仓库所有代码都在wandabox.org上验证过，也建议使用wandbox.org来运行代码，能够支持多文件编译，并且也比较稳定。
- 有一些实验代码来自`cppreference.com`，已经足够优秀，为了保证教程的完整性，本教程会将其代码拷贝下来，但是会注明出处。
- `changkun/modern-cpp-tutorial`是一本非常优秀的C++书籍，但是本教程会更加着重讲述特性的使用场景，让读者明白特性设计动机，并更积极地去使用。
- `BartVandewoestyne/Cpp`是一个优秀的教程，也是以实验为基本单元，但是缺少文档讲解，更缺少像书本一样的目录结构，想要抱着问题找答案，比较困难。
- `Kobzol/hardware-effects`是一个优秀的教程，讲述关于CPU编程中的硬件利用效率，但本教程会试图涵盖更多的话题，例如语法、STL、设计模式等。

在这里，我们把所有的话题分为3个级别：特性、规则、语法糖。

- [特  性]：对开发效率或者执行效率有提升，我们应该使用。
- [规  则]：其他特性的附加内容，对开发效率和执行效率没有明显提升，但是如果不知道，可能会踩到坑，例如编译失败或者程序结果不符合预期。
- \[语法糖\]：对开发效率有提升，用了可以让代码更简洁，但不用也没有关系。

每个话题的标题会标记相应的级别。

## 目录
* [语言]
    * [[特 性] 实验0：如何让一个接口既能接受左值，也能接受右值作为参数？](https://github.com/qinzhengke/cpplab/blob/test/doc/language/both_lvalue_rvalue.md)
    * [[特 性] 实验1：如何优雅地拷贝基类指针指向的派生类对象？](https://github.com/qinzhengke/cpplab/blob/test/doc/language/copy_by_base_pointer.md)
    * [[特 性] 实验2：const关键字有什么作用？](https://github.com/qinzhengke/cpplab/blob/test/doc/language/keyword_const.md)
    * [[特 性] 实验3：如何定义类成员引用？](https://github.com/qinzhengke/cpplab/blob/test/doc/language/member_reference.md)
    * [[特 性] 实验4：override关键字有什么作用？](https://github.com/qinzhengke/cpplab/blob/test/doc/language/override.md)
    * [[特 性] 实验5：基于引用来调用虚函数](https://github.com/qinzhengke/cpplab/blob/test/doc/language/polymorphism_by_reference.md)
    * [[特 性] 实验6：为什么需要右值引用？](https://github.com/qinzhengke/cpplab/blob/test/doc/language/rvalue.md)
    * [[特 性] 实验7：重写（override）操作一定要虚函数形参和返回值完全一样吗？](https://github.com/qinzhengke/cpplab/blob/test/doc/language/special_override.md)
    * [[特 性] 实验8：模板参数包（template paramter pack，可变长模板参数）的使用场景是什么？](https://github.com/qinzhengke/cpplab/blob/test/doc/language/template_parameter_pack.md)
    * [[规 则] 实验9：构造与析构的执行顺序是什么？](https://github.com/qinzhengke/cpplab/blob/test/doc/language/constructor_deconstructor_order.md)
    * [[规 则] 实验10：什么是名字隐藏（name hiding）？](https://github.com/qinzhengke/cpplab/blob/test/doc/language/name_hiding.md)
    * [[规 则] 实验11：有了编译器返回值优化（RVO），为何还需要右值引用？](https://github.com/qinzhengke/cpplab/blob/test/doc/language/rvo_limit.md)
    * [[规 则] 实验12：指向内置类型的智能指针如何进行类型转换？](https://github.com/qinzhengke/cpplab/blob/test/doc/language/smart_pointer_cast.md)
    * [[规 则] 实验13：指向类的智能指针如何进行类型转换？](https://github.com/qinzhengke/cpplab/blob/test/doc/language/smart_pointer_cast_class.md)
    * [[规 则] 实验14：如何定义静态成员变量？](https://github.com/qinzhengke/cpplab/blob/test/doc/language/static_member_variable.md)
    * [[规 则] 实验15：模板类中的模板方法如何定义？](https://github.com/qinzhengke/cpplab/blob/test/doc/language/t_method_in_t_class.md)
    * [[规 则] 实验16：如何访问模板基类成员？](https://github.com/qinzhengke/cpplab/blob/test/doc/language/template_base_member.md)
    * [[规 则] 实验17：如何实现模板分离编译？](https://github.com/qinzhengke/cpplab/blob/test/doc/language/template_split.md)
    * [[规 则] 实验18：为什么析构函数要声明为virtual？](https://github.com/qinzhengke/cpplab/blob/test/doc/language/virtual_deconstructor.md)
    * [[规 则] 实验19：为什么不要在构造和析构函数中调用虚函数？](https://github.com/qinzhengke/cpplab/blob/test/doc/language/virtual_in_constructor.md)
    * [[规 则] 实验20：模板函数能够声明为virtual吗？](https://github.com/qinzhengke/cpplab/blob/test/doc/language/virtual_template.md)
    * [[语法糖] 实验21：为什么要定义匿名结构体？](https://github.com/qinzhengke/cpplab/blob/test/doc/language/anonymous_struct.md)
    * [[TODO] [语法糖] 实验22：如何使](https://github.com/qinzhengke/cpplab/blob/test/doc/language/memory_align.md)
    * [[TODO] [语法糖] 实验23：字符串字面](https://github.com/qinzhengke/cpplab/blob/test/doc/language/string_literal.md)
* [标准库]
    * [[特 性] 实验24：如何使用标准库chrono来测耗时？](https://github.com/qinzhengke/cpplab/blob/test/doc/std/chrono.md)
    * [[TODO] [特 性] 实验25：有了mutex::lock，为啥还需要lock_guard](https://github.com/qinzhengke/cpplab/blob/test/doc/std/lock_guard.md)
    * [[特 性] 实验26：什么场景需要std::bind？](https://github.com/qinzhengke/cpplab/blob/test/doc/std/std_bind.md)
    * [[TODO] [特 性] 实验27：std::forward是什么，为什么需要它](https://github.com/qinzhengke/cpplab/blob/test/doc/std/std_forward.md)
    * [[特 性] 实验28：有了函数指针，为什么还需要std::function？](https://github.com/qinzhengke/cpplab/blob/test/doc/std/std_function.md)
    * [[TODO] [特 性] 实验29：函数如何返回多个变量？](https://github.com/qinzhengke/cpplab/blob/test/doc/std/std_tuple.md)
    * [[规 则] 实验30：为什么std::bind绑定引用必须需要std::ref()？](https://github.com/qinzhengke/cpplab/blob/test/doc/std/ref_in_std_bind.md)
* [标准模板库STL]
    * [[特 性] 实验31：push_back vs emplace_back](https://github.com/qinzhengke/cpplab/blob/test/doc/stl/push_back_vs_emplace_back.md)
    * [[TODO] [特 性] 实验32：返回码 vs 异常机](https://github.com/qinzhengke/cpplab/blob/test/doc/stl/ret_code_vs_exception.md)
    * [[特 性] 实验33：std::array vs C风格数组(C-style array)](https://github.com/qinzhengke/cpplab/blob/test/doc/stl/std_array.md)
    * [[规 则] 实验34：vector\<A>(n,A())中，A()会执行n次吗？](https://github.com/qinzhengke/cpplab/blob/test/doc/stl/vector_n_A.md)
