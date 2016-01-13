__author__ = 'kurnagar'
'''
 There are 2 sorted arrays A and B of size n each.
 Write an algorithm to find the median of the array obtained after merging the above 2 arrays(i.e. array of length 2n).
 The complexity should be O(log(n))
'''

# Time Complexity : O(n)
# Space Complexity : O(1)

def get_median_of_two_sorted_arrays(A,B):

    n = len(A)

    desired_k = -1
    if 2*n % 2 == 0 :
        print
        desired_k = ((2*n)//2)-1
    else:
        desired_k = (2*n) // 2

    desired_k = desired_k + 1   ## THIS IS BECAUSE....Array index starts from 0, index 2 implies we should find the 3rd smallest :)
    count = 0
    #print desired_k

    k_now = 0
    i = j = 0

    while i < n and j < n:

        while A[i] < B[j]:
            k_now = k_now + 1

            if k_now == desired_k:
                print "("+str(A[i])+"+"+str(B[j])+")"
                return (A[i] + B[j])//2
            i = i+1

        while B[j] < A[i]:
            k_now = k_now + 1

            if k_now == desired_k:
                print "("+str(A[i])+"+"+str(B[j])+")"
                return (A[i] + B[j])//2
            j = j+1
    print "Done"


A = [1,12,15,26,38]
B = [2,13,17,30,45]

A = [1,3,5,7]
B = [2,4,6,8]
print ""+str(get_median_of_two_sorted_arrays(A,B))