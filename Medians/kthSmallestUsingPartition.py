__author__ = 'kurnagar'


def partition(Ar,low,high):

    Ar[low],Ar[high] = Ar[high],Ar[low] # Ar[high] will be the pivot now

    for i in range(low,high):
        if Ar[i] <= Ar[high]:
            Ar[i],Ar[low] = Ar[low],Ar[i]  # upto elements before low are less than Ar[high] (ideally pivot)
            low = low + 1
    Ar[low],Ar[high] = Ar[high],Ar[low]

    return low

# QuickSelect Algorithm
# Time Complexity - O(n) Average Case
#                    O(n*n) Worst Case   depending on the partition logic

# Space Complexity - O(1)
def find_k_smallest_using_partition(Ar,first,last,k):

    # say pivot = 2 .... 1st , 2nd , 3rd smallest will be in first half , remaining will be in second half.

    # pivot - first + 1 = 3 :)
    pivot  = partition(Ar,first,last)

    if k < pivot - first + 1:
        return find_k_smallest_using_partition(Ar,first,pivot,k)

    elif k > pivot - first + 1:
        return find_k_smallest_using_partition(Ar,pivot+1,last,k-(pivot - first + 1))

    else:
        return Ar[pivot]

Ar = [4,6,3,9,1,5,7]

#print ""+str(partition(Ar,0,len(Ar)-1))
print ""+str(find_k_smallest_using_partition(Ar,0,len(Ar)-1,2))


