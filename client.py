#!/usr/bin/env python
# coding=utf-8
import socket

s = socket.socket()
hostname = socket.gethostname()
s.connect((hostname, 8888))
print(bytes.decode(s.recv(1024)))
s.close()
