__author__ = 'kurnagar'

'''
    Given a string check if it is a palindrome or not
'''

# Time Complexity : O(n)
# Space Complexity : O(1)

def check_palindrome(Ar):

    low = 0
    high = len(Ar)-1

    while low <= high:

        if Ar[low] != Ar[high]:

            return False

        low = low + 1
        high = high - 1
    return True

mystr = "madama"
print ""+str(check_palindrome(list(mystr)))

