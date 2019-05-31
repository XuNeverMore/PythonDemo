import requests
import json
from bs4 import BeautifulSoup
import re

# main > div > div.mtop.firstMod.clearfix > div.leftBox > div:nth-child(2) > ul > li:nth-child(2) > a
url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
From_data = {
    'i': '我爱中国',
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': '15592951571776',
    'sign': 'd4e17717c46ed2a6d7b7616d86caed06',
    'ts': '1559295157177',
    'bv': '1d3fa10e88645a42c654834aec201f63',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME',
    'typoResult': 'false'
}
# main > div > div.mtop.firstMod.clearfix > div.leftBox > div:nth-child(2) > ul > li:nth-child(2) > a
# main > div > div.mtop.firstMod.clearfix > div.leftBox > div:nth-child(2) > ul > li:nth-child(2)
# <a target="_blank" href="http://www.cntour.cn/news/6534/" title="中国生态环境持续向好 森林覆盖率升至22.96%">中国生态环境持续向好 森林覆盖率升至22.96%</a>
html = requests.get('http://www.cntour.cn/')
# print(html.text)
soup = BeautifulSoup(html.text, 'lxml')
data = soup.select('#main > div > div.mtop.firstMod.clearfix > div.leftBox > div:nth-child(2) > ul > li> a')
pt = '[0-9]{1,}'
for item in data:
    result = {
        'title': item.get_text(),
        'link': item.get('href')
    }
    str = result['link']
    print(re.findall(pt, str))
    print(result)
