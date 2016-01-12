__author__ = 'kurnagar'

import sys

# Time Complexity : O(n)
# Worst Case Comparisons : n-1

# Space Complexity : O(1)
def find_largest_element_in_array(Ar):
    max = -sys.maxint - 1  # pythonic way of assigning most minimum value
    #print type(max)
    #max = -sys.maxint - 2
    #print type(max)

    for i in range(0,len(Ar)):
        if Ar[i] > max:
            max = Ar[i]

    return max


Ar = [2, 1, 5, 234, 3, 44, 7, 6, 4, 5, 9, 11, 12, 14, 13]
print ""+str(find_largest_element_in_array(Ar))