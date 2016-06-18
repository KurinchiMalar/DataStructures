'''
     A child is running up a staircase with n steps and can hop either 1 step, 2 steps or 3 steps at a time.
     Implement a method to count how many possible ways the child can run up the stairs.

      n = 4 -->


                                     4
    1 (3)                          2 (2)                         3 (1)    #  3step jump from 1  , 2step jump from 2 , 1step jump from 3

0(1)   - 1(0)  -2(0)            -1(0)   0(2)   1(1)          0(3)   1(2)    2(1)

                                                0(1)                0(1)    0(2)  1(1)
                                                                                    0(1)

Take all the root to 0 as leaf paths  ==> totally 7 paths

4 --> f(3) + f(2) + f(1)
  --> 4  + 2 + 1

1 --> f(0) + f(-1) + f(-2)
      1+ 0 + 0

0 --> 0
'''

# Time Complexity : O( 3 * n )

def count_ways_naive(n):

    if n == 0:
        return 1

    if n < 0:
        return 0

    return  count_ways_naive(n-1)+count_ways_naive(n-2)+count_ways_naive(n-3)

# Time Complexity : O(n)
# Space Complexity : O(n)
def count_ways_hash(n,memo):

    if n == 0:
        return 1

    if n < 0:
        return 0

    if memo.__contains__(n):
        if memo[n] > -1:
            return memo[n]

    memo[n] = count_ways_hash(n-1,memo)+count_ways_hash(n-2,memo)+count_ways_hash(n-3,memo)
    return  memo[n]


memo = {}


print (""+str(count_ways_naive(7)))
print(""+str(count_ways_hash(7,memo)))