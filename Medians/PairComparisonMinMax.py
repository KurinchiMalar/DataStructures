
# Time Complexity : O(n)
# Space Complexity : O(1)
'''
Number of Comparisons:

        n is even : (3n/2) - 2

        n is odd : (3n/2) - 3/2

'''

def get_MinMax_using_paircomparison(Ar):

    start = -1

    if len(Ar)% 2 == 0 : # even
        min_elem = Ar[0]
        max_elem = Ar[1]
        start = 2
    else: # odd
        min_elem = max_elem = Ar[0]
        start = 1

    for i in range(start,len(Ar),2):
        #print ""+str(i)
        first = Ar[i]
        second = Ar[i+1]

        if first < second:
            if first < min_elem:
                min_elem = first
            if second > max_elem:
                max_elem = second
        else:
            if second < min_elem:
                min_elem = second
            if first > max_elem:
                max_elem = first

    return min_elem,max_elem

Ar = [2,67,1,5,3,7,8,234,55,72,9]
Ar = [2,3,1,5,6,7]

min_elem , max_elem = get_MinMax_using_paircomparison(Ar)

print "min: "+str(min_elem)+"max: "+str(max_elem)