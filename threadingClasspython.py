# -*- coding: UTF-8 -*- 
import time
import random
import threading
class myThread(threading.Thread):
    #初始化构造器
    def __init__(self,name,urls):
        threading.Thread.__init__(self,name=name)
        self.urls = urls

    #run方法
    def run(self):
        print("当前%s 正在运行"%(threading.currentThread().name))
        for url in self.urls:
            print("%s --->>>%s"%(threading.currentThread().name,url))
            time.sleep(random.random())
        print("%s 结束"%(threading.currentThread().name))

if __name__ == "__main__":
    print("线程%s在运行"%(threading.currentThread().name))
    t1 = myThread(name='Thread1',urls=['url1','url2','url3'])
    t2 = myThread(name='Thread2',urls=['url4','url5','url6'])

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("%s结束运行"%(threading.currentThread().name))

