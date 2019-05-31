#!/usr/bin/env python
# coding=utf-8
import os
print(os.getcwd())

f = open('xct.txt','w')
f.write('Hello!\n')
f.write("XuNeverMore\n")
print(dir(f))
# text = f.read()
# print(text)

s = set('abc')
for x in s:
    print('=>',x*2)