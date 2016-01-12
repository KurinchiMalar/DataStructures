__author__ = 'kurnagar'
'''
Given an array arr[] , find the maximum distance of indices such that arr[j] > arr[i].


Examples:

  Input: {34, 8, 10, 3, 2, 80, 30, 33, 1}
  Output: 6  (j = 7, i = 1)

  Input: {9, 2, 3, 4, 5, 6, 7, 8, 18, 0}
  Output: 8 ( j = 8, i = 0)

  Input:  {1, 2, 3, 4, 5, 6}
  Output: 5  (j = 5, i = 0)

  Input:  {6, 5, 4, 3, 2, 1}
  Output: -1
'''

# maximum distance of indices = max(j-i)

# Time Complexity : O(n*n)
# Space Complexity : O(1)
def find_distance_bruteforce(Ar):

    max_dist = 0
    for i in range(0,len(Ar)):
        for j in range(len(Ar)-1,i,-1):  # come from end because the distance should be more between i and j.
            if Ar[i] < Ar[j]:
                max_dist = max(max_dist,j-i)
    return max_dist

'''
To solve this problem,

 we need to get two optimum indexes of arr[]: left index i and right index j.

For an element arr[i], we do not need to consider arr[i] for left index if there is an element smaller than arr[i] on left side of arr[i].

Similarly, if there is a greater element on right side of arr[j] then we do not need to consider this j for right index.

    1) So we construct two auxiliary arrays LMin[] and RMax[] such that LMin[i] holds the smallest element on left side of arr[i] including arr[i], and RMax[j] holds the greatest element on right side of arr[j] including arr[j].

    2) After constructing these two auxiliary arrays, we traverse both of these arrays from left to right. While traversing LMin[] and RMa[] if we see that LMin[i] is greater than RMax[j],

     Satisfy condition RMax[j] > Lmin[i] & go to the most minimum.... we need the max distance.

'''
# Time Complexity : O(n)
# Space Complexity : O(n)

def find_maxdistance_efficient(Ar):

    lmin_ar = [0] * len(Ar)
    rmax_ar = [0] * len(Ar)

    lmin_ar[0] = Ar[0]
    rmax_ar[len(Ar)-1] = Ar[len(Ar)-1]
    for i in range(1,len(Ar)):
        lmin_ar[i] = min(Ar[i],lmin_ar[i-1])
    for j in range(len(Ar)-2,-1,-1):
        rmax_ar[j] = max(Ar[j],rmax_ar[j+1])

    print "Array:"+str(Ar)
    print "LMin:"+str(lmin_ar)
    print "RMax:"+str(rmax_ar)

    i = j = 0
    max_diff = 0


    while i < len(lmin_ar) and j < len(rmax_ar):
        #print "-------------------------------------"
        #print "(i,j):"+str(i)+","+str(j)
        #print "existing_maxdiff:"+str(max_diff)

        if lmin_ar[i] < rmax_ar[j]:
            #print "j :"+str(j-i)
            max_diff = max(max_diff,j-i)
            j = j+1
        else:
            i = i+1
    return max_diff


Ar = [4,9,3,1,5,6,7,2]
Ar = [9,2,3,10,5,6,7]
print "BruteForce:"+str(find_distance_bruteforce(Ar))
print "With LMin and RMax:"+str(find_maxdistance_efficient(Ar))


