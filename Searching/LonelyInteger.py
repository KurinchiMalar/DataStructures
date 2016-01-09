'''
    Given an array of 2n+1 elements, of which all elements are repeating twice

    One element occurs only once. Find the lonely element.
'''

def find_lonely_element(Ar):

    xor = 0
    for i in range(0,len(Ar)):
        xor = xor ^ Ar[i]
    return xor

Ar = [7,3,6,3,6,7,8]

print ""+str(find_lonely_element(Ar))