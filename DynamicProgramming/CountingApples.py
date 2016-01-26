'''
    Given a matrix with n rows and m columns. (m*n)

    In each cell there are a number of apples. WE start from the upper-left corner of the matrix. We can go down or right one cell.

    Finally we need to arrive at the bottom - right corner.

    Find the maximum number of apples that we can collect.
'''
'''
    Clue:

        We can come to a cell in two ways.
            1) from left (if it is not the leftmost column)
            2) from top ( if it is not the topmost row)

            So for the two exceptions precalculate and for the remaining, T[i][j] = max(T[i-1][j],T[i][j-1])
'''
# Time Complexity : O(m * n)
# Space Complexity : O(m * n)
def find_max_number_apples_that_we_can_collect_down_right(Apples,n,m):

    T = [[0 for x in range(m)] for x in range(n)]

    T[0][0] = Apples[0][0]
    #print T

    for i in range(1,n): # prefilling first column.
        T[i][0] = Apples[i][0] + T[i-1][0]
    #print T

    for j in range(1,m):  # prefilling first row
        T[0][j] = Apples[0][j] + T[0][j-1]

    print "------Prefilled and ready----------"
    for list in T:
        print list

    for i in range(1,n):
        for j in range(1,m):
            T[i][j] = max(T[i-1][j],T[i][j-1]) # max(top , left)
    print "------RESULT----------"
    for list in T:
        print list


    return T[n-1][m-1]

Apples = [ [5, 24], [15, 25], [27, 40], [50, 60] ]
print "Maximum Number of Apples that can be collected down+right: "+str(find_max_number_apples_that_we_can_collect_down_right(Apples,4,2))


'''
    Given a matrix with n rows and m columns. (m*n)

    In each cell there are a number of apples.

        WE start from the upper-left corner of the matrix. We can go down or right one cell.

        We can also go diagonal.

    Finally we need to arrive at the bottom - right corner.

    Find the maximum number of apples that we can collect.
'''

def find_max_number_apples_that_we_can_collect_down_right_diagonal(Apples,n,m):

    T = [[0 for x in range(m)]for x in range(n)]

    T[0][0] = Apples[0][0]

    for i in range(0,n):
        T[i][0] = Apples[i][0] + T[i-1][0]

    for j in range(0,m):
        T[0][j] = Apples[0][j] + T[0][j-1]
    print "------Prefilled and ready----------"
    for list in T:
        print list

    for i in range(1,n):
        for j in range(1,m):
            T[i][j] = max(T[i-1][j],T[i][j-1],T[i-1][j-1])  # max of diagonal also
    print "------RESULT----------"
    for list in T:
        print list
    return T[n-1][m-1]

Apples = [ [5, 24], [15, 25], [27, 40], [50, 60] ]
print "Maximum Number of Apples that can be collected down+right+diagonal: "+str(find_max_number_apples_that_we_can_collect_down_right_diagonal(Apples,4,2))