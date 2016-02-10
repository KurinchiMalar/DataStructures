'''
    Implement one queue efficiently using two stacks. Analyze the running time of the queue operations.

    # Version 1: dequeue costly

        Enqueue:
            1. push input to stack1

        Dequeue:
            1. push all elements of stack1 to stack2
            2. pop top element.

    # Version 2: enqueue costly

        enQueue(q, x)
          1) While stack1 is not empty, push everything from satck1 to stack2.
          2) Push x to stack1 (assuming size of stacks is unlimited).
          3) Push everything back to stack1.

        dnQueue(q)
          1) If stack1 is empty then error
          2) Pop an item from stack1 and return it
'''

# Time Complexity : O(n)   for enqueue and O(n) for dequeue
# Space Complexity : O(n)

import Stack

class Queue():
    def __init__(self):
        self.stack1 = Stack.Stack()
        self.stack2 = Stack.Stack()

    def enqueue(self,data):
        self.stack1.push(data)

    def dequeue(self):
        while self.stack1.size > 0:
            self.stack2.push(self.stack1.pop().get_data())
        return self.stack2.pop().get_data()

    def enqueue_v2(self,data):
        while self.stack1.size > 0:
            self.stack2.push(self.stack1.pop().get_data())
        self.stack1.push(data)
        while self.stack2.size > 0:
            self.stack1.push(self.stack2.pop().get_data())

    def dequeue_v2(self):

        if self.stack1.size == 0:
            return -1
        return self.stack1.pop().get_data()

    def print_queue(self):
        self.stack1.print_stack()
        self.stack2.print_stack()

def queue_using_stacks(inp):

    if inp == None:
        return None

    stack1 = Stack.Stack()
    stack2 = Stack.Stack()

    for elem in inp:
        stack1.push(elem)
    stack1.print_stack()
    while stack1.size > 0:
        stack2.push(stack1.pop().get_data())
    stack2.print_stack()
    result = []
    while stack2.size > 0:
        result.append(stack2.pop().get_data())

    result = "".join(result)
    return result

#inp = "123456789"
#inp = list(inp)
#print "Result: "+str(queue_using_stacks(inp))

result = []
q = Queue()
'''q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
result.append(q.dequeue())
result.append(q.dequeue())
result.append(q.dequeue())
q.print_queue()'''

q.enqueue_v2(1)
q.enqueue_v2(2)
q.enqueue_v2(3)
result.append(q.dequeue_v2())
result.append(q.dequeue_v2())
print result