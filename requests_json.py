import requests

response = requests.get('http://httpbin.org/get')

print('json:%s'%(response.json))
