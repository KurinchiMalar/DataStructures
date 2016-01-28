__author__ = 'kurnagar'


'''
    Given k, find the kth node from the last.
'''
'''

Algorithm:
    Take two pointers at head node.

    Move ptr1 k steps

    After that move ptr2 and ptr1 subsequently unttil ptr1 is None

    return ptr2.

    Tip: You are maintaining k distance everytime between ptr1 and ptr2
'''

# Time Complexity : O(n)
import ListNode
def traverse_list(node):
    current = node
    count = 0
    while current != None:
        print current.get_data(),
        count = count + 1
        current = current.get_next()
    print
    return count

def find_kth_node_from_last(node,k):

    ptr1 = node
    ptr2 = node

    for i in range(0,k):
        if ptr1 != None:
            print ListNode.ListNode.__str__(ptr1)
            ptr1 = ptr1.get_next()

    while ptr1 != None:
        ptr2 = ptr2.get_next()
        ptr1 = ptr1.get_next()

    return ptr2



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

traverse_list(head)
k = 2
print "k: "+str(2)+" node from last: "+str(find_kth_node_from_last(head,2))


