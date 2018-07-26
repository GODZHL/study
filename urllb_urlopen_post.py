import urllib.request
import urllib.parse

data = bytes(urllib.parse.urlencode({'name':'zhanghanlin'}),encoding='utf8')

response = urllib.request.urlopen('http://httpbin.org/post',data)

print(response.read())

