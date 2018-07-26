import http.cookiejar,urllib.request

#声明cookie保存对象
cookie = http.cookiejar.CookieJar()

#构建handler
handler = urllib.request.HTTPCookieProcessor(cookie)

#通过handler构建opener
opener = urllib.request.build_opener(handler)

response = opener.open('http://www.baidu.com')

for item in cookie:
    print(item.name+"="+item.value)
    
    with open('cookie.txt','a+') as file:
        file.write(item.name+'\n')

