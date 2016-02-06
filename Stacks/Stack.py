
from LinkedLists.ListNode import ListNode
class Stack:
    def __init__(self,head=None):
        self.head = head
        self.size = 0

    def push(self,data):
        newnode = ListNode(data)
        newnode.set_next(self.head)
        self.head = newnode
        self.size = self.size + 1

    def pop(self):
        if self.head is None:
            print "Nothing to pop. Stack is empty!"
            return -1
        toremove = self.head
        self.head = self.head.get_next()
        self.size = self.size - 1
        return toremove

    def peek(self):
        if self.head is None:
            print "Nothing to peek!. Stack is empty!"
            return -1
        return self.head.get_data()

    def print_stack(self):

        current = self.head
        while current != None:
            print current.get_data(),
            current = current.get_next()
        print
'''
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
stack.print_stack()
stack.pop()
stack.print_stack()
print stack.size
print "top: "+str(stack.peek())
print stack.size
'''