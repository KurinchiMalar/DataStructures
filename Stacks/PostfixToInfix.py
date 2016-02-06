'''

Postfix expression : 123 * + 5 -
corresponding
Infix expression : 1 + (2 * 3) - 5  = 2

'''
# Time Complexity : O(n)
# Space Complexity : O(n)
import Stack
def doMath(operator,operand1,operand2):
    operand1 = int(operand1)
    operand2 = int(operand2)
    if operator == "+":
        return operand1+operand2
    elif operator == "-":
        return operand1-operand2
    elif operator == "*":
        return operand1*operand2
    else:
        return operand1/operand2

def evaluate_postfix(postfix):

    opstack = Stack.Stack()
    operators = list("+-*/")
    for item in postfix:

        if item in "0123456789":
            opstack.push(item)
        elif item in operators:
            operand1 = opstack.pop().get_data()
            operand2 = opstack.pop().get_data()
            print "operand1: "+str(operand1)
            print "operand2: "+str(operand2)
            opstack.push(doMath(item,operand2,operand1))  # note: operand2 is the earlier element in stack.
    print opstack.print_stack()

postfix = "123*+5-"
postfix = list(postfix)
evaluate_postfix(postfix)