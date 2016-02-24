

from threading import Thread
import time
from random import randint

class MyThread(Thread): # now MyThread is a subclass of Thread.

    # Constructor
    def __init__(self,val):
        Thread.__init__(self)
        self.val = val

    def run(self):
        for i in range(1,self.val):
            print "%s -  i : %d" %(self.getName(),i)
            sleepfor = randint(1,5)
            print "%s - going to sleep for - %d seconds" %(self.getName(),sleepfor)
            time.sleep(sleepfor)

if __name__ == '__main__':
    t1 = MyThread(4)
    t1.setName("Thread1")
    t2 = MyThread(3)
    t2.setName("Thread2")
    t3 = MyThread(5)
    t3.setName("Thread3")
    t1.start()
    t2.start()
    t3.start()



