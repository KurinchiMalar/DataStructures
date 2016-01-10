'''
    Maximum difference between two elements:

         Given an array A[] of integers, find out the differencebetween any two elements

         such that the larger element appears after the smaller number in A[].

         eg) [2,3,10,6,4,8,1] then returned value should be 8 (Diff between 10 and 2)
            [7,9,5,6,3,2] then returned value should be 2 (Diff between 7 and 9)
'''
import sys
# Brute Force
# Time Complexity : O(n*n)

def find_max_diff_bruteforce(Ar):

    max_diff = 0

    for i in range(0,len(Ar)):
        for j in range(i+1,len(Ar)):
            if Ar[j] - Ar[i] > max_diff:
                max_diff = Ar[j] - Ar[i]
    return max_diff


'''
Method 2 (Tricky and Efficient)
In this method, instead of taking difference of the picked element with every other element,
we take the difference with the minimum element found so far. So we need to keep track of 2 things:

1) Maximum difference found so far (max_diff).
2) Minimum number visited so far (min_element).
'''

# Time Complexity : O(n)
# Space Complexity : O(1)

def find_max_diff_minelemMethod(Ar):

    min_elem = Ar[0]
    max_diff = 0

    for i in range(1,len(Ar)):

        if Ar[i] - min_elem > max_diff:
            max_diff = Ar[i] - min_elem

        if Ar[i] < min_elem:
            min_elem = Ar[i]

    return max_diff

'''
First find the difference between the adjacent elements of the array
and store all differences in an auxiliary array diff[] of size n-1.

Now this problems turns into finding the maximum sum subarray of this difference array.
'''
# Time Complexity : O(n)
# Space Complexity : O(n-1)
def find_max_diff_diffarrayMethod(Ar):
    diff_Ar = [0]*(len(Ar)-1)
    #print diff_Ar
    j = 0
    for i in range(1,len(Ar)):
        diff_Ar[j] = Ar[i] - Ar[i-1]
        j = j + 1

    #print diff_Ar

    max_diff = diff_Ar[0]

    for i in range(1,len(diff_Ar)):
        # if the previous holder has a negative, we dont want to get a subtraction and reduce current diff value, so ignore.
        if diff_Ar[i-1] > 0:
            diff_Ar[i] = diff_Ar[i-1] + diff_Ar[i]

        # THE ABOVE STEP WILL PUT IN CURRENT INDEX i , the difference of current with the most minimum upto now.
        if diff_Ar[i] > max_diff:
            max_diff = diff_Ar[i]

    return max_diff

Ar = [2,3,10,6,4,8,1]
print Ar
Ar = [7,9,5,6,3,2]
#Ar = [1,2,90,10,110]
#Ar = [1,2,6,80,100]

#print ""+str(find_max_diff_bruteforce(Ar))
#print ""+str(find_max_diff_minelemMethod(Ar))
print ""+str(find_max_diff_diffarrayMethod(Ar))