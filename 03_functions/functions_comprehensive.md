# Python 函数详解

## 一、函数介绍

### 什么是函数？

函数是一段可重复使用的代码块，用于执行特定的任务。函数可以接收输入（参数），处理数据，并返回结果。

### 为什么使用函数？

1. **代码重用** - 避免重复编写相同的代码
2. **模块化** - 将复杂问题分解为小的、可管理的部分
3. **易于维护** - 修改功能时只需要改动一个地方
4. **提高可读性** - 使代码更清晰、更易理解

### 函数的基本概念

```
def function_name(parameters):
    """文档字符串（可选）"""
    # 函数体
    return value  # 返回值（可选）

```

组成部分：

* `def` - 定义函数的关键字
* `function_name` - 函数名称
* `parameters` - 参数列表
* `docstring` - 文档字符串（描述函数功能）
* `function body` - 函数体（执行的代码）
* `return` - 返回语句（可选）

* * *

## 二、调用函数

### 内置函数调用

### Python 提供了许多内置函数：

```
# 常用内置函数
print("Hello World")        # 输出
len("Python")               # 获取长度 -> 6
max(1, 5, 3)               # 获取最大值 -> 5
min([1, 2, 3])             # 获取最小值 -> 1
sum([1, 2, 3, 4])          # 求和 -> 10
abs(-5)                    # 绝对值 -> 5
round(3.14159, 2)          # 四舍五入 -> 3.14
type(42)                   # 获取类型 -> <class 'int'>

# 类型转换函数
int("123")                 # 字符串转整数 -> 123
float("3.14")              # 字符串转浮点数 -> 3.14
str(42)                    # 数字转字符串 -> "42"
bool(1)                    # 转布尔值 -> True
list("abc")                # 转列表 -> ['a', 'b', 'c']

```

### 函数调用的语法

```
# 基本调用
result = function_name(argument1, argument2)

# 示例
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)       # 调用 sum 函数
print(f"总和是: {total}")  # 输出: 总和是: 15

```

* * *

## 三、定义函数

### 简单函数定义

```
def greet():
    """打招呼函数"""
    print("Hello, World!")

# 调用函数
greet()  # 输出: Hello, World!

```

### 带返回值的函数

```
def add_numbers(a, b):
    """计算两个数的和"""
    result = a + b    return result
# 调用并接收返回值
sum_result = add_numbers(3, 5)
print(sum_result)  # 输出: 8

```

### 多个返回值

```
def get_name_age():
    """返回姓名和年龄"""
    name = "张三"
    age = 25
    return name, age  # 返回元组

# 接收多个返回值
person_name, person_age = get_name_age()
print(f"姓名: {person_name}, 年龄: {person_age}")

# 也可以作为元组接收
info = get_name_age()
print(info)  # 输出: ('张三', 25)

```

### 文档字符串

```
def calculate_area(length, width):
    """    计算矩形面积
    参数:        length (float): 矩形的长度        width (float): 矩形的宽度
    返回:        float: 矩形的面积
    示例:        >>> calculate_area(5, 3)        15    """
    return length * width
# 查看函数文档
print(calculate_area.__doc__)
help(calculate_area)

```

* * *

## 四、函数的参数

### 位置参数

```
def introduce(name, age, city):
    """按位置顺序传递参数"""
    print(f"我是{name}，{age}岁，来自{city}")

# 位置参数调用
introduce("张三", 25, "北京")  # 输出: 我是张三，25岁，来自北京

```

### 关键字参数

```
def introduce(name, age, city):
    print(f"我是{name}，{age}岁，来自{city}")

# 关键字参数调用（顺序可以改变）
introduce(age=25, city="北京", name="张三")
introduce("李四", city="上海", age=30)  # 混合使用

```

### 默认参数

```
def greet_person(name, greeting="你好"):
    """带默认参数的函数"""
    print(f"{greeting}, {name}!")

# 使用默认参数
greet_person("张三")           # 输出: 你好, 张三!
greet_person("李四", "欢迎")    # 输出: 欢迎, 李四!

```

注意事项：

```
# ❌ 错误：可变对象作为默认参数
def add_item(item, target_list=[]):
    target_list.append(item)
    return target_list
# ✅ 正确：使用 None 作为默认值
def add_item(item, target_list=None):
    if target_list is None:
        target_list = []
    target_list.append(item)
    return target_list
```

### 可变参数 (*args)

```
def sum_all(*numbers):
    """接收任意数量的位置参数"""
    total = 0
    for num in numbers:
        total += num    return total
# 调用方式
print(sum_all(1, 2, 3))           # 输出: 6
print(sum_all(1, 2, 3, 4, 5))     # 输出: 15
print(sum_all())                  # 输出: 0

# 传递列表
numbers = [1, 2, 3, 4]
print(sum_all(*numbers))          # 输出: 10 (解包列表)

```

### 关键字可变参数 (**kwargs)

```
def create_profile(**info):
    """接收任意数量的关键字参数"""
    print("个人信息:")
    for key, value in info.items():
        print(f"  {key}: {value}")

# 调用方式
create_profile(name="张三", age=25, city="北京", hobby="篮球")

# 传递字典
person_info = {"name": "李四", "age": 30, "occupation": "工程师"}
create_profile(**person_info)  # 解包字典

```

### 参数的组合使用

```
def flexible_function(required, default="默认值", *args, **kwargs):
    """演示各种参数类型的组合"""
    print(f"必需参数: {required}")
    print(f"默认参数: {default}")
    print(f"位置参数: {args}")
    print(f"关键字参数: {kwargs}")

# 调用示例
flexible_function(
    "必须的",           # required
    "自定义默认值",      # default
    1, 2, 3,           # *args
    name="张三",        # **kwargs
    age=25
)

```

### 强制关键字参数

```
def create_user(name, *, age, email):
    """* 后面的参数必须使用关键字传递"""
    print(f"用户: {name}, 年龄: {age}, 邮箱: {email}")

# 正确调用
create_user("张三", age=25, email="zhang@example.com")

# 错误调用 - 会报错
# create_user("张三", 25, "zhang@example.com")

```

* * *

## 五、递归函数

### 什么是递归？

递归是一种函数调用自身的编程技术。递归函数必须有：

1. **基础情况** - 停止递归的条件
2. **递归情况** - 函数调用自身，问题规模逐渐减小

### 经典递归示例

#### 1. 计算阶乘

```
def factorial(n):
    """    计算 n 的阶乘    n! = n × (n-1) × (n-2) × ... × 1    """
    # 基础情况
    if n == 0 or n == 1:
        return 1

    # 递归情况
    return n * factorial(n - 1)

# 测试
print(factorial(5))  # 输出: 120 (5×4×3×2×1)
print(factorial(0))  # 输出: 1

```

执行过程：

```
factorial(5)= 5 * factorial(4)= 5 * 4 * factorial(3)= 5 * 4 * 3 * factorial(2)= 5 * 4 * 3 * 2 * factorial(1)= 5 * 4 * 3 * 2 * 1= 120
```

#### 2. 斐波那契数列

```
def fibonacci(n):
    """    计算斐波那契数列的第 n 项    F(0) = 0, F(1) = 1    F(n) = F(n-1) + F(n-2)    """
    # 基础情况
    if n <= 1:
        return n
    # 递归情况
    return fibonacci(n - 1) + fibonacci(n - 2)

# 测试
for i in range(10):
    print(f"F({i}) = {fibonacci(i)}")

```

#### 3. 计算幂

```
def power(base, exponent):
    """    计算 base 的 exponent 次幂    """
    # 基础情况
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    # 递归情况
    if exponent % 2 == 0:
        # 偶数指数：base^n = (base^(n/2))^2
        half_power = power(base, exponent // 2)
        return half_power * half_power    else:
        # 奇数指数：base^n = base * base^(n-1)
        return base * power(base, exponent - 1)

print(power(2, 10))  # 输出: 1024

```

#### 4. 遍历嵌套列表

```
def flatten_list(nested_list):
    """    将嵌套列表展平    """
    result = []
    for item in nested_list:
        if isinstance(item, list):
            # 递归处理嵌套列表
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result
# 测试
nested = [1, [2, 3], [4, [5, 6]], 7]
flat = flatten_list(nested)
print(flat)  # 输出: [1, 2, 3, 4, 5, 6, 7]

```

#### 5. 目录遍历

```
import os
def list_files(directory, indent=0):
    """    递归遍历目录结构    """
    items = os.listdir(directory)
    for item in items:
        item_path = os.path.join(directory, item)
        print("  " * indent + item)

        if os.path.isdir(item_path):
            # 递归遍历子目录
            list_files(item_path, indent + 1)

# 使用示例
# list_files("/path/to/directory")

```

### 递归的优化

#### 记忆化（Memoization）

```
def fibonacci_memo(n, memo={}):
    """    使用记忆化优化的斐波那契函数    """
    if n in memo:
        return memo[n]

    if n <= 1:
        result = n    else:
        result = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)

    memo[n] = result    return result
# 性能对比
import time
# 普通递归（较慢）
start = time.time()
result1 = fibonacci(35)
time1 = time.time() - start
# 记忆化递归（较快）
start = time.time()
result2 = fibonacci_memo(35)
time2 = time.time() - start
print(f"普通递归: {result1}, 耗时: {time1:.4f}秒")
print(f"记忆化递归: {result2}, 耗时: {time2:.4f}秒")

```

### 递归的注意事项

1. **避免无限递归**

```
def bad_recursion(n):
    # ❌ 没有基础情况，会导致无限递归
    return bad_recursion(n - 1)

def good_recursion(n):
    # ✅ 有明确的基础情况
    if n <= 0:
        return 0
    return n + good_recursion(n - 1)

```

1. **考虑递归深度限制**

```
import sys
# 查看当前递归限制
print(sys.getrecursionlimit())  # 通常是 1000

# 设置递归限制（谨慎使用）
# sys.setrecursionlimit(2000)

```

1. **何时使用递归**

* ✅ 适合：树形结构、分治算法、数学定义递归的问题
* ❌ 不适合：简单的循环可以解决的问题、性能要求极高的场景

### 递归 vs 迭代

```
# 递归版本
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

# 迭代版本
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i    return result
# 两种方式结果相同，但迭代版本通常更高效
print(factorial_recursive(5))  # 120
print(factorial_iterative(5))  # 120

```

## 总结

函数是Python编程的重要组成部分，掌握函数的定义、调用、参数传递和递归概念对于编写高质量的代码至关重要。记住：

1. **函数设计原则**：单一职责、参数合理、命名清晰
2. **参数使用**：合理使用默认参数、*args 和 **kwargs
3. **递归应用**：确保有基础情况，注意性能和深度限制
4. **文档编写**：为函数编写清晰的文档字符串

* * *

## Python 函数 vs Java 方法对比

|特性	|Python	|Java	|
|---	|---	|---	|
|**定义关键字**	|`def`	|`public/private static`	|
|---	|---	|---	|
|**类型声明**	|无需声明参数和返回值类型	|必须声明所有类型	|
|**默认参数**	|直接支持	|需要方法重载实现	|
|**可变参数**	|`*args`, `**kwargs`	|`...` (varargs)，只支持同类型	|
|**函数对象**	|函数是第一类对象，可以赋值、传递	|方法不是对象，需要反射或函数式接口	|
|**多返回值**	|支持元组返回	|需要创建对象或数组	|
|**动态性**	|运行时可以动态创建函数	|编译时确定	|
|**闭包**	|原生支持	|Lambda表达式有限支持	|

### 对比示例

**Python:**

```
# 简洁的函数定义
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# 函数作为对象
func = greetresult = func("World")

```

**Java:**

```
// 需要类和方法声明
public class Example {    public static String greet(String name) {        return greet(name, "Hello");    }
    public static String greet(String name, String greeting) {        return greeting + ", " + name + "!";    }}
```

总结: Python函数更加灵活简洁，Java方法更加严格规范。
