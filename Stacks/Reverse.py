'''
    Given a stack, how to reverse the elements of the stack using only stack operations (push &  pop)
'''

# Time Complexity : O(n)
# Space Complexity : O(n)

import Stack
def reverse_input(inp):
    if inp == None:
        return None

    stack = Stack.Stack()
    for i in inp:
        stack.push(i)

    result = []
    while stack.size > 0:
        result.append(stack.pop().get_data())

    result = "".join(result)
    return result

inp = "banana"
inp = list(inp)
print "Reversed using stacks: "+str(reverse_input(inp))