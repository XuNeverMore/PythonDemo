#!/usr/bin/env python
# coding=utf-8
import this
# 元组元素不可重新赋值，其他用法和列表list一样
tuple = ("c", 1, 2.0, ["c", 2])
print(tuple)
print(tuple * 2)

# a = ["1", "2"]

tuple = ["1", 1]

print(tuple)

tuple[0] = 0

print(tuple)
