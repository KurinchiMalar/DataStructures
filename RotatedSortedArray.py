

def find_elem_rotated_sorted_array(Ar,first,last,k):

    if first == last:
        if Ar[first] == k:
            return first
        else:
            return -1

    if first+1 == last:
        if Ar[first] == k:
            return first
        elif Ar[last] == k:
            return last
        else:
            return -1

    middle = (first + last) / 2

    if k == Ar[middle]:
        return middle
    #10 13 1 2 3 4 8 9

    #13
    if k > Ar[middle] and k >= Ar[first] and Ar[middle] <= Ar[first]:
        return find_elem_rotated_sorted_array(Ar, first, middle - 1, k)

    #1
    if k < Ar[middle] and k <= Ar[first] and Ar[middle] <= Ar[first]:
        return find_elem_rotated_sorted_array(Ar, first, middle - 1, k)

    #8
    if k > Ar[middle] and k <= Ar[last] and Ar[middle] <= Ar[last]:  # 8
        return find_elem_rotated_sorted_array(Ar, middle + 1, last, k)

    # 4 8 9 10 13 1 2 3

    #9
    if k < Ar[middle] and k >= Ar[first] and Ar[middle] >= Ar[first]:
        return find_elem_rotated_sorted_array(Ar, first, middle - 1, k)

    #13
    if k > Ar[middle] and k >= Ar[last] and Ar[middle] >= Ar[last]:  # 13
        return find_elem_rotated_sorted_array(Ar, middle + 1, last, k)

    #1
    if k < Ar[middle] and k <= Ar[last] and Ar[middle] >= Ar[last]:
        return find_elem_rotated_sorted_array(Ar, middle + 1, last, k)

Ar = [10,13,1,2,3,4,8,9 ]
for item in Ar:
    print str(item) + " found at index "+str(find_elem_rotated_sorted_array(Ar,0,len(Ar)-1,item))

Ar = [ 4,8,9,10,13,1,2,3 ]

for item in Ar:
    print str(item) + " found at index "+str(find_elem_rotated_sorted_array(Ar,0,len(Ar)-1,item))
