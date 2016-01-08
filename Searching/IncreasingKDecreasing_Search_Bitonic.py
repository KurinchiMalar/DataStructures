'''
Bitonic Search:

    An array is bitonic if it is comprised of an increasing sequence of integers followed immediately by a decreasing sequence of integers.
    Given a bitonic array A of n distinct integers, describe how to determine whether a given integer is in the array in
    O(logn) steps.
'''

# Time Complexity: O(logn)

def find_element_bitonic_array(Ar,low,high,k):

    if low == high:
        if Ar[low] == k:
            return low

    if low+1 == high:
        if Ar[low] == k:
            return low
        elif Ar[high] == k:
            return high

    while low < high:

        middle = (low+high)// 2
        print "--------------------------------------"
        print "low ,  middle , high  ----"+str(low)+", "+str(middle)+", "+str(high)
        if Ar[middle] == k:
            return middle

        if Ar[middle-1] <= k and Ar[middle+1] <= k: # middle+1 less means no way it could be in the right half.
            return find_element_bitonic_array(Ar,low,middle-1,k)
        else:
            return find_element_bitonic_array(Ar,middle+1,high,k)

Ar = [15,17,13,12,11,10,9,8,7]
Ar = [11,12,13,9,8,5,4,3,2,1]
print ""+str(find_element_bitonic_array(Ar,0,len(Ar)-1,12))