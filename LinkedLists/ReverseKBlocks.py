'''
Given a linked list, write a function to reverse every k nodes (where k is an input to the function).

Example:
Inputs:  1->2->3->4->5->6->7->8->NULL and k = 3
Output:  3->2->1->6->5->4->8->7->NULL.

Inputs:   1->2->3->4->5->6->7->8->NULL and k = 5
Output:  5->4->3->2->1->8->7->6->NULL.

'''

# Time Complexity : O(n)

import ListNode

def reverse_kblocks(node,k):

    if node == None:
        return

    if node.get_next() == None:
        head = node
        return head

    head = node   # store the start of k traversal... say 1-> 2-> 3 ....for next list appending 1-> should be caught.
    count = 0
    p = None  # breaking chunk
    q = node
    r = q.get_next()

    while q != None and count < k:

        q.set_next(p)
        p = q
        q = r
        if q is None:
            return p
        else:
            r = q.get_next()
            count = count + 1
    # fitting it back.S
    head.set_next(reverse_kblocks(q,k))
    return p  # this is the new head of the reversed list in every iteration.


def traverse_list(node):
    current = node
    count = 0
    while current != None:
        print current.get_data(),
        count = count + 1
        current = current.get_next()
    print
    return count

head = ListNode.ListNode(1)
#print ListNode.ListNode.__str__(head)
n1 = ListNode.ListNode(2)
n2 = ListNode.ListNode(3)
n3 = ListNode.ListNode(4)
n4 = ListNode.ListNode(5)
n5 = ListNode.ListNode(6)
n6 = ListNode.ListNode(7)
n7 = ListNode.ListNode(8)

#orig_head = ListNode.ListNode(1)
#orig_head.set_next(n1)

head.set_next(n1)
n1.set_next(n2)
n2.set_next(n3)
n3.set_next(n4)
n4.set_next(n5)
n5.set_next(n6)
n6.set_next(n7)

traverse_list(head)
result = reverse_kblocks(head,3)
traverse_list(result)