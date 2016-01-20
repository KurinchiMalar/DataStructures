'''
Find the median of two sorted arrays in O(logn) --> Divide and Conquer (Binary Search)
'''
'''
Example:

   ar1[] = {1, 5, 7, 10, 13}
   ar2[] = {11, 15, 23, 30, 45}

Middle element of ar1[] is 7. Let us compare 7 with 23 and 30,
    since 7 smaller than both 23 and 30,

    move to right in ar1[].
        Do binary search in {10, 13}, this step will pick 10.
            Now compare 10 with 15 and 23.
    Since 10 is smaller than both 15 and 23,
            again move to right.
            Only 13 is there in right side now.
    Since 13 is greater than 11 and smaller than 15, terminate here. We have got the median as 12 (average of 11 and 13)
'''
# Time Complexity : O(log n)

def get_median_divide_and_conquer(A,B,low,high,n):

    # we have reached the end of A array... median should be in B array :)
    if low > high:
        return get_median_divide_and_conquer(B,A,0,n-1,n) # --> search in B

    i = (low + high) // 2
    j = n-1-i    # find the ith index in B array... n-1 - i

    # Base condition

    if A[i] >= B[j] and A[i] <= B[j+1]:

        return (A[i]+B[j]) // 2

    # current element in A greater than both j and j+1 in B --> go to left half of A
    elif A[i] > B[j] and A[i] > B[j+1]:

        return get_median_divide_and_conquer(A,B,low,i-1,n)

    else:
        return get_median_divide_and_conquer(A,B,i+1,high,n)    # --> go to right half of A

A = [1, 12, 15, 26, 38]
B = [2, 13, 17, 30, 45]

print "Median : "+str(get_median_divide_and_conquer(A,B,0,4,5))
