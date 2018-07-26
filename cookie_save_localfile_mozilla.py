import http.cookiejar,urllib.request

#文件名
filname = 'cookies.txt'

cookie = http.cookiejar.MozillaCookieJar(filname)

handler = urllib.request.HTTPCookieProcessor(cookie)

opener = urllib.request.build_opener(handler)

response = opener.open('http://www.baidu.com')

cookie.save(ignore_discard=True,ignore_expires=True)

print('保存成功')

