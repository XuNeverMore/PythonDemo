#!/usr/bin/python
# -*- coding: UTF-8 -*-

x = 0


def change(a):
    global x
    x += 1


change(x)

print(x)


def params(*args):
    print(args)


list = [1, 2, 3]
params(*list)
print(dict(a=1, b=2))
