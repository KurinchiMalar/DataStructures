'''
    Given a matrix with 0's and 1's , give an algorithm for finding the maximum size square sub-matrix with all 1s.

    For example, consider the binary matrix below.
                0 1 1 0 1
                1 1 0 1 0
                0 1 1 1 0
                1 1 1 1 0
                1 1 1 1 1
                0 0 0 0 0
    The maximum square sub-matrix with all set bits is
                1 1 1
                1 1 1
                1 1 1
'''
'''
Algorithm:

      If you see a 1 in input matrix put 1+ min of all neighbours, in T[i][j]
      else put 0 in T[i][j]

      T[i][j] = 1 means, there exists a 1*1 sub-matrix with all 1s until now.
        = 2 means, there exists a 2*2 sub-matrix with all 1s until now
'''

# Time Complexity : O(m*n)
# Space Complexity : O(m*n)
def get_size_of_max_sub_matrix_with_all_1s(Ar,n,m):

    T = [[0]*(m+1) for x in range(n+1)]
    #for list in T:
    #   print list
    '''
    for i in range(0,n+1):
        T[i][0] = 0
    for j in range(0,m+1):
        T[0][j] = 0
    '''
    for i in range(1,n+1):
        for j in range(1,m+1):
            if Ar[i-1][j-1] == 1:
                T[i][j] = 1 + min(T[i-1][j],T[i-1][j-1],T[i][j-1])

    for list in T:
       print list

    return T[n][m]

Ar = [[0,0,1,1,1],[1,0,1,1,1],[0,1,1,1,1],[1,0,1,1,1]]
print "Maximum size square submatrix with all 1's: "+str(get_size_of_max_sub_matrix_with_all_1s(Ar,4,5))