import http.cookiejar,urllib.request

filename = "cookie.txt"

cookie = http.cookiejar.LWPCookieJar()
cookie.load(filename,ignore_discard=True,ignore_expires=True)   

handler = urllib.request.HTTPCookieProcessor(cookie)

opener = urllib.request.build_opener(handler)

response = opener.open('http://www.baidu.com')


print(response.read().decode("utf-8"))
