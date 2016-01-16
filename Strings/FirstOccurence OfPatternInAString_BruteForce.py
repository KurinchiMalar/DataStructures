
'''
STRING MATCHING ALGORITHMS

Find  the first occurence of a pattern P of len m in  a text T of len n.

'''

# BruteForce
'''
For a Pattern P of len m, in a Text T of length n.... for every elem in input we will have to make n - m + 1 comparisons.

C++ - strstr() functionality
'''
# Time Complexity : O(m * (n-m+1)) = O(n*m)

def find_occurence_of_pattern_in_string(inputstring,pattern):

    pat_index = 0

    n = len(inputstring)
    m = len(pattern)
    i = 0 # iterator for inputstring
    j = 0 # iterator for pattern
    while i < n-m+1: # number of comparisons. For every elem in input string.
        print "--------------------"
        print "i:"+str(i)
        tempi = i

        while tempi < n and j < m and inputstring[tempi] == pattern[j]:
            print "    Comparing :"+str(inputstring[tempi])+"and "+str(pattern[j])
            tempi = tempi + 1
            j = j + 1

        if j == m:
            print inputstring[i]
            return i

        i = i + 1
    return -1

inputstring = "hellohai"
pattern = "ll"
print "first occurence at index:"+str(find_occurence_of_pattern_in_string(inputstring,pattern))

