#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Python集合类型示例
对比Java集合框架
"""

# ===== 列表（List）- 类似Java的ArrayList =====
print("=== 列表（List）===")

# 创建列表
numbers = [1, 2, 3, 4, 5]
names = ["张三", "李四", "王五"]
mixed = [1, "hello", 3.14, True]  # 可以混合类型

print(f"数字列表：{numbers}")
print(f"姓名列表：{names}")
print(f"混合列表：{mixed}")

# 列表操作
numbers.append(6)  # 添加元素
print(f"添加6后：{numbers}")

first_name = names[0]  # 获取元素（索引从0开始）
print(f"第一个姓名：{first_name}")

names[1] = "李二"  # 修改元素
print(f"修改后的姓名：{names}")

# ===== 元组（Tuple）- 不可变序列 =====
print("\n=== 元组（Tuple）===")

# 创建元组
point = (10, 20)  # 坐标点
rgb = (255, 128, 0)  # RGB颜色
person = ("张三", 25, "北京")  # 个人信息

print(f"坐标点：{point}")
print(f"RGB颜色：{rgb}")
print(f"个人信息：{person}")

# 元组解包
name, age, city = person
print(f"姓名：{name}，年龄：{age}，城市：{city}")

# ===== 字典（Dict）- 类似Java的HashMap =====
print("\n=== 字典（Dict）===")

# 创建字典
student = {
    "name": "张三",
    "age": 20,
    "major": "计算机科学",
    "scores": [90, 85, 92]
}

print(f"学生信息：{student}")

# 字典操作
print(f"姓名：{student['name']}")  # 获取值
student["age"] = 21  # 修改值
student["email"] = "zhangsan@example.com"  # 添加键值对

print(f"更新后：{student}")

# 获取所有键和值
print(f"所有键：{list(student.keys())}")
print(f"所有值：{list(student.values())}")

# ===== 集合（Set）- 类似Java的HashSet =====
print("\n=== 集合（Set）===")

# 创建集合
fruits = {"苹果", "香蕉", "橙子"}
numbers_set = {1, 2, 3, 4, 5}

print(f"水果集合：{fruits}")
print(f"数字集合：{numbers_set}")

# 集合操作
fruits.add("葡萄")  # 添加元素
print(f"添加葡萄后：{fruits}")

# 集合运算
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(f"交集：{set1 & set2}")  # {3, 4}
print(f"并集：{set1 | set2}")  # {1, 2, 3, 4, 5, 6}
print(f"差集：{set1 - set2}")  # {1, 2}

# ===== 集合类型总结 =====
print("\n=== 类型特点总结 ===")
print("List：有序、可变、允许重复")
print("Tuple：有序、不可变、允许重复")
print("Dict：无序、可变、键唯一")
print("Set：无序、可变、元素唯一")