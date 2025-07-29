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

Java 对应：

```java
int age = 16;
if (age >= 18) {
    System.out.println("已成年");
} else {
    System.out.println("未成年");
}
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

Java 对应：

```java
int score = 85;
if (score >= 90) {
    System.out.println("优秀");
} else if (score >= 80) {
    System.out.println("良好");
} else if (score >= 60) {
    System.out.println("及格");
} else {
    System.out.println("不及格");
}
```

**注意**：Python 使用 `elif`，Java 使用 `else if`。

* * *

## 四、嵌套条件语句

```python
weather = "晴天"
temperature = 25

if weather == "晴天":
    if temperature > 30:
        print("太热了，待在室内")
    elif temperature > 20:
        print("天气不错，适合出门")
    else:
        print("有点凉，记得穿外套")
else:
    print("天气不好，不适合出门")
```

* * *

## 五、逻辑运算符在条件中的应用

```python
age = 25
has_license = True

# 使用 and
if age >= 18 and has_license:
    print("可以开车")

# 使用 or
weather = "雨天"
if weather == "晴天" or weather == "多云":
    print("适合户外活动")

# 使用 not
is_weekend = False
if not is_weekend:
    print("工作日")
```

Java 对应：

```java
int age = 25;
boolean hasLicense = true;

// 使用 &&
if (age >= 18 && hasLicense) {
    System.out.println("可以开车");
}

// 使用 ||
String weather = "雨天";
if (weather.equals("晴天") || weather.equals("多云")) {
    System.out.println("适合户外活动");
}

// 使用 !
boolean isWeekend = false;
if (!isWeekend) {
    System.out.println("工作日");
}
```

* * *

## 六、三元运算符（条件表达式）

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

## 七、None 值的判断

```python
name = None

# 检查是否为 None
if name is None:
    print("姓名未设置")

# 检查是否不为 None
if name is not None:
    print(f"你好，{name}")

# 简化写法（利用 None 为 False 的特性）
if not name:
    print("姓名未设置")

if name:
    print(f"你好，{name}")
```

* * *

## 八、布尔值的真假性

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

## 九、成员运算符在条件中的应用

```python
# 检查字符是否在字符串中
text = "hello world"
if 'o' in text:
    print("包含字母 o")

# 检查元素是否在列表中
fruits = ["苹果", "香蕉", "橘子"]
if "苹果" in fruits:
    print("有苹果")

# 检查键是否在字典中
person = {"name": "张三", "age": 25}
if "name" in person:
    print(f"姓名：{person['name']}")
```

* * *

## 十、常用模式

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

### 4. 异常处理替代

```python
# 使用条件语句避免错误
numbers = [1, 2, 3]
index = 5

if index < len(numbers):
    print(numbers[index])
else:
    print("索引超出范围")
```