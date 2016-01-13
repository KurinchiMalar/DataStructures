'''
    find k nearest neighbours to the median of n distinct numbers in O(n) time.
'''

# Time Complexity : O(n)
# Space Complexity : O(1)

def get_k_nearest_neighbours_of_median(Ar,k):

    n = len(Ar)

    median_i = -1
    if n % 2 == 0:
        median_i = (n / 2) -1
    else:
        median_i = n / 2

    print "median is :"+str(Ar[median_i])

    i = median_i -1
    j = median_i + 1



    result = []

    for iter in range(0,k):

        if i < 0 or j >= n :
            print "yes"
            break

        left_val = Ar[median_i] - Ar[i]
        right_val = Ar[j] - Ar[median_i]

        if left_val < right_val:
            result.append(Ar[i])
            i = i - 1

        else:
            result.append(Ar[j])
            j = j + 1


    if i > 0 and iter in range(0,k):

        result.append(Ar[i])
        i = i - 1

    if j < n and iter in range(0,k):

        result.append(Ar[j])
        j = j -1

    #print iter
    print result



Ar = [1,2,3,4,7,9]
#Ar = [1,2,3,4]
get_k_nearest_neighbours_of_median(Ar,3)


