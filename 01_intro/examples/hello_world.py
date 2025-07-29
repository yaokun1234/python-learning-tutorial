#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
第一个Python程序
与Java的Hello World对比

Java版本：
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}

Python版本：
"""

# Python只需要一行代码
print("Hello, World!")

# 变量定义（无需声明类型）
message = "你好，Python！"
print(message)

# 注释
# 这是单行注释

"""
这是多行注释
类似Java的 /* */
但在Python中通常用于文档字符串
"""

# 交互式使用
if __name__ == "__main__":
    print("这个脚本被直接运行")
    print("类似Java的main方法的作用")