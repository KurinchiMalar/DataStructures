'''
The cost of a stock on each day is given in an array,

find the max profit that you can make by buying and selling in those days.

For example, if the given array is {100, 180, 260, 310, 40, 535, 695},

the maximum profit can earned by buying on day 0, selling on day 3.

Again buy on day 4 and sell on day 6.

If the given array of prices is sorted in decreasing order, then profit cannot be earned at all.

Algorithm:

If we are allowed to buy and sell only once, then we can use following algorithm. Maximum difference between two elements. Here we are allowed to buy and sell multiple times. Following is algorithm for this problem.
1. Find the local minima and store it as starting index. If not exists, return.
2. Find the local maxima. and store it as ending index. If we reach the end, set the end as ending index.
3. Update the solution (Increment count of buy sell pairs)
4. Repeat the above steps if end is not reached.
'''

 # Time Complexity : O(n)
 # Space Complexity : O(1)
def maximize_profit(price_ar):

    i = 0

    n = len(price_ar)

    buy = []
    sell = []

    max_profit = 0
    max_profit_set = []

    while i < n-1:   # Go upto prev of last... because we will be comparing i and i+1

        # I want to by at an index when tomorrow's price is more than that of today,,, so keep moving when tomorrow's price is less..
        cur_profit = 0
        while i < n-1 and price_ar[i] >= price_ar[i+1]:
            i = i+1

        buy.append(price_ar[i])
        i = i + 1


        # i+1 is greater --> keep going till you find a drop in price... so that you can sell at the most max price
        while i < n-1 and price_ar[i] <=  price_ar[i+1]:
            i = i+1

        sell.append(price_ar[i])

        cur_profit = sell[len(sell)-1] - buy[len(buy)-1]
        if cur_profit > max_profit:
            max_profit_set = []
            max_profit = cur_profit
            max_profit_set.extend([buy[len(buy)-1],sell[len(sell)-1]])
        i = i + 1

    print "Buy:  "+str(buy)
    print "Sell: "+str(sell)
    print "MaxProfit:"+str(max_profit)
    print "MaxProfit set:"+str(max_profit_set)
price_ar = [100,180,260,310,40,535,695]
maximize_profit(price_ar)
