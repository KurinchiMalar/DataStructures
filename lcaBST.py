
# Time Complexity : O(n)
class BstNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def print_bst(root):

    if root == None:
        return

    print_bst(root.left)
    print(root.data)
    print_bst(root.right)

def isNodePresentBst(root, node):

    if node == None:
        return True

    if root == None:
        return False

    if root == node:
        return True

    if node.data < root.data:
        return isNodePresentBst(root.left, node)

    return isNodePresentBst(root.right, node)

def lca_bst(root, a, b):

    if root == None:
        return None

    if root == a or root == b:
        return root

    if a.data <= root.data and root.data < b.data:
        return root

    if a.data < root.data and b.data < root.data:
        return lca_bst(root.left, a, b)

    return lca_bst(root.right, a, b)

def util(root,a,b):
    if (not isNodePresentBst(root, a)) or (not isNodePresentBst(root, b)):
        return None

    if a.data < b.data:
        return lca_bst(root,a,b)
    return lca_bst(root,b,a)

root = BstNode(6)
four = BstNode(4)
five = BstNode(5)
seven = BstNode(7)
eight = BstNode(8)

root.left = four
root.right = seven

four.right = five
seven.right = eight


lca = util(root,four,eight)
print(str(lca.data))
