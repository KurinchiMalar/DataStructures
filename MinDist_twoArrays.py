'''Given two unsorted arrays, find two indices that are at minimum distance between them.'''


import sys


def mindiff(A,B):

    A = sorted(A)
    B = sorted(B)

    i = 0
    j = 0

    min_diff = sys.maxint
    result = []
    while i < len(A) and j < len(B):

        if abs(A[i]-B[j]) < min_diff:
            min_diff = abs(A[i]-B[j])
            result = []
            result.append(A[i])
            result.append(B[j])

        if i < j:
            i = i + 1
        else:
            j = j + 1

    print min_diff
    print result


A = [1000,101,6,8]
B = [90,100,50]


mindiff(A,B)

