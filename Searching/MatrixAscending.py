'''
    Given an array of n*n elements such that each row is in ascending order and each column is in ascending order,
    devise an O(n) algorithm to determine if element x is in the array.
'''

# Time Complexity : O(n)
# Space Complexity : O(1)

def find_element_in_matrix(Ar,n,k):

    i = 0
    j = n-1
    index_list = []
    while i < n and j >= 0:
        #print "(i,j): "+str(i)+",  "+str(j)
        if Ar[i][j] == k:
            #print "(i,j):"+str(i)+","+str(j)
            index_list.extend((i,j))
            return index_list

        if Ar[i][j] < k:
            i = i + 1  # Eliminate current row and move to next

        else:
            j = j - 1 # Eliminate current column

    return index_list

Ar = []

Ar.append([1,2,3,4])
Ar.append([2,5,6,7])
Ar.append([3,8,10,11])
Ar.append([4,9,12,13])
#Ar = [[y for y in range(3)] for x in range(3)]

print Ar
print ""+str(find_element_in_matrix(Ar,4,13))
#print Ar[2][2]
