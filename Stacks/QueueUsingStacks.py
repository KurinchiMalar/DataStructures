'''
    Implement one queue efficiently using two stacks. Analyze the running time of the queue operations.
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
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
result.append(q.dequeue())
result.append(q.dequeue())
result.append(q.dequeue())
q.print_queue()
print result