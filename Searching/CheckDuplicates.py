

# BruteForce Solution with two for loops
# Complexity - O(n*n)
from Sorting import MergeSort
def check_duplicates_bruteforce(Ar):
    for i in range(0,len(Ar)):
        for j in range(i+1,len(Ar)):
            if Ar[i] == Ar[j]:
                return Ar[i] # duplicates exist
    return -1 # no duplicates

# Sorting Solution
# Complexity - O(nlogn) + O(n) = O(nlogn)

# Worst case : say input with no duplicates --> O(nlogn) + O(n*n) = O(n*n)
def check_duplicates_sorting(Ar):
    tempAr = Ar[:] # taking copy just for implementation purpose , not to corrupt orig...python will always point by reference.
    tempAr = MergeSort.mergesort(tempAr)
    for i in range(0,len(tempAr)):
        for j in range(i+1,len(tempAr)):
            if Ar[i] == Ar[j]:
                return Ar[i]
    return -1

#Hashing Solution - Initially value at indices zero.Increment on occurences. On insert at index if already 1. stop and return--> Duplicate
# Time Complexity = O(n)
# Space Complexity = O(n)
def check_duplicates_hashing(Ar,n):
    hash_ar = [0]*(n+1)
    for i in range(0,len(Ar)):
        if hash_ar[Ar[i]] == 1: # duplicate exist
            return Ar[i]
        hash_ar[Ar[i]] = hash_ar[Ar[i]] + 1
    return -1


# Time Complexity = O(n)
# Space Complextity = O(1) --> since we are modifying the original array
'''
Input Constraints:

1) Ar values should be from 0 to n-1

2) Ar values should not be negative

3) Ar should not be read-only

'''
def check_duplicates_hashing_negate(Ar,n):
    for i in range(0,len(Ar)):
        if Ar[abs(Ar[i])] < 0 : # already we have negated at a previous occurence.
            return Ar[i]
        else:
            Ar[Ar[i]] = -Ar[Ar[i]]
    return -1

Ar = [33,2,10,20,22,32]
Ar = [3,2,1,2,2,3]
Ar = [5,4,3,2,1]
#print("Duplicates_BruteForce:"+str(check_duplicates_bruteforce(Ar)))
print("Duplicates_Sorting:"+str(check_duplicates_sorting(Ar)))
#print("Duplicates_Hashing:"+str(check_duplicates_hashing(Ar,3)))  # n = 3 ==> 0,1,2,3 .... create Ar[4]
#temp = Ar[:]
#print("Duplicates_Negate:"+str(abs(check_duplicates_hashing_negate(temp,3))))
