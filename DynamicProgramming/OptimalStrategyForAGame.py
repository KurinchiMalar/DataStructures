'''
Optimal Strategy for  a Game:

    Two player game. Consider a row of n coins of values v1,v2,...vn where n is even. In each turn, a player selects either the
    first or last coin from the row, removes it from the row permanently , and receives the value of the coin.

    Determine the maximum possible amount of money we can definitely win if we move first.

'''

# Time Complexity : O(n*n)
# Space Complexity : O(n*n)

def optimal_game_strategy_moves(Ar):

    n = len(Ar)
    T = [[{"first":-1,"second":-1} for y in range(n)] for x in range(n)]

    #print T

    i = 0
    j = 0
    level = 1
    while i < n and j < n: # when there is only one coin, when the first player picks it up, the second player has nothing so 0.
        T[i][j]["first"] = Ar[i]
        T[i][j]["second"] = 0

        i = i + 1
        j = j + 1

    #print T

    level = 2

    while level <= n:

        for i in range(0,n-level+1):
            j = i + level -1

            if (Ar[i] + T[i+1][j]["second"]) > (Ar[j] + T[i][j-1]["second"]):  # trying Ar[i] as first  comparing with Ar[j] as first.

                T[i][j]["first"] = Ar[i] + T[i+1][j]["second"]
                T[i][j]["second"] = T[i+1][j]["first"]

            else:
                T[i][j]["first"] = Ar[j] + T[i][j-1]["second"]
                T[i][j]["second"] = T[i][j-1]["first"]

        level = level+1

    #for list in T:
        #print list

    return T[0][n-1]

Ar = [3,9,1,2]
result = optimal_game_strategy_moves(Ar)

print "Optimal score for first player:"+str(result["first"])
print "Optimal score for second player:"+str(result["second"])


'''

UNDERSTANDING:

            # For Ar[i] + after position's second, Ar[j]+before positions'second
            # As a player I am guessing, on taking Ar[i] first and corresponding second (precalculated) I get max (or)
            #                               taking Ar[j] first and corresponding second  I get max?


level = 2 (0 1)
             take for instance there is 3,9
                Picking 3 first --> 3 + T[1][1]second ==> will be my ultimate first. if this is big
                Picking 9 first --> 9 + T[0][0]second ==> will be my ultimate first. if this is big.

level = 2

    0 1
		3 + T[1][1]second
		9 + T[0][0]second
    1 2
		9 + T[2][2]
		1 + T[1][1]
    2 3
		1 + T[3][3]
		2 + T[2][2]

level = 3

    0 2
		3 + T[1][2]
		1 + T[0][1]

    1 3
		9 + T[2][3]
		2 + T[0][2]

level = 4

    0 3
		3 + T[1][3]
		2 + T[0][2]
'''
