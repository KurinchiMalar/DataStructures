'''
Given a BT , in which each node contains an integer value(positive or negative). Design an algorithm to count the number of
paths that sum to a given value. The path need not need to start but will end at the leaf.
'''
# Time Complexity : O(n)
# Hash Table : O(log n)  At any time there will be max of height of tree, number of nodes.
class BTNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def isLeaf(root):
    if root == None:
        return 0
    if root.left == None and root.right == None:
        return 1
    return 0

def insert_in_hashtable(hash_table,runningsum):
    if hash_table.__contains__(runningsum) == False:
        hash_table[runningsum] = 1
    else:
        hash_table[runningsum] = hash_table[runningsum]+1

def countpath_AnyNodeToLeaf(root,runningsum,targetsum,hash_table):

    if root == None:
        return 0

    runningsum = runningsum + root.data
    insert_in_hashtable(hash_table,runningsum)

    totalpathroot = 0

    if isLeaf(root):

        if runningsum == targetsum:

            totalpathroot = totalpathroot + 1

        elif hash_table.__contains__(runningsum-targetsum) == True:

            totalpathroot = totalpathroot + hash_table[runningsum-targetsum]

    totalpathleft = countpath_AnyNodeToLeaf(root.left,runningsum,targetsum,hash_table)
    totalpathright = countpath_AnyNodeToLeaf(root.right,runningsum,targetsum,hash_table)

    hash_table[runningsum] = hash_table[runningsum] - 1
    if hash_table[runningsum] == 0:
        hash_table.pop(runningsum)

    return totalpathroot + totalpathleft + totalpathright

root = BTNode(10)
five = BTNode(5)
minusthree = BTNode(-3)
three = BTNode(3)
one = BTNode(1)
eleven = BTNode(11)
three3 = BTNode(3)
minustwo = BTNode(-2)
two = BTNode(2)

root.left = five
root.right = minusthree

five.left = three
five.right = one

one.right = two

three.right = minustwo
three.left = three3

minusthree.right = eleven
hash_table = {}
print(countpath_AnyNodeToLeaf(root,0,1,hash_table))
