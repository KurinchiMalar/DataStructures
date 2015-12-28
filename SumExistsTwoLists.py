# a+b = k
from HeapSort import Heap
ob = Heap()

def binary_search(Ar,k):
    low = 0
    high = len(Ar)-1

    while low <= high:
        middle = (high + low) // 2
        if k < Ar[middle]:
            high = middle - 1
        elif k > Ar[middle]:
            low = middle + 1
        else:
            return middle #index at which value is found : middle
    return -1

#heapsort -> nlogn
#binarysearch --> logn
#nlogn + n* (logn)    n = for every element in A...you are doing a logn binary search = n* (logn)

def is_two_nos_sum_is_k_Exists(A,B,ksum):
    ob.heapList = A
    ob.HeapSort(0,len(A)-1)

    for i in range(0,len(B)-1):
        diff = ksum - B[i]
        print "diff :"+str(diff)
        result = binary_search(ob.heapList,diff)
        print "result :"+ str(result)

        if result != -1 :
            print str(ob.heapList[result]) +"+"+ str(B[i])
            return True

    return False

#nlogn + n solution
def is_two_nos_sum_is_k_Exists_method2(A,B,ksum):
    ob.heapList = A
    ob.HeapSort(0,len(A)-1)
    A = ob.heapList
    print "Sorted A:"+str(A)

    ob.heapList = B
    ob.heapSort_desc(0,len(B)-1)
    B = ob.heapList
    print "Sorted B:"+str(B)

    i = j = 0
    while i < len(A) and j < len(B):
        tmp = A[i] + B[j]
        if ksum > tmp:
            i = i+1
        elif ksum < tmp:
            j = j+1
        else:
            print str(A[i])+"+"+str(B[j])
            return True
    return False



A = [3,2,6,1,7]
#A = [1,2,3,4,6,7]

#print "found:"+str(binary_search(A,7))

B = [2,5,8,9,3,1]
#print str(is_two_nos_sum_is_k_Exists(A,B,10))
A = [6,3,7,1,2]
B = [5,1,2,4,6]
print str(is_two_nos_sum_is_k_Exists_method2(A,B,12))



