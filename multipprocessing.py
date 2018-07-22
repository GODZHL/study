import os 
from multiprocessing import Process

#子进程要执行的代码
def run_pro(name):
    print('子进程%s (%s) 运行中...'%(name,os.getpid()))

if __name__ == "__main__":
    print('父进程%s'%os.getpid())

    for i in range(5):
        p = Process(target=run_pro,args=(str(i),))
        print('进程等待...')
        p.start()
    p.join()
    print('进程结束')

