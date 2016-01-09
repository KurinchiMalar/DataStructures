# Given an array of n elements , can we output in sorted order the K elements following the median in sorted order
# in time O(n + KlogK)


#STEPS:
#
#Find the median and partition about the median. With this we can find all elements greater than it.
#Now find Kth largest element in this set and partition about it.
#And get all the elements less than it.
#Output the sorted list of final set of elements.
#This operation takes O(n + KlogK)
from kthLargestSmallest_QuickSelect import quick_select_kthlargest
from HeapSort import Heap
ob = Heap()

def print_upto_k(resultAr,k):
    #print resultAr
    bkp = resultAr[:]
    kthelem = quick_select_kthlargest(bkp,0,len(bkp)-1,k)
    final = []

    for i in resultAr:
        if i == kthelem:
            final.append(i)
            break
        final.append(i)

    print "K sorted elems after median:"+str(final)

def get_list_of_k_sorted_after_median(Ar,k):
    print("Input:"+str(Ar))
    ob.heapList = Ar
    ob.HeapSort(0,len(Ar)-1)
    Ar = ob.heapList
    print("Sorted:"+str(Ar))
    if len(Ar) % 2 != 0:
        print "odd"
        median = len(Ar) / 2
    else:
        print "even"
        median = (len(Ar)/2)-1
    print "Median element is :"+str(Ar[median])
    remaining = []
    for i in range(median+1,len(Ar)):
        remaining.append(Ar[i])
    print "Elements after median:"+str(remaining)
    print_upto_k(remaining,k)

Ar = [4,2,5,7,12,10,11]

get_list_of_k_sorted_after_median(Ar,2)
