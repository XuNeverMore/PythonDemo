#!/usr/bin/env python
# coding=utf-8
import socket

s = socket.socket()
hostname = socket.gethostname()
port = 8888
s.bind((hostname, port))
s.listen(5)  # 等待客户端连接
while True:
    c, addr = s.accept()  # 建立客户端连接。
    print('连接地址：', addr)
    c.send(bytes('欢迎访问菜鸟教程！', encoding='utf-8'))
    c.close()  # 关闭连接
