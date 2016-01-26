
'''
Given a string, find the longest substring which is palindrome.

For example, if the given string is "forgeeksskeegfor", the output should be "geeksskeeg"

for agbdba

[1, 0, 0, 0, 0, 0]
[0, 1, 0, 0, 0, 0]
[0, 0, 1, 0, 1, 0]
[0, 0, 0, 1, 0, 0]
[0, 0, 0, 0, 1, 0]
[0, 0, 0, 0, 0, 1]
'''
# Time Complexity : O(n*n)
# Space Complexity : O(n*n)
def length_longest_palindromic_substring(Ar):

    n = len(Ar)
    T = [[0]*n for x in range(n)]

    palindrome_start= 0
    max_len = 1
    #print T
    level = 1
    i = 0
    j = 0
    while i < n and j < n:
        T[i][j] = 1
        i = i + 1
        j = j + 1

    level = 2
    for i in range(1,n):
        if Ar[i] == Ar[i-1]:
            T[i-1][i] = 1
            palindrome_start = i
            print"start: "+Ar[palindrome_start]
            max_len = 2
        else:
            T[i-1][i] = 0

    level = 3
    while level <= n:

        for i in range(0,n-level+1):
            j = i+level-1

            if Ar[i] == Ar[j] and T[i+1][j-1] == 1:
                T[i][j] = 1
                if level > max_len:
                    #print"start: "+Ar[palindrome_start] It expands from inside.... from 2 char, 3 char,...goes towards n char... so palindrome_start will be moving towards start.
                    palindrome_start = i
                    max_len = level

        level = level + 1



    for list in T:
        print list

    print palindrome_start
    #print max_len

    return max_len,Ar[palindrome_start:palindrome_start+max_len]


Ar = "agbdba"
Ar = "forgeeksskeegfor"
Ar = "banana"
max_len,result = length_longest_palindromic_substring(list(Ar))
print "length of longest palindromic substring: "+str(max_len)
print "longest palindromic substring: "+str(result)



