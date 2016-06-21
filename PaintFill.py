
# Time Complexity : O(m * n)

def paint_fill(i, j, input, m, n, color):

    if i < 0 or j < 0 or i >= m or j >= n:
        return
    print("i = "+str(i)+" j = "+str(j))

    if input[i][j] != color:
        input[i][j] = color

        paint_fill(i - 1, j, input, m, n, color)
        paint_fill(i, j + 1, input, m, n, color)
        paint_fill(i + 1, j, input, m, n, color)
        paint_fill(i, j - 1, input, m, n, color)

input = [[0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0]]

paint_fill(4,5,input,6,7,1)

print input