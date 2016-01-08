'''
     Given a sorted array of n integers that has been rotated unknown number of times. Give a O(logn) algorithm that finds
     an element in the array.
'''

# Binary Search Method

# Time Complexity : O(log n)

def find_element_in_rotated_sorted_array(Ar,low,high,k):

    print "----------------------------------"

    print "(low , high):"+str(low)+","+str(high)
    if low == high:
        if Ar[low] == k:
            return low

    if low+1 == high:

        if Ar[low] == k:
            return low
        elif Ar[high] == k:
            return high


    while low < high:

        middle = (low+high) // 2
        print "middle:"+str(middle)

        if Ar[middle] == k:
            return middle

        if Ar[low] <= k and Ar[middle - 1] >= k:
            return find_element_in_rotated_sorted_array(Ar,low,middle-1,k)
        else:
            return find_element_in_rotated_sorted_array(Ar,middle+1,high,k)



Ar = [15,16,19,20,25,13,4,5,7,10,14]

print ""+str(find_element_in_rotated_sorted_array(Ar,0,len(Ar)-1,19))