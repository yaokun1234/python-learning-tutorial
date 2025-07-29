## 一、函数定义基础

### 最简单的函数

```python
def greet():
    print("Hello, World!")

# 调用函数
greet()  # Hello, World!
```

等价于 Java：

```java
public static void greet() {
    System.out.println("Hello, World!");
}

// 调用
greet();
```

**注意**：Python 使用 `def` 关键字定义函数，不需要指定返回类型。

* * *

## 二、带参数的函数

### 位置参数

```python
def greet_person(name):
    print(f"Hello, {name}!")

def add_numbers(a, b):
    return a + b

# 调用
greet_person("张三")      # Hello, 张三!
result = add_numbers(3, 5)  # 8
```

Java 对应：

```java
public static void greetPerson(String name) {
    System.out.println("Hello, " + name + "!");
}

public static int addNumbers(int a, int b) {
    return a + b;
}
```

* * *

## 三、默认参数

```python
def greet_with_title(name, title="先生"):
    print(f"Hello, {title} {name}!")

# 调用方式
greet_with_title("张三")              # Hello, 先生 张三!
greet_with_title("李四", "女士")       # Hello, 女士 李四!
greet_with_title("王五", title="博士")  # Hello, 博士 王五!
```

Java 需要方法重载：

```java
public static void greetWithTitle(String name) {
    greetWithTitle(name, "先生");
}

public static void greetWithTitle(String name, String title) {
    System.out.println("Hello, " + title + " " + name + "!");
}
```

* * *

## 四、关键字参数

```python
def create_profile(name, age, city="未知", occupation="未知"):
    return f"{name}, {age}岁, 来自{city}, 职业：{occupation}"

# 不同的调用方式
print(create_profile("张三", 25))
print(create_profile("李四", 30, city="北京"))
print(create_profile("王五", 35, occupation="工程师", city="上海"))
print(create_profile(age=28, name="赵六"))  # 参数顺序可以改变
```

* * *

## 五、可变参数

### *args - 接收任意数量的位置参数

```python
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# 调用
print(sum_all(1, 2, 3))        # 6
print(sum_all(1, 2, 3, 4, 5))  # 15

# 也可以传入列表
nums = [1, 2, 3, 4]
print(sum_all(*nums))  # 10 (解包列表)
```

### **kwargs - 接收任意数量的关键字参数

```python
def create_person(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

# 调用
create_person(name="张三", age=25, city="北京")
# 输出:
# name: 张三
# age: 25
# city: 北京

# 也可以传入字典
person_info = {"name": "李四", "age": 30}
create_person(**person_info)
```

### 混合使用

```python
def flexible_function(required, *args, **kwargs):
    print(f"必需参数: {required}")
    print(f"位置参数: {args}")
    print(f"关键字参数: {kwargs}")

flexible_function("必须的", 1, 2, 3, name="张三", age=25)
# 输出:
# 必需参数: 必须的
# 位置参数: (1, 2, 3)
# 关键字参数: {'name': '张三', 'age': 25}
```

* * *

## 六、返回值

### 单个返回值

```python
def square(x):
    return x ** 2

result = square(5)  # 25
```

### 多个返回值

```python
def divide_with_remainder(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder

# 接收多个返回值
q, r = divide_with_remainder(17, 5)
print(f"商: {q}, 余数: {r}")  # 商: 3, 余数: 2

# 也可以作为元组接收
result = divide_with_remainder(17, 5)
print(result)  # (3, 2)
```

### 无返回值的函数

```python
def print_info(name):
    print(f"姓名: {name}")
    # 没有 return 语句，默认返回 None

result = print_info("张三")
print(result)  # None
```

* * *

## 七、作用域和局部变量

```python
global_var = "我是全局变量"

def test_scope():
    local_var = "我是局部变量"
    print(local_var)      # 可以访问
    print(global_var)     # 可以访问全局变量

def modify_global():
    global global_var
    global_var = "修改后的全局变量"

test_scope()
modify_global()
print(global_var)  # 修改后的全局变量
```

* * *

## 八、lambda 函数（匿名函数）

```python
# 普通函数
def square(x):
    return x ** 2

# 等价的 lambda 函数
square_lambda = lambda x: x ** 2

print(square(5))        # 25
print(square_lambda(5)) # 25

# 常用于排序
students = [
    {"name": "张三", "score": 85},
    {"name": "李四", "score": 92},
    {"name": "王五", "score": 78}
]

# 按分数排序
students.sort(key=lambda student: student["score"])
```

Java 8+ 对应：

```java
// Lambda 表达式
Function<Integer, Integer> square = x -> x * x;
System.out.println(square.apply(5)); // 25

// 排序
students.sort((s1, s2) -> Integer.compare(s1.getScore(), s2.getScore()));
```

* * *

## 九、高阶函数

### map() - 对每个元素应用函数

```python
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)  # [1, 4, 9, 16, 25]

# 等价于列表推导式
squares = [x ** 2 for x in numbers]
```

### filter() - 过滤元素

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4, 6, 8, 10]

# 等价于列表推导式
even_numbers = [x for x in numbers if x % 2 == 0]
```

* * *

## 十、函数作为参数

```python
def apply_operation(numbers, operation):
    return [operation(x) for x in numbers]

def double(x):
    return x * 2

def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
print(apply_operation(numbers, double))  # [2, 4, 6, 8, 10]
print(apply_operation(numbers, square))  # [1, 4, 9, 16, 25]
```

* * *

## 十一、文档字符串

```python
def calculate_area(length, width):
    """
    计算矩形的面积
    
    参数:
        length (float): 矩形的长度
        width (float): 矩形的宽度
    
    返回:
        float: 矩形的面积
    """
    return length * width

# 查看文档
print(calculate_area.__doc__)
help(calculate_area)
```

* * *

## 十二、常用函数模式

### 1. 输入验证

```python
def safe_divide(a, b):
    if b == 0:
        return None
    return a / b

result = safe_divide(10, 0)
if result is not None:
    print(result)
else:
    print("除数不能为零")
```

### 2. 工厂函数

```python
def create_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

double = create_multiplier(2)
triple = create_multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15
```

### 3. 装饰器模式基础

```python
def timer(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 执行时间: {end - start:.4f}秒")
        return result
    return wrapper

@timer
def slow_function():
    import time
    time.sleep(1)
    return "完成"

slow_function()  # 会显示执行时间
```