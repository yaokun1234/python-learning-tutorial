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

Java 对应：

```java
int a = 5, b = 3;
System.out.println(a == b);   // false
System.out.println(a != b);   // true
System.out.println(a > b);    // true
// 其他类似...
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

Java 对应：

```java
boolean a = true, b = false;
System.out.println(a && b);   // false
System.out.println(a || b);   // true
System.out.println(!a);       // false
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

Java 类似：

```java
int a = 10;
a += 5;     // a = a + 5
a -= 3;     // a = a - 3
a *= 2;     // a = a * 2
a /= 4;     // a = a / 4
a %= 2;     // a = a % 2
// Java 没有 **= 运算符
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

Java 需要使用方法：

```java
String text = "hello world";
List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);

System.out.println(text.contains("h"));     // true
System.out.println(numbers.contains(3));    // true
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