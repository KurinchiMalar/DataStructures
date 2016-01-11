__author__ = 'kurnagar'

import sys

# Time Complexity : O(n)

# Worst Case number of comparisons : 2(n-1).   For every element we are making two comparisons.
# Space Complexity : O(1)

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


