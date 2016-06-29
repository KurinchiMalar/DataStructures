class Stack:

    def __init__(self,size):
        self.Ar = []
        self.top = -1
        self.size = size

    def push(self,data):

        if self.top >= self.size:  # stack full
            return -1

        if data != None:
            self.Ar.append(data) # append
            self.top = self.top + 1

    def pop(self):

        if self.top == -1:  # stack empty
            return -1

        popedelem = self.Ar.pop() # pops from last (Last in First out)
        self.top = self.top - 1
        return popedelem

    def peek(self):

        if self.top != -1 and self.top < self.size:
            return self.Ar[self.top]

    def print_stack(self):
        print self.Ar

stk = Stack(6)
stk.push(1)
stk.push(2)
stk.push(3)
stk.print_stack()

print(stk.peek())
stk.pop()
stk.print_stack()
stk.pop()
print(stk.peek())
stk.pop()
stk.print_stack()

stk.push(4)
stk.print_stack()
stk.pop()
stk.pop()
stk.print_stack()