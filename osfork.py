import os 

if __name__ == '__main__':
    print('当前进程(%s)启动...'%(os.getpid()))
    pid = os.fork()
    if pid < 0 :
        print('fork 出现错误')
    elif pid == 0:
        print('我是子进程(%s),父进程是(%s)'%(os.getpid(),os.getppid()))
    else:
        print('我(%s)创建了一个子进程(%s)'%(os.getpid,pid))
