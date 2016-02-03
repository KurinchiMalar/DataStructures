'''
   Given a singly linked list, write a function to find the sqrt(n) th element, where n is the number of elements in the list.

   Assume the value of n is not known in advance.
'''
# Time Complexity : O(n)
# Space Complexity : O(1)
import ListNode
def sqrtNthNode(node):

    if node == None:
        return None

    current = node
    count = 1
    sqrt_index = 1

    crossedthrough = []
    result = None
    while current != None:

        if count == sqrt_index * sqrt_index:
            crossedthrough.append(current.get_data())
            result = current.get_data()
            print "Checking if current count = sq( "+str(sqrt_index)+" )"
            sqrt_index = sqrt_index + 1

        count = count + 1
        current = current.get_next()

    print "We have crossed through: (sqrt(n))== 0 for :"+str(crossedthrough)
    return result


head = ListNode.ListNode(1)
#print ListNode.ListNode.__str__(head)
n1 = ListNode.ListNode(2)
n2 = ListNode.ListNode(3)
n3 = ListNode.ListNode(4)
n4 = ListNode.ListNode(5)
n5 = ListNode.ListNode(6)
n6 = ListNode.ListNode(7)
n7 = ListNode.ListNode(8)
n8 = ListNode.ListNode(9)
n9 = ListNode.ListNode(10)
n10 = ListNode.ListNode(11)
n11 = ListNode.ListNode(12)
n12 = ListNode.ListNode(13)
n13 = ListNode.ListNode(14)
n14 = ListNode.ListNode(15)

#orig_head = ListNode.ListNode(1)
#orig_head.set_next(n1)

head.set_next(n1)
n1.set_next(n2)
n2.set_next(n3)
n3.set_next(n4)
n4.set_next(n5)
n5.set_next(n6)
n6.set_next(n7)
n7.set_next(n8)
n9.set_next(n10)
n10.set_next(n11)
n11.set_next(n12)
n12.set_next(n13)
n13.set_next(n14)


print "Sqrt node (last from beginning): "+str(sqrtNthNode(head))
