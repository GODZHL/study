from gevent import monkey;monkey.patch_all()
import gevent
import urllib.request

def run_task(url):
    print('访问-->%s'%(url))
    
    try:
        response =urllib.request.urlopen(url)
        data = response.read().decode('utf-8')

        print("%d bytes 接收来自%s"%(len(data),url))

    except Exception as e:
        print("%s 出了%s的错"%(url,e))

if __name__ == "__main__":

    urls = ['http://www.baidu.com','https://www.gavbus518.com']
    greenlets = [gevent.spawn(run_task,url) for url in urls]
    gevent.joinall(greenlets)

