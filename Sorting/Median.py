#Assuming the array x is sorted and is of length n:

#If n is odd then the median is x[(n-1)/2].
#If n is even than the median is ( x[n/2] + x[(n/2)-1] ) / 2.

# which can simply be
#odd -> n/2
#even -> (n/2) - 1
from QuickSelect_kthsmallest import quick_select
from HeapSort import Heap
ob = Heap()

#Complexity --> O(nlogn)
def getMedian_SortingLogic(Ar):
    ob.heapList = Ar
    ob.HeapSort(0,len(Ar)-1)
    Ar = ob.heapList
    print Ar
    if len(Ar) % 2 != 0:
        print "odd"
        median = len(Ar) / 2
    else:
        print "even"
        median = (len(Ar)/2)-1
    print "Median element is :"+str(Ar[median])


#COMPLEXITY --> O(n) average , O(n*n) worstcase for QUICK_SELECT
def getMedian_LinearTime(Ar):
    if len(Ar) % 2 != 0:
        print "odd"
        median = len(Ar) / 2
        print "Finding the : "+str(median+1)+"smallest..."
        #quick_select(Ar,0,len(Ar)-1,median+1)
    else:
        print "even"
        median = ( len(Ar) / 2 ) - 1
        print "Finding the : "+str(median+1)+"smallest..."
        #quick_select(Ar,0,len(Ar)-1,median+1)
    return quick_select(Ar,0,len(Ar)-1,median+1)

Ar = [4,5,2,1,7,6,3,8,10,12]

#getMedian_SortingLogic(Ar)

print str(getMedian_LinearTime(Ar))
