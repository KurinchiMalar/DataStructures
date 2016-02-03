__author__ = 'kurnagar'

import ListNode
'''
Segregate a link list to put odd nodes in the beginning and even behind
'''
# Time Complexity : O(n)
# Space Complexity : O(1)

def swap_values_nodes(node1,node2):
    temp = node1.get_data()
    node1.set_data(node2.get_data())
    node2.set_data(temp)

def segregate_odd_and_even(node):

    if node == None:
        return node

    if node.get_next() == None:
        return node

    oddptr = node
    evenptr = oddptr.get_next()

    while oddptr != None and evenptr != None:


        while oddptr != None and oddptr.get_data() % 2 != 0:

            if oddptr.get_data() % 2 == 0: # found even location.
                #oddptr = current
                break

            oddptr = oddptr.get_next()

        if oddptr == None:
            return node
        evenptr = oddptr.get_next()
        while evenptr != None and evenptr.get_data() % 2  == 0:

            if evenptr.get_data() % 2 != 0: # found odd location
                #evenptr = current
                break
            evenptr = evenptr.get_next()
        if evenptr == None:
            return node

        print "oddptr: "+str(ListNode.ListNode.__str__(oddptr))
        print "evenptr: "+str(ListNode.ListNode.__str__(evenptr))
        swap_values_nodes(oddptr,evenptr)
        oddptr = oddptr.get_next()
        evenptr = evenptr.get_next()

    return node

def traverse_list(node):
    current = node
    count = 0
    while current != None:
        print current.get_data(),
        count = count + 1
        current = current.get_next()
    print



head = ListNode.ListNode(12)
#print ListNode.ListNode.__str__(head)
n1 = ListNode.ListNode(92)
n2 = ListNode.ListNode(32)
n3 = ListNode.ListNode(12)
n4 = ListNode.ListNode(19)
n5 = ListNode.ListNode(8)
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
#swap_values_nodes(n5,n6)
#traverse_list(head)

head1 = segregate_odd_and_even(head)
traverse_list(head1)
