
import ListNode

# Time Complexity : O(n)
# Space Complexity : O(n) for recursive stack
def display_list_in_reverse(node):

    if node is None:
        return

    display_list_in_reverse(node.get_next())
    print node.get_data(),



head = ListNode.ListNode(1)
#print ListNode.ListNode.__str__(head)
n1 = ListNode.ListNode(2)
n2 = ListNode.ListNode(3)
n3 = ListNode.ListNode(4)
n4 = ListNode.ListNode(5)
n5 = ListNode.ListNode(6)
n6 = ListNode.ListNode(7)

head.set_next(n1)
n1.set_next(n2)
n2.set_next(n3)
n3.set_next(n4)
n4.set_next(n5)
n5.set_next(n6)

display_list_in_reverse(head)