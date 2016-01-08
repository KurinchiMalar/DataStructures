'''
    Given a sorted array of n elements, possibly with duplicates. Find the number of occurrences of a number.
'''

# BruteForce
# Time Complexity - O(n)
from FirstAndLastOccurence import find_first_occurence,find_last_occurence
def count_occurence_bruteforce(Ar,k):

    count = 0
    for i in range(0,len(Ar)):
        if Ar[i] == k:
            count = count + 1
    return count

def do_binary_search(Ar,low,high,elem):

    if low == high:
        if Ar[low] == elem:
            return low

    if low+1 == high:
        if Ar[low] == elem:
            return low
        if Ar[high] == elem:
            return high

    while low < high:

        middle = (low+high) // 2

        if Ar[middle] == elem:
            return middle

        if Ar[middle] > elem:
            return do_binary_search(Ar,low,middle,elem)
        else:
            return do_binary_search(Ar,middle+1,high,elem)


# BinarySearch + Scan

# Time Complexity : O(log n) + S ...where S is the number of occurences of the data.
def count_occurence_binarysearch(Ar,k):

    searched_index = do_binary_search(Ar,0,len(Ar)-1,k)

    count = 1
    for i in range(searched_index-1,-1,-1):
        if Ar[i] != k:
            break
        count = count + 1
    for j in range(searched_index+1,len(Ar)):
        if Ar[j] != k:
            break
        count = count + 1

    print "The number "+str(k)+"occured:"+str(count)+"times..."

    return count

# With First and Last Occurence

# Time Complexity = O(log n) + O(log n) = O(log n)

def count_occurence_withfirstandlast(Ar,k):

    first_occur = find_first_occurence(Ar,0,len(Ar)-1,k)
    last_occur = find_last_occurence(Ar,0,len(Ar)-1,k)
    return (last_occur-first_occur)+1


Ar = [1,3,3,3,6,6,7]
#Ar = [1,2,3,4,5,6,7]

#print ""+str(do_binary_search(Ar,0,len(Ar)-1,7))
#print ""+str(count_occurence_bruteforce(Ar,6))
#print ""+str(count_occurence_binarysearch(Ar,6))
print ""+str(count_occurence_withfirstandlast(Ar,1))