import urllib.request

response = urllib.request.urlopen('http://www.baidu.com')

#打印类型
print("类型是:%s"%(type(response)))

#打印状态码
print("状态码是:%s"%(response.status))

#打印head信息
print("head信息是:%s"%(response.getheaders()))

#打印指定的header信息
print("Server信息:%s"%(response.getheader('Server')))
