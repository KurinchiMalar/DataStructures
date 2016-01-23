'''
    Given a sequence of n numbers A(1)....A(n) give an algorithm for finding a contiguous subsequence A(i)....A(j) for
    which the sum of elements in the subsequence is maximum.

    Example : {-2, 11,-4, 13, -5, 2}  --> 20 (11 + -4 + 13)

              {1, -3, 4, -2, -1, 6} --> 7 (4 + -2,+ -1 + 6)

'''

# Time Complexity : O(n)
# Space Complexity : O(1)
'''
Kadane's Algorithm:

    Look at all positive contiguous segments of the array and keep track of the maximum sum contiguous segment(sum_end_here)
    among all the positvite segments(sum_so_far). Each time we get a positive sum , update sum_so_far accordingly.
'''
def max_sum_contiguous_subseq_KadaneAlgorithm(Ar):

    sum_end_here = 0
    sum_so_far = 0
    for i in range(0,len(Ar)):
        sum_end_here = sum_end_here + Ar[i]

        if sum_end_here < 0:
            sum_end_here = 0
            continue

        if sum_so_far < sum_end_here:
            sum_so_far = sum_end_here

    return sum_so_far


# Time Complexity : O(n)
# Space Complexity : O(n)

# M[i] indicates maximum sum of all windows ending at i.
def max_sum_contiguous_subseq_dynamic(Ar):

    M = [0]*(len(Ar)+1)
    result = []

    if Ar[0] > 0:
        M[0] = Ar[0]
    else:
        M[0] = 0

    for i in range(0,len(Ar)):

        if M[i-1]+Ar[i] > 0 :
            M[i] = M[i-1]+Ar[i]

        else:
            M[i] = 0

    max_sum = 0
    max_index = 0
    for i in range(0,len(M)): # one complete scan to find the max value.
        if M[i] > max_sum:
            max_sum = M[i]
            max_index = i

    for i in range(0,max_index+1):

        if M[i] == 0:
            result = []
        else:
            result.append(Ar[i])

    print "The maxsum_contiguous_subseq_fromlefttoright:"+str(result) # to print the maximum seq
    return max_sum

# Time Complexity : O(n)
# Space Complexity : O(n)
# M[i] indicates maximum sum of all windows starting at i.
def max_sum_contiguous_subseq_dynamic_fromrighttoleft(Ar):

    n = len(Ar)
    M = [0]*(n+1)
    result = []

    if Ar[n-1] > 0:
        M[n-1] = Ar[n-1]
    else:
        M[n-1] = 0

    for i in range(n-2,-1,-1):

        if M[i+1]+Ar[i] > 0 :
            M[i] = M[i+1]+Ar[i]

        else:
            M[i] = 0

    max_sum = 0
    max_index = 0
    for i in range(0,len(M)): # one complete scan to find the max value.
        if M[i] > max_sum:
            max_sum = M[i]
            max_index = i

    for i in range(n-1,max_index-1,-1):

        if M[i] == 0:
            result = []
        else:
            result.append(Ar[i])

    print "The maxsum_contiguous_subseq_fromrighttoleft:"+str(result) # to print the maximum seq
    return max_sum

# Time Complexity : O(nlogn)   # Divide and Conquer approach
# Recurrence : 2T(n/2) + O(n)

import sys
def max_crossing_sum(Ar,l,m,hi):

    left_max = -sys.maxint-1
    left_sum = 0
    for i in range(m,l-1,-1):
        left_sum += Ar[i]

        if left_sum > left_max:
            left_max = left_sum

    right_max = -sys.maxint-1
    right_sum = 0
    for i in range(m+1,hi+1):
        right_sum += Ar[i]

        if right_sum > right_max:
            right_max = right_sum

    return left_max + right_max

def max_value_contiguous_subsequence(Ar,low,high):

    if low == high:
        return Ar[low]

    mid = (low + high) // 2

    return max( max_value_contiguous_subsequence(Ar,low,mid),\
                max_value_contiguous_subsequence(Ar,mid+1,high),\
                max_crossing_sum(Ar,low,mid,high))


Ar = [2, 3, 4, 5, 7]
Ar = [-2, 11,-4, 13, -5, 2]

print "max_Recursive_O(nlogn):"+str(max_value_contiguous_subsequence(Ar,0,5))
print "max_DP_O(n):"+str(max_sum_contiguous_subseq_dynamic(Ar))
print "max_DP_O(n):"+str(max_sum_contiguous_subseq_dynamic_fromrighttoleft(Ar))
print "max_Kadane's Algorithm_O(n):"+str(max_sum_contiguous_subseq_KadaneAlgorithm(Ar))
