'''
Given some matrices, in what order you would multiply them to minimize cost of multiplication.

Also called Matrix Paranthesization.

http://www.personal.kent.edu/~rmuhamma/Algorithms/MyAlgorithms/Dynamic/chainMatrixMult.htm

https://www.youtube.com/watch?v=vgLJZMUfnsU
'''
'''

Complexity Analysis

# Space Complexity : O(n*n)

# Time Complexity : O(n*n*n)

    As far as the time complexity is concern,
        a simple inspection of the for-loop(s) structures gives us a running time of the procedure.

        Since, the three for-loops are nested three deep, and each one of them iterates at most n times
'''

def optimal_cost_matrix_chain_multiplication(Ar):

    n = len(Ar)

    T = [[0]*n for x in range(n)]

    i = 0
    j = 0

    level = 1
    while i < n and j < n:
        T[i][j] = 0
        i = i+1
        j = j+1
    #print T
    level = 2
    while level < n:

        for i in range(0,n-level):

            j = i + level

            T[i][j] = 100000

            for k in range(i+1,j):

                cur_cal = T[i][k] + T[k][j] + Ar[i]*Ar[k]*Ar[j]

                if T[i][j] > cur_cal:
                    T[i][j] = cur_cal

        level = level+1


    print T
    return T[0][n-1]


Ar = [2,3,6,4,5]
print "Optimal cost for multiplication:"+str(optimal_cost_matrix_chain_multiplication(Ar))
'''
TRACE FOR UNDERSTANDING:

temp: [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
------------------------
level: 2
i= 0 j= 2
	k= 1
       temp[0][1]: 0 temp[1][2]: 0
       2 * 3 * 6
       cur_calc: 36
        temp: [[0, 0, 36, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
i= 1 j= 3
	k= 2
       temp[1][2]: 0 temp[2][3]: 0
       3 * 6 * 4
       cur_calc: 72
        temp: [[0, 0, 36, 0, 0], [0, 0, 0, 72, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
i= 2 j= 4
	k= 3
       temp[2][3]: 0 temp[3][4]: 0
       6 * 4 * 5
       cur_calc: 120
        temp: [[0, 0, 36, 0, 0], [0, 0, 0, 72, 0], [0, 0, 0, 0, 120], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
------------------------
level: 3
i= 0 j= 3
	k= 1
       temp[0][1]: 0 temp[1][3]: 72
       2 * 3 * 4
       cur_calc: 96
        temp: [[0, 0, 36, 96, 0], [0, 0, 0, 72, 0], [0, 0, 0, 0, 120], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
	k= 2
       temp[0][2]: 36 temp[2][3]: 0
       2 * 6 * 4
       cur_calc: 84
        temp: [[0, 0, 36, 84, 0], [0, 0, 0, 72, 0], [0, 0, 0, 0, 120], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
i= 1 j= 4
	k= 2
       temp[1][2]: 0 temp[2][4]: 120
       3 * 6 * 5
       cur_calc: 210
        temp: [[0, 0, 36, 84, 0], [0, 0, 0, 72, 210], [0, 0, 0, 0, 120], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
	k= 3
       temp[1][3]: 72 temp[3][4]: 0
       3 * 4 * 5
       cur_calc: 132
        temp: [[0, 0, 36, 84, 0], [0, 0, 0, 72, 132], [0, 0, 0, 0, 120], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
------------------------
level: 4
i= 0 j= 4
	k= 1
       temp[0][1]: 0 temp[1][4]: 132
       2 * 3 * 5
       cur_calc: 162
        temp: [[0, 0, 36, 84, 162], [0, 0, 0, 72, 132], [0, 0, 0, 0, 120], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
	k= 2
       temp[0][2]: 36 temp[2][4]: 120
       2 * 6 * 5
       cur_calc: 216
        temp: [[0, 0, 36, 84, 162], [0, 0, 0, 72, 132], [0, 0, 0, 0, 120], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
	k= 3
       temp[0][3]: 84 temp[3][4]: 0
       2 * 4 * 5
       cur_calc: 124
        temp: [[0, 0, 36, 84, 124], [0, 0, 0, 72, 132], [0, 0, 0, 0, 120], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

temp[0][4]
Optimal Cost:124
'''
