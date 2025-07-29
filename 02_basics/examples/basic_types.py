#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Python基本数据类型示例
对比Java数据类型的使用
"""

# ===== 数字类型 =====
print("=== 数字类型 ===")

# 整数（Python3中int可以是任意大小）
age = 25
big_number = 12345678901234567890  # Java需要BigInteger
print(f"年龄：{age}")
print(f"大数：{big_number}")

# 浮点数
height = 1.75
print(f"身高：{height}米")

# 布尔值（注意首字母大写）
is_student = True
is_working = False
print(f"是学生：{is_student}")

# ===== 字符串类型 =====
print("\n=== 字符串类型 ===")

# 字符串定义（单引号、双引号都可以）
name = "张三"
city = '北京'
print(f"姓名：{name}，城市：{city}")

# 多行字符串
description = """这是一个
多行字符串
类似Java的文本块功能"""
print(description)

# 字符串操作
full_name = name + " " + "同学"  # 字符串连接
print(f"全名：{full_name}")
print(f"名字长度：{len(name)}")  # len()函数获取长度

# ===== None类型 =====
print("\n=== None类型 ===")
# None相当于Java的null
result = None
print(f"结果：{result}")

# ===== 类型检查 =====
print("\n=== 类型检查 ===")
print(f"age的类型：{type(age)}")
print(f"name的类型：{type(name)}")
print(f"is_student的类型：{type(is_student)}")

# isinstance检查（类似Java的instanceof）
print(f"age是否为int：{isinstance(age, int)}")
print(f"name是否为str：{isinstance(name, str)}")