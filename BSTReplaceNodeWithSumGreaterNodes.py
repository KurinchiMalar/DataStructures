class BSTNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def printBST(root):
    if root == None:
        return
    printBST(root.left)
    print "" + str(root.data) + " "
    printBST(root.right)
    return


def replace(root, sum):
    if root == None:
        return sum
    sum = replace(root.right, sum)
    root.data = root.data + sum
    sum = root.data
    sum = replace(root.left, sum)
    return sum

root = BSTNode(10)
five = BSTNode(5)
seven = BSTNode(7)
six = BSTNode(6)
eight = BSTNode(8)
twenty = BSTNode(20)
fifteen = BSTNode(15)
twentyfive = BSTNode(25)
seventeen = BSTNode(17)

root.left = five
five.right = seven
seven.left = six
seven.right = eight
root.right = twenty
twenty.left = fifteen
twenty.right = twentyfive
fifteen.right = seventeen

printBST(root)
replace(root, 0)
print "     "
printBST(root)