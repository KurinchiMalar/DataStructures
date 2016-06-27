'''
x x x
o x x
o o x


0  1  2
1
2

0,0  --> 0,0 1,1, 2,2
0,2  --> 0,2  1,1 2,0

Centre === n/ 2   (1,1)
1,1 --> 0,0 1,1, 2,2
		0,2  1,1 2,0

2,2 -->  2,2  1,1  0,0
2,0  --> 2,0  1,1  0,2
'''

# Time Complexity : O(n*n)
def capturedRow(board, n, player):
    # in this row has he captured the entire column

    for i in range(n):
        captured = True
        for j in range(n):
            if board[i][j] != player:
                captured = False
                break
    return captured


def capturedColumn(board, n, player):
    # in this column has he captured the entire row.
    for i in range(n):
        captured = True
        for j in range(n):
            if board[j][i] != player:
                captured = False
                break
    return captured


def capturedDiagonal(board, n, player):
    # in this diagonal has he captured the entire diagonal.
    if board[0][0] == player:
        i = 1
        j = 1
        while i < n and j < n:
            if board[i][j] != player:
                return False
            i = i + 1
            j = j + 1
        return True

    elif board[0][n - 1] == player:
        i = 1
        j = n - 2
        while i < n and j > 0:
            if board[i][j] != player:
                return False
            i = i + 1
            j = j - 1
        return True


def hasWon(player, board, n):

    if capturedRow(board, n, player) or capturedColumn(board, n, player) or capturedDiagonal(board, n,player):
            return True

    return False


def print_board(Ar):
    for i in range(len(Ar)):
        for j in range(len(Ar)):
            print(Ar[i][j], end=' ')
        print()
    print()


# board = [[0 for y in range(3)]for x in range(3)]

board = [[0, 0, 1],
         [1, 1, 0],
         [1, 1, 0]]
print_board(board)
player = 1
print("" + str(player) + " hasWon ? " + str(hasWon(player, board, 3)))
