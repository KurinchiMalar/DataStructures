from Sorting.MergeSort import mergesort
# Given an array of n elements. Find three elements in the array such that their sum is equal to K.

# BruteForce
# Time Complexity : O(n*n*n)

def find_three_elements_sum_k_bruteforce(Ar,k1):
    elem_list = []
    for i in range(0,len(Ar)-2):
        for j in range(i+1,len(Ar)-1):
            for k in range(j+1,len(Ar)):
                if Ar[i] + Ar[j] + Ar[k] == k1:
                    elem_list.extend((Ar[i],Ar[j],Ar[k]))
                    return elem_list

    return elem_list

# Sorting
# Time Complexity : O(nlogn) + O(n * (n) ) n times for n elements. == O(n*n)

def find_three_elements_sum_k_sorting(Ar,k):
    tempAr = Ar[:]
    Ar = mergesort(Ar)
    elem_list = []
    for i in range(0,len(Ar)-2):
        low = i+1
        high = len(Ar)-1

        while low < high:

            if Ar[i] + Ar[low] + Ar[high] < k:
                low = low + 1
            elif Ar[i] + Ar[low] + Ar[high] > k:
                high = high -1
            else:
                print "came in"
                elem_list.extend((Ar[i],Ar[low],Ar[high]))
                return elem_list

# Hashing
# Time Complexity : O(n*n)
# Space Complexity : O(n)


Ar = [1,6,45,4,10,18,34,29,2,5]

#print "" + str(find_three_elements_sum_k_bruteforce(Ar,50))
print "" + str(find_three_elements_sum_k_sorting(Ar,11))
