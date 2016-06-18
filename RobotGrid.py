# Time Complexity : O(2 pow(m+n))
# Space Complexity : O(m + n)

def moveRobot(Ar,row,column,m,n,result):

    if row > m or column > n :
        return False

    if row == m and column == n : # found dest
        return  True

    if Ar[row][column] == 1: # False
        return False

    if moveRobot(Ar,row,column+1,m,n,result) or moveRobot(Ar,row+1,column,m,n,result):
        result.append([row,column])
        return True
    return False

Ar = [[0, 1, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 1, 1],
      [0, 0, 0, 0, 0, 0]]

m = 5
n = 6
result = []
moveRobot(Ar,0,0,m-1,n-1,result)
print result