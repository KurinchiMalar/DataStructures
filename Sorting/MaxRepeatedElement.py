#Complexity Analysis Chart - http://bigocheatsheet.com/
#Naive n*n solution --> for every element i, go through i+1 to end and increment counter.
#Sorting Solution
from HeapSort import Heap
ob = Heap()
def get_max_repeated_element_SortAndScan(Ar):
    max_counter = -1
    ob.heapList = Ar
    ob.HeapSort(0,len(Ar)-1)
    Ar = ob.heapList
    i = 0
    j = 0
    max_counter = -1
    for i in range(0,len(Ar)):
        #j = i + 1
        count = 0
        for j in range(i+1,len(Ar)):

            if Ar[i] != Ar[j]:
                break
            else:
                count = count + 1

        if max_counter < count:
            print "max:"+str(Ar[i])
            max_counter = count
            max_elem = Ar[i]
        i = j

    print "MaxElem: "+str(max_elem)+"occured"+str(max_counter)+"times"

#BST Solution Complexity
#Time Complexity - O(n) + O(logn) --> n (creation) + logn for insertion
#Space Complexity - O(2n) = O(n) since every node in BST needs two extra pointers.
class BstNode:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.key = key
        self.count = 1

'''
The worst case time complexity of search and insert operations is O(h) where h is height of Binary Search Tree.
 In worst case, we may have to travel from root to the deepest leaf node.
 The height of a skewed tree may become n and the time complexity of search and insert operation may become O(n).

 AverageCase : logn
'''
def search_in_bst(root,key):
    if root is None:
        return -1
    else:
        if key < root.key:
            return search_in_bst(root.left,key)
        elif key >root.key:
            return search_in_bst(root.right,key)
        else:
            return 1

#Average CAse : O(logn)
def insert_in_bst_iterative(root,node):

    max_count = 1
    max_elem = root

    if root is None:
        root = node
        return root

    while root != None:

        if node.key == root.key:
            root.count = root.count + 1
            if max_count < root.count:
                max_count = root.count
                max_elem = root
            break

        elif node.key < root.key:
            if root.left is None:
                root.left = node
                break
            else:
                root = root.left
        else:
            if root.right is None:
                root.right = node
                break
            else:

                root = root.right
    #print "max_elem : "+str(max_elem.key)+"occured -"+str(max_count)+"times"
    return max_elem

def insert_in_bst_recursive(root,node):

    if root is None:
        root = node
        return root

    # if node is None has to be checked before calling insert
    else:
        if node.key == root.key:
            node.count = node.count+1

        if node.key < root.key:
            if root.left is None:
                root.left = node
            else:
                insert_in_bst_recursive(root.left,node)
        else:
            if root.right is None:
                root.right = node
            else:
                insert_in_bst_recursive(root.right,node)
        return root

def create_bst(Ar):
    print Ar
    r = BstNode(Ar[0])
    max_node = r

    for i in range(1,len(Ar)):
        max_node = insert_in_bst_iterative(r,BstNode(Ar[i]))
    return max_node


def inorder_bst(root):

    if root:
        inorder_bst(root.left)
        print str(root.key) + "-" + str(root.count) + " times"
        inorder_bst(root.right)




#Hashing Solution
#Time Complexity - O(n)
#Space Complexity - O(n)
#Input Restriction - should know range of elements...ie eg) range from 0 to k.

def get_repeated_hashing(Ar,k):
    C = [0 for i in range(0,k+1)]

    for i in range(0,len(Ar)):
        C[Ar[i]] = C[Ar[i]] +1
    print C
    max_count = 0
    max_elem = -1
    for i in range(0,len(C)):
        if C[i] > max_count:
            max_count = C[i]
            max_elem = i

    print "elem:"+str(max_elem)+"count:"+str(max_count)
    return max_elem



Ar = [4,6,3,5,1,5,3,5,6,1,5,3,3,5]
get_max_repeated_element_SortAndScan(Ar)

#Ar = [80,30,90,80,90,80,70,90,80]
#r = create_bst(Ar)
#print "result"+str(r.key)

#inorder_bst(r)

#Ar = [8,4,3,3,8,1,8,5]
#get_repeated_hashing(Ar,8)

