import requests

response = requests.get('http://www.baidu.com')


for key,value in response.cookies.items():
    print(key+'='+value)


