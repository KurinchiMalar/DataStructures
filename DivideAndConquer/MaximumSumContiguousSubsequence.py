'''
    Given a sequence of n numbers A(1)....A(n) give an algorithm for finding a contiguous subsequence A(i)....A(j) for
    which the sum of elements in the subsequence is maximum.

    Example : {-2, 11,-4, 13, -5, 2}  --> 20 (11 + -4 + 13)

              {1, -3, 4, -2, -1, 6} --> 7 (4 + -2,+ -1 + 6)

Algorithm:

    Using Divide and Conquer approach, we can find the maximum subarray sum in O(nLogn) time. Following is the Divide and Conquer algorithm.

1) Divide the given array in two halves
2) Return the maximum of following three
    a) Maximum subarray sum in left half (Make a recursive call)
    b) Maximum subarray sum in right half (Make a recursive call)
    c) Maximum subarray sum such that the subarray crosses the midpoint

The lines 2.a and 2.b are simple recursive calls.
How to find maximum subarray sum such that the subarray crosses the midpoint?
We can easily find the crossing sum in linear time.
The idea is simple,
    find the maximum sum starting from mid point and ending at some point on left of mid,
    then find the maximum sum starting from mid + 1 and ending with sum point on right of mid + 1.
    Finally, combine the two and return.
'''

# Time Complexity : O(nlogn)
# T(n) = 2T(n/2) + Θ(n)
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

print "max:"+str(max_value_contiguous_subsequence(Ar,0,4))