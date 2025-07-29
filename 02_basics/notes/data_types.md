## 一、变量声明与赋值

### Python 中的变量不需要声明类型：

```
a = 10
b = "hello"
c = True
```

等价于 Java：

```
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
|---	|---	|---	|
|`float`	|`b = 1.23`	|`float` / `double`	|
|`bool`	|`c = True`	|`boolean`	|
|`str`	|`d = 'Hello'`	|`String`	|
|`None`	|`e = None`	|`null`	|

`None` 相当于 Java 的 `null`，表示“什么都没有”。
* * *

## 三、字符串操作

### 单引号和双引号都可以表示字符串

```
s1 = 'hello'
s2 = "world"
```

### 多行字符串用三引号 `'''` 或 `"""`

```
s3 = '''第一行
第二行'''
```

### 字符串拼接

```
name = 'Sonny'
greeting = 'Hello, ' + name  # 拼接
```

等价 Java：

```
String name = "Sonny";
String greeting = "Hello, " + name;

```

* * *

## 四、格式化字符串

Python 有多种方式格式化字符串：

#### f-string（推荐）：

```
name = "Sonny"
age = 25
print(f"My name is {name}, and I'm {age} years old.")
```

等价于 Java：

```
System.out.printf("My name is %s, and I'm %d years old.\n", name, age);
```

* * *

## 五、布尔类型与运算

```
a = True
b = False
print(a and b)  # 与
print(a or b)   # 或
print(not a)    # 非
```

Java 对应：

```
boolean a = true;
boolean b = false;
System.out.println(a && b);
System.out.println(a || b);
System.out.println(!a);
```

* * *

## 六、类型转换

```
int("123")      # 字符串转整数
float("3.14")   # 字符串转浮点数
str(123)        # 数值转字符串
bool(1)         # True
```

Java 需要调用包装类：

```
Integer.parseInt("123");
Double.parseDouble("3.14");
String.valueOf(123);
```

* * *

## 七、常见内置函数

|函数	|功能	|
|---	|---	|
|`len()`	|返回字符串/列表长度	|
|---	|---	|
|`type()`	|查看变量类型	|
|`print()`	|打印	|

```
print(len("hello"))  # 5
print(type(123))     # <class 'int'>
```


