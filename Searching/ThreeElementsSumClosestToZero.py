'''
    Given an array of n integers, the 3- sum problem is to find three integers whose sum is closest to zero.
'''
import sys
from Sorting.MergeSort import mergesort

# Sorting Solution
# Time Complexity = O(nlogn) + O( n*n )
def find_three_elements_sum_closest_to_zero(Ar):
    tempAr = mergesort(Ar)

    print tempAr
    min_sum = sys.maxint
    elem_list = []

    for i in range(0,len(Ar)-2):

        low = i
        high = len(Ar) - 1

        while low < high:
            print "----------------------------------------------------"
            print "...."+str(Ar[i])+","+str(Ar[low])+","+str(Ar[high])
            sum = Ar[i] + Ar[low] + Ar[high]
            print sum
            if abs(sum) < abs(min_sum):
                min_sum = sum
                elem_list_temp = []
                elem_list_temp.extend((Ar[i],Ar[low],Ar[high]))
                print "###templist"+str(elem_list_temp) +"minsum:"+str(min_sum)

            if sum < 0:
                low = low + 1
            else:
                high = high-1

    elem_list = elem_list_temp
    print str(elem_list)

Ar = [1,60,-10,70,-80,85]

find_three_elements_sum_closest_to_zero(Ar)