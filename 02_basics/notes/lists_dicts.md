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

Java 对应（需要使用方法）：

```java
List<Integer> numbers = Arrays.asList(0, 1, 2, 3, 4, 5, 6, 7, 8, 9);
List<Integer> subset = numbers.subList(2, 5); // [2, 3, 4]
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

# 删除最后一个元素
last = fruits.pop()
print(last)     # 香蕉
print(fruits)   # ['苹果']

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

## 七、嵌套结构

### 列表中的列表

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][2])  # 6 (第二行第三列)

# 遍历二维列表
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()  # 换行
```

### 字典中的列表和字典

```python
students = {
    "张三": {
        "年龄": 20,
        "成绩": [85, 92, 78],
        "爱好": ["篮球", "读书"]
    },
    "李四": {
        "年龄": 21,
        "成绩": [88, 85, 90],
        "爱好": ["游泳", "音乐"]
    }
}

print(students["张三"]["成绩"][0])  # 85
print(students["李四"]["爱好"])     # ['游泳', '音乐']
```

* * *

## 八、常用内置函数

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

### 检查元素

```python
fruits = ["苹果", "香蕉", "橘子"]

print("苹果" in fruits)     # True
print("葡萄" not in fruits) # True
print(fruits.index("香蕉"))  # 1 - 返回索引
print(fruits.count("苹果"))  # 1 - 计算出现次数
```

* * *

## 九、元组（Tuple）

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

## 十、集合（Set）

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

## 十一、常用模式

### 1. 列表去重但保持顺序

```python
def remove_duplicates(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

numbers = [1, 2, 2, 3, 1, 4, 3, 5]
unique = remove_duplicates(numbers)
print(unique)  # [1, 2, 3, 4, 5]
```

### 2. 分组操作

```python
students = [
    {"name": "张三", "class": "A"},
    {"name": "李四", "class": "B"},
    {"name": "王五", "class": "A"},
    {"name": "赵六", "class": "B"}
]

# 按班级分组
classes = {}
for student in students:
    class_name = student["class"]
    if class_name not in classes:
        classes[class_name] = []
    classes[class_name].append(student["name"])

print(classes)  # {'A': ['张三', '王五'], 'B': ['李四', '赵六']}
```

### 3. 计数器

```python
from collections import Counter

text = "hello world"
char_count = Counter(text)
print(char_count)  # Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

# 手动实现计数
words = ["苹果", "香蕉", "苹果", "橘子", "香蕉", "苹果"]
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)  # {'苹果': 3, '香蕉': 2, '橘子': 1}
```