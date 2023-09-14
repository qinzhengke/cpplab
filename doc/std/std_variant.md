[语法糖] 实验xx:std::variant

`std::variant` 是 C++17 中引入的标准库类型，它允许一个变量可以同时持有多种不同类型的值。这在需要灵活处理多种类型的情况下非常有用。
是一种类型安全的union，所以也叫做tagged union。

以下是 `std::variant` 的一些主要作用：

1. **代替联合体 (union)**：
   `std::variant` 提供了比传统联合体更安全、更易用的方式来处理多种类型。
   联合体无法存储非POD对象，对象的析构函数无法使用。

   例如，一个可以存储整数、浮点数和字符串的数据结构：

   ```cpp
   std::variant<int, float, std::string> data;
   data = 42; // 存储一个整数
   data = 3.14f; // 存储一个浮点数
   data = "Hello"; // 存储一个字符串
   ```

2. **避免使用指针或裸指针**：
   在需要处理多种类型的情况下，通常会使用基类指针或者裸指针。而 `std::variant` 可以提供一种类型安全的替代方式。

   ```cpp
   std::variant<int, std::string> data = 42;

   if (std::holds_alternative<int>(data)) {
       int value = std::get<int>(data);
   } else if (std::holds_alternative<std::string>(data)) {
       std::string str = std::get<std::string>(data);
   }
   ```

3. **避免使用标志位 (flag)**：
   有时候会使用一个标志位来表示当前变量中存储的是哪种类型的值，而 `std::variant` 可以更直接地表示这种情况。

   ```cpp
   enum Type { Integer, Float, String };
   
   struct Data {
       Type type;
       union {
           int intValue;
           float floatValue;
           std::string stringValue;
       };
   };
   ```

   使用 `std::variant` 可以避免了联合体中可能存在的问题，如正确的构造和析构等。

4. **提供类型安全的访问方式**：
   使用 `std::get` 可以安全地访问 `std::variant` 中的值，并在类型不匹配时抛出异常。

   ```cpp
   std::variant<int, float, std::string> data = 42;

   int value = std::get<int>(data); // 正确
   float floatValue = std::get<float>(data); // 会抛出异常，因为数据类型不匹配
   ```

总的来说，`std::variant` 提供了一种类型安全、直观、灵活的方式来处理可能包含多种不同类型的值的情况，避免了一些传统做法中可能出现的问题。