'''
    Given a stack of integers, how do i check whether each successive pair of numbers in the stack is consecutive or not.

    The pairs can be increasing or decreasing, and if the stack has an odd number of elements,

        the element at the top is left out of a pair.

    For example, if the stack elements are [4,5,-2,-3,11,10,5,6,20] , then the output should be true because each of the pairs

    (4,5), (-2,-3), (11,10) and (5,6) consists of consequtive numbers.
'''
# Time Complexity : O(n)
# Space Complexity : O(n)

import Queue
from Stacks import Stack
def is_pairwise_sorted(stk):
    pairwise_sorted = True
    result = {}
    queue = Queue.Queue()  # queue is needed , since inplace stack reversal not possible
    while stk.size > 0:
        queue.enqueue(stk.pop().get_data())

    #queue.print_queue()

    while queue.size > 0:
        stk.push(queue.dequeue().get_data())

    # Stack reversal is done...
    # ideally for the element at top should be left out pair if odd, hence reverse and keep comparing from top, until you reach the bottom most elem.
    print "Reversed Stack: "
    stk.print_stack()

    while stk.size > 0:

        m = stk.pop().get_data()
        n = None
        if stk.size > 0:
            n = stk.pop().get_data()

            if abs(n-m) != 1:
                pairwise_sorted = False
                break
        result[m] = n

    return pairwise_sorted,result

def create_stack(Ar,stk):
    for elem in Ar:
        stk.push(elem)
    return stk

Ar = [4,5,-2,-3,11,10,5,6,20]
stk = Stack.Stack()
stk = create_stack(Ar,stk)
print "Orig stack: "
stk.print_stack()
pairwise_sorted,result = is_pairwise_sorted(stk)
print "is_pairwise_sorted: "+str(pairwise_sorted)
print "pairs: "+str(result)

