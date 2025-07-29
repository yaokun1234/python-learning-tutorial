#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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