'''
    Given two strings S and T, give an algorithm to find the number of times S appears in T. It's not compulsory that all the
    characters of S should appear contiguous to T.

    eg) S = ab and T = abadcb   ---> ab is occuring 2 times in abadcb.
'''
'''
Algorithm:

    if dest[i-1] == source[j-1]:
        T[i][j] = T[i][j-1] + T[i-1][j]
    else:
        T[i][j] = T[i][j-1]


    If same --> a b a
            a
            b     x y


   x indicates how many times ab occurs in ab substring of aba.

   y indicates how many times ab occurs in aba


   Logic --> if equal --> left + top ( how many times a has occured till now(top) + how many times ab has appeared (left) )
              if not equal --> copy the left alone.
'''
# Time Complexity : O(n1 * n2)
# Space Complexity : O(n1 * n2)
def count_number_of_times_dest_in_source(source,dest):

    n1 = len(source)
    n2 = len(dest)

    T= [[0]*(n1+1) for x in range(n2+1)]

    #T[0][0] = 1 # since searching \0 in \0 is 1
    i = 1 # starting from 1 for the above reason
    j = 0
    #print T
    while i <= n2: # dest
        T[i][0] = 0  # if source string is empty, then nothing to check.
        i = i + 1

    while j <= n1: # source
        T[0][j] = 1  # /0 in dest , will be available in non empty source.
        j = j + 1
    #print T

    for i in range(1,n2+1):
        for j in range(1,n1+1):

            if dest[i-1] == source[j-1]:
                T[i][j] = T[i][j-1] + T[i-1][j]
            else:
                T[i][j] = T[i][j-1]

    print T
    return T[n2][n1]

#source = "geeksforgeeks"
#dest = "geek"
source = "abadcb"
dest = "ab"
source = "ababab"
dest ="ab"
#print source.count(dest)
print "Number of times : "+str(dest)+" appears in : "+str(source)+" is :"+str(count_number_of_times_dest_in_source(list(source),list(dest)))