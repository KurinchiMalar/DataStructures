'''
Given a BT , in which each node contains an integer value(positive or negative). Design an algorithm to count the number of
paths that sum to a given value. The path need not need to start or end at the root or a leaf.
'''
# Time Complexity : O(n)
# Hash Table : O(log n)
class BTNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def insert_in_hashtable(hash_table,runningsum):

    if hash_table.__contains__(runningsum) == False:
        hash_table[runningsum] = 1
    else:
        hash_table[runningsum] = hash_table[runningsum] + 1

def countPath_AnynodeToAnynode(root,runningsum,targetsum,hash_table):

    if root == None:
        return 0

    runningsum = runningsum + root.data
    insert_in_hashtable(hash_table,runningsum)
    totalpath = 0
    if runningsum == targetsum:
        totalpath = totalpath + 1

    elif hash_table.__contains__(runningsum-targetsum) == True:
        totalpath = totalpath + hash_table[runningsum-targetsum]

    totalpathleft = countPath_AnynodeToAnynode(root.left,runningsum,targetsum,hash_table)
    totalpathright = countPath_AnynodeToAnynode(root.right,runningsum,targetsum,hash_table)
    hash_table[runningsum] = hash_table[runningsum] - 1
    if hash_table[runningsum] == 0:
        hash_table.pop(runningsum)
    return totalpath + totalpathleft + totalpathright

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
print(countPath_AnynodeToAnynode(root,0,8,hash_table))


