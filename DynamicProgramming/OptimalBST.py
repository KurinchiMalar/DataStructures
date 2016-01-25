'''

Optimal Binary Search Tree:

    Given a set of n sorted keys A[1...n] build the best bst for the elements of A,

    Also assume that each element is associated with frequency which indicates the number of times that particular item is
    searched in the bst. That means we need to construct a bst so that the total search time will be reduced.

    https://www.youtube.com/watch?v=hgA4xxlVvfQ
'''

'''
1) The time complexity of the solution is O(n^4).
    The time complexity can be easily reduced to O(n^3) by pre-calculating sum of frequencies instead of calling sum() again and again.

2) In the below solution, we have computed optimal cost only.
    The solutions can be easily modified to store the structure of BSTs also.
    We can create another auxiliary array of size n to store the structure of tree.
    All we need to do is, store the chosen root in the innermost loop.
'''

# Time Complexity : O(n*n*n*n)  # by precalculating frequencies we can reduce complexity to O(n*n*n)

# Space Complexity : O(n*n)

def get_sum_in_range(Ar):
    sum = 0
    for i in range(len(Ar)):
        sum += Ar[i]
    return sum

def find_minimum_cost(inputAr,freqAr):

    n = len(inputAr)

    T = [[100000]*n for x in range(n)]

    #print T
    i = 0
    j = 0
    level = 1
    root_dic = [[-1]*n for x in range(n)]
    while i < n and j < n:
        T[i][j] = freqAr[i]
        i = i + 1
        j = j + 1
    #print T
    level = 2
    while level <= n:
        #print "-------------------------level : "+str(level)
        for i in range(0,n-level+1):
            j = i+level-1

            sum = get_sum_in_range(freqAr[i:j+1])
            for k in range(i,j+1):  # k has to start from i and end at j.... must include both i and j...since we will consider i and j both as root
                #print "i: "+str(i)+" j: "+str(j)+" k: "+str(k)
                leftsum = 0
                rightsum = 0

                if k-1 < i:
                    leftsum = 0
                else:
                    leftsum = T[i][k-1]

                if k+1 > j:
                    rightsum = 0
                else:
                    rightsum = T[k+1][j]

                #print "sum : "+str(sum)+" leftsum: "+str(leftsum)+" rightsum: "+str(rightsum)
                final = sum + leftsum + rightsum

                if T[i][j] > final:
                    root_dic[i][j] = k
                    T[i][j] = final
        level = level + 1

    #print T
    print "Root dic:"+str(root_dic)
    return T[0][n-1]

inputAr = [10,12,16,21]
freqAr = [4,2,6,3]
print "Minimal cost for search: "+str(find_minimum_cost(inputAr,freqAr))
#print ""+str(get_sum_in_range(freqAr[1:3]))

'''
Understanding the algo:

inputAr = [10,12,16,21]

level 2 -->

10 12
	10 as root ---> sum + T[1][1] # index of 12
	12 as root ---> sum + T[0][0]  # index of 10

12 16
	12 as root --> sum + T[2][2]
	16 as root --> sum + T[1][1]

16  21
	16 as root ---> sum + T[3][3]
	21 as root ---> sum + T[2][2]
=================================================

level 3 --->

10 12 16
		10 as root ---> sum + T[1][2]  # index of 12 to index of 16
		12 as root ---> sum + T[0][0] + T[2][2]
		16 as root ---> sum + T[0][1]

12 16 21
		12 as root ---> sum + T[2][3]
		16 as root ---> sum + T[1][1]+T[3][3]
		21 as root ---> sum + T[1][2]
===================================================

level 4 --->

10 12 16 21

	10 as root ---> sum + T[1][3]
	12 as root ---> sum + T[0][0] + T[2][3]
	16 as root ---> sum + T[0][1] + T[3][3]
	21 as root ---> sum + T[0][2]
'''