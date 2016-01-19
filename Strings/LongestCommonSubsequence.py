
'''
LCS for input Sequences "ABCDGH" and "AEDFHR" is "ADH" of length 3.
LCS for input Sequences "AGGTAB" and "GXTXAYB" is "GTAB" of length 4.
'''

# Time Complexity : O(m*n)
# Space Complexity : O(m*n)

def get_longest_common_subsequence(s1,s2):

    m = len(s1)
    n = len(s2)

    lcss = [[0]*(n+1) for x in range(m+1)]

    i = 0
    j = 0

    for i in range(0,m):
        for j in range(0,n):

            if s1[i] == s2[j]:
                lcss[i+1][j+1] = 1 + lcss[i][j]
            else:
                lcss[i+1][j+1] = max(lcss[i+1][j],lcss[i][j+1])
    print lcss

    longest = lcss[m][n]
    print "longest:"+str(longest)
    result = []

    i = m
    j = n

    while i > 0 and j > 0:

        if s1[i-1] == s2[j-1]:
            result.insert(0,s1[i-1])

            i = i-1
            j = j-1

        else:

            if lcss[i-1][j] > lcss[i][j-1]:

                i = i - 1
            else:

                j = j - 1

    print result





s1 = "acbcf"
s2 = "abcdaf"

get_longest_common_subsequence(s1,s2)




def sameproblem_just_diff_logic_iandj(s1,s2):

    m = len(s1)
    n = len(s2)

    lcss = [[0]*(n+1) for x in range(m+1)]

    i = 0
    j = 0

    for i in range(0,m+1):
        for j in range(0,n+1):

            if i == 0 or j == 0:
                lcss[i][j] = 0

            elif s1[i-1] == s2[j-1]:
                lcss[i][j] = 1 + lcss[i-1][j-1]
            else:
                lcss[i][j] = max(lcss[i][j-1],lcss[i-1][j])
    print lcss
