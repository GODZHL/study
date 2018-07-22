# -*- coding: UTF-8 -*-
import random
import time,threading

#新线程执行的代码
def thread_run(urls):
    print("当前线程 %s 在运行..."%threading.currentThread().name)
    for url in urls:
        print ("%s---->>>%s"%(threading.currentThread().name,url))
        time.sleep(random.random())

    print("%s 结束"%(threading.currentThread().name))


if __name__ == "__main__":
    print("%s正在运行..."%(threading.currentThread().name))
    t1 = threading.Thread(target=thread_run,args=(['url1','url2','url3'],))
    t2 = threading.Thread(target=thread_run,args=(['url4','url5','url6'],))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("%s结束"%(threading.currentThread().name))


