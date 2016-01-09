'''
   Given an array of n distinct integers, design an O(logn) algorithm to find an index i, such that A[i-1] < A[i] < A[i+1]
'''

def find_local_minimum(Ar,low,high):

    if low == high:
        return Ar[low]

    if low+1 == high:
        if Ar[low] < Ar[high]:
            return Ar[low]
        return -1

    while low < high:

        middle = (low+high) // 2

        if Ar[middle] <= Ar[middle-1] and Ar[middle] <= Ar[middle+1]:
            return Ar[middle]

        if Ar[middle-1] < Ar[middle+1]: # go to first half
            return find_local_minimum(Ar,low,middle)
        else:
            return find_local_minimum(Ar,middle+1,high)

Ar = [2,1,3,4,10,8,11]

print ""+str(find_local_minimum(Ar,0,len(Ar)-1))