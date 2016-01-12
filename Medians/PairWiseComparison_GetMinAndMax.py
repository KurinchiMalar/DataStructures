__author__ = 'kurnagar'

import sys

# Time Complexity : O(n)

# Worst Case number of comparisons : 2(n-1)   ....(n-1) for Ar[i] and Ar[i-1] comparisons, (n-1) comparing Ar[i] with min/max
# Space Complexity : O(1)

def get_MinMax_pairwise_comparison(Ar):

    min_elem = sys.maxint
    max_elem = -sys.maxint-1

    for i in range(1,len(Ar)):

        if Ar[i] > Ar[i-1]:
            max_elem = max(max_elem,Ar[i])

        else:
            min_elem = min(min_elem,Ar[i-1])

    return min_elem,max_elem  # automatically tuple is created

Ar = [2, 1, 5, 234, 3, 44, 7, 6, 4, 5, 9, 11, 12, 14, 13]
min , max =  get_MinMax_pairwise_comparison(Ar) # tuple unpacking

print ""+str(min)+" "+str(max)


