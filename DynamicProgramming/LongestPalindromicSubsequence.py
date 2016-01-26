__author__ = 'kurnagar'
'''

'''

# Time Complexity : O(n*n)
# Space Complexity : O(n*n)

'''
Algorithm:

1) Fill all diagonal to 1. lcps[i][i] = 1  # meaning single letter palindrome (lvl = 1)

2) if Ar[i] == Ar[j]:
        lcps[i][j] = lcps[i+1][j-1] + 2     # 2 means, say i corresponds to a , then j also will be a .. so we have a   a
    else:
        lcps[i][j] = max(lcps[i][j-1],lcps[i+1][j])   # take the max

3)  lcps[0][n-1] is the answer.

'''

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

        lvl = lvl + 1

    max_pali_seq_len = lcps[0][n-1]
    result = [0]* max_pali_seq_len
    i = 0
    j = n-1

    start = 0
    end = max_pali_seq_len  - 1
    for list in lcps:
        print list
    while i < n and  j >= 0:

        if lcps[i][j] == 0:
            break

        if lcps[i+1][j] == lcps[i][j-1]: # Move diagonal
            #if lcps[i+1][j] != lcps[i][j]: # if not equal then it should have a +2 from diagonal, so append to result and move diagonal..
            if Ar[i] == Ar[j]:
                result[start] = Ar[i]
                result[end] = Ar[j]
                start = start + 1
                end = end - 1
            i = i + 1
            j = j - 1
        else:
            if lcps[i+1][j] > lcps[i][j-1]:
                i = i + 1
            else:
                j = j -1

    return lcps[0][n-1],result

mystr = "agbdba"
length,result = get_length_of_longest_palindromic_subsequence(list(mystr))
print "Longest palindromic subseq : "+str(result)
print "Length of longest palindromic subseq : "+str(length)

