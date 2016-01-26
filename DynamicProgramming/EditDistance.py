'''
    Given two strings A of length m and B of length n, transform A into B with a minimum number of operations of the following
    types:
            delete a character from A
            insert a character into A
            replace some character in A into a new character.
    The minimal number of such operations required to transform A into B is called the edit distance between A and B.
'''

# Time Complexity : O(m * n)
# Space Complexity : O(m * n)
def calculate_edit_distance(A,B):

    m = len(A)
    n = len(B)

    T = [[0]*(m+1) for x in range(n+1)]

    i = 0
    j = 0
    while i <= n:
        T[i][0] = i
        i = i + 1

    while j <= m:
        T[0][j] = j
        j = j + 1

    #print T
    for i in range(1,n+1):
        for j in range(1,m+1):

            if B[i-1] == A[j-1]:
                T[i][j] = T[i-1][j-1]
            else:
                T[i][j] = 1 + min(T[i-1][j-1],T[i][j-1],T[i-1][j])

    print T

    i = n
    j = m

    operations = ["delete","insert","replace"]

    result = {k:[] for k in operations}

    while i > 0 and j > 0:

        if T[i][j] == 0:
            break

        if B[i-1] == A[j-1]: # Move diagonal no operation
            i = i - 1
            j = j - 1
        else:
            if T[i-1][j-1] < T[i][j-1] and T[i-1][j-1] < T[i-1][j]: # diagonal is less than both up and side. --> Replace
                temp = ""+str(A[j-1])+"-->"+str(B[i-1])
                util = result['replace']
                util.append(temp)
                result['replace'] = util
                i = i - 1
                j = j - 1

            elif T[i][j-1] < T[i-1][j-1] and T[i][j-1] < T[i-1][j]: # T[i][j-1] is the smallest --> delete in A
                util = result['delete']
                util.append(A[j-1])
                result['delete'] = util
                j = j - 1
            else:  # up is small --> insert   T[i-1][j] is the smallest  --> insert in A.
                util = result['insert']
                util.insert(0,B[i-1])
                result['insert'] = util
                i = i - 1

                #print "i = "+str(i)+"j = "+str(j)

    return T[n][m],result

A = "sunday"
B = "saturday"
minoperations,operations=calculate_edit_distance(list(A),list(B))
print "Minimum number of operations to convert "+str(A)+" to "+str(B)+" is : "+str(minoperations)
print "The operations are : "+str(operations)