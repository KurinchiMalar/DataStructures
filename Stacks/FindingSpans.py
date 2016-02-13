'''
    Given an array A, the span S[i] of A[i] is the maximum number of consecutive elements A[k] immediately preceding A[i]
    such that A[k] <= A[i]

    Other way of asking:
    -------------------

    Given an array A of integers, find the maximum j-i such that A[j] > A[i]



    Algorithm:

    Number consecutive elements less than A[i] can be easily found out, if the first greater element towards left of A[i] is found!

    then # of elements = i - (above found index)

    eg)  1 2 6 4 5

    #case 1
  including 5       Number of consecutive smaller elements than 5 = (index of 5) - (index of 6) = 4-2 = 2   { 2 elements are 4,5}

    #case 2
  including 6       Number of consecutive smaller elements than 6 = (index of 6) + 1 = 2 + 1 = 3  {3 elements are 1,2,6}
                    # since 6 is the biggest until now.

'''

# Time Complexity : O(n)
# Space Complexity : O(n) # for stack

import Stack

def construct_span(Ar):

    stack = Stack.Stack()

    result_span = [0] * len(Ar)
    result_span[0] = 1  # including itself.
    stack.push(0)

    for i in range(1,len(Ar)):

        while stack.size > 0 and Ar[stack.peek()] <= Ar[i]:  # keep moving left
            stack.pop()


        if stack.size == 0:    # case 2
            result_span[i] = i + 1
        else:    # case 1
            result_span[i] = i - stack.peek()

        stack.push(i)

    print result_span

Ar = [6,3,4,5,2]
construct_span(Ar)

