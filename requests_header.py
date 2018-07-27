import requests

head = {
        'User':'zhanghanlin'
        }

response = requests.get('http://www.baidu.com',headers=head)

print(response,type(response))
