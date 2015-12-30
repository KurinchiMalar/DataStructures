#from QuickSort import quick_sort
#from Sorting.QuickSort import quick_sort


def swap(Ar,x,y):
    temp = Ar[x]
    Ar[x] = Ar[y]
    Ar[y] = temp

def partition(Ar,low,high):
    '''pivot = low
    swap(Ar,pivot,high)
    for i in range(low,high+1):
        if Ar[low] <= Ar[high]:
            swap(Ar,i,low)
            low = low + 1
    swap(Ar,low,high)'''
    return 4

#Complexity == O(n)
def dutch_flag_algo(Ar):
    low = mid = 0
    high = len(Ar) - 1

    while mid < high:
        print "(low,mid,high): "+str(low)+","+str(mid)+","+str(high)
        '''
        terminate condition (if mid < high) is not correct. mid can go upto high
        (low,mid,high): 3,8,9
            [0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 2, 2]
        '''
        if Ar[mid] == 0:
            swap(Ar,low,mid)
            low = low + 1
            mid = mid + 1
        elif Ar[mid] == 1:
            mid = mid + 1
        else: # Ar[mid] == 2
            swap(Ar,mid,high)
            high = high - 1
            # DONT INCREMENT MID --- because high could have given a zero which should be swapped with low.
    print Ar
    return Ar


def sort_0_and_1_quicksort(Ar):
   return dutch_flag_algo(Ar)


# Time Complexity : O(n)
#Space Complexity : O(1)
#Counting Sort
def sort_0_and_1(Ar,k):
    C = [0 for i in range(0,k+1)]
    for i in range(0,len(Ar)):
        C[Ar[i]] = C[Ar[i]] + 1

    print C
    Ar = []
    for i in range(0,len(C)):
        while C[i] != 0:
            Ar.append(i)
            C[i] = C[i] - 1
        #C += i * C[i]

    print Ar


Ar = [0,1,1,0,1,2,1,2,0,0,0,1]
A = Ar[:]
print A
#sort_0_and_1(Ar,2)
sort_0_and_1_quicksort(Ar)
#sprint str(Ar)
