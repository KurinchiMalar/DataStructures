'''
    Given an integer k and a queue of integers, how do you reverse the order of the first k elements of the queue, leaving
    the other elements in the same relative order?

    For eg. if k = 4 and queue has the elements [10,20,30,40,50,60,70,80,90] the output should be [40,30,20,10,50,60,70,80,90]
'''

from Stacks import Stack
import Queue

# Time Complexity : O(n)
# Space Complexity : O(n)

def reverse_k_elements(queue,k):

    stk = Stack.Stack()
    for i in range(0,k):
        stk.push(queue.dequeue().get_data())
    stk.print_stack()
    queue.print_queue()

    while stk.size > 0:
        queue.enqueue(stk.pop().get_data())

    queue.print_queue()

    for i in range(0,queue.size - k):
        queue.enqueue(queue.dequeue().get_data())

    queue.print_queue()

def create_queue(Ar,queue):
    for elem in Ar:
        queue.enqueue(elem)
    return queue

Ar = [10,20,30,40,50,60,70,80,90]
queue = Queue.Queue()
queue = create_queue(Ar,queue)
reverse_k_elements(queue,5)