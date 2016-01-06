
from Sorting.MergeSort import mergesort
# Given a list of n-1 integers in the range 1 to n. There are no duplicates in the list. One of them is missing.
# Find the missing integer.

# Brute Force
# Time Complexity - O(n*n)

def get_missing_number_bruteforce(Ar,n):
    for i in xrange(1,n+1): # compare every element from 1 to n with every other element in array.
        missing_found = 1
        for j in xrange(0,len(Ar)):
            #print "...."+str(i)+" == " +str(Ar[j])
            if i == Ar[j]:
                missing_found = 0

        if missing_found == 1:
            print "Missing element is :"+str(i)
            return i
    return -1


#Sorting
#Time Complexity - O(nlogn)

def get_missing_number_sorting(Ar):

    tempAr = mergesort(Ar)

    for i in range(0,len(tempAr)):
        if tempAr[0] != 1:
            return 1  # 1  is the missing number.
        if Ar[i+1] != Ar[i]+1:
            return Ar[i]+1
    return -1 # no missing number

# Hashing
# Time Complexity - O(n)
# Space Complexity - O(n)

def get_missing_number_hashing(Ar,n):

    hash_ar = [0]*(n+1)
    for i in xrange(0,len(Ar)):
        hash_ar[Ar[i]] = hash_ar[Ar[i]] + 1

    print hash_ar
    for i in xrange(1,len(hash_ar)):
        if hash_ar[i] == 0:
            return i
    return -1

# Sum logic
# Time Complexity - O(n)
# Space Complexity - O(1)

def get_missing_number_sumlogic(Ar,n):
    sum = 0
    for i in xrange(1,n+1):
        sum = (n*(n+1)) // 2

    print str(sum)

    for i in range(0,len(Ar)):
        sum -= Ar[i]

    return sum

Ar = [8,2,1,6,3,4,7,9]


# when sum [n*(n+1)]/2 is greater than INTEGER.MAX , xor logic is used.
# XOR logic
# Time Complexity - O(n)
# Space Complexity - O(1)

def get_missing_number_xorlogic(Ar,n):

    x = 0
    y = 0

    for i in range(1,n+1):
        x = x ^ i

    for i in range(0,len(Ar)):
        y = y ^ Ar[i]

    return x ^ y

#get_missing_number_bruteforce(Ar,9)
#print(""+str(get_missing_number_sorting(Ar)))
#print(""+str(get_missing_number_hashing(Ar,9)))
#print(""+str(get_missing_number_sumlogic(Ar,9)))
print(""+str(get_missing_number_xorlogic(Ar,9)))