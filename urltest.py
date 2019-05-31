#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib.request
import re

# User-Agent是爬虫与反爬虫的第一步
ua_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}
# 向指定的url地址发送请求，并返回服务器响应的类文件对象
request = urllib.request.Request('https://movie.douban.com/typerank?type_name=%E5%96%9C%E5%89%A7&type=24&interval_id=100:90&action=', headers=ua_headers)
response = urllib.request.urlopen(request)
# 服务器返回的类文件对象支持python文件对象的操作方法
# read()方法就是读取文件里的全部内容，返回字符串

# 返回HTTP的响应吗，成功返回200,4服务器页面出错，5服务器问题
print(response.getcode())  # 200

# 返回数据的实际url,防止重定向
print(response.geturl())  # https://www.baidu.com/

# 返回服务器响应的HTTP报头
# print(response.info())

html = str(response.read())
print(html)
# m = re.match('/^<tr class="item"></div>$/', html, 0)
pattern = re.compile('(<tr class="item">).*(</tr>)')

m = pattern.search(html)
print(m)

# print(html)

you = input('请输入')
print(you)
