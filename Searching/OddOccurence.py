# Find the number occuring odd number of times in an array ( just one number should occur odd times in input)

# Time Complexity - O(n)
# Space Complexity - O(1)

def get_number_occuring_odd_times(Ar):

    xor = 0

    for i in xrange(0,len(Ar)):
        xor = xor ^ Ar[i]

    return xor

Ar = [1,1,3,2,2,3,1,3,3]

print(""+str(get_number_occuring_odd_times(Ar)))