from urllib import request,parse

url = 'http://httpbin.org/post'

headers = {
        'User-Agent':'zhanghanlin-servers',
        'Host':'httpbin.org'
        }

dict = {
        'name':'zhanghanlin'
        }

#将dict数据编码
data = bytes(parse.urlencode(dict),encoding='utf8')

req = request.Request(url=url,data=data,headers=headers,method='POST')
req.add_header('Connection2','keep-alive')

response = request.urlopen(req)

print(response.read().decode('utf-8'))
