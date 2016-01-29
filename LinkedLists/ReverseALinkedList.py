__author__ = 'kurnagar'

import ListNode
import copy
def traverse_list(node):
    current = node
    count = 0
    while current != None:
        print current.get_data(),
        count = count + 1
        current = current.get_next()
    print
    return count

# Time Complexity : O(n)
# Space Complexity : O(n) # for recursive stack.
def reverse_recursive(node):

    if node == None:
        return

    if node.get_next() == None:
        head = node
        return node

    head = reverse_recursive(node.get_next())
    node.get_next().set_next(node)
    node.set_next(None)
    return head

# Time Complexity : O(n)
# Space Complexity : O(1)

def reverse_iterative(node): # using three pointers

    if node == None:
        return None

    p = None
    q = node
    r = q.get_next()

    while q != None:

        q.set_next(p)
        p = q
        q = r
        if r != None:
            r = r.get_next()

    node = p
    return node


head = ListNode.ListNode(1)
#print ListNode.ListNode.__str__(head)
n1 = ListNode.ListNode(2)
n2 = ListNode.ListNode(3)
n3 = ListNode.ListNode(4)
n4 = ListNode.ListNode(5)
n5 = ListNode.ListNode(6)
n6 = ListNode.ListNode(7)

#orig_head = ListNode.ListNode(1)
#orig_head.set_next(n1)

head.set_next(n1)
n1.set_next(n2)
n2.set_next(n3)
n3.set_next(n4)
n4.set_next(n5)
n5.set_next(n6)

orig_head = copy.deepcopy(head)

#headnow = reverse_iterative(head)
#print "After reverse iterative :"+str(traverse_list(headnow))

head = copy.deepcopy(orig_head)

headnow = reverse_recursive(head)
print "After reverse recursive:"+str(traverse_list(headnow))