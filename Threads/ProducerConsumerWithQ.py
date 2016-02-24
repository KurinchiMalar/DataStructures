


import Queue
from random import randint
from threading import Thread
import time
'''
Queue.put(item[, block[, timeout]])

Put item into the queue.
If optional args block is true and timeout is None (the default),
    block if necessary until a free slot is available.
If timeout is a positive number,
    it blocks at most timeout seconds and raises the Full exception
    if no free slot was available within that time.

Otherwise (block is false),
    put an item on the queue if a free slot is immediately available,
    else raise the Full exception (timeout is ignored in that case).

---------------------------------
Queue.get([block[, timeout]])


'''

class ProduceToQueue(Thread):

    def __init__(self,threadName,queue):
        Thread.__init__(self,name=threadName)
        self.sharedQ = queue


    def run(self):

        for i in range(1,11):

            time.sleep(randint(1,4))  # sleep till you get an empty slot to put in.
            print "%s putting %d "%(self.getName(),i)
            self.sharedQ.put(i)
        print self.getName(), "finished producing values"
        print "Terminating", self.getName()

class ConsumeFromQueue(Thread):

    def __init__(self,threadName,queue):
        Thread.__init__(self,name=threadName)
        self.sharedQ = queue


    def run(self):
        sum = 0
        current = 1
        for i in range(10):

            time.sleep(randint(1,4)) # sleep till something is available.
            print "%s attempting to read %s..." % (self.getName(), current)
            current = self.sharedQ.get()
            print "%s read %s" % (self.getName(), current)
            sum += current
        print "%s finished consuming values SUM: %d" % (self.getName(), sum)
        print "Terminating", self.getName()


queue = Queue.Queue()
producer = ProduceToQueue("Producer",queue)
consumer = ConsumeFromQueue("Consumer",queue)
producer.start()
consumer.start()

producer.join()   # consumer will wait till producer is finished.
consumer.join() # mainthread will wait till both finished.







