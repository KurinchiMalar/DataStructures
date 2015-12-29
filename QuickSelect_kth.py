#http://stackoverflow.com/questions/10846482/quickselect-algorithm-understanding

def swap(Ar,x,y):
    temp = Ar[x]
    Ar[x] = Ar[y]
    Ar[y] = temp

def partition_LowToHigh(Ar,low,high):
    pivot = low
    swap(Ar,pivot,high)
    for i in range(low,high+1):
        if Ar[i] < Ar[high]:
            swap(Ar,i,low)
            low = low + 1
    swap(Ar,low,high)
    return low

def partition_HighToLow(Ar,low,high):
    pivot = low
    swap(Ar,pivot,high)
    for i in range(low,high+1):
        if Ar[i] > Ar[high]:
            swap(Ar,i,low)
            low = low + 1
    swap(Ar,low,high)
    return low

'''
eg) 1

 4 3 2 5 7 6  --> pivot = 3 ( Ar[3] = 5 .. means 4th( pivot-first+1 (3-0+1)) smallest is Ar[3]... )

 pivot = 3 (which is 4th smallest)
 ie) pivot-first+1 = 4
 Say we want to find 2nd smallest k = 2
      then our element is in range (0,pivot)
      [4 3 2 5]
      and we have to find 2nd smallest --> quick_select(0,3,2)


eg) 2

 3 2 1 4 6 9 11 7 8 --> pivot = 4 (Ar[4] = 6 ...means 5th(4-0+1) smallest is Ar[4] )

 pivot = 4 (which is 5th smallest already)
 ie) pivot-first+1 = 5
 Say we want to find 7th smallest k = 7

    k > pivot-first+1 == True
        7 - 5 = 2 ...we should find 2nd smallest from right half of pivot

        k - (pivot-first+1)

        then our element is in range(pivot+1,last)
         [9 11 7 8]
        quick_select(pivot+1,last,k-(pivot-first+1))



COMPLEXITY --> O(n) average , O(n*n) worstcase
http://stackoverflow.com/questions/5945193/average-runtime-of-quickselect
As in quick sort, we have to do partition in halves *, and then in halves of a half, but this time, we only need to do the next round partition in one single partition (half) of the two where the element is expected to lie in.

It is like (not very accurate)

n + 1/2 n + 1/4 n + 1/8 n + ..... < 2 n
'''
def quick_select_kthsmallest(Ar,first,last,k):

    #say pivot = 3 ... it means 0,1,2,3....it is the 4th smallest....pivot-first+1 = 3-0+1
    pivot = partition_LowToHigh(Ar,first,last)

    if k < (pivot-first+1): #go in left half
        return quick_select_kthsmallest(Ar,first,pivot,k)

    elif k > (pivot-first+1): #go in right half
        return quick_select_kthsmallest(Ar,pivot+1,last,k-(pivot-first+1))

    else:
        #print pivot
        return Ar[pivot]

def quick_select_kthlargest(Ar,first,last,k):

    #say pivot = 3 ... it means 0,1,2,3....it is the 4th smallest....pivot-first+1 = 3-0+1
    pivot = partition_HighToLow(Ar,first,last)

    if k < (pivot-first+1): #go in left half
        return quick_select_kthlargest(Ar,first,pivot,k)

    elif k > (pivot-first+1): #go in right half
        return quick_select_kthlargest(Ar,pivot+1,last,k-(pivot-first+1))

    else:
        #print pivot
        return Ar[pivot]



Ar = [4,2,5,7,12,10,11]

#print quick_select(Ar,0,len(Ar)-1,7)
print quick_select_kthlargest(Ar,0,len(Ar)-1,7)
