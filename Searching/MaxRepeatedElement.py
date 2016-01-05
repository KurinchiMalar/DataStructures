# BruteForce Solution with two for loops
# Complexity - O(n*n)
from Sorting import MergeSort
def max_repeated_element_BruteForce(Ar):
    max = -1
    max_elem = -1
    for i in xrange(0,len(Ar)):
        counter = 0
        for j in xrange(i+1,len(Ar)):
            if Ar[i] == Ar[j]:
                counter = counter + 1
        if counter > max:
            max = counter
            max_elem = Ar[i]
    return max_elem

# Sorting Solution
# Time Complexity - O(nlogn)
def max_repeated_element_Sorting(Ar):
    tempAr = Ar[:]
    tempAr = MergeSort.mergesort(tempAr)
    #print tempAr

    max = -1
    max_elem = -1

    counter = 1 # tempAr[0] has already occured once.
    cur_elem = tempAr[0]

    for i in xrange(1,len(tempAr)):
        if tempAr[i] == cur_elem:
            counter = counter+1
            if counter > max:
                max = counter
                max_elem = tempAr[i]
        else:
            counter = 1
            cur_elem = tempAr[i]

    return max_elem

#Hashing Solution
# Space Complexity - O(n)
# Time Complexity - O(n)
def max_repeated_element_Hashing(Ar,n):
    count_array = [0] * (n+1)
    for i in xrange(0,len(Ar)):
        count_array[Ar[i]] = count_array[Ar[i]] + 1
    print count_array

    max_elem = -1
    max_count = -1
    for i in xrange(0,len(count_array)):
        if count_array[i] > max_count:
            max_count = count_array[i]
            max_elem = i
    return max_elem


# Time Complexity = O(n)
# Space Complextity = O(1) --> since we are modifying the original array
'''
Input Constraints:

1) Ar values should be from 0 to n-1

2) Ar values should not be negative

3) Ar should not be read-only

'''
def max_repeated_element_Hashing_AddingNtoValueAtModuloIndex(Ar):

    n = len(Ar)
    max_count = -1
    max_elem = -1


    for i in range(0,len(Ar)):
        Ar[Ar[i]%n] = Ar[Ar[i]%n] + n
        '''print "---"+str(i)
        print Ar
        print str(Ar[i]%n)
        print str(Ar[i])
        Ar[Ar[i]] = Ar[Ar[i]] + n''' # when Ar[i] becomes something like 9 ,15 ie) repetitions added. then you will get out of bounds. 9%6 = 3 , 15%6 = 3..., 21%6 = 3
    print Ar

    for i in range(0,len(Ar)):
        if max_count < Ar[i] // n:
            max_count = Ar[i] // n
            max_elem = i
    return max_elem


Ar = [3,5,6,3,3,8,4,3,2,8,9]
print max_repeated_element_BruteForce(Ar)

print max_repeated_element_Sorting(Ar)

Ar = [3,5,8,3,3,8,4,8,2,8,9]
print max_repeated_element_Hashing(Ar,10)

Ar = [5,3,3,3,5,3]
print max_repeated_element_Hashing_AddingNtoValueAtModuloIndex(Ar)