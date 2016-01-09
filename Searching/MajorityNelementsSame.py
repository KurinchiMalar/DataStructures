
'''
   Given an array of 2n elements, where n elements are same and remaining n elements are different.

    Solution:

         One of the below properties will definitely be true

         1) The different elements will be away by a distance of two. n x n y n z
          or
         2) Atleast two same elements may be next to each other. n n x y n z  ,   n x n n y z....


'''

# Time Complexity : O(n)
# Space Complexity : O(1)

def check_if_two_adjacent_elements_same(Ar):

    for i in range(1,len(Ar)):
        if Ar[i] == Ar[i-1]:
            return Ar[i]
    return -1

def check_if_same_elements_at_distance_of_2(Ar):
    for i in range(2,len(Ar),2):
        if Ar[i] == Ar[i-2]:
            return Ar[i]
    return -1


def find_n_elements_same(Ar):

    adj_same = check_if_same_elements_at_distance_of_2(Ar)
    elements_at_dist_two = check_if_same_elements_at_distance_of_2(Ar)
    print "adj_same:"+str(adj_same)+"...  elements_at_dist_two:"+str(elements_at_dist_two)
    if adj_same != -1 and elements_at_dist_two != -1:
        return adj_same

    elif adj_same != -1:
        return adj_same

    elif elements_at_dist_two != -1:
        return elements_at_dist_two

    else:
        return -1

Ar = [5,7,5,9,5,10]
Ar = [9,19,17,8,9,7,9,6,9,9]
#print ""+str(find_n_elements_same(Ar))
print ""+str(find_n_elements_same(Ar))


