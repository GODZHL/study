from urllib.parse import urlencode

params = {
        'name':'zhanghanlin',
        'age':22
        }

base_url = 'http://www.baidu.com?'

url = base_url+urlencode(params)

print("拼接后的url:%s"%(url))

