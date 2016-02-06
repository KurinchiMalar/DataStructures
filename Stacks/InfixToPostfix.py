'''
Consider an infix expression : A * B - (C + D) + E

and convert to postfix

the postfix expression : AB * CD + - E +


Algorithm:

   1) if operand
        just add to result
   2) if (
        push to stack
   3) if )
        till a ( is encountered, pop from stack and append to result.
   4) if operator
            if top of stack has higher precedence
                pop from stack and append to result
                push the current operator to stack
            else
                push the current operator to stack
'''
# Time Complexity : O(n)
# Space Complexity : O(n)

import Stack
def get_precedence_map():
    prec_map = {}
    prec_map["*"] = 3
    prec_map["/"] = 3
    prec_map["+"] = 2
    prec_map["-"] = 2
    prec_map["("] = 1
    return prec_map

def convert_infix_to_postfix(infix):
    if infix is None:
        return None

    prec_map = get_precedence_map()
    #print prec_map
    opstack = Stack.Stack()

    result_postfix = []

    for item in infix:
        print "--------------------------item: "+str(item)
        # if operand just add it to result
        if item in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or item in "0123456789":
            print "appending: "+str(item)
            result_postfix.append(item)
            opstack.print_stack()

        # if "(" just push it to stack
        elif item == "(":
            opstack.push(item)
            opstack.print_stack()

        # add to result upto open brace
        elif item == ")":
            top_elem = opstack.pop()
            while top_elem.get_data() != "(" and opstack.size > 0:
                print "appending: "+str(top_elem.get_data())
                result_postfix.append(top_elem.get_data())
                top_elem = opstack.pop()

            opstack.print_stack()
            #result_postfix.append(top_elem) # no need to append paranthesis in result.

        else:
            # should be an operator
            while opstack.size > 0 and prec_map[opstack.peek()] >= prec_map[item]:
                temp = opstack.pop()
                print "appending: "+str(temp.get_data())
                result_postfix.append(temp.get_data())


            opstack.push(item) # after popping existing operator , push the current one. (or) without popping just push. based on the precedence check.
            opstack.print_stack()
        #print result_postfix

    while opstack.size != 0:
        result_postfix.append(opstack.pop().get_data())
    return result_postfix

infixstring = "A*B-(C+D)+E"
infix = list(infixstring)
postfix = convert_infix_to_postfix(infix)
postfix = "".join(postfix)
print "Postfix for :"+str(infixstring)+" is : "+str(postfix)
