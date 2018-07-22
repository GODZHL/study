# -*- coding: UTF-8 -*- 
from multiprocessing import Pool
import os,time,random

def run_task(name):
    print('任务%s(pid = %s) 正在运行...'%(name,os.getpid()))
    time.sleep(random.random()*3)
    print('任务%s结束.'%(name))

if __name__ == '__main__':
    print('当前进程%s.'%(os.getpid()))
    p=Pool(processes=3)
    for i in range(5):
        p.apply_async(run_task,args=(i,))
    print('等待所有的任务完成')
    p.close()
    p.join()
    print('所有任务都完成')


    
