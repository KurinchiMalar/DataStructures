'''
Find Fractional Node:

    Given a singly linked list, write a functionn to find the n/k th element, where n is the number of elements in the list.
'''
import ListNode

# Time Complexity : O(n)
# Space Complexity : O(1)
def fractional_node(node,k):

    if node == None:
        return None

    if k <= 0:
        return None

    current = node
    crossedthrough= []
    result = None
    count = 1

    while current != None:
        print "count : "+str(count)+" current : "+str(current)
        if count // k  == 0:
            crossedthrough.append(current.get_data())
            result = current

        count = count + 1
        current = current.get_next()

    print "We have crossed through: (n/k)== 0 for : "+str(crossedthrough)
    return result.get_data()



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

print "Fractional node (last from beginning) : "+str(fractional_node(head,3))













