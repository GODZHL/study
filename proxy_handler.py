import urllib.request

proxy_handler = urllib.request.ProxyHandler({
    'http':'http://115.223.252.206:9000',
    'https':'https://36.6.88.177:63909'
    })

#构建代理处理器
opener =urllib.request.build_opener(proxy_handler)

#通过代理处理器来获取网站
response = opener.open('http://www.baidu.com')

print(response.read())
