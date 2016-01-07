'''
 Given an array with both positive and negative numbers, find the two elements such that their sum is closest to zero.
'''
import sys
from Sorting.MergeSort import mergesort

# Bruteforce

# Time Complexity : O(n*n)
def find_two_elements_sumclosest_to_zero_bruteforce(Ar):

    if len(Ar) < 2:
        print "Invalid Input"
        return -1

    min_sum = sys.maxint
    elem1 = 0
    elem2 = 0
    for i in range(0,len(Ar)):
        for j in range(i+1,len(Ar)):
            print "------------------------------"
            print ("...."+str(Ar[i])+ ","+ str(Ar[j]))
            print ("...."+str(abs(Ar[i]))+","+str(abs(Ar[j])))
            if abs(Ar[i]+Ar[j]) < abs(min_sum):
                min_sum = Ar[i] + Ar[j]
                elem1 = Ar[i]
                elem2 = Ar[j]
    elem_list = []
    elem_list.append(elem1)
    elem_list.append(elem2)
    return elem_list


# Sorting solution

# Time Complexity : O(nlogn) + O(n)
def find_two_elements_sumclosest_to_zero_sorting(Ar):
    tempAr = Ar[:]

    tempAr = mergesort(tempAr)

    low = 0
    high = len(tempAr) - 1
    min_sum = sys.maxint

    elem_list = []
    print tempAr
    while low < high:

        sum = tempAr[low] + tempAr[high]
        #print "sum:"+str(sum)

        #sum = abs(tempAr[low]) + abs(tempAr[high])   --> find the sum and then put abs.... other wise -80+85 = 5 will become 165!!!
        #print "sum:"+str(sum)

        if abs(sum) < abs(min_sum):
            min_sum = sum
            elem1 = tempAr[low]
            elem2 = tempAr[high]
            #print "--"+str(elem1)+","+str(elem2)

        if sum > 0:
            high = high -1
        else:
            low = low + 1

    elem_list.append(elem1)
    elem_list.append(elem2)

    return elem_list

Ar = [10,8,3,5,-9,-7,6]
Ar = [1,60,-10,70,-80,85]

#print ""+str(find_two_elements_sumclosest_to_zero_bruteforce(Ar))
print ""+str(find_two_elements_sumclosest_to_zero_sorting(Ar))