
'''
[1, 1, 1, 1, 3, 5]
[0, 1, 1, 1, 3, 3]
[0, 0, 1, 1, 3, 3]
[0, 0, 0, 1, 1, 1]
[0, 0, 0, 0, 1, 1]
[0, 0, 0, 0, 0, 1]
'''

def get_len_longest_pali_subseq(Ar):

    n = len(Ar)
    level = 0
    T = [[0] * n for x in range(n)]

    level = 1
    i = 0
    j = 0
    while i < n and j < n:
        T[i][j] = 1 # unipalindrome strings
        i = i + 1
        j = j + 1

    #print T

    level = 2
    while level <= n:
        for i in range(0,n-level+1):
            j = i + level - 1
            if Ar[i] == Ar[j]:
                T[i][j] = 2 + T[i+1][j-1]
            else:
                T[i][j] = max(T[i][j-1],T[i+1][j])

        level = level + 1
    for list in T:
        print list


    i = 0
    j = n-1
    result = [0]*T[0][n-1]
    start = 0
    end = T[0][n-1]-1
    while i < n and j >= 0:

        if T[i][j] == 0:
            break

        if T[i+1][j] == T[i][j-1]:

            if Ar[i] == Ar[j]:
                result[start] = Ar[i]
                result[end] = Ar[i]
                start =start+1
                end = end - 1
            i = i + 1
            j = j - 1

        else:
            if T[i+1][j] > T[i][j-1]:
                i = i + 1
            else:
                j = j - 1

    print result

    return T[0][n-1]

Ar = "banana"
get_len_longest_pali_subseq(Ar)

