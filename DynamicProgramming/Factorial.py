__author__ = 'kurnagar'

'''
Yes, the algorithm is linear, running in O(n) time.
This is the case because it executes once every time it decrements the value n, and it decrements the value n until it reaches 0, meaning the function is called recursively n times.
This is assuming, of course, that both decrementation and multiplication are constant operations.
'''
# Time Complexity : O(n)
# Space Complexity : O(n) --> for recursive call stack

def fact(n):

    if n == 0:
        return 1

    if n == 1:
        return 1

    return n*fact(n-1)

print ""+str(fact(5))

'''
Say we want to find m! and n! ...if m < n then.... n! can be found in less than O(n), because m! would have already been computed and save.
Complexity will be : O(max(m,n))
'''
# Time Complexity : O(n)
# Space Complexity : O(n)

def fact_dynamic(n):
    fact_table = [0]*(n+1)

    fact_table[0] = 1

    for i in range(1,n+1):
        fact_table[i] = i * fact_table[i-1]

    return fact_table[i]

print ""+str(fact_dynamic(4))
