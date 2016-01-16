'''
    Give an algorithm for reversing a string.
'''

# Time Complexity : O(n)
# Space Complexity : O(1) # ideally, but here in python string is immutable , so creating a list ...O(n)

def reverse_given_string(inputstring):
    start = 0
    end = len(inputstring) - 1

    mutablelist = list(inputstring)
    while start < end:
        mutablelist[start],mutablelist[end] = mutablelist[end],mutablelist[start]
        start = start+1
        end = end -1

    inputstring = "".join(mutablelist)
    return inputstring

'''
   reverse(hello)
 = reverse(ello) + h           # The recursive step
 = reverse(llo) + e + h
 = reverse(lo) + l + e + h
 = reverse(o) + l + l + e + h  # Base case
 = o + l + l + e + h
 = olleh
'''
def reverse_given_string_recursive(inputstring):
    if len(inputstring) <= 1:
        return inputstring

    return reverse_given_string(inputstring[1:]+inputstring[0])

inputstring = "kurinchimalar"
print ""+str(reverse_given_string(inputstring))

# Another Implementation
print "".join(inputstring[c] for c in xrange(len(inputstring)-1,-1,-1))

# Another Implementation

print inputstring[::-1]

# Another Implementation

print "".join(reversed(inputstring))
print "recursive solution: "+str(reverse_given_string_recursive(inputstring))
