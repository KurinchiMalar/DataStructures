'''
Magic Index: A magic index in an array A[1....n-1] is defined to be an index such that A[i] = i. Given a sorted array of
            distinct integers, write a method to find a magic index, if one exists in array A.
'''

# Time Complexity : O(log n)
def magic_index(Ar,first,last):

    if first == last:
        if Ar[first] == first:
            return first

    if last == first + 1:
        if Ar[last] == last:
            return last
    elif Ar[first] == first:
        return first

    middle = (first + last) / 2

    if Ar[middle] == middle:
        return middle

    if Ar[middle] < middle:
        return magic_index(Ar,first,middle-1)

    return magic_index(Ar,middle+1,last)

Ar = [-10,-5,2,2,2,3,4,7,9,12,13]
print(""+str(magic_index(Ar,0,len(Ar)-1)))