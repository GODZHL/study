import requests

files = {
        'file':open('cookie.txt','rb')
        }

response =  requests.post('http://httpbin.org/post',files=files)

print(response.text)
