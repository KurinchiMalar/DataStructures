'''
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

00 01  02        01  02  03       02 03 04              03  04  05

   11                 12             13            			14

20 21  22        21   22  23       22 23  24			23   24   25




10  11  12

	21

30  31  32


20


30
'''

# Time Complexity : (n*n)
import sys

def get_max_hourGlassSum(Ar,n):
    maxSum = -sys.maxsize-1
    print(str(maxSum))
    for hrow in range(0, (n - 1) - 1):  # (n-1) - 2 + 1 #  00 10 20 30

        sum = 0
        for hcol in range(0, (n - 1) - 1):  # 00 01  02 03

            start = hcol
            end = hcol + 2

            topsum = 0
            bottomsum = 0
            while start <= end:
                topsum = topsum + Ar[hrow][start]
                bottomsum = bottomsum + Ar[hrow + 2][start]
                start = start + 1

            sum = topsum + bottomsum + Ar[hrow + 1][hcol + 1]

            if sum > maxSum:
                maxSum = sum
    return maxSum


'''arr = []
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)'''

Ar = [[1,1,1,0,0,0],
      [0,1,0,0,0,0],
      [1,1,1,0,0,0],
      [0,9,2,-4,-4,0],
      [0,0,0,-2,0,0],
      [0,0,-1,-2,-4,0]]
print(str(get_max_hourGlassSum(Ar,6)))

