from Sorting.MergeSort import mergesort
# Numbers are in range 1 to n. N-1 elements are repeating thrice and remaining element repeated twice.
# Find the element that repeated twice.
'''
   x x x y y z z z  -  Input - A

   x y z  -  1 to n - B

   A ^ B = y

   because (x ^ x ^ x) ^ x = 0

            (y ^ y) ^ y = y

'''
def find_twice_repeating_among_thrice_repeated_xorlogic(Ar,n):

    xor = 0

    for i in range(0,len(Ar)):

        xor = xor ^ Ar[i]

    for i in range(1,n+1):

        xor = xor ^ i

    return xor

Ar = [4,5,2,4,3,1,1,2,1,3,2,5,3,5]

#tempAr =  mergesort(Ar)
#print tempAr

print ""+str(find_twice_repeating_among_thrice_repeated_xorlogic(Ar,5))