#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Fibonacci:

    def __init__(self):
        self.flist = [0, 1]

    def check(self, num):
        if num <= len(self.flist):
            pass
        else:
            while len(self.flist) < num:
                self.flist.append(self.flist[-1] + self.flist[-2])

    def get_list(self, num):
        self.check(num)
        return self.flist
