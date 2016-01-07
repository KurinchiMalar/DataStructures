from Sorting.MergeSort import mergesort
import math
# Find the two repeating elements in a given array.

# Given an array with size, all elements of the array are in range 1 to n and also all the elements occur only once
# except two numbers which occur twice. Find those two repeating numbers.

# Brute Force Solution
# Time Complexity : O(n*n)

def find_two_repeating_elements_bruteforce(Ar):

    repeating_element = []
    for i in xrange(0,len(Ar)):
        for j in xrange(i+1,len(Ar)):
            if Ar[i] == Ar[j]:
                repeating_element.append(Ar[i])
    return repeating_element

# Sorting
# Time Complexity = O(nlogn) + O(n*n) = O(n*n)
# Space Complexity = O(n)

def find_two_repeating_elements_sorting(Ar):

    tempAr = Ar[:]
    tempAr = mergesort(Ar)
    repeating_element = []
    for i in xrange(0,len(tempAr)):
        for j in xrange(i+1,len(tempAr)):
            if tempAr[i] == tempAr[j]:
                repeating_element.append(tempAr[i])
    return repeating_element

# Sum Product Equation
# Time Complexity = O(n)
'''

Take Ar = [4,2,4,5,2,3,1]

Say X and Y are the repeating elements

n = 5 ==>
    Sum_n = 15
    Sum_ar = 21

    Sum_ar - Sum_n = 21 - 15 = 6 ie) X+Y = 6

    Prod_n = 120
    Prod_ar = 960

    Prod_ar / Prod_n = 960/120 = 8 ie) XY = 8

    Now we have
        X+Y = 6 and XY = 8

            Substitution ==> x(6-x) = 8 ==> x*x - 6x + 8 =0

            x*x = b*2 - 4ac (Formula for quadratic eqn)

            x = (-b +- sqrt(b*b -4ac)) / 2a

            x = sqrt((-6)*(-6) -4 (1)(8)) ==> (xplusy+math.sqrt((xplusy*xplusy) - (4*xstary)))//2

            x = 2
            y = 4
'''
def find_two_repeating_elements_equation(Ar,n):

    sum_n = sum_ar = 0
    prod_n = prod_ar = 1
    repeating_elements=[]

    for i in range(1,n+1):
        sum_n += i
        prod_n *= i

    for i in range(0,len(Ar)):
        sum_ar += Ar[i]
        prod_ar *= Ar[i]

    xplusy = sum_ar - sum_n
    xstary = prod_ar // prod_n

    print "xplusy -- xstary"+str(xplusy)+"--"+str(xstary)

    x = (xplusy+math.sqrt((xplusy*xplusy) - (4*xstary)))//2
    #x = math.sqrt(36-32)
    print x

    y = xplusy - x

    repeating_elements.append(x)
    repeating_elements.append(y)

    return repeating_elements


# XOR Solution

# Time Complexity = O(n)
# Space Complexity = O(1)

def find_two_repeating_elements_xorlogic(Ar,n):

    xor = 0

    x = y = 0

    for i in range(1,n+1):
        xor = xor ^ i

    for i in range(0,len(Ar)):
        xor = xor ^ Ar[i]

    rightmost_bit_on = xor & ~(xor-1)

    print "rightmost_bit_on: "+str(rightmost_bit_on)

    for i in xrange(0,len(Ar)):
        if rightmost_bit_on & Ar[i]:
            x = x ^ Ar[i]
        else:
            y = y ^ Ar[i]

    for j in xrange(1,n+1):
        if rightmost_bit_on & i:
            x = x ^ i
        else:
            y = y ^ i

    repeating_elements = []
    repeating_elements.append(x)
    repeating_elements.append(y)
    return repeating_elements

Ar = [4,2,4,5,2,3,1]

#Ar = [4,5,2,5,3,1,3]
#print ""+str(find_two_repeating_elements_bruteforce(Ar))
#print ""+str(find_two_repeating_elements_sorting(Ar))
#print ""+str(find_two_repeating_elements_equation(Ar,5))
print ""+str(find_two_repeating_elements_xorlogic(Ar,5))

