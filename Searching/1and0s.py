'''
    Given an input array of size unknown with all 1's in the beginning and 0's in the end. Find the index in the array from
    where 0's start. Consider there are millions of 1's and 0's
'''

# Binary Search Solution
# Time Complexity - O(log n)
def find_start_of_0(Ar,low,high):

    # We have to check for 1 elem , 2 elem scenerio because binary search to find middle needs atleast 3 elem.

    if low == high:
        if Ar[low] == 0:
            return low

    if low+1 == high:
        if Ar[low] != Ar[high]:
            if Ar[low] == 1:
                return low
            else:
                return high

    while low < high:

        middle = (low + high) // 2

        if Ar[middle] == 0 and Ar[middle-1] == 1:
            return middle

        if Ar[middle] == 0 and Ar[middle-1] == 0:
            return find_start_of_0(Ar,low,middle)

        if Ar[middle] == 1 and Ar[middle+1] == 1:
            return find_start_of_0(Ar,middle+1,high)


Ar = [1,1,1,1,1,1,1,0,0,0,0,0]

print ""+str(find_start_of_0(Ar,0,len(Ar)-1))
