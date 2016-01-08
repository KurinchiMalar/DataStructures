'''
     Given a sorted array of n elements, possibly with duplicates, find the index of first occurence of a number in O(logn) time
'''


def find_first_occurence(Ar,low,high,k):

    if low == high:
        if Ar[low] == k:
            return low

    if low+1 == high:
        if Ar[low] == k and Ar[high] == k:
            return low
        elif Ar[low] == k:
            return low
        elif Ar[high] == k:
            return high

    while low < high:

        middle = (low+high) // 2

        print "--------------------------------------"
        print "low ,  middle , high  ----"+str(low)+", "+str(middle)+", "+str(high)
        if Ar[middle] == k and Ar[middle-1] < k:
            return middle

        if Ar[middle] == k and Ar[middle-1] == k:
            return find_first_occurence(Ar,low,middle-1,k)
        elif Ar[middle] > k :
            return find_first_occurence(Ar,low,middle-1,k)
        else:
            return find_first_occurence(Ar,middle+1,high,k)

def find_last_occurence(Ar,low,high,k):

    if low == high:
        if Ar[low] == k:
            return low

    if low+1 == high:
        if Ar[low] == k and Ar[high] == k:
            return high
        if Ar[high] == k:
            return high
        if Ar[low] == k:
            return low

    while low < high:

        middle = (low + high) // 2

        if Ar[middle] == k and Ar[middle+1] > k:
            return middle

        if Ar[middle] == k and Ar[middle+1] == k:
            return find_last_occurence(Ar,middle+1,high,k)

        if Ar[middle] > k:
            return find_last_occurence(Ar,low,middle,k)
        else:
            return find_last_occurence(Ar,middle+1,high,k)



Ar = [5,5,9,12,21,21,21,34,34,57,70,84]
#print ""+str(find_first_occurence(Ar,0,len(Ar)-1,34))
print ""+str(find_last_occurence(Ar,0,len(Ar)-1,5))
