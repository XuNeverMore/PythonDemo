import requests

# http://www.cntour.cn/news/6534/
url = 'http://www.cntour.cn/news/6534/'
html = requests.get(url)
print(html.text)
