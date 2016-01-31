'''
    Convert a binary tree to doubly linked list.
    # http://www.geeksforgeeks.org/in-place-convert-a-given-binary-tree-to-doubly-linked-list/
'''

# Time Complexity : O(nlogn)   # for every treenode we are finding the inorder predecessor and successor
import TreeNode


def convert_bt_to_dll(root):
    print "--------------------------------------------"
    print "root: "+str(TreeNode.TreeNode.__str__(root))
    if root == None:
        return root

    if root.get_left() != None:
        print "leftnotnone: "+str(TreeNode.TreeNode.__str__(root))
        leftmost = convert_bt_to_dll(root.get_left())

        # find the inorder predecessor --> rightmost of left subtree... because the greatest element of left will be immediate previous of root.(in it's inorder traversal)
        while leftmost.get_right() != None:
            leftmost = leftmost.get_right()

        root.set_left(leftmost)
        leftmost.set_right(root)

    if root.get_right() != None:
        print "rightnotnone: "+str(TreeNode.TreeNode.__str__(root))
        rightmost = convert_bt_to_dll(root.get_right())

        # find the inorder successor --> leftmost of right subtree ...because the smallest elem of right will be the immediate successor of root.(in inorder)

        while rightmost.get_left() != None:
            rightmost = rightmost.get_left()

        root.set_right(rightmost)
        rightmost.set_left(root)

    return root

def invoke_convertbsttodll(root):

    if root == None:
        return root

    root = convert_bt_to_dll(root)

    # the above convert_bt_to_dll will give us the tree root. We need to get the dll head...which is ideally the leftmost node.
    while root.get_left() != None:
        root = root.get_left()

    return root

def create_new_treenode(data):
    return TreeNode.TreeNode(data)

def traverse_list(node):
    current = node
    while current != None:
        print current.get_data(),
        current = current.get_right()
    print
    return

def traverse_tree(root): # inorder traversal
    if root == None:
        return

    traverse_tree(root.get_left())
    print root.get_data(),
    traverse_tree(root.get_right())

root = create_new_treenode(10)
root.set_left(create_new_treenode(12))
root.set_right(create_new_treenode(15))
root.get_left().set_left(create_new_treenode(25))
root.get_left().set_right(create_new_treenode(30))
root.get_right().set_left(create_new_treenode(36))
print "Traversing original tree:"
traverse_tree(root)
root1 = invoke_convertbsttodll(root)
print
print "Traversing list:"
traverse_list(root1)