
# Time Complexity : O(n)
#Space Complexity : O(1)
#Counting Sort

# Takes two scans
def sort_0_and_1_counting(Ar,k):
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

# Single Scan - Efficient
#Complexity == O(n)
def dutch_flag_algo(Ar):
    low = mid = 0
    high = len(Ar) - 1

    while mid <= high:
        print "(low,mid,high): "+str(low)+","+str(mid)+","+str(high)
        '''
        terminate condition (if mid < high) is not correct. mid can go upto high
        (low,mid,high): 3,8,9
            [0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 2, 2]
        '''
        if Ar[mid] == 0:
            #swap(Ar,low,mid)
            Ar[low],Ar[mid] = Ar[mid],Ar[low]
            low = low + 1
            mid = mid + 1
        elif Ar[mid] == 1:
            mid = mid + 1
        else: # Ar[mid] == 2
            #swap(Ar,mid,high)
            Ar[mid],Ar[high] = Ar[high],Ar[mid]
            high = high - 1
            # DONT INCREMENT MID --- because high could have given a zero which should be swapped with low.

    return Ar

Ar = [0,1,1,0,1,2,1,2,0,0,0,1]
A = Ar[:]
print A
print ""+str(sort_0_and_1_counting(Ar,2))
print ""+str(dutch_flag_algo(Ar))
#sprint str(Ar)
