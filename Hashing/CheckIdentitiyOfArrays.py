'''
     Given two arrays of unordered numbers, check whether both the arrays have the same set of numbers.
'''

# Time Complexity : O(n*n)
# Space Complexity : O(1)

# Logic: Comparing every element of A with every element of B will fail if there are duplicates. Because the arrays may have the
#           same elements with different frequency of occurences. Hence on finding an element in B , move them either to the
#           beginning or end , and start after that.

# Disadv : This method needs extra swaps.

def check_identity_twoarrays_bruteforce(A,B):

    if len(A) != len(B):
        return False

    for i in range(0,len(A)):

        for j in range(i,len(B)):

            found = 0
            if A[i] == B[j]:
                found = 1
                B[i],B[j] = B[j],B[i] #  those we have encountered move them to the beginning of B and next iteration start from the same index you start in A array.(i)
                break

    if found == 0:
        return False

    return True

# Time Complexity : O(nlogn)
# Space Complexity : O(1)

def check_identity_twoarrays_sorting(A,B):

    A.sort()
    B.sort()

    i = j = 0

    if len(A) != len(B):
        return False

    while i < len(A) and j < len(B):

        if A[i] != B[j]:
            return False

        i = i+1
        j = j+1
    return True

# Time Complexity : O(n)
# Space Complexity : O(n)
def check_identity_twoarrays_hashing(A,B):

    hash_dict = dict()
#    print hash_dict[2]
    for i in A:

        if i not in hash_dict:
            hash_dict[i] = 1
        else:
            hash_dict[i] = hash_dict[i]+1

    print hash_dict

    for i in B:

        if i in hash_dict:
            hash_dict[i] = hash_dict[i]-1
        else:
            hash_dict[i] = 1

    print hash_dict

    for key in hash_dict:
        if hash_dict[key] != 0:
            return False

    return True




A = [2,5,6,8,10,2,2]
A = [2,5,5,8,10,5,6]
B = [2,5,5,8,10,5,6]

#print ""+str(check_identity_twoarrays_bruteforce(A,B))
#print ""+str(check_identity_twoarrays_sorting(A,B))
print ""+str(check_identity_twoarrays_hashing(A,B))



