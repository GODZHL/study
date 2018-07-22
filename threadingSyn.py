import threading

#简单的线程锁
mylock = threading.RLock()

num = 0

class myThread(threading.Thread):
    
    def __init__(self,name):
        threading.Thread.__init__(self,name=name)

    def run(self):
        #使用全局变量num
        global num
        
        while True:
            #类似于获取锁
            mylock.acquire()
            
            print("%s 被加锁，数字:%d"%(threading.currentThread().name,num))            
            
            if num >= 4:

                #释放锁
                mylock.release()
                print("%s 被释放，数字:%d"%(threading.currentThread().name,num))
                break
            num+=1
            
            print("%s 被释放，数字:%d"%(threading.currentThread().name,num))
            mylock.release()



if __name__ == "__main__":
    thread1 = myThread("线程1")
    thread2 = myThread("线程2")

    thread1.start()
    thread2.start()





