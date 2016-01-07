from Sorting.MergeSort import mergesort
# Given an array of n elements. Find two elements in the array such that their sum is equal to K.

# BruteForce
# Time Complexity : O(n*n)

def find_two_elements_sum_k_bruteforce(Ar,k):

    k_sum_elements=[]

    for i in range(0,len(Ar)):
        for j in range(i+1,len(Ar)):
            if Ar[i] + Ar[j] == k:
                k_sum_elements.append(Ar[i])
                k_sum_elements.append(Ar[j])
    return k_sum_elements

# Sorting
# Time Complexity : O(n logn) + O(n)

def find_two_elements_sum_k_sorting(Ar,k):

    tempAr = mergesort(Ar)

    low = 0
    high = len(tempAr) - 1
    elem_list = []
    print tempAr

    while low < high:
        if tempAr[low] + tempAr[high] < k:
            low = low + 1
        elif tempAr[low] + tempAr[high] > k:
            high = high-1
        else:
            elem_list.append(tempAr[low])
            elem_list.append(tempAr[high])
            break
        #print "low -- high"+str(low)+"--"+str(high)
    return elem_list

# Hashing
# Time Complexity = O(n)
# Space Complexity = O(n)

def find_two_elements_sum_k_hashing(Ar,k,n):

    hash_ar = [0] * (n+1)
    elem_list = []

    for i in range(0,len(Ar)):
        hash_ar[Ar[i]] = hash_ar[Ar[i]]+1
    print hash_ar

    #for i in range(0,len(Ar)):

    for i in range(0,len(Ar)):
        other = k - Ar[i]
        print "other:"+str(other)
        if other <= n and hash_ar[other] == 1 : # other elem present in source array already.
            elem_list.append(Ar[i])
            elem_list.append(other)
            break

    return elem_list

Ar = [9,2,3,6,1,7]
#print ""+str(find_two_elements_sum_k_bruteforce(Ar,13))
#print ""+str(find_two_elements_sum_k_sorting(Ar,13))
print ""+str(find_two_elements_sum_k_hashing(Ar,13,9))