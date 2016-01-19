'''
Longest common substring of "GeeksforGeeks" and "GeeksQuiz" is "Geeks" of length 5.
'''
import sys
'''
    Algorithm : construct lcs matrix...fill all entries 0 to m+1 and 0 to n+1 to 0.

                if two chars in input equal ==> diagonalvalue + 1

                thats all....if not equal ...let it be zero...do nothing

'''
# Time Complexity : O(m*n)
# Space Complexity : O(m*n)

def get_longest_common_substring(s1,s2):

    i = 0
    j = 0
    m = len(s1)
    n = len(s2)

    lcs = [[0]*(n+1) for x in range(m+1)]

    longest = -1
    result = set()

    for i in range(0,m):
        for j in range(0,n):

            if s1[i] == s2[j]:

                lcs[i+1][j+1] = 1 + lcs[i][j]   # Upto now longest will be the previous diagonal element.

                if longest < lcs[i+1][j+1]:

                    result = set()
                    longest = lcs[i+1][j+1]

                    result.add("".join(s1[i-longest+1 : i+1]))

                elif longest == lcs[i+1][j+1]: # equal ==> longest substrings of equal length

                    result.add("".join(s1[i-longest+1 : i+1]))
    #print lcs
    return longest,result

def get_smallest_common_substring(s1,s2):

    i = 0
    j = 0
    m = len(s1)
    n = len(s2)

    lcs = [[0]*(n+1) for x in range(m+1)]

    smallest = sys.maxint
    result = set()

    for i in range(0,m):
        for j in range(0,n):

            if s1[i] == s2[j]:

                lcs[i+1][j+1] = 1 + lcs[i][j]   # Upto now longest will be the previous diagonal element.

                if smallest > lcs[i+1][j+1]:

                    result = set()
                    smallest = lcs[i+1][j+1]

                    result.add("".join(s1[i-smallest+1 : i+1]))

                elif smallest == lcs[i+1][j+1]: # equal ==> longest substrings of equal length

                    result.add("".join(s1[i-smallest+1 : i+1]))
    #print lcs
    return smallest,result

s1 = "banana"
s2 = "ana"

s1 = "ababc"
s2 = "abcdaba"

#s1 = "ababcbcbaaabbdef"
#s2 = "ababcbcbaaabbdefggggg"

print "s1: "+str(s1)+"   s2: "+str(s2)
length_of_longest_substring,result = get_longest_common_substring(list(s1),list(s2))

print "Length : "+str(length_of_longest_substring)
print "Longest Common Substring is :"+str(result)


length_of_smallest_substring,result = get_smallest_common_substring(list(s1),list(s2))

print "Length : "+str(length_of_smallest_substring)
print "Smallest Common Substring is :"+str(result)


def sameproblem_just_diff_logic_iandj(s1,s2):

    m = len(s1)
    n = len(s2)
    lcs = [[0]*(n+1) for x in range(0,m+1)]
    longest = -1
    result = set()

    for i in range(0,m+1):
        for j in range(0,n+1):

            if i == 0 or j == 0:
                lcs[i][j] = 0

            elif s1[i-1] == s2[j-1]:
                lcs[i][j] = 1 + lcs[i-1][j-1]
                if longest < lcs[i][j]:
                    longest = lcs[i][j]
                    result = set()
                    result.add("".join(s1[i-longest:i]))
                elif longest == lcs[i][j]:
                    result.add("".join(s1[i-longest:i]))
    print lcs
    return longest,result
