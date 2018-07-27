import requests

data = {
        'name':'zhanghanlin',
        'age':24
        }
response = requests.get('http://httpbin.org/get',params=data)

print(response.text)
