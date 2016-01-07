
# Sorting Solution

# Time Complexity - O(nlgon) + O(n*n)
'''
Square each element. (This takes O(n) time).
This will reduce the original task to "find three numbers in array, one of which is the sum of other two".


Sort the array in ascending order. This takes O(n log n).

Now consider each element a[i]. If a[i]=a[j]+a[k], then, since numbers are positive and array is now sorted, k<i and j<i.

    To find such indexes, run a loop that increases j from 0 to i,

     and decreases k from i-1 to 0 at the same time, until they meet.

     Increase j if a[j]+a[k] < a[i], and decrease k if the sum is greater than a[i].

     If the sum is equal, that's one of the answers, print it, and shift both indexes.

    This takes O(i) operations.

Repeat step 2 for each index i. This way you'll need totally O(n2) operations, which will be the final estimate.

'''
from Sorting.MergeSort import mergesort
import math
def find_pythagorian_triplets(Ar):

    if len(Ar) < 3:
        print "Invalid input"
        return -1
    '''
    Now consider each element a[i].
    If a[i]=a[j]+a[k], then, since numbers are positive and array is now sorted,
                        k<i and j<i
    '''
    squares = []
    for i in range(0,len(Ar)):
        squares.append(Ar[i]*Ar[i])

    print "squares:" +str(squares)

    tempAr = squares[:]
    tempAr = mergesort(tempAr)

    print "sorted squares:"+str(tempAr)
    elem_list = []
    for i in range(2,len(Ar)):
        k = i-1
        j = 0
        while k > 0 and j < i:
            if tempAr[j] + tempAr[k] < tempAr[i]:
                j = j + 1
            elif tempAr[j] + tempAr[k] > tempAr[i]:
                k = k -1
            else:
                elem_list.extend((tempAr[i],tempAr[j],tempAr[k]))
                for k in range(0,len(elem_list)):
                    elem_list[k] = math.sqrt(elem_list[k])
                return elem_list
    return elem_list

Ar = [2,6,1,3,16,5,12,4,9]
Ar = [2,6,1,3,8,5,12,14,13]
print ""+str(find_pythagorian_triplets(Ar))