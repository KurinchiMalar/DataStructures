'''
    Given an array of elements,replace every element with nearest greater element on the right side of that element.
'''

import Stack

# Time Complexity : O(n)
# Space Complexity : O(n)
def replace_with_nearest_greater(Ar):

    stack = Stack.Stack()
    stack.push(0)
    for i in range(1,len(Ar)):

        while stack.size > 0 and Ar[i] > Ar[stack.peek()]:   # for all elements in current stack, this is the nearest greatest.
            Ar[stack.peek()] = Ar[i]
            stack.pop()  # pop after replacing.
        stack.push(i)  # when stack empty go to next i.

    stack.print_stack()
    while stack.size > 0: # there is no greater element on the right
        Ar[stack.peek()] = -1
        stack.pop()

    print Ar


Ar = [6,12,4,1,2,111,2,2,10]
replace_with_nearest_greater(Ar)