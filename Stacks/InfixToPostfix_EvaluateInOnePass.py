'''
    Evaluate the infix expression with stacks in one pass.

    Normal method:
    -------------

    Infix : 1 + (3 * 2) - 5

        1) we convert this to postfix (InfixToPostfix.py) --> 132 * + 5 -
        2) Evaluate the postfix expression (EvaluatePostfix.py) --> 2

    We can do this in one pass . using two stacks. operandstack and operator stack

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

def evaluate_infix(input):

    operandstack = Stack.Stack()
    operatorstack = Stack.Stack()

    for token in input:
        print "---------------------token: "+str(token)
        if token in "0123456789": # it is operand. put into operand stack.
            operandstack.push(token)
        elif token == "(":
            operatorstack.push(token)
        elif token == ")":
            if operatorstack.size == 0:
                print "Improper infix input"
                return -1
            else:
                while operatorstack.peek() != "(":
                    operand1 = operandstack.pop().get_data()
                    operand2 = operandstack.pop().get_data()
                    op = operatorstack.pop().get_data()
                    result = doMath(op,operand2,operand1)
                    operandstack.push(result)
                if operatorstack.peek() == "(":
                    operatorstack.pop() # we don't really want (
        else:  # it is an operator
            if operatorstack.size == 0:
                operatorstack.push(token)
            else:
                prec_map = get_precedence_map()
                top = operatorstack.peek()
                if prec_map[top] >= prec_map[token]:
                    operand1 = operandstack.pop().get_data()
                    operand2 = operandstack.pop().get_data()
                    op = operatorstack.pop().get_data()
                    result = doMath(op,operand2,operand1)
                    operandstack.push(result)
                    operatorstack.push(token)
                else:
                    operatorstack.push(token)
        print "operatorstack:"
        operatorstack.print_stack()
        print "operandstack:"
        operandstack.print_stack()

    while operatorstack.size > 0:
        operand1 = operandstack.pop().get_data()
        operand2 = operandstack.pop().get_data()
        op = operatorstack.pop().get_data()
        result = doMath(op,operand2,operand1)
        operandstack.push(result)

    print "Result: "+str(operandstack.pop().get_data())

input = "1+(3*2)-5"
input = list(input)
evaluate_infix(input)