from gevent import monkey
monkey.patch_all()

import urllib.request 
from gevent.pool import Pool

def run_task(url):
    print('访问--->%s'%url)

    try:
        response = urllib.request.urlopen(url)
        data = response.read().decode('utf-8')
        print('%d bytes 接收来自%s'%(len(data),url))
    except Exception as e:
        print('%s出了%s'%(url,e))

    return 'urlL:%s--->finish'%(url)

if __name__ =="__main__":
    pool = Pool(2)
    urls = ['http://www.baidu.com','https://www.gavbus518.com']
    results = pool.map(run_task,urls)
    print(results)


