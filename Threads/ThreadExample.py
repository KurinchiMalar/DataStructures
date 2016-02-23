'''
Python thread example
'''

from threading import Thread
import time

# Define a function for the thread

def print_time(threadName):

    #count = 0
    print "%s : start sleeping 5 sec" % (threadName)
    time.sleep(5)
    print "%s : finished sleeping 5 sec" % (threadName)
        #count = count + 1
        # time.time() --> Return the time in seconds since the epoch as a floating point number.
        # time.ctime() --> Convert a time expressed in seconds since the epoch to a string representing local time
        #print "%s : %s" %(threadName,time.ctime(time.time()))


'''
args=("Thread-"+str(i), i ,)

the ',' after is necessary here since the argument (or the set of arguments) is a tuple.
remember (tuple,) [list,] {dictionary,}
in the above types,
a comma is not mandated after the last element unless it only has a single element.
So, you would not have to type list = [1,2,] but you would have to type list = [1,] or it would not be a list.
'''
for i in range(10):
    try:
        t = Thread( target=print_time, args=("Thread-"+str(i),) )  # not giving , here is a problem. but if more than one arg no need comma.
        t.start()
    except:
       print "Error: unable to start thread"


'''
Thread-0 : start sleeping 5 sec
 Thread-1 : start sleeping 5 sec
Thread-2 : start sleeping 5 sec
Thread-3 : start sleeping 5 sec
Thread-4 : start sleeping 5 sec
Thread-5 : start sleeping 5 sec
Thread-6 : start sleeping 5 sec
Thread-7 : start sleeping 5 sec
Thread-8 : start sleeping 5 sec

Thread-9 : start sleeping 5 sec
Thread-1 : finished sleeping 5 secThread-2 : finished sleeping 5 sec
 Thread-4 : finished sleeping 5 sec
 Thread-7 : finished sleeping 5 sec

Thread-3 : finished sleeping 5 secThread-9 : finished sleeping 5 secThread-8 : finished sleeping 5 sec
 Thread-5 : finished sleeping 5 sec

Thread-0 : finished sleeping 5 sec

Thread-6 : finished sleeping 5 sec
'''
