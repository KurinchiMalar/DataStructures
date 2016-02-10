'''
    Implement one stack using two queues.

    # Version 1
        Making push operation costly

        PUSH
        1) Let every new element be in q1
        2) enqueue all elements from q2 to q1
        3) swap q1 and q2
        4) again q1 is empty push next new element to q1.

        # At any time head of q1 will contain the top of stack. (or) the latest element pushed.

        POP
        1) if q1 is not empty that is the top
        2) else... head of q2 is top.

    # Version 2
        Making pop operation costly

        PUSH
        1) push element to q1

        POP
        1) dequeue everything except last element from q1 and enqueue to q2
        2) dequeue q1  _ the last element. is the top so pop it --> this is the value to return
        3) swap q1 and q2

'''

import Queue
class Stack():
    def __init__(self):
        self.queue1 = Queue.Queue()
        self.queue2 = Queue.Queue()

    def swap(self):
        temp = self.queue2
        self.queue2 = self.queue1
        self.queue1 = temp

    def push(self,data):
        #print "pushing :"+str(data)
        self.queue1.enqueue(data)
        print self.queue1.size
        print self.queue2.size
        while self.queue2.size > 0:
            temp = self.queue2.dequeue()
            self.queue1.enqueue(temp)
        #print "Before swap"
        #self.print_stack()
        self.swap()

    def pop(self):

        if self.queue1.size == 0:
            return self.queue2.dequeue()
        else:
            return self.queue1.dequeue()

    def push_v2(self,data):
        self.queue1.enqueue(data)

    def pop_v2(self):

        while self.queue1.size > 1:
            self.queue2.enqueue(self.queue1.dequeue())

        top = self.queue1.head.get_data()
        self.swap()
        return top

    def print_stack(self):
        self.queue1.print_queue()
        self.queue2.print_queue()

result = []

stack = Stack()
'''stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.print_stack()
result.append(stack.pop())
result.append(stack.pop())
result.append(stack.pop())
print result'''
stack.push_v2(1)
stack.push_v2(2)
stack.push_v2(3)
stack.push_v2(4)
result.append(stack.pop_v2())
result.append(stack.pop_v2())
result.append(stack.pop_v2())
print result