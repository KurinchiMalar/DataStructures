'''
Given coins of certain denominations and a total, how many minimum coins would you need to make this total.

https://www.youtube.com/watch?v=Y0ZqKpToTic&feature=youtu.be&t=390
'''

# Time Complexity : O(total * len(coins))
# Space Complexity : O(total * len(coins))

def minimum_coins_required_to_get_total(coins,total):

    n = len(coins)

    T = [[0]*(total+1) for x in range(len(coins))]

    for k in range(total+1):
        T[0][k] = k

    #print T
    for i in range(1,n):
        for j in range(1,total+1):

            if coins[i] > j:
                T[i][j] = T[i-1][j]
            else:
                T[i][j] = min(T[i-1][j] , 1+T[i][j-coins[i]])   # min of previously calculated, and same row move coins[i] steps back


    print T
    i = n-1
    j = total
    result = []

    while i >= 0 and j >= 0:
        if T[i][j] == 0:
            break

        if T[i-1][j] > T[i][j]:   # only if greater append to result.
            result.append(coins[i])
            j = j - coins[i]
        else:           # keep moving up.
            i = i - 1

    return T[n-1][total],result

    print

coins = [1,5,6,8]
total = 11
min_no_coins,result =minimum_coins_required_to_get_total(coins,total)

print "Minimum number of coins required : "+str(min_no_coins)
print "The coins are:"+str(result)+" totals to :"+str(total)