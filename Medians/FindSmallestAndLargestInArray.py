__author__ = 'kurnagar'

import sys

# Time Complexity : O(n)

# Space Complexity : O(1)

'''
Number of Comparisons:

 Worst Case : 2(n-1). Descending Array.  For every element we are making two comparisons.

 Best Case : n-1 . Ascending Array . Only if Ar[i] < min_elem will be happening.

 Average Case : 3n/2 -1
'''

def get_MinMax(Ar):

    min_elem = sys.maxint
    max_elem = -sys.maxint-1

    for i in range(1,len(Ar)):

        if Ar[i] < min_elem:
            min_elem = Ar[i]

        elif Ar[i] > max_elem:
            max_elem = Ar[i]

    return min_elem,max_elem  # automatically tuple is created

Ar = [2, 1, 5, 234, 3, 44, 7, 6, 4, 5, 9, 11, 12, 14, 13]
min , max =  get_MinMax(Ar) # tuple unpacking

print ""+str(min)+" "+str(max)


