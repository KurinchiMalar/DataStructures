import ListNode


def traverse_list(node):
    current = node
    count = 0
    while current != None:
        #print current.get_data(),
        count = count + 1
        current = current.get_next()
    return count

def get_length_of_list(node):
    length = traverse_list(node)
    return length






head = ListNode.ListNode(1)
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

length = get_length_of_list(head)
print "Length: "+ str(length)

