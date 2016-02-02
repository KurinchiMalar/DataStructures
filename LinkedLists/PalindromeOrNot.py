'''
Give a function to check if linked list is palindrome or not.
'''
import ListNode
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

def get_middle_node(node):

    prev_tort = node
    tort = node
    hare = node

    while hare != None and hare.get_next() != None:
        prev_tort = tort
        tort = tort.get_next()
        hare = hare.get_next().get_next()

    if hare != None: # odd list.
        return tort
    else:
        return prev_tort

def chec_pali(node):

    if node == None:
        return

    if node.get_next() == None:
        return True

    middlenode = get_middle_node(node)

    traverse_list(middlenode)
    print "middlenode: "+ListNode.ListNode.__str__(middlenode)
    #revlist = reverse_recursive(middlenode)


    #traverse_list(revlist)


def traverse_list(node):
    current = node
    count = 0
    while current != None:
        print current.get_data(),
        count = count + 1
        current = current.get_next()
    print

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
head1 = reverse_recursive(head)
chec_pali(head1)
