#!/usr/bin/python
# -*- coding: UTF-8 -*-
from person import *
import shelve
from fibonacci import Fibonacci

p = Person('jim', 25)
# p.introduce()

r = Robot('Android', 0)
# print(r)

# db = shelve.open('person.db')
# db[r.name] = r
# db[p.name] = p

# ps = list(db.keys())
# for x in ps:
#     print(x)
#
# db.close()
f = Fibonacci()
print(f.get_list(20))
