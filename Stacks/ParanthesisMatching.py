# Time Complexity : O(n)
# Space Complexity : O(n)

import Stack
def construct_hashtable():
    hash_table = {}
    hash_table[")"] = "("
    hash_table["]"] = "["
    hash_table["}"] = "{"
    return hash_table

def is_balanced_symbols(input,stack):

    hash_table = construct_hashtable()

    #print hash_table
    for item in input:
        if item not in hash_table:
            stack.push(item)
            print "push : "+str(item)
            stack.print_stack()
        else:
            if stack.peek() == hash_table[item]:
                print "popped : "+str(stack.pop())
                stack.print_stack()

            else:
                print "Not balanced"
                return -1
    if stack.size == 0:
        print "Perfect"


input = "()(()[()])"
input = "()(()[())" # wrong input
stack = Stack.Stack()
input = list(input)
print ""+str(is_balanced_symbols(input,stack))
