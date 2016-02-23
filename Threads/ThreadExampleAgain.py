# Very nice blog: http://www.bogotobogo.com/python/Multithread/python_multithreading_Daemon_join_method_threads.php

from threading import Thread
import time
import urllib2
import Queue

def myfunc(threadname):
    print "%s : start sleep(5)" %(threadname)
    time.sleep(5)
    print "%s: done sleep(5)" %(threadname)

def put_url(queue,url):
    queue.put(urllib2.urlopen(url).read())

def thread_example1():
    for i in range(5):
        t = Thread(target=myfunc,args=("Thread-"+str(i),))
        t.start()
'''
t.daemon = True
By setting them as daemon threads, we can let them run and forget about them, and when our program quits, any daemon threads are killed automatically.
'''
def thread_example2():
    queue = Queue.Queue()
    theurls = ["http://google.com", "http://yahoo.com"]

    for u in theurls:
        t = Thread(target=put_url,args=(queue,u))
        t.daemon = True
        t.start()
    s = queue.get()
    print s


#thread_example1()
thread_example2()
'''
Thread-1 : start sleep(5)
Thread-2 : start sleep(5)
Thread-3 : start sleep(5)
Thread-4 : start sleep(5)
Thread-0: done sleep(5)Thread-2: done sleep(5)
Thread-3: done sleep(5)Thread-4: done sleep(5)
Thread-1: done sleep(5)
'''