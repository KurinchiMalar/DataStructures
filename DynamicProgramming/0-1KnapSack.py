'''
Given a bag which can only take certain weight W. Given list of items with their weights and price.
How do you fill this bag to maximize value of items in the bag.

https://www.youtube.com/watch?v=8LusJS5-AGo
'''

# Time Complexity : O(n*C)   # n is the size of weight array, C is the capacity of knapsack
# Space Complexity : O(n*C)
def knapsack_0_1(capacity,weight,value):

    n = len(weight)

    T  = [[0]*(capacity+1)for x in range(n)]

    #print T

    for k in range(weight[0],capacity+1):
        T[0][k] = value[0]
    #print T

    for i in range(1,n):
        for j in range(0,capacity+1):

            if weight[i] > j:  # not taking current weight, take previously calculated upto now.
                T[i][j] = T[i-1][j]
            else:
                T[i][j] = max( (value[i] + T[i-1][j-weight[i]]) , T[i-1][j])
                # comparing prev value and (val of cur weight + (capacity-weight) times move back in prev row)
                # say our weight is 4 and capacity is 5...there is 1 weight extra...so with one weight what is the maximum so far...
                # ie) we are reducing the capacity to 1. and checking max at that point already calculated.

    print T

    # Printing items to be chosen

    i = n-1
    j = capacity
    items=dict()
    while i >= 0 and j >= 0:

        if T[i][j] == 0:
            break

        if T[i-1][j] < T[i][j]:

            items[weight[i]] = value[i]

            i = i - 1
            j = j - weight[i]
        else:
            i = i - 1



    #print items
    return T[n-1][capacity],items

weight = [1,3,4,5]
value = [1,4,5,7]

maxweight,items=knapsack_0_1(7,weight,value)
print "maxweight that can be placed in knapsack: "+str(maxweight)
print "weight:value that can be chosen: "+str(items)