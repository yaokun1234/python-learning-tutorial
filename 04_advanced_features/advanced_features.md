# 高级特性教程

> 代码不是越多越好，而是越少越好。代码不是越复杂越好，而是越简单越好。  
> —— Python之禅

---

# 第一章：切片（Slice）

## 一、切片基础

切片是Python中提取序列片段的强大工具，支持列表、元组、字符串等序列类型。

### Java vs Python：数组/集合操作对比

在Java中，要获取数组或List的子集，通常需要：

```java
// Java - 获取数组片段
int[] numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
int[] subArray = Arrays.copyOfRange(numbers, 2, 5); // [2, 3, 4]

// Java - 获取List片段
List<Integer> list = Arrays.asList(0, 1, 2, 3, 4, 5, 6, 7, 8, 9);
List<Integer> subList = list.subList(2, 5); // [2, 3, 4] - 注意：这是视图，不是新列表

// Java - 数组反转需要额外代码
Collections.reverse(Arrays.asList(numbers)); // 只能对List操作
```

而Python的切片操作非常直观和强大：

### 基本语法

```python
# Python切片语法：序列[start:stop:step]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[2:5])     # [2, 3, 4] - 从索引2到4（不包含5）
print(numbers[:3])      # [0, 1, 2] - 从开头到索引2
print(numbers[7:])      # [7, 8, 9] - 从索引7到末尾
print(numbers[:])       # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] - 完整浅复制
print(numbers[::2])     # [0, 2, 4, 6, 8] - 每隔一个元素（步长2）
print(numbers[::-1])    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] - 倒序（步长-1）
```

**关键点解释**：
- `start`：起始索引（包含），默认为0
- `stop`：结束索引（不包含），默认为序列长度  
- `step`：步长，默认为1，负数表示反向

**Java程序员注意**：
1. Python的切片**总是创建新对象**，不像Java的`subList()`返回视图
2. Python支持负索引和负步长，Java没有直接等价物
3. Python的切片语法比Java的`Arrays.copyOfRange()`更简洁直观

### 负索引切片

**Java vs Python：负索引处理**

Java中处理"倒数第N个元素"需要计算：
```java
// Java - 获取最后3个元素
int[] numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
int[] lastThree = Arrays.copyOfRange(numbers, numbers.length - 3, numbers.length);

// Java - 去除最后3个元素
int[] exceptLastThree = Arrays.copyOfRange(numbers, 0, numbers.length - 3);
```

Python的负索引让这变得非常直观：
```python
numbers = list(range(10))

print(numbers[-3:])     # [7, 8, 9] - 最后3个元素
print(numbers[:-3])     # [0, 1, 2, 3, 4, 5, 6] - 除了最后3个
print(numbers[-5:-2])   # [5, 6, 7] - 从倒数第5个到倒数第3个
print(numbers[3:-3])    # [3, 4, 5, 6] - 去掉前3个和后3个
```

**负索引的工作原理**：
- `-1` 表示最后一个元素
- `-2` 表示倒数第二个元素  
- 负索引 = 正索引 - 序列长度

这在Java中需要手动计算`array.length - index`，Python直接支持。

* * *

## 二、字符串切片

**Java vs Python：字符串操作对比**

Java中的字符串操作相对繁琐：
```java
// Java - 字符串切片操作
String text = "Hello, Python!";
String first5 = text.substring(0, 5);           // "Hello"
String from7 = text.substring(7);               // "Python!"
String reversed = new StringBuilder(text).reverse().toString();  // "!nohtyP ,olleH"

// Java - 获取文件扩展名
String filename = "document.pdf";
String extension = filename.substring(filename.lastIndexOf('.') + 1);  // "pdf"
```

Python的字符串切片更加简洁优雅：
```python
text = "Hello, Python!"

print(text[:5])         # "Hello" - 前5个字符
print(text[7:])         # "Python!" - 从第7个字符开始  
print(text[::2])        # "Hlo yhn" - 每隔一个字符
print(text[::-1])       # "!nohtyP ,olleH" - 字符串反转（Java需要StringBuilder）

# 提取文件扩展名（比Java简洁）
filename = "document.pdf"
extension = filename[filename.rfind('.') + 1:]
print(extension)        # "pdf"

# 去掉首尾空格（类似strip，但展示切片能力）
text_with_spaces = "  Hello World  "
cleaned = text_with_spaces[2:-2]
print(f"'{cleaned}'")   # "Hello World"
```

**优势对比**：
1. **简洁性**：Python一行代码实现，Java需要多行
2. **可读性**：`text[::-1]` 比 `new StringBuilder(text).reverse().toString()` 更直观
3. **统一性**：所有序列类型（字符串、列表、元组）使用相同语法

* * *

## 三、元组切片

```python
coordinates = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(coordinates[2:6])    # (3, 4, 5, 6)
print(coordinates[::3])    # (1, 4, 7, 10)
print(coordinates[-3:])    # (8, 9, 10)

# 元组切片返回新元组
original = (1, 2, 3, 4, 5)
sliced = original[1:4]
print(type(sliced))        # <class 'tuple'>
```

* * *

## 四、多维切片

```python
# 二维列表切片
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# 获取前两行
print(matrix[:2])          # [[1, 2, 3, 4], [5, 6, 7, 8]]

# 获取每行的前三列
rows_sliced = [row[:3] for row in matrix]
print(rows_sliced)         # [[1, 2, 3], [5, 6, 7], [9, 10, 11]]

# 获取第二列（所有行）
second_column = [row[1] for row in matrix]
print(second_column)       # [2, 6, 10]
```

* * *

## 五、切片的高级应用

### 列表的就地修改

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 替换切片
numbers[2:5] = [20, 30, 40]
print(numbers)             # [0, 1, 20, 30, 40, 5, 6, 7, 8, 9]

# 插入元素
numbers[3:3] = [100, 200]
print(numbers)             # [0, 1, 20, 100, 200, 30, 40, 5, 6, 7, 8, 9]

# 删除切片
del numbers[3:5]
print(numbers)             # [0, 1, 20, 30, 40, 5, 6, 7, 8, 9]
```

### 切片复制vs引用

```python
original = [1, 2, 3, 4, 5]

# 浅复制
shallow_copy = original[:]
shallow_copy[0] = 100
print(original)            # [1, 2, 3, 4, 5] - 原列表不变
print(shallow_copy)        # [100, 2, 3, 4, 5]

# 引用（不是切片）
reference = original
reference[0] = 200
print(original)            # [200, 2, 3, 4, 5] - 原列表改变
```

### 实用工具函数

```python
def get_last_n_elements(sequence, n):
    """获取序列的最后n个元素"""
    return sequence[-n:] if n > 0 else []

def remove_prefix_suffix(text, prefix_len=0, suffix_len=0):
    """移除字符串的前缀和后缀"""
    start = prefix_len if prefix_len > 0 else None
    end = -suffix_len if suffix_len > 0 else None
    return text[start:end]

# 测试
print(get_last_n_elements([1, 2, 3, 4, 5], 3))    # [3, 4, 5]
print(remove_prefix_suffix("Hello World", 2, 2))   # "llo Wor"
```

---

# 第二章：迭代（Iteration）

## 一、可迭代对象

**Java vs Python：迭代机制对比**

Java的迭代相对复杂，需要显式使用Iterator或增强for循环：
```java
// Java - 迭代List
List<String> fruits = Arrays.asList("apple", "banana", "orange");

// 方式1：传统for循环
for (int i = 0; i < fruits.size(); i++) {
    System.out.println(fruits.get(i));
}

// 方式2：增强for循环（Java 5+）
for (String fruit : fruits) {
    System.out.println(fruit);
}

// 方式3：Iterator（更底层）
Iterator<String> iterator = fruits.iterator();
while (iterator.hasNext()) {
    System.out.println(iterator.next());
}

// Java - 迭代Map
Map<String, Object> person = new HashMap<>();
person.put("name", "张三");
person.put("age", 25);

// 迭代键值对（Java 8+）
person.entrySet().forEach(entry -> 
    System.out.println(entry.getKey() + ": " + entry.getValue()));
```

Python的迭代非常直观，统一的语法适用于所有可迭代对象：
```python
# 迭代列表
fruits = ['apple', 'banana', 'orange']
for fruit in fruits:
    print(fruit)

# 迭代字符串（Java中需要toCharArray()或charAt()）
for char in 'Python':
    print(char)

# 迭代字典（比Java简洁很多）
person = {'name': '张三', 'age': 25, 'city': '北京'}

# 迭代键（默认行为）
for key in person:
    print(f"{key}: {person[key]}")

# 迭代值
for value in person.values():
    print(value)

# 迭代键值对（一行代码实现Java的复杂操作）
for key, value in person.items():
    print(f"{key}: {value}")
```

**Python迭代的优势**：
1. **统一语法**：`for item in iterable` 适用于所有类型
2. **自动解包**：如 `for key, value in dict.items()`
3. **直接支持**：字符串、范围等直接可迭代，Java需要额外转换
    print(char)

# 迭代字典
```python
person = {'name': '张三', 'age': 25, 'city': '北京'}
for key in person:
    print(f"{key}: {person[key]}")

# 迭代字典的值
for value in person.values():
    print(value)

# 迭代字典的键值对
for key, value in person.items():
    print(f"{key}: {value}")
```

* * *

## 二、判断对象是否可迭代

```python
from collections.abc import Iterable

# 检查对象是否可迭代
def is_iterable(obj):
    return isinstance(obj, Iterable)

# 测试不同类型
test_objects = [
    [1, 2, 3],           # 列表
    (1, 2, 3),           # 元组
    'hello',             # 字符串
    {'a': 1},            # 字典
    {1, 2, 3},           # 集合
    range(5),            # range对象
    123,                 # 整数
    3.14                 # 浮点数
]

for obj in test_objects:
    print(f"{obj} 是否可迭代: {is_iterable(obj)}")
```

* * *

## 三、enumerate() - 获取索引

```python
# 基本用法
fruits = ['apple', 'banana', 'orange']
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# 指定起始索引
for index, fruit in enumerate(fruits, start=1):
    print(f"第{index}个水果: {fruit}")

# 在字典中的应用
students = ['张三', '李四', '王五']
student_dict = {index: name for index, name in enumerate(students, 1)}
print(student_dict)        # {1: '张三', 2: '李四', 3: '王五'}
```

* * *

## 四、同时迭代多个序列

### zip() 函数

```python
# 基本用法
names = ['张三', '李四', '王五']
ages = [25, 30, 35]
cities = ['北京', '上海', '广州']

for name, age, city in zip(names, ages, cities):
    print(f"{name}, {age}岁, 来自{city}")

# 长度不同时，以最短的为准
numbers1 = [1, 2, 3, 4, 5]
numbers2 = [10, 20, 30]

for a, b in zip(numbers1, numbers2):
    print(f"{a} + {b} = {a + b}")
# 输出：1 + 10 = 11, 2 + 20 = 22, 3 + 30 = 33

# 使用zip创建字典
keys = ['name', 'age', 'city']
values = ['张三', 25, '北京']
person = dict(zip(keys, values))
print(person)              # {'name': '张三', 'age': 25, 'city': '北京'}
```

### itertools.zip_longest()

```python
from itertools import zip_longest

# 以最长序列为准，短的用fillvalue填充
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c', 'd', 'e']

for num, char in zip_longest(list1, list2, fillvalue=0):
    print(f"{num} - {char}")
# 输出：1 - a, 2 - b, 3 - c, 0 - d, 0 - e
```

* * *

## 五、迭代的高级技巧

### 嵌套迭代

```python
# 二维列表迭代
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 方式1：嵌套循环
for row in matrix:
    for element in row:
        print(element, end=' ')
    print()  # 换行

# 方式2：使用itertools.chain展平
from itertools import chain
flattened = list(chain.from_iterable(matrix))
print(flattened)           # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 方式3：生成器表达式
flattened = [element for row in matrix for element in row]
print(flattened)           # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### 条件迭代

```python
numbers = range(1, 21)

# 迭代偶数
for num in numbers:
    if num % 2 == 0:
        print(f"偶数: {num}")

# 使用filter
even_numbers = filter(lambda x: x % 2 == 0, numbers)
for num in even_numbers:
    print(f"偶数: {num}")

# 找到第一个满足条件的元素
def find_first(iterable, condition):
    for item in iterable:
        if condition(item):
            return item
    return None

first_even = find_first(range(1, 10), lambda x: x % 2 == 0)
print(f"第一个偶数: {first_even}")  # 2
```

### 迭代器协议

```python
# 手动迭代
numbers = [1, 2, 3, 4, 5]
iterator = iter(numbers)

try:
    while True:
        item = next(iterator)
        print(item)
except StopIteration:
    print("迭代结束")

# 带默认值的next()
iterator = iter([1, 2, 3])
print(next(iterator, 'end'))  # 1
print(next(iterator, 'end'))  # 2
print(next(iterator, 'end'))  # 3
print(next(iterator, 'end'))  # end（默认值）
```

---

# 第三章：列表生成式（List Comprehension）

## 一、基础语法

**Java vs Python：集合操作对比**

在Java中创建和变换集合通常需要多行代码：
```java
// Java - 创建平方数列表（传统方式）
List<Integer> squares = new ArrayList<>();
for (int x = 1; x <= 10; x++) {
    squares.add(x * x);
}

// Java 8+ Stream API（更函数式，但仍然冗长）
List<Integer> squaresStream = IntStream.rangeClosed(1, 10)
    .map(x -> x * x)
    .boxed()
    .collect(Collectors.toList());

// Java - 字符串转换
List<String> words = Arrays.asList("hello", "world", "python");
List<String> upperWords = words.stream()
    .map(String::toUpperCase)
    .collect(Collectors.toList());

// Java - 过滤偶数
List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
List<Integer> evenNumbers = numbers.stream()
    .filter(x -> x % 2 == 0)
    .collect(Collectors.toList());
```

Python的列表生成式让这些操作变得极其简洁：
```python
# Python - 基本语法：[表达式 for 变量 in 可迭代对象]
# Python - 条件语法：[表达式 for 变量 in 可迭代对象 if 条件]

# 传统方式 vs 列表生成式对比
squares_traditional = []
for x in range(1, 11):
    squares_traditional.append(x ** 2)

squares_comprehension = [x ** 2 for x in range(1, 11)]  # 一行代码！

print(squares_traditional)   # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(squares_comprehension) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 字符串处理（比Java Stream简洁）
words = ['hello', 'world', 'python', 'programming']
upper_words = [word.upper() for word in words]
print(upper_words)          # ['HELLO', 'WORLD', 'PYTHON', 'PROGRAMMING']

# 数学表达式
results = [x * 2 + 1 for x in range(5)]
print(results)              # [1, 3, 5, 7, 9]
```

**Python列表生成式的优势**：
1. **极致简洁**：一行代码实现Java需要多行的功能
2. **高性能**：比循环+append更快，比Java Stream更高效
3. **可读性强**：接近自然语言的表达方式
4. **无需导包**：不像Java Stream需要导入额外类

* * *

## 二、带条件的列表生成式

### 过滤条件

```python
# 生成偶数列表
even_numbers = [x for x in range(20) if x % 2 == 0]
print(even_numbers)         # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# 多重条件
numbers = range(1, 21)
filtered = [x for x in numbers if x % 2 == 0 and x % 3 == 0]
print(filtered)             # [6, 12, 18]

# 字符串过滤
text = "Hello World 123"
digits = [char for char in text if char.isdigit()]
letters = [char for char in text if char.isalpha()]
print(digits)               # ['1', '2', '3']
print(letters)              # ['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd']
```

### 条件表达式

```python
# 使用三元运算符
numbers = range(-5, 6)
abs_values = [x if x >= 0 else -x for x in numbers]
print(abs_values)           # [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5]

# 分类处理
grades = [85, 92, 78, 96, 88, 73, 90]
grade_levels = ['优秀' if g >= 90 else '良好' if g >= 80 else '及格' if g >= 60 else '不及格' 
                for g in grades]
print(grade_levels)         # ['良好', '优秀', '及格', '优秀', '良好', '及格', '优秀']
```

* * *

## 三、嵌套列表生成式

### 处理二维列表

```python
# 创建矩阵
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(matrix)               # [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

# 展平二维列表
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [element for row in matrix for element in row]
print(flattened)            # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 矩阵转置
original = [[1, 2, 3], [4, 5, 6]]
transposed = [[row[i] for row in original] for i in range(len(original[0]))]
print(transposed)           # [[1, 4], [2, 5], [3, 6]]

# 使用zip转置（更简洁）
transposed_zip = [list(col) for col in zip(*original)]
print(transposed_zip)       # [[1, 4], [2, 5], [3, 6]]
```

### 复杂嵌套

```python
# 生成坐标点
coordinates = [(x, y) for x in range(3) for y in range(3)]
print(coordinates)          # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

# 带条件的坐标生成
diagonal_coords = [(x, y) for x in range(5) for y in range(5) if x == y]
print(diagonal_coords)      # [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]

# 生成乘法表
multiplication_table = [f"{i} x {j} = {i*j}" for i in range(1, 4) for j in range(1, 4)]
for item in multiplication_table:
    print(item)
```

* * *

## 四、字典和集合生成式

### 字典生成式

```python
# 基本字典生成式
squares_dict = {x: x**2 for x in range(1, 6)}
print(squares_dict)         # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 从两个列表创建字典
keys = ['name', 'age', 'city']
values = ['张三', 25, '北京']
person = {k: v for k, v in zip(keys, values)}
print(person)               # {'name': '张三', 'age': 25, 'city': '北京'}

# 条件字典生成式
numbers = range(1, 11)
even_squares = {x: x**2 for x in numbers if x % 2 == 0}
print(even_squares)         # {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# 字符统计
text = "hello world"
char_count = {char: text.count(char) for char in set(text) if char != ' '}
print(char_count)           # {'e': 1, 'h': 1, 'l': 3, 'o': 2, 'r': 1, 'd': 1, 'w': 1}
```

### 集合生成式

```python
# 基本集合生成式
unique_squares = {x**2 for x in range(-5, 6)}
print(unique_squares)       # {0, 1, 4, 9, 16, 25}

# 字符去重
text = "hello world"
unique_chars = {char.lower() for char in text if char.isalpha()}
print(unique_chars)         # {'h', 'e', 'l', 'o', 'w', 'r', 'd'}

# 数据清洗
raw_data = ['  Hello  ', 'WORLD', '  python  ', 'Programming']
cleaned_data = {item.strip().lower() for item in raw_data}
print(cleaned_data)         # {'hello', 'world', 'python', 'programming'}
```

* * *

## 五、实际应用示例

### 数据处理

```python
# 学生成绩处理
students = [
    {'name': '张三', 'scores': [85, 92, 78]},
    {'name': '李四', 'scores': [90, 88, 94]},
    {'name': '王五', 'scores': [76, 82, 89]}
]

# 计算平均分
averages = [{**student, 'average': sum(student['scores']) / len(student['scores'])} 
            for student in students]

# 找出优秀学生（平均分>=85）
excellent_students = [student['name'] for student in averages if student['average'] >= 85]
print(excellent_students)   # ['张三', '李四']
```

### 文件处理

```python
import os

# 获取目录下的Python文件（示例）
def get_python_files(directory):
    try:
        return [f for f in os.listdir(directory) if f.endswith('.py')]
    except FileNotFoundError:
        return []

# 文件大小分类
def classify_files_by_size(files):
    file_sizes = [(f, os.path.getsize(f)) for f in files if os.path.exists(f)]
    return {
        'small': [f for f, size in file_sizes if size < 1024],
        'medium': [f for f, size in file_sizes if 1024 <= size < 10240],
        'large': [f for f, size in file_sizes if size >= 10240]
    }
```

### Web数据处理

```python
# 模拟API响应数据
api_response = [
    {'id': 1, 'name': 'Product A', 'price': 29.99, 'category': 'electronics'},
    {'id': 2, 'name': 'Product B', 'price': 15.50, 'category': 'books'},
    {'id': 3, 'name': 'Product C', 'price': 99.99, 'category': 'electronics'},
    {'id': 4, 'name': 'Product D', 'price': 8.99, 'category': 'books'}
]

# 提取特定类别的产品名称
electronics = [product['name'] for product in api_response 
               if product['category'] == 'electronics']
print(electronics)          # ['Product A', 'Product C']

# 价格转换（美元到人民币，假设汇率7.0）
products_cny = [{**product, 'price_cny': product['price'] * 7.0} 
                for product in api_response]

# 按价格分类
expensive_products = [p['name'] for p in products_cny if p['price_cny'] > 100]
print(expensive_products)   # ['Product C']
```

---

# 第四章：生成器（Generator）

## 一、什么是生成器

**Java vs Python：延迟计算对比**

Java中实现延迟计算相对复杂，通常需要：
```java
// Java - 传统方式，必须预先计算所有值
List<Integer> squares = new ArrayList<>();
for (int i = 0; i < 1000000; i++) {
    squares.add(i * i);  // 占用大量内存
}

// Java 8+ Stream（有一定延迟计算能力，但仍有限制）
Stream<Integer> squareStream = IntStream.range(0, 1000000)
    .map(x -> x * x);  // 延迟计算，但Stream只能使用一次

// Java - 自定义Iterator实现延迟计算（代码复杂）
class SquareIterator implements Iterator<Integer> {
    private int current = 0;
    private final int limit;
    
    public SquareIterator(int limit) { this.limit = limit; }
    
    @Override
    public boolean hasNext() { return current < limit; }
    
    @Override
    public Integer next() {
        if (!hasNext()) throw new NoSuchElementException();
        return current * current++;
    }
}
```

Python的生成器让延迟计算变得极其简单：
```python
# 生成器的核心优势
# 1. 内存效率：只在需要时生成值，不占用大量内存
# 2. 延迟计算：惰性求值，提高程序效率  
# 3. 无限序列：可以生成无限长的序列

# 生成器表达式 vs 列表生成式
list_comp = [x**2 for x in range(1000000)]    # 立即计算，占用大量内存
gen_exp = (x**2 for x in range(1000000))      # 延迟计算，几乎不占内存

print(type(list_comp))      # <class 'list'>
print(type(gen_exp))        # <class 'generator'>

# 内存占用对比
import sys
print(f"列表占用内存: {sys.getsizeof(list_comp)} bytes")      # 约8MB+
print(f"生成器占用内存: {sys.getsizeof(gen_exp)} bytes")      # 约200bytes

# 使用生成器（Java需要复杂的Iterator实现）
for i, value in enumerate(gen_exp):
    if i >= 10:  # 只计算前10个值
        break
    print(value)
```

**关键理解**：
- **Java的问题**：传统方式必须预先计算所有值；Stream API有限制且语法复杂
- **Python的优势**：语法简单，真正的延迟计算，可重复使用（通过重新创建）
```python
list_comp = [x**2 for x in range(1000000)]    # 占用大量内存
gen_exp = (x**2 for x in range(1000000))      # 几乎不占内存

print(type(list_comp))      # <class 'list'>
print(type(gen_exp))        # <class 'generator'>
```
### 内存占用对比
```python
import sys
print(f"列表占用内存: {sys.getsizeof(list_comp)} bytes")
print(f"生成器占用内存: {sys.getsizeof(gen_exp)} bytes")
```
## 使用生成器
```python
for i, value in enumerate(gen_exp):
    if i >= 10:  # 只打印前10个值
        break
    print(value)
```

* * *

## 二、生成器函数

使用 `yield` 关键字的函数会返回一个生成器对象。

### 基本生成器函数

```python
def simple_generator():
    """简单的生成器函数"""
    print("开始生成")
    yield 1
    print("生成了1")
    yield 2
    print("生成了2")
    yield 3
    print("结束生成")

# 创建生成器对象
gen = simple_generator()
print(type(gen))            # <class 'generator'>

# 逐个获取值
print(next(gen))            # 开始生成 \n 1
print(next(gen))            # 生成了1 \n 2
print(next(gen))            # 生成了2 \n 3

# 或者使用for循环
gen2 = simple_generator()
for value in gen2:
    print(f"接收到: {value}")
```

### 实用生成器示例

```python
def fibonacci_generator(n):
    """斐波那契数列生成器"""
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

# 使用斐波那契生成器
fib_gen = fibonacci_generator(10)
fib_list = list(fib_gen)
print(fib_list)             # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

def even_numbers(start, end):
    """生成指定范围内的偶数"""
    current = start if start % 2 == 0 else start + 1
    while current <= end:
        yield current
        current += 2

# 生成1到20之间的偶数
evens = list(even_numbers(1, 20))
print(evens)                # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

def countdown(n):
    """倒计时生成器"""
    print(f"开始倒计时从 {n}")
    while n > 0:
        yield n
        n -= 1
    print("倒计时结束！")

# 使用倒计时
for num in countdown(5):
    print(f"还剩 {num} 秒")
```

* * *

## 三、生成器的高级特性

### send() 方法

```python
def echo_generator():
    """回声生成器，可以接收发送的值"""
    while True:
        received = yield
        if received is not None:
            yield f"回声: {received}"

# 使用send()方法
gen = echo_generator()
next(gen)  # 启动生成器

print(gen.send("Hello"))    # 回声: Hello
next(gen)  # 准备接收下一个值
print(gen.send("World"))    # 回声: World

def accumulator():
    """累加器生成器"""
    total = 0
    while True:
        value = yield total
        if value is not None:
            total += value

acc = accumulator()
next(acc)  # 启动生成器
print(acc.send(10))         # 10
print(acc.send(20))         # 30
print(acc.send(5))          # 35
```

### throw() 和 close() 方法

```python
def robust_generator():
    """健壮的生成器，处理异常"""
    try:
        for i in range(10):
            print(f"生成 {i}")
            yield i
    except ValueError as e:
        print(f"捕获异常: {e}")
        yield "异常处理"
    finally:
        print("生成器清理")

gen = robust_generator()
print(next(gen))            # 生成 0 \n 0
print(next(gen))            # 生成 1 \n 1

# 向生成器抛出异常
try:
    print(gen.throw(ValueError, "测试异常"))  # 捕获异常: 测试异常 \n 异常处理
except StopIteration:
    pass

# 关闭生成器
gen2 = robust_generator()
next(gen2)
gen2.close()                # 生成器清理
```

* * *

## 四、无限生成器

```python
def infinite_sequence():
    """无限数列生成器"""
    num = 0
    while True:
        yield num
        num += 1

def prime_generator():
    """无限素数生成器"""
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

# 使用无限生成器（注意要有停止条件）
inf_gen = infinite_sequence()
first_10 = [next(inf_gen) for _ in range(10)]
print(first_10)             # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 前10个素数
prime_gen = prime_generator()
first_10_primes = [next(prime_gen) for _ in range(10)]
print(first_10_primes)      # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def cycle_generator(iterable):
    """循环生成器，无限循环一个可迭代对象"""
    while True:
        for item in iterable:
            yield item

# 循环颜色
colors = ['red', 'green', 'blue']
color_cycle = cycle_generator(colors)
for i, color in enumerate(color_cycle):
    if i >= 10:  # 只演示10次
        break
    print(f"第{i+1}次: {color}")
```

* * *

## 五、生成器的实际应用

### 文件处理

```python
def read_file_lines(filename):
    """逐行读取文件的生成器"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, 1):
                yield line_num, line.strip()
    except FileNotFoundError:
        print(f"文件 {filename} 不存在")

def process_large_file(filename, batch_size=100):
    """批量处理大文件"""
    batch = []
    for line_num, line in read_file_lines(filename):
        batch.append((line_num, line))
        if len(batch) >= batch_size:
            yield batch
            batch = []
    
    # 处理剩余的行
    if batch:
        yield batch

# 使用示例（需要实际文件）
# for batch in process_large_file('large_file.txt'):
#     print(f"处理批次，包含 {len(batch)} 行")
```

### 数据管道

```python
def data_source():
    """数据源生成器"""
    import random
    for i in range(100):
        yield {
            'id': i,
            'value': random.randint(1, 100),
            'category': random.choice(['A', 'B', 'C'])
        }

def filter_data(data_gen, condition):
    """数据过滤生成器"""
    for item in data_gen:
        if condition(item):
            yield item

def transform_data(data_gen, transformer):
    """数据转换生成器"""
    for item in data_gen:
        yield transformer(item)

# 构建数据处理管道
source = data_source()
filtered = filter_data(source, lambda x: x['value'] > 50)
transformed = transform_data(filtered, lambda x: {**x, 'processed': True})

# 处理数据
results = list(transformed)
print(f"处理了 {len(results)} 条记录")
for item in results[:5]:  # 显示前5条
    print(item)
```

### 协程式编程

```python
def consumer():
    """消费者协程"""
    print("消费者准备就绪")
    try:
        while True:
            item = yield
            print(f"消费: {item}")
    except GeneratorExit:
        print("消费者关闭")

def producer(consumer_gen):
    """生产者函数"""
    next(consumer_gen)  # 启动消费者
    for i in range(5):
        print(f"生产: item_{i}")
        consumer_gen.send(f"item_{i}")
    consumer_gen.close()

# 使用协程
consumer_gen = consumer()
producer(consumer_gen)
```

---

# 第五章：迭代器（Iterator）

## 一、迭代器协议

迭代器是实现了迭代器协议的对象，必须实现以下两个方法：
- `__iter__()`：返回迭代器对象本身
- `__next__()`：返回下一个值，没有更多值时抛出 `StopIteration` 异常

### 迭代器 vs 可迭代对象

```python
from collections.abc import Iterable, Iterator

# 可迭代对象
numbers = [1, 2, 3, 4, 5]
print(isinstance(numbers, Iterable))    # True
print(isinstance(numbers, Iterator))    # False

# 获取迭代器
numbers_iter = iter(numbers)
print(isinstance(numbers_iter, Iterable))    # True
print(isinstance(numbers_iter, Iterator))    # True

# 使用迭代器
print(next(numbers_iter))    # 1
print(next(numbers_iter))    # 2
print(next(numbers_iter))    # 3

# 迭代器只能使用一次
for num in numbers_iter:
    print(num)               # 4, 5

# 再次使用会发现已经耗尽
for num in numbers_iter:
    print(num)               # 没有输出
```

* * *

## 二、自定义迭代器

### 简单计数器迭代器

```python
class CounterIterator:
    """计数器迭代器"""
    
    def __init__(self, start, end):
        self.current = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        self.current += 1
        return self.current - 1

# 使用自定义迭代器
counter = CounterIterator(1, 6)
for num in counter:
    print(num)              # 1, 2, 3, 4, 5

# 手动使用
counter2 = CounterIterator(10, 13)
print(next(counter2))       # 10
print(next(counter2))       # 11
print(next(counter2))       # 12
# print(next(counter2))     # StopIteration异常
```

### 斐波那契迭代器

```python
class FibonacciIterator:
    """斐波那契数列迭代器"""
    
    def __init__(self, max_count):
        self.max_count = max_count
        self.count = 0
        self.current = 0
        self.next_val = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count >= self.max_count:
            raise StopIteration
        
        if self.count == 0:
            self.count += 1
            return self.current
        elif self.count == 1:
            self.count += 1
            return self.next_val
        else:
            result = self.current + self.next_val
            self.current = self.next_val
            self.next_val = result
            self.count += 1
            return result

# 使用斐波那契迭代器
fib = FibonacciIterator(10)
fib_list = list(fib)
print(fib_list)             # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

* * *

## 三、可迭代类

### 自定义可迭代类

```python
class NumberCollection:
    """数字集合类"""
    
    def __init__(self, numbers):
        self.numbers = numbers
    
    def __iter__(self):
        return NumberIterator(self.numbers)

class NumberIterator:
    """数字集合迭代器"""
    
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.numbers):
            raise StopIteration
        value = self.numbers[self.index]
        self.index += 1
        return value

# 使用自定义可迭代类
collection = NumberCollection([1, 2, 3, 4, 5])

# 可以多次迭代
for num in collection:
    print(f"第一次: {num}")

for num in collection:
    print(f"第二次: {num}")

# 可以创建多个独立的迭代器
iter1 = iter(collection)
iter2 = iter(collection)
print(next(iter1))          # 1
print(next(iter2))          # 1
print(next(iter1))          # 2
```

### 倒序迭代器

```python
class ReverseIterator:
    """倒序迭代器"""
    
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index <= 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

class ReversibleCollection:
    """支持正序和倒序迭代的集合"""
    
    def __init__(self, data):
        self.data = data
    
    def __iter__(self):
        """正序迭代"""
        return iter(self.data)
    
    def __reversed__(self):
        """倒序迭代"""
        return ReverseIterator(self.data)

# 使用倒序迭代
collection = ReversibleCollection([1, 2, 3, 4, 5])

print("正序:")
for item in collection:
    print(item)

print("倒序:")
for item in reversed(collection):
    print(item)
```

* * *

## 四、迭代器工具

### itertools 模块

```python
import itertools

# count - 无限计数器
counter = itertools.count(10, 2)  # 从10开始，步长为2
first_5 = [next(counter) for _ in range(5)]
print(first_5)              # [10, 12, 14, 16, 18]

# cycle - 循环迭代
colors = itertools.cycle(['red', 'green', 'blue'])
color_list = [next(colors) for _ in range(8)]
print(color_list)           # ['red', 'green', 'blue', 'red', 'green', 'blue', 'red', 'green']

# repeat - 重复值
repeated = itertools.repeat('hello', 3)
print(list(repeated))       # ['hello', 'hello', 'hello']

# chain - 连接多个迭代器
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
chained = itertools.chain(list1, list2, list3)
print(list(chained))        # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# compress - 根据选择器过滤
data = ['a', 'b', 'c', 'd', 'e']
selectors = [1, 0, 1, 0, 1]
filtered = itertools.compress(data, selectors)
print(list(filtered))       # ['a', 'c', 'e']

# dropwhile 和 takewhile
numbers = [1, 3, 5, 2, 4, 6, 7, 9]
dropped = itertools.dropwhile(lambda x: x < 5, numbers)
print(list(dropped))        # [5, 2, 4, 6, 7, 9]

taken = itertools.takewhile(lambda x: x < 5, numbers)
print(list(taken))          # [1, 3]

# groupby - 分组
students = [
    ('张三', 'A'), ('李四', 'A'), ('王五', 'B'), ('赵六', 'B'), ('孙七', 'A')
]
students.sort(key=lambda x: x[1])  # 按班级排序
grouped = itertools.groupby(students, key=lambda x: x[1])
for class_name, group in grouped:
    print(f"{class_name}班: {[name for name, _ in group]}")
```

### 组合和排列

```python
import itertools

# 排列
data = ['A', 'B', 'C']
perms = list(itertools.permutations(data, 2))
print(perms)                # [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

# 组合
combs = list(itertools.combinations(data, 2))
print(combs)                # [('A', 'B'), ('A', 'C'), ('B', 'C')]

# 可重复组合
combs_with_replacement = list(itertools.combinations_with_replacement(data, 2))
print(combs_with_replacement)  # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]

# 笛卡尔积
colors = ['red', 'blue']
sizes = ['S', 'M', 'L']
products = list(itertools.product(colors, sizes))
print(products)             # [('red', 'S'), ('red', 'M'), ('red', 'L'), ('blue', 'S'), ('blue', 'M'), ('blue', 'L')]
```

* * *

## 五、迭代器的实际应用

### 大数据处理

```python
class BatchIterator:
    """批处理迭代器"""
    
    def __init__(self, iterable, batch_size):
        self.iterator = iter(iterable)
        self.batch_size = batch_size
    
    def __iter__(self):
        return self
    
    def __next__(self):
        batch = []
        try:
            for _ in range(self.batch_size):
                batch.append(next(self.iterator))
        except StopIteration:
            if batch:
                return batch
            raise
        return batch

# 使用批处理迭代器
data = range(25)
batch_iter = BatchIterator(data, 5)
for batch in batch_iter:
    print(f"批次: {batch}")
```

### 惰性求值链

```python
class LazyMap:
    """惰性映射迭代器"""
    
    def __init__(self, func, iterable):
        self.func = func
        self.iterator = iter(iterable)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        return self.func(next(self.iterator))

class LazyFilter:
    """惰性过滤迭代器"""
    
    def __init__(self, predicate, iterable):
        self.predicate = predicate
        self.iterator = iter(iterable)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while True:
            value = next(self.iterator)
            if self.predicate(value):
                return value

# 构建惰性求值链
numbers = range(1, 20)
filtered = LazyFilter(lambda x: x % 2 == 0, numbers)  # 过滤偶数
mapped = LazyMap(lambda x: x ** 2, filtered)           # 平方

# 只在需要时计算
result = list(mapped)
print(result)               # [4, 16, 36, 64, 100, 144, 196, 256, 324]
```

### 内存友好的文件处理

```python
class CSVRowIterator:
    """CSV行迭代器"""
    
    def __init__(self, filename, delimiter=','):
        self.filename = filename
        self.delimiter = delimiter
        self.file = None
    
    def __iter__(self):
        self.file = open(self.filename, 'r', encoding='utf-8')
        return self
    
    def __next__(self):
        if self.file is None:
            raise StopIteration
        
        line = self.file.readline()
        if not line:
            self.file.close()
            raise StopIteration
        
        return line.strip().split(self.delimiter)
    
    def __del__(self):
        if self.file and not self.file.closed:
            self.file.close()

# 使用示例（需要实际的CSV文件）
# csv_iter = CSVRowIterator('data.csv')
# for row in csv_iter:
#     print(row)
```

---

# 总结

## Python高级特性的核心思想

1. **简洁优雅**：用更少的代码表达更多的逻辑
2. **内存效率**：按需生成，避免不必要的内存占用
3. **惰性求值**：延迟计算，提高程序性能
4. **可组合性**：不同特性可以组合使用，构建强大的数据处理管道

## Java程序员的学习路径

### 思维转换

从Java到Python，需要转换以下思维模式：

1. **从静态类型到动态类型**
   ```java
   // Java - 需要显式声明类型
   List<String> words = new ArrayList<>();
   Stream<String> upperWords = words.stream().map(String::toUpperCase);
   ```
   ```python
   # Python - 类型推断，专注逻辑
   words = ['hello', 'world']  
   upper_words = [word.upper() for word in words]
   ```

2. **从冗长语法到简洁表达**
   ```java
   // Java - 多行代码实现简单逻辑
   List<Integer> evenSquares = numbers.stream()
       .filter(x -> x % 2 == 0)
       .map(x -> x * x)
       .collect(Collectors.toList());
   ```
   ```python
   # Python - 一行代码表达完整逻辑
   even_squares = [x**2 for x in numbers if x % 2 == 0]
   ```

3. **从预先分配到按需生成**
   ```java
   // Java - 通常需要预先分配内存
   List<Integer> results = new ArrayList<>(1000000);
   for (int i = 0; i < 1000000; i++) {
       results.add(process(i));  // 全部计算并存储
   }
   ```
   ```python
   # Python - 按需生成，节省内存
   results = (process(i) for i in range(1000000))  # 只在需要时计算
   ```

### 对应关系表

| Java概念 | Python等价物 | 优势对比 |
|----------|---------------|----------|
| `for(int i=0; i<n; i++)` | `for i in range(n)` | 更直观，无需索引管理 |
| `Arrays.copyOfRange()` | `list[start:end]` | 语法简洁，支持负索引 |
| `Stream.map().filter()` | 列表生成式 | 一行代码，性能更好 |
| `Iterator<T>` | 生成器函数 | 语法简单，功能更强 |
| `Iterable<T>` | 任何可迭代对象 | 统一的迭代协议 |

### 学习建议

1. **从简单开始**：先掌握切片和基本迭代
2. **多写列表生成式**：替代传统for循环思维
3. **理解惰性求值**：生成器概念对Java程序员较新
4. **实践组合使用**：将多个特性结合使用
5. **关注性能**：Python的这些特性通常比Java更高效

### 常见陷阱

1. **生成器只能用一次**
   ```python
   gen = (x for x in range(5))
   list(gen)  # [0, 1, 2, 3, 4]
   list(gen)  # [] - 已经耗尽！
   ```

2. **切片创建新对象**
   ```python
   original = [1, 2, 3]
   sliced = original[:]  # 新对象，不是视图（不同于Java的subList）
   ```

3. **列表生成式的作用域**
   ```python
   # 列表生成式有自己的作用域
   x = 'global'
   result = [x for x in range(5)]  # 不会影响外部的x
   print(x)  # 'global'
   ```

## 选择指南

| 场景 | 推荐特性 | Java对比 |
|------|----------|----------|
| 提取序列片段 | 切片 | 比Arrays.copyOfRange()简洁 |
| 遍历数据结构 | 迭代 | 比索引循环更Pythonic |
| 创建简单列表 | 列表生成式 | 比Stream API简洁高效 |
| 处理大数据集 | 生成器 | 比Java Iterator更易用 |
| 自定义遍历逻辑 | 迭代器 | 实现更简单，功能更强 |

## 最佳实践

1. **优先使用内置特性**：切片、列表生成式等内置特性通常比手写循环更高效
2. **合理使用生成器**：处理大数据时优先考虑生成器
3. **组合使用**：不同特性可以组合使用，如生成器表达式配合itertools
4. **注意内存使用**：对于大数据集，优先使用惰性求值的特性
5. **保持代码可读性**：不要为了炫技而牺牲代码的可读性

掌握这些高级特性，作为Java程序员的您将能够写出更加优雅、高效和Pythonic的代码！Python的表达能力会让您感受到编程的另一种美感。