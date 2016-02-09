'''
    Design a stack such that GetMinimum() should be O(1)
'''
# Time Complexity : O(1)
# Space Complexity : O(n) for minstack

import Stack
import sys
class FastMinStack():
    def __init__(self):
        self.currentmin = sys.maxint
        self.minstack = Stack.Stack()
        self.inputstack = Stack.Stack()

    def get_minimum(self):
        return self.currentmin

    def push(self,data):
        if self.inputstack.size == 0:
            self.inputstack.push(data)
            self.currentmin = min(data,self.currentmin)
            self.minstack.push(self.currentmin)
        else:
            self.inputstack.push(data)
            if data < self.currentmin:
                self.currentmin = data
                self.minstack.push(data)

    def pop(self):
        inp_top = self.inputstack.pop().get_data()
        if self.currentmin == inp_top:
            self.minstack.pop()
            self.currentmin = self.minstack.peek()

    def print_stack(self):
        print "Current min: "+str(self.currentmin)
        print "Input Stack: "
        self.inputstack.print_stack()
        print "Min Stack: "
        self.minstack.print_stack()

fastminstack = FastMinStack()
fastminstack.push(5)
fastminstack.push(4)
fastminstack.push(6)
fastminstack.push(1)
fastminstack.push(8)
fastminstack.pop()
fastminstack.pop()
fastminstack.print_stack()