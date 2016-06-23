# Time Complexity : O(n) 

class BTNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def isNodePresentBT(root, node):
    if node == None:
        return True

    if root == None:
        return False

    if root == node:
        return True

    return isNodePresentBT(root.left, node) or isNodePresentBT(root.right, node)


def lca_bt(root, a, b):
    if root == None:
        return None

    if root == a or root == b:
        return root

    isAOnLeft = isNodePresentBT(root.left, a)
    isBOnLeft = isNodePresentBT(root.left, b)

    if isAOnLeft != isBOnLeft:
        return root

    if isAOnLeft == True and isBOnLeft == True:
        return lca_bt(root.left, a, b)

    return lca_bt(root.right, a, b)


def util(root, a, b):
    if (not isNodePresentBT(root, a)) or (not isNodePresentBT(root, b)):
        return None

    if a.data < b.data:
        return lca_bt(root, a, b)

        return lca_bt(root, b, a)
    
root = BTNode(1)
two = BTNode(2)
three = BTNode(2)
four = BTNode(4)
five = BTNode(5)
six = BTNode(6)
seven = BTNode(7)
eight = BTNode(8)

root.left = two
root.right = three

two.left = four
two.right = five

three.left = six
three.right = seven

seven.right = eight

lca = util(root,four,five)
print(str(lca.data))

