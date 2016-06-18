# Time Complexity : O(2 pow(m+n)) without visitedmap.... O(m*n) with visited map
# Space Complexity : O(m + n) result , O(m+n) visitedmap

def moveRobot(Ar,row,column,m,n,result,visitedmap):

    if visitedmap.__contains__([row,column]):
        return False

    visitedmap.append([row,column])
    if row > m or column > n :
        return False

    if row == m and column == n : # found dest
        return  True

    if Ar[row][column] == 1: # False
        return False

    if moveRobot(Ar,row,column+1,m,n,result,visitedmap) or moveRobot(Ar,row+1,column,m,n,result,visitedmap):
        result.append([row,column])
        return True
    return False

Ar = [[0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0],
      [0, 1, 1, 1, 1, 1],
      [0, 0, 0, 0, 0, 0]]

m = 5
n = 6
result = []
visited_map = []
moveRobot(Ar,0,0,m-1,n-1,result,visited_map)
print result

