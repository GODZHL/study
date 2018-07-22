from multiprocessing import Process,Queue 
import os,time,random 

#写数据进程执行的代码
def proc_write(q,urls):
    print('进程(%s)正在写...'%(os.getpid()))
    for url in urls:
        q.put(url)
        print('把url(%s)放入到队列中'%(url))
        time.sleep(random.random())

#读数据进程执行的代码
def proc_read(q):
    print('进程(%s)正在读...'%(os.getpid()))
    while True:
        url = q.get(True)
        print('获取%s'%(url))

if __name__ == '__main__':
    #父进程创建Queue,并传给各个子进程
    q=Queue()
    proc_write1 = Process(target=proc_write,args=(q,['url1','url2','url3']))
    proc_write2 = Process(target=proc_write,args=(q,['url4','url5','url6']))
    proc_reader = Process(target=proc_read,args=(q,))

    #启动子进程proc_writer,写入
    proc_write1.start()
    proc_write2.start()

    #启动子进程proc_reader读出
    proc_reader.start()

    #等待proc_write结束
    proc_write1.join()
    proc_write2.join()

    #proc_reader进程是死循环，无法等待其结束，只能强行终止
    proc_reader.terminate()



