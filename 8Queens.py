def print_board(chosen_column):

    for i in range(8):
        for j in range(8):
            if chosen_column[i] == j:
                print "Q ",
            else:
                print "X ",
        print
    print "==============================================="


def place_queen(row,chosen_column):

    if row == 8:
        print_board(chosen_column)
        return

    for i in range(8): # go all columns

        if is_column_clear(row,i,chosen_column) == False or is_diagonal_clear(row,i,chosen_column) == False:
            continue

        chosen_column[row] = i
        place_queen(row+1,chosen_column)
    #return

def is_column_clear(row,column,chosen_column):

    for i in range(0,row):

        if chosen_column[i] == column: # if we have marked current column as chosen_column already.
            return False
    return True


def is_diagonal_clear(row,column,chosen_column):

    for i in range(0,row):

        if abs(i-row) == abs(chosen_column[i]-column): # for diagonal abs(x1-x2) == abs(y1-y2)
            return False

    return True


chosen_column = [-1,-1,-1,-1,-1,-1,-1,-1]  # row = index, column = value. Final positons of queens in board
place_queen(0,chosen_column)