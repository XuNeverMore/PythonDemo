#!/usr/bin/python
# -*- coding: UTF-8 -*-

from abc import abstractclassmethod


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print('My name is {0},age is {1}'.format(self.name, self.age))

    @classmethod
    def action(self):
        pass


class Robot(Person):
    def __init__(self, name, age):
        Person.__init__(self, name, age)

    def __str__(self):
        return 'My name is %s,age is %d' % (self.name, self.age)
