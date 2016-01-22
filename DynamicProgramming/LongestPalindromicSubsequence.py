__author__ = 'kurnagar'
'''

'''

# Time Complexity : O(n*n)
# Space Complexity : O(n*n)

def get_length_of_longest_palindromic_subsequence(Ar):

    n = len(Ar)

    lcps = [[0] * n for x in range(len(Ar))]

    lvl = 1

    for i in range(0,n):

        lcps[i][i] = 1

    lvl = 2
    while lvl <= n:
        print "---------------------------"
        for i in range(0, n-lvl+1):

            j = i + lvl - 1

            print "lvl :"+str(lvl)+" i = "+str(i)+" j = "+str(j)
            if Ar[i] == Ar[j]:
                lcps[i][j] = lcps[i+1][j-1] + 2
            else:
                lcps[i][j] = max(lcps[i][j-1],lcps[i+1][j])
            j = j + 1
        lvl = lvl + 1

    return lcps[0][n-1]

mystr = "agbdba"
print "Length of longest palindromic subseq : "+str(get_length_of_longest_palindromic_subsequence(list(mystr)))

