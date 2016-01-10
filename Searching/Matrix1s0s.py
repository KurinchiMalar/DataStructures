'''
    Given a n*n matrix, and in eadch row all 1s are followd by 0s. Find row with maximum number of 0s
'''

def find_row_with_max_number_of_zero(Ar,n):

    i = 0
    j = n - 1

    zero_counter = 0
    zero_max_rowi = -1
    while i < n and j >= 0:

        if Ar[i][j] == 0:
            zero_counter = zero_counter + 1
            zero_max_rowi = i
            j = j - 1
        else:
            i = i +1
    print "in row : "+str(zero_max_rowi)+"zero occured:"+str(zero_counter)+"times..."
    return zero_max_rowi

Ar = []

Ar.append([1,1,1,0])
Ar.append([0,0,0,0])
Ar.append([1,0,0,0])
Ar.append([1,1,1,0])

print ""+str(find_row_with_max_number_of_zero(Ar,4))