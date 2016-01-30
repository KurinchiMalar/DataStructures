
import ListNode

def check_if_even_or_odd(node):

    hare = node

    while hare != None and hare.get_next() != None:

        hare = hare.get_next().get_next()

    if hare != None:
        return "odd"
    return "even"


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

print ""+str(check_if_even_or_odd(head))