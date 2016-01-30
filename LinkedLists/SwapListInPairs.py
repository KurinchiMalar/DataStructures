import ListNode
'''
   Swap list in pairs.
'''
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
# Space Complexity : O(1)

def swap_list_in_pairs(node):

    if node == None:
        return None

    current = node

    while current != None and current.get_next() != None:

        current.data,current.next.data = current.next.data,current.data
        current = current.get_next().get_next()


    #traverse_list(node)

    return node

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

print "Input List:"
traverse_list(head)

print "After swap"
head = swap_list_in_pairs(head)
traverse_list(head)
