def moverobot(Ar, row, column, m, n,tempAr):

    if row >= m or column >= n or Ar[row][column] != 0:
        return False

    if (row == m-1 and column == n-1) or \
            moverobot(Ar, row, column + 1, m, n,tempAr) or \
            moverobot(Ar, row + 1, column, m, n,tempAr):
        #print " ( "+str(row)+" , "+str(column)+" ) "
        #tempAr = [" ( "+str(row)+" , "+str(column)+" ) "] + tempAr
        tempAr.insert(0,"("+str(row)+","+str(column)+")")
        #resultAr[row] = column

        return True

    return False

Ar = [[0, 1, 0, 0, 0, 1],
      [0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 1, 1],
      [0, 0, 0, 0, 0, 0]]

m = 5
n = 6


tempAr = [None] *(m*n)
moverobot(Ar, 0, 0, m, n,tempAr)
print tempAr

