# Python 基础语法教程

本教程涵盖Python编程的基础语法，包括数据类型、运算符、条件语句、循环、函数和数据结构等核心概念。每个概念都包含与Java的对比，帮助有编程背景的学习者快速上手。

---

# 第一章：数据类型与变量

## 一、变量声明与赋值

### Python 中的变量不需要声明类型：

```python
a = 10
b = "hello"
c = True
```

等价于 Java：

```java
int a = 10;
String b = "hello";
boolean c = true;
```

**Python 是动态类型语言**，变量的类型由赋值自动推断。你可以把 `a = 10` 改成 `a = "hello"`，不会报错。

* * *

## 二、基本数据类型

|Python 类型	|示例	|Java 对应类型	|
|---	|---	|---	|
|`int`	|`a = 123`	|`int` / `long`	|
|`float`	|`b = 1.23`	|`float` / `double`	|
|`bool`	|`c = True`	|`boolean`	|
|`str`	|`d = 'Hello'`	|`String`	|
|`None`	|`e = None`	|`null`	|

`None` 相当于 Java 的 `null`，表示"什么都没有"。

* * *

## 三、字符串操作

### 单引号和双引号都可以表示字符串

```python
s1 = 'hello'
s2 = "world"
```

### 多行字符串用三引号 `'''` 或 `"""`

```python
s3 = '''第一行
第二行'''
```

### 字符串拼接

```python
name = 'Sonny'
greeting = 'Hello, ' + name  # 拼接
```

等价 Java：

```java
String name = "Sonny";
String greeting = "Hello, " + name;
```

* * *

## 四、格式化字符串

Python 有多种方式格式化字符串：

#### f-string（推荐）：

```python
name = "Sonny"
age = 25
print(f"My name is {name}, and I'm {age} years old.")
```

等价于 Java：

```java
System.out.printf("My name is %s, and I'm %d years old.\n", name, age);
```

* * *

## 五、布尔类型与运算

```python
a = True
b = False
print(a and b)  # 与
print(a or b)   # 或
print(not a)    # 非
```

Java 对应：

```java
boolean a = true;
boolean b = false;
System.out.println(a && b);
System.out.println(a || b);
System.out.println(!a);
```

* * *

## 六、类型转换

```python
int("123")      # 字符串转整数
float("3.14")   # 字符串转浮点数
str(123)        # 数值转字符串
bool(1)         # True
```

Java 需要调用包装类：

```java
Integer.parseInt("123");
Double.parseDouble("3.14");
String.valueOf(123);
```

* * *

## 七、常见内置函数

|函数	|功能	|
|---	|---	|
|`len()`	|返回字符串/列表长度	|
|`type()`	|查看变量类型	|
|`print()`	|打印	|

```python
print(len("hello"))  # 5
print(type(123))     # <class 'int'>
```

---

# 第二章：运算符

## 一、算术运算符

### Python 中的基本算术运算：

```python
a = 10
b = 3

print(a + b)    # 13 - 加法
print(a - b)    # 7  - 减法
print(a * b)    # 30 - 乘法
print(a / b)    # 3.333... - 除法（结果为浮点数）
print(a // b)   # 3  - 整除（向下取整）
print(a % b)    # 1  - 取余
print(a ** b)   # 1000 - 幂运算
```

等价于 Java：

```java
int a = 10, b = 3;
System.out.println(a + b);    // 13
System.out.println(a - b);    // 7
System.out.println(a * b);    // 30
System.out.println(a / b);    // 3 (整数除法)
System.out.println(a % b);    // 1
System.out.println(Math.pow(a, b)); // 幂运算需要用方法
```

**注意**：Python 的 `/` 总是返回浮点数，而 `//` 是整除运算符。

* * *

## 二、比较运算符

```python
a = 5
b = 3

print(a == b)   # False - 等于
print(a != b)   # True  - 不等于
print(a > b)    # True  - 大于
print(a < b)    # False - 小于
print(a >= b)   # True  - 大于等于
print(a <= b)   # False - 小于等于
```

* * *

## 三、逻辑运算符

```python
a = True
b = False

print(a and b)  # False - 逻辑与
print(a or b)   # True  - 逻辑或
print(not a)    # False - 逻辑非
```

* * *

## 四、赋值运算符

```python
a = 10
a += 5      # a = a + 5  -> 15
a -= 3      # a = a - 3  -> 12
a *= 2      # a = a * 2  -> 24
a /= 4      # a = a / 4  -> 6.0
a //= 2     # a = a // 2 -> 3.0
a %= 2      # a = a % 2  -> 1.0
a **= 3     # a = a ** 3 -> 1.0
```

* * *

## 五、身份运算符

Python 特有的运算符，用于比较对象的内存地址：

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a is b)       # False - 不是同一个对象
print(a is c)       # True  - 是同一个对象
print(a is not b)   # True  - 不是同一个对象
```

**重要**：`is` 比较的是对象的身份（内存地址），`==` 比较的是值。

* * *

## 六、成员运算符

检查元素是否在序列中：

```python
text = "hello world"
numbers = [1, 2, 3, 4, 5]

print('h' in text)          # True
print('x' in text)          # False
print(3 in numbers)         # True
print(6 not in numbers)     # True
```

* * *

## 七、运算符优先级

从高到低：

|优先级	|运算符	|说明	|
|---	|---	|---	|
|1	|`()`	|括号	|
|2	|`**`	|幂运算	|
|3	|`+x`, `-x`, `~x`	|正号、负号、按位取反	|
|4	|`*`, `/`, `//`, `%`	|乘除取余	|
|5	|`+`, `-`	|加减	|
|6	|`==`, `!=`, `>`, `<`, `>=`, `<=`	|比较运算符	|
|7	|`not`	|逻辑非	|
|8	|`and`	|逻辑与	|
|9	|`or`	|逻辑或	|

示例：

```python
result = 2 + 3 * 4      # 14 (不是 20)
result = (2 + 3) * 4    # 20
result = True or False and False  # True (and 优先级高于 or)
```

* * *

## 八、常用技巧

### 链式比较

```python
age = 25
print(18 <= age <= 65)  # True，等价于 age >= 18 and age <= 65
```
Java中没有类似的语法，需要使用 `&&` 和 `||`。

### 交换变量

```python
a, b = 10, 20
a, b = b, a     # 交换 a 和 b 的值
print(a, b)     # 20 10
```

### 多重赋值

```python
x = y = z = 0   # 同时给多个变量赋值
a, b, c = 1, 2, 3  # 解包赋值
```

---

# 第三章：条件语句

## 一、if 语句基础

### 基本语法

```python
age = 18

if age >= 18:
    print("已成年")
```

等价于 Java：

```java
int age = 18;
if (age >= 18) {
    System.out.println("已成年");
}
```

**注意**：Python 使用**缩进**来表示代码块，而不是大括号 `{}`。

* * *

## 二、if-else 语句

```python
age = 16

if age >= 18:
    print("已成年")
else:
    print("未成年")
```

* * *

## 三、if-elif-else 语句

```python
score = 85

if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")
```

**注意**：Python 使用 `elif`，Java 使用 `else if`。

* * *

## 四、三元运算符（条件表达式）

```python
age = 20
status = "成年" if age >= 18 else "未成年"
print(status)  # 成年
```

Java 对应：

```java
int age = 20;
String status = (age >= 18) ? "成年" : "未成年";
System.out.println(status);
```

**语法**：`值1 if 条件 else 值2`

* * *

## 五、布尔值的真假性

Python 中以下值被认为是 **False**：

- `False`
- `None`
- `0`（任何数值类型的零）
- 空字符串 `""`
- 空列表 `[]`
- 空字典 `{}`
- 空元组 `()`

```python
# 这些都会打印 "空值"
values = [False, None, 0, "", [], {}, ()]

for value in values:
    if not value:
        print(f"{value} 是空值")
```

* * *

## 六、常用模式

### 1. 范围检查

```python
score = 85
if 80 <= score <= 90:
    print("良好")
```

### 2. 多值比较

```python
grade = "A"
if grade in ["A", "B", "C"]:
    print("及格")
```

### 3. 类型检查

```python
value = "123"
if isinstance(value, str):
    print("这是字符串")
```

---

# 第四章：循环语句

## 一、for 循环基础

### 遍历列表

```python
fruits = ["苹果", "香蕉", "橘子"]

for fruit in fruits:
    print(fruit)
```

等价于 Java：

```java
String[] fruits = {"苹果", "香蕉", "橘子"};
for (String fruit : fruits) {
    System.out.println(fruit);
}
```

### 遍历字符串

```python
text = "hello"

for char in text:
    print(char)  # 逐个打印字符
```

* * *

## 二、range() 函数

### 基本用法

```python
# range(stop) - 从 0 到 stop-1
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# range(start, stop) - 从 start 到 stop-1
for i in range(1, 6):
    print(i)  # 1, 2, 3, 4, 5

# range(start, stop, step) - 指定步长
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8
```

* * *

## 三、enumerate() 函数

获取索引和值：

```python
fruits = ["苹果", "香蕉", "橘子"]

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
    
# 输出：
# 0: 苹果
# 1: 香蕉
# 2: 橘子
```

* * *

## 四、while 循环

### 基本语法

```python
count = 0
while count < 5:
    print(f"计数：{count}")
    count += 1
```

### 无限循环

```python
while True:
    user_input = input("输入 'q' 退出：")
    if user_input == 'q':
        break
    print(f"你输入了：{user_input}")
```

* * *

## 五、循环控制语句

### break - 跳出循环

```python
for i in range(10):
    if i == 5:
        break
    print(i)  # 0, 1, 2, 3, 4
```

### continue - 跳过当前迭代

```python
for i in range(10):
    if i % 2 == 0:  # 跳过偶数
        continue
    print(i)  # 1, 3, 5, 7, 9
```

* * *

## 六、zip() 函数

同时遍历多个序列：

```python
names = ["张三", "李四", "王五"]
ages = [25, 30, 35]
cities = ["北京", "上海", "广州"]

for name, age, city in zip(names, ages, cities):
    print(f"{name}, {age}岁, 来自{city}")

# 输出：
# 张三, 25岁, 来自北京
# 李四, 30岁, 来自上海
# 王五, 35岁, 来自广州
```

* * *

## 七、列表推导式

简化的循环语法：

```python
# 传统方式
squares = []
for x in range(10):
    squares.append(x ** 2)

# 列表推导式
squares = [x ** 2 for x in range(10)]

# 带条件的列表推导式
even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
```

* * *

## 八、else 子句

Python 特有：循环正常结束时执行 else：

```python
# for-else
for i in range(5):
    print(i)
else:
    print("循环正常结束")  # 会执行

# 如果遇到 break，else 不会执行
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("这不会打印")  # 不会执行
```
---

# 第五章：列表和字典

## 一、列表基础

### 创建列表

```python
# 空列表
empty_list = []
empty_list2 = list()

# 有初始值的列表
fruits = ["苹果", "香蕉", "橘子"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]  # 可以混合不同类型
```

等价于 Java：

```java
// Java 需要指定类型
List<String> fruits = Arrays.asList("苹果", "香蕉", "橘子");
List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);
// Java 不能轻易混合类型，需要 Object 类型
```

* * *

## 二、列表操作

### 访问元素

```python
fruits = ["苹果", "香蕉", "橘子", "葡萄"]

print(fruits[0])   # 苹果 (第一个元素)
print(fruits[-1])  # 葡萄 (最后一个元素)
print(fruits[-2])  # 橘子 (倒数第二个元素)
```

### 切片操作

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[2:5])    # [2, 3, 4] (从索引2到4)
print(numbers[:3])     # [0, 1, 2] (从开始到索引2)
print(numbers[7:])     # [7, 8, 9] (从索引7到结束)
print(numbers[::2])    # [0, 2, 4, 6, 8] (步长为2)
print(numbers[::-1])   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (倒序)
```

* * *

## 三、列表方法

### 添加元素

```python
fruits = ["苹果", "香蕉"]

# 在末尾添加单个元素
fruits.append("橘子")
print(fruits)  # ['苹果', '香蕉', '橘子']

# 在指定位置插入元素
fruits.insert(1, "草莓")
print(fruits)  # ['苹果', '草莓', '香蕉', '橘子']

# 添加多个元素
fruits.extend(["葡萄", "桃子"])
print(fruits)  # ['苹果', '草莓', '香蕉', '橘子', '葡萄', '桃子']
```

### 删除元素

```python
fruits = ["苹果", "香蕉", "橘子", "香蕉"]

# 删除指定值的第一个匹配项
fruits.remove("香蕉")
print(fruits)  # ['苹果', '橘子', '香蕉']

# 删除指定索引的元素并返回
removed = fruits.pop(1)
print(removed)  # 橘子
print(fruits)   # ['苹果', '香蕉']

# 清空列表
fruits.clear()
print(fruits)   # []
```

* * *

## 四、字典基础

### 创建字典

```python
# 空字典
empty_dict = {}
empty_dict2 = dict()

# 有初始值的字典
person = {"name": "张三", "age": 25, "city": "北京"}
scores = {"语文": 85, "数学": 92, "英语": 78}

# 使用 dict() 构造函数
person2 = dict(name="李四", age=30, city="上海")
```

Java 对应：

```java
Map<String, Object> person = new HashMap<>();
person.put("name", "张三");
person.put("age", 25);
person.put("city", "北京");
```

* * *

## 五、字典操作

### 访问和修改

```python
person = {"name": "张三", "age": 25, "city": "北京"}

# 访问值
print(person["name"])        # 张三
print(person.get("age"))     # 25
print(person.get("phone", "未知"))  # 未知 (默认值)

# 修改值
person["age"] = 26
person["phone"] = "12345678901"  # 添加新键值对
print(person)

# 删除键值对
del person["city"]
removed_age = person.pop("age", None)
print(f"删除的年龄: {removed_age}")
```

### 遍历字典

```python
person = {"name": "张三", "age": 25, "city": "北京"}

# 遍历键
for key in person:
    print(key)

# 遍历值
for value in person.values():
    print(value)

# 遍历键值对
for key, value in person.items():
    print(f"{key}: {value}")
```

* * *

## 六、列表和字典的高级操作

### 列表推导式

```python
# 基本列表推导式
squares = [x**2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 带条件的列表推导式
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]

# 复杂表达式
words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
print(upper_words)  # ['HELLO', 'WORLD', 'PYTHON']
```

### 字典推导式

```python
# 基本字典推导式
squares_dict = {x: x**2 for x in range(5)}
print(squares_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# 从列表创建字典
names = ["张三", "李四", "王五"]
name_lengths = {name: len(name) for name in names}
print(name_lengths)  # {'张三': 2, '李四': 2, '王五': 2}

# 带条件的字典推导式
scores = {"语文": 85, "数学": 92, "英语": 78, "物理": 95}
good_scores = {subject: score for subject, score in scores.items() if score >= 90}
print(good_scores)  # {'数学': 92, '物理': 95}
```

* * *

## 七、元组（Tuple）

不可变的序列：

```python
# 创建元组
coordinates = (3, 5)
colors = ("红", "绿", "蓝")
single_item = (42,)  # 单个元素的元组需要逗号

# 元组解包
x, y = coordinates
print(f"x={x}, y={y}")  # x=3, y=5

# 元组作为字典的键（因为不可变）
locations = {
    (0, 0): "原点",
    (1, 0): "东",
    (0, 1): "北"
}
```

* * *

## 八、集合（Set）

无序且不重复的集合：

```python
# 创建集合
fruits = {"苹果", "香蕉", "橘子"}
numbers = set([1, 2, 3, 2, 1])  # {1, 2, 3} - 自动去重

# 集合操作
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1 & set2)  # {3, 4} - 交集
print(set1 | set2)  # {1, 2, 3, 4, 5, 6} - 并集
print(set1 - set2)  # {1, 2} - 差集

# 添加和删除
fruits.add("葡萄")
fruits.remove("香蕉")  # 如果不存在会报错
fruits.discard("桃子")  # 如果不存在不会报错
```

* * *

## 九、常用内置函数

### 对列表使用

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

print(len(numbers))    # 8 - 长度
print(max(numbers))    # 9 - 最大值
print(min(numbers))    # 1 - 最小值
print(sum(numbers))    # 31 - 总和
print(sorted(numbers)) # [1, 1, 2, 3, 4, 5, 6, 9] - 排序后的新列表

# 原地排序
numbers.sort()
print(numbers)  # [1, 1, 2, 3, 4, 5, 6, 9]

# 反转
numbers.reverse()
print(numbers)  # [9, 6, 5, 4, 3, 2, 1, 1]
```

---

# 总结

本教程涵盖了Python编程的核心基础概念：

1. **数据类型与变量** - 动态类型、基本数据类型、字符串操作
2. **运算符** - 算术、比较、逻辑、赋值、身份、成员运算符
3. **条件语句** - if/elif/else、三元运算符、布尔值判断
4. **循环语句** - for/while循环、range()、enumerate()、列表推导式
5. **函数** - 函数定义、参数传递、返回值、lambda函数
6. **数据结构** - 列表、字典、元组、集合及其操作

### 关键要点

- **缩进很重要**：Python使用缩进来组织代码结构
- **动态类型**：变量类型由赋值自动推断
- **丰富的内置功能**：列表推导式、多重赋值、切片操作等
- **简洁的语法**：相比Java更加简洁和直观
- **强大的数据结构**：内置支持列表、字典、集合等

掌握这些基础概念是学习Python高级特性的重要基础。建议通过大量练习来加深理解和记忆。