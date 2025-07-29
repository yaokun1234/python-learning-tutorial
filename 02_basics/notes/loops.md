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

Java 对应：

```java
// 类似 range(5)
for (int i = 0; i < 5; i++) {
    System.out.println(i);
}

// 类似 range(1, 6)
for (int i = 1; i < 6; i++) {
    System.out.println(i);
}

// 类似 range(0, 10, 2)
for (int i = 0; i < 10; i += 2) {
    System.out.println(i);
}
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

# 指定起始索引
for index, fruit in enumerate(fruits, 1):
    print(f"{index}: {fruit}")
    
# 输出：
# 1: 苹果
# 2: 香蕉
# 3: 橘子
```

Java 对应：

```java
String[] fruits = {"苹果", "香蕉", "橘子"};
for (int i = 0; i < fruits.length; i++) {
    System.out.println(i + ": " + fruits[i]);
}
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

Java 对应：

```java
int count = 0;
while (count < 5) {
    System.out.println("计数：" + count);
    count++;
}
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

Java 对应：

```java
// break
for (int i = 0; i < 10; i++) {
    if (i == 5) break;
    System.out.println(i);
}

// continue
for (int i = 0; i < 10; i++) {
    if (i % 2 == 0) continue;
    System.out.println(i);
}
```

* * *

## 六、嵌套循环

```python
# 打印乘法表的一部分
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print("---")  # 分隔线
```

* * *

## 七、遍历字典

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

Java 对应：

```java
Map<String, Object> person = new HashMap<>();
person.put("name", "张三");
person.put("age", 25);
person.put("city", "北京");

// 遍历键值对
for (Map.Entry<String, Object> entry : person.entrySet()) {
    System.out.println(entry.getKey() + ": " + entry.getValue());
}
```

* * *

## 八、zip() 函数

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

## 九、列表推导式

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

Java 8+ 对应：

```java
// 使用 Stream API
List<Integer> squares = IntStream.range(0, 10)
    .map(x -> x * x)
    .boxed()
    .collect(Collectors.toList());
```

* * *

## 十、else 子句

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

# while-else
count = 0
while count < 3:
    print(count)
    count += 1
else:
    print("while 循环正常结束")
```

* * *

## 十一、常用循环模式

### 1. 计数循环

```python
# 倒计时
for i in range(10, 0, -1):
    print(i)
print("发射！")
```

### 2. 累计计算

```python
# 计算总和
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print(total)  # 15

# 使用内置函数更简单
total = sum(numbers)
```

### 3. 查找元素

```python
names = ["张三", "李四", "王五"]
target = "李四"

for name in names:
    if name == target:
        print(f"找到了：{name}")
        break
else:
    print(f"没找到：{target}")
```

### 4. 处理文件

```python
# 逐行读取文件
with open("data.txt", "r") as file:
    for line_num, line in enumerate(file, 1):
        print(f"第{line_num}行：{line.strip()}")
```

### 5. 批处理

```python
items = range(100)
batch_size = 10

for i in range(0, len(items), batch_size):
    batch = items[i:i + batch_size]
    print(f"处理批次：{batch}")
```