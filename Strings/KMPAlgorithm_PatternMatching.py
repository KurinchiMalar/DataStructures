'''

Constructing LPS Array:

https://www.youtube.com/watch?v=t4xUA-aHzy8

KMP Algorithm:

https://www.youtube.com/watch?v=t4xUA-aHzy8
'''

# Time Complexity : O(n)
# Space Complexity : O(m) --> where m is the length of the pattern.

def construct_lps_for_pattern(pattern):

    i = 1
    j = 0
    lps = [-1]*len(pattern)
    lps[0] = 0

    # Clue --> At any instant j should point the index of longest prefix which is also a suffix
    while i < len(pattern):

        if pattern[i] == pattern[j]:

            lps[i] = j + 1   # j = 2 ===> 3 chars have matched... so put in Ar[i] = 3
            j = j + 1
            i = i + 1

        else:

            if j != 0:

                j = lps[j-1]  # move j to penultimate longest. lps[j-1] indicates longest prefix which is also suffix from (0 to j-1)

            else: # j == 0

                lps[i] = 0  # no longest prefix which is also a suffix is found for this substring (0 to i)
                i = i + 1
    return lps


def kmp_pattern_match(inputstring,pattern,lps):


    i = 0
    j = 0
    result = []

    if len(pattern) <= 0:
        return -1

    while i < len(inputstring):

        #print "i:"+str(i)

        if inputstring[i] == pattern[j]:

            i = i + 1
            j = j + 1

            if j == len(pattern): # full pattern matched :)

                print "Match found at :"+str(i-j)

                result.append(i-j)

                j = lps[j-1]   # we dont want to stop at a find. find all the occurences.

        else:

            if j != 0:  # this means some portion has matched but suddenly failed... so this is not the appropriate one.

                # so move j to last successfully matched :)
                j = lps[j-1]

            else: # if j is 0, just move input pointer, lets for luck on other places.

                i = i + 1

    return result

pattern = "ana"
inputstring = "banana"
#inputstring = "abcdabcyabcdabcxabxabcdabcdabcy"
#pattern = "abcdabcy"

lps = construct_lps_for_pattern(list(pattern))
print "lps:"+str(lps)
print "result:"+str(kmp_pattern_match(inputstring,pattern,lps))


