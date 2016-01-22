__author__ = 'kurnagar'

# Recurrence:  T(n) = T(n-1) + T(n-2)

# Time Complexity : O(2 pow n)
# Space Complexity : O(n) if we consider the function call stack size, otherwise O(1).
def fibo(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return fibo(n-1)+fibo(n-2)

print ""+str(fibo(4))


# Time Complexity : O(n)
# Space Complexity : O(n) --- for fib_table
def fibo_dynamic(n):

    fib_table = [0]*(n+1)
    fib_table[0] = 0
    fib_table[1] = 1

    i = 0
    for i in range(2,n+1):
        fib_table[i] = fib_table[i-1]+fib_table[i-2]


    return fib_table[n]

print ""+str(fibo_dynamic(4))


# Time Complexity : O(n)
# Space Complexity : O(1)
def fibo_dynamic_optimised(n):

    a = 0
    b = 1

    if n == 0:
        return a

    if n == 1:
        return b

    for i in range(2,n+1):
        a,b = b,a+b

    return b

print ""+str(fibo_dynamic_optimised(3))





