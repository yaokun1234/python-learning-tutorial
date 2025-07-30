#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python - 基本语法：[表达式 for 变量 in 可迭代对象]
# Python - 条件语法：[表达式 for 变量 in 可迭代对象 if 条件]

# ===== 列表生成式 =====
# print("=== 列表生成式 ===")
#
# a = [x ** 2 for x in range(1, 11) ]
# print(a)
#
# b = [x ** 2 for x in range(1, 11) if x % 2 == 0]
# print(b)
#
# # 字符串处理（比Java Stream简洁）
# words = ['hello', 'world', 'python', 'programming']
# A = [ word.upper() for word in words ]
# print(A)


# original = [[1, 2, 3], [4, 5, 6]]
# for a,b in zip(*original):
#     print(a,b)

# # 使用zip转置（更简洁）
# transposed_zip = [list(col) for col in zip(*original)]
# print(transposed_zip)       # [[1, 4], [2, 5], [3, 6]]

multiplication_table = [f"{i} x {j} = {i*j}" for i in range(1, 4) for j in range(1, 4)]
for item in multiplication_table:
    print(item)