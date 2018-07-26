from urllib.parse import urlparse

result = urlparse('https://www.baidu.com/s?ie=UTF-8&wd=%E7%99%BE%E5%BA%A6')

print(type(result),result)

results = urlparse('www.baidu.com/s?ie=UTF-8&wd=%E7%99%BE%E5%BA%A6',scheme='https')

print(type(results),results)


