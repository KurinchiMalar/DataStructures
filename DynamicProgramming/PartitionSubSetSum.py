'''
    Partition problem is to determine whether a given a set can be partitioned into two subsets such that the sum of elements in both
    subsets is same.(Similar to SubsetHalfSum.py)

    For example:

        if A = [1,5,11,5] the array can be partitioned as {1,5,5} and {11}.

        if A = [1,5,3] the array cannot be partioned.

'''
'''
Algorithm:

    1) Calculate the sum of the array. If sum is odd, there cannot be two subsets with equal sum, so return false.
    2) If sum of elements is even, calculate sum/2 and find a subset in the array with sum equal to sum/2
'''
#from DynamicProgramming import SubsetSum

# Time Complexity : O(sum * n)
# Space Complexity : O(sum * n)

def check_if_subset_exists_with_given_sum(Ar,sum):

    n = len(Ar)
    T = [[0]*(sum+1) for x in range(n+1)]

    for i in range(0,n+1):
        T[i][0] = 1

    for j in range(1,sum+1):
        T[0][j] = 0

    for i in range(1,n+1):
        for j in range(1,sum+1):
            if Ar[i-1] > j:
                T[i][j] = T[i-1][j]
            else:
                T[i][j] = T[i-1][j] or T[i-1][j-Ar[i-1]]

    i = n
    j = sum
    result = []
    while i >= 0 and j >= 0:

        if T[i][j] == 0:
            return result

        if T[i][j] == 1 and T[i-1][j] == 0:
            result.insert(0,Ar[i-1])
            j = j - Ar[i-1]
            i = i - 1
        else:
            i = i - 1

    #print result

    return T[n][sum],result

def partition_into_equal_subset(Ar):

    n = len(Ar)

    if n % 2 != 0: # odd
        return 0

    sum = 0
    for i in range(0,n):
        sum += Ar[i]

    #result,isExists = SubsetSum.check_if_subset_exists_with_given_sum(Ar,sum)
    #print result
    isExists,subset1 = check_if_subset_exists_with_given_sum(Ar,sum//2)

    subset2 = [x for x in Ar if x not in subset1]
    return isExists,subset1,subset2

Ar = [1,5,11,5]
isExists,subset1,subset2 = partition_into_equal_subset(Ar)

print "Given Ar: "+str(Ar)
print "Subset exists? : "+str(isExists)
print "Subsets are :"+str(subset1)+" and "+str(subset2)
