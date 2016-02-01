__author__ = 'kurnagar'

#Time Complexity: O(n)

# where n is the number of nodes in given Binary Tree. The solution simply does two traversals of all Binary Tree nodes.

import TreeNode


# Changes left pointers to work as previous pointers
# in converted DLL
# The function simply does inorder traversal of
# Binary Tree and updates
# left pointer using previously visited node
def fix_prev(root):

    if root is not None:
        fix_prev(root.get_left())

        root.set_left(fix_prev.previous)
        fix_prev.previous = root
        fix_prev(root.get_right())

# Changes right pointers to work as next pointers in
# converted DLL
def fix_next(root):

    # go to the rightmost, this will be the last node in the inorder traversal.

    while root and root.get_right() != None:
        root = root.get_right()
    # Start from the rightmost node, traverse back using
    # left pointers
    # While traversing, change right pointer of nodes

    while root and root.get_left() != None:
        prev = root
        root = root.get_left()
        root.set_right(prev)

    return root

def bt_to_dll(root):

    if root == None:
        return root

    fix_prev(root)

    return fix_next(root)

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
print
fix_prev.previous = None

root1 = bt_to_dll(root)

print "Traversing list:"
traverse_list(root1)


















