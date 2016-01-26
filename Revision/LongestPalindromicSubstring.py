
def get_length_of_longest_palindromic_substring(Ar):

    n = len(Ar)
    T = [[0]*n for x in range(n)]

    palindrome_start = 0
    max_len = 1
    level = 1

    for i in range(0,n):
        T[i][i] = 1

    #print T

    level = 2
    i = 0
    j = 0
    for i in range(0,n-1):
        if Ar[i] == Ar[i+1]:
            T[i][i+1] = 1
            palindrome_start = i
            max_len = 2

    level = 3
    while level <= n:
        for i in range(0,n-level+1):
            j = i+level-1

            if Ar[i] == Ar[j] and T[i+1][j-1] == 1:
                T[i][j] = 1
                if level > max_len:
                    palindrome_start = i
                    max_len = level
        level = level + 1

    for list in T:
        print T
    print Ar[palindrome_start:palindrome_start+max_len]














Ar = "forgeeksskeegfor"
get_length_of_longest_palindromic_substring(list(Ar))