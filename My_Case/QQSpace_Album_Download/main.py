# -*- coding: UTF-8 -*-
import requests

url = input("请输入你登录后的URL：")
print(url)

headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
resp = requests.get(url=url,headers=headers)
print(resp.text)