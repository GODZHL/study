import requests

response = requests.get('http://www.baidu.com')
response2 = requests.post('http://www.baidu.com')
response3 = requests.delete('http://www.baidu.com')
response4 = requests.put('http://www.baidu.com')

print(response,response2,response3,response4)


