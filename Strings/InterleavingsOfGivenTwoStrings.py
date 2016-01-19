'''
Given two strings str1 and str2, write a function that prints all interleavings of the given two strings

All Chars are different.

eg) str1 = "AB"   str2 = "CD"

The possible interleavings are

ABCD  ACBD  ACDB CABD CADB CDAB.

An interleaved string preserves the order of characters in individual strings.
A comes before B
C comes before D
'''

# Time Complexity : O(m! * n!). This is the total number of inter-leavings for the 2 strings.
def get_interleaves(str1,str2):

    perms = []
    if len(str1)+len(str2) == 1:  # single char
        return [str1 or str2]

    # If some characters of str1 are left to be included, then
    # include the first character from the remaining characters
    # and recur for rest

    if str1:  # str1 is not null
        for item in get_interleaves(str1[1:],str2): # fix str[0] and combine (str[1:] , str2 )
            perms.append(str1[0]+str(item))   # finally append with fixed char.

    # If some characters of str2 are left to be included, then
    # include the first character from the remaining characters
    # and recur for rest
    if str2:
        for item in get_interleaves(str1,str2[1:]):
            perms.append(str2[0]+str(item))

    return perms



def get_interleave_anotherway(str1,str2,soFar):

    if (str1 == None or len(str1) == 0) and (str2 == None or len(str2) == 0):
        return

    if str1 == None or len(str1) == 0:

        print "" + soFar + str2
        return

    if str2 == None or len(str2) == 0:

        print "" + soFar + str1
        return

    get_interleave_anotherway(str1[1:],str2,soFar+str1[0])
    get_interleave_anotherway(str1,str2[1:],soFar+str2[0])


str1 = "AB"
str2 = "CD"
#print ""+str(get_interleaves(list(str1),list(str2)))

get_interleave_anotherway(str1,str2,"")

