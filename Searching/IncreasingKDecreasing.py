
'''
    Given an Array of n distinct integers. Suppose A has the following property, there exists an index i < k < n

    such that A[1] ....A[k] is an increasing sequence
              A[k+1] ....A[n] is a decreasing sequence
'''

# Modified Binary Search
# Time Complexity : O(log n)

def find_pivot_increasing_k_decreasing(Ar,low,high):

    if low == high:
        return Ar[low]

    if low+1 == high:
        return min(Ar[low],Ar[high])

    while low < high:

        middle = (high+low)//2

        if Ar[middle-1] < Ar[middle] and Ar[middle+1] < Ar[middle]: #RETURN CRITERIA: Ar[mid-1] < Ar[mid] > Ar[mid+1]
            return Ar[middle]

        '''
            Ar[middle-1] < Ar[middle] and Ar[middle+1] > Ar[middle] ==> ascending sequence

            Ar[middle-1] > Ar[middle] and Ar[middle+1] < Ar[middle] ==> descending sequence
        '''

        if Ar[middle-1] > Ar[middle] and Ar[middle+1] < Ar[middle]: # First half.. trace and see eg) 15,17,13,12,11,10,9,8,7
            return find_pivot_increasing_k_decreasing(Ar,low,middle)
        else:
            return find_pivot_increasing_k_decreasing(Ar,middle+1,high)


def find_pivot_decreasing_k_increasing(Ar,low,high):

    if low == high:
        return Ar[low]

    # With two elements, the smaller one should follow the bigger one to satify the property.
    if low+1 == high:
        return max(Ar[low],Ar[high])

    while low < high:

        middle = (high+low) // 2
        #print "--------------------------------------"
        #print "low ,  middle , high  ----"+str(low)+", "+str(middle)+", "+str(high)

        if Ar[middle-1] > Ar[middle] and Ar[middle] < Ar[middle+1]: #RETURN CRITERIA: Ar[mid-1] > Ar[mid] < Ar[mid+1]
            return Ar[middle] #GOTCHA!!
        '''
            Ar[middle-1] < Ar[middle] and Ar[middle+1] > Ar[middle] ==> ascending sequence

            Ar[middle-1] > Ar[middle] and Ar[middle+1] < Ar[middle] ==> descending sequence
        '''

        if Ar[middle-1] < Ar[middle] and Ar[middle+1] > Ar[middle]: # ascending sequence... go to first half
            return find_pivot_decreasing_k_increasing(Ar,low,middle)
        else:
            return find_pivot_decreasing_k_increasing(Ar,middle+1,high)


Ar = [15,1,2,3,4,5]
#Ar = [11,12,13,15,2,3,4,5]
Ar = [17,16,15,13,1,2,3,4,5]
print "Decreasing ...k...Increasing"
print Ar
print ""+str(find_pivot_decreasing_k_increasing(Ar,0,len(Ar)-1))

print "--------------------------"
Ar = [11,12,13,14,15,10,9,8,7]
Ar = [15,17,13,12,11,10,9,8,7]
print "Increasing ...k...Decreasing"
print Ar
print ""+str(find_pivot_increasing_k_decreasing(Ar,0,len(Ar)-1))