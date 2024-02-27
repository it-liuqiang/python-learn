import requests
from requests.cookies import RequestsCookieJar

headers = {
    'authority': 'api.m.jd.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Connection': 'keep-alive'
           }
request_url = "https://order.jd.com/center/list.action"
res = requests.get(request_url, headers=headers)
set_cookie = res.headers['Set-Cookie']
print("set_cookie:", set_cookie)