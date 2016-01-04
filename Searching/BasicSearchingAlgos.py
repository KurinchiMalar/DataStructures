'''
Comparing basic search Algorithms (WORST  - AVERAGE time comparison)

Array

    Unordered  - O(n) - O(n/2)
    Ordered - O(logn) - O(logn)(Binary Search)

List

    Unordered - O(n) - O(n/2)
    Ordered - O(n) - O(n/2)

Trees

   BST - O(n)(skew)  - (logn)


'''


from Sorting import MergeSort
#Unordered Linear Search
def unordered_linear_search(numbersList,value):
    for i in range(0,len(numbersList)):
        if numbersList[i] == value:
            return 1
    return -1

#Ordered Linear Search

def ordered_linear_search(numbersList,value):

    tempList = numbersList[:]
    tempList = MergeSort.mergesort(tempList)
    print(tempList)

    for i in range(0 , len(tempList)):
        if tempList[i] == value:
            return 1
        elif tempList[i] > value:
            return -1
    return -1


def binary_search_iterative(numbersList,value):
    low = 0
    high = len(numbersList)-1

    tempList = numbersList[:]
    print tempList
    tempList = MergeSort.mergesort(tempList)
    print tempList

    while low <= high:
        middle = (low+high)/2
        if value < tempList[middle]:
            high = middle - 1
        elif value > tempList[middle]:
            low = middle + 1
        else:
            return 1
    return -1

def binary_search_recursive(nList,value,low,high):
    if low > high:
        return -1

    middle = (low+high)/2
    if value ==  nList[middle]:
        return 1
    elif value < nList[middle]:
        return binary_search_recursive(nList,value,low,middle-1)
    else:
        return binary_search_recursive(nList,value,middle+1,high)

    #return -1

Ar = [6,4,9,2,1,4,3,8,0,12,5]
#print "Unordered Search:"+str(unordered_linear_search(Ar,13))
#print "Ordered Search:"+str(ordered_linear_search(Ar,7))
tempAr = MergeSort.mergesort(Ar)
print "Binary Search:" + str((binary_search_recursive(tempAr,13,0,len(tempAr)-1)))