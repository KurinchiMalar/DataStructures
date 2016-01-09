
# Sorting Solution

# Time Complexity : O(nlogn) + O(n)
from Sorting.MergeSort import mergesort
from Sorting.Median import getMedian_LinearTime
def find_majorityelem_bruteforce(Ar):
    Ar = mergesort(Ar)
    print Ar
    max_elem = -1
    max_count = 0

    for i in range(0,len(Ar)):
        count = 1
        for j in range(i+1,len(Ar)):
            if Ar[i] != Ar[j]:
                break
            count = count + 1
        if count > max_count:
            max_elem = Ar[i]
            max_count = count
            count = 0
    print "max elem is :"+ str(max_elem) +"occured :"+str(max_count)+"times."
    if max_count > len(Ar)/2:
        return max_elem
    return -1

# Median Logic
# Time Complexity : O(n) + O(n)   ---> worst case LinearSelection - O(n*n)
'''
    1) Use Linear Selection to find median of Ar
    2) Do one more pass to count number of occurences of median. Return true if it is more than n/2
'''

def find_majority_median_logic(Ar):

    median = getMedian_LinearTime(Ar)

    print "median is "+str(median)

    count = 0
    for i in range(0,len(Ar)):
        if Ar[i] == median:
            count = count + 1

    if count > len(Ar)/2:
        return median
    return -1

# BST logic
#Time Complexity - O(n) + O(logn) --> n (creation) + logn for insertion
#Space Complexity - O(2n) = O(n) since every node in BST needs two extra pointers.
class BstNode:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        self.count = 1

def insert_bst(root,node):

    if root is None:
        root = node
        return root

    max_elem = None
    max_count = 0

    while root != None:

        if root.key == node.key:
            root.count = root.count+1

            if max_count < root.count:
                max_count = root.count
                max_elem = root
            break

        elif node.key < root.key:
            if root.left is None:
                root.left = node
            else:
                root = root.left

        else:
            if root.right is None:
                root.right = node
            else:
                root = root.right
    return root

def create_bst(Ar):

    root = BstNode(Ar[0])
    for i in range(1,len(Ar)):
        max_node = insert_bst(root,BstNode(Ar[i]))
    return max_node

def find_majority_bst_logic(Ar):
    r = create_bst(A)
    print "result"+str(r.key)

    if r.count > len(Ar) // 2:
        return r.key
    else:
        return -1


# Time Complexity : O(n)
# Space Complexity : O(1)
def find_majority_MooresVotingAlgorithm(Ar):

    # Find candidate
    element = 0
    count = 0

    for i in range(0,len(Ar)):

        if count == 0:
            element = Ar[i]
            count =  1
        elif element == Ar[i]:
            count = count + 1
        else:
            count = count -1

    print "majority_candidate:"+str(element)

    count_in_ar = 0
    for i in range(0,len(Ar)):

        if Ar[i] == element:
            count_in_ar = count_in_ar + 1

    if count_in_ar > len(Ar) // 2:
        return element
    return -1



A = [3,3,4,2,4,4,2,4,4]
A = [7,3,2,3,3,6,9]


#print ""+str(find_majorityelem_bruteforce(A))
#print ""+str(find_majority_median_logic(A))
#print ""+str(find_majority_bst_logic(A))
print ""+str(find_majority_MooresVotingAlgorithm(A))
