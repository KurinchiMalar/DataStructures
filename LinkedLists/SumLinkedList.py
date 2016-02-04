
import ListNode

# Time Complexity : O(n)
# Space Complexity : O(n) for recursive stack
def linkedlist_sum(node):
    if node == None:
        return 0

    return node.get_data()+linkedlist_sum(node.get_next())

def linkedlist_len(node):
    if node == None:
        return 0

    return 1+linkedlist_len(node.get_next())

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

print "USING RECURSION"
print "Sum : "+str(linkedlist_sum(head))
print "Len : "+str(linkedlist_len(head))