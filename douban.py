#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib.parse, urllib.request

url = 'https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action='
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}

# start和limit可以自己随便设置
formdata = {'start': '20', 'limit': '100'}

str = urllib.parse.urlencode(formdata)
d = bytes(str, encoding="utf8")
request = urllib.request.Request(url, data=d, headers=headers)
response = urllib.request.urlopen(request)
print(response.read())
