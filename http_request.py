from urllib import request,parse

request1 = request.Request('http://www.baidu.com')

response = request.urlopen(request1)

#打印信息
print(response.read().decode('utf-8'))


