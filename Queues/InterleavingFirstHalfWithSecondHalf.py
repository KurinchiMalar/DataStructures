'''
    Given a queue of integers, rearrange the elements by interleaving the first half of the list with the second half of the list.

    eg) input = [11,12,13,14,15,16,17,18,19,20]

        firsthalf = [11,12,13,14,15]
        secondhalf = [16,17,18,19,20]

        Result = [11,16,12,17,13,18,14,19,15,20]

    Algorithm:

        we need firsthalf as such without being reversed.

        1) dequeue upto halfsize and push in stack
                --> stack = 15 14 13 12 11    (15 is top)
                ---> queue = 16,17,18,19,20
        2) pop from stack and enqueue in queue
                --> stack =
                ---> queue = 16,17,18,19,20,15 14 13 12 11

        3)upto halfsize q.enqueue(q.dequeue)

                --> stack =
                ---> queue = 15 14 13 12 11 16,17,18,19,20

        3) push upto halfsize in stack....
                --> stack = 11 12 13 14 15 ( 11 is top)
                ---> queue = 16,17,18,19,20

        4) Now, q.enqueue( stack.pop) q.enqueue(queue.dequeue)
'''
# Time Complexity : O(n)
# Space Complexity : O(n)
from Stacks import Stack
import Queue
def interleave_queue(queue):
    half_size = queue.size // 2
    stk = Stack.Stack()
    for i in range(0,half_size):
        stk.push(queue.dequeue().get_data())
    stk.print_stack()
    queue.print_queue()
    print "----------------------"
    while stk.size > 0:
        queue.enqueue(stk.pop().get_data())
    stk.print_stack()
    queue.print_queue()
    print "----------------------"

    for i in range(0,queue.size - half_size):   ### note this point.... queue.size - half_size
        queue.enqueue(queue.dequeue().get_data())

    for i in range(0,half_size):
        stk.push(queue.dequeue().get_data())

    stk.print_stack()
    queue.print_queue()
    result = []
    while stk.size > 0:
        result.append(stk.pop().get_data())
        result.append(queue.dequeue().get_data())

    if queue.size > 0:
        result.append(queue.dequeue().get_data())
    print result




def create_queue(Ar,queue):
    for elem in Ar:
        queue.enqueue(elem)
    return queue

Ar = [11,12,13,14,15,16,17,18,19,20,21]

queue = Queue.Queue()
queue = create_queue(Ar,queue)
#queue.print_queue()
interleave_queue(queue)
