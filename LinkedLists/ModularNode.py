'''

Find Modular Node:

    Given a singly linked list, write a function to find the last element from the beginning whose n % k == 0, where n is
    the number of elements in the list and k is an integer constant.

    For example: if n = 19 and k = 3 then we should return the 18th node
'''
import ListNode

# Time Complexity : O(n)
# Space Complexity : O(1)

def find_modular_node_frombeginning(node,k):

    if node == None:
        return None

    count = 1
    current = node
    result = None
    crossedthrough = []
    while current != None:
        print "count : "+str(count)+" current : "+str(current)

        if count % k == 0:
            crossedthrough.append(current.get_data())
            result = current # find the last element from the beginning whose n % k == 0 , so we are overwriting . we want only the last elem.

        current = current.get_next()
        count = count + 1

    print "We have crossed through: (n%k)== 0 for : "+str(crossedthrough)
    return result.get_data()

# Time Complexity : O(n)
# Space Complexity : O(1)
'''
 Given a singly linked list, write a function to find the last element from the end whose n % k == 0, where n is
    the number of elements in the list and k is an integer constant.
'''
def find_modular_node_fromend(node,k):

    if node == None:
        return None

    if k <= 0:
        return None

    current = node
    result = None
    count = 1
    while current != None:

        if count % k == 0:
            result = current
            return result.get_data()
        current = current.get_next()
        count = count + 1

    return result

def traverse_list(node):
    current = node
    count = 0
    while current != None:
        print current.get_data(),
        count = count + 1
        current = current.get_next()


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

#traverse_list(head)
print "Modular node from beginning: "+str(find_modular_node_frombeginning(head,3))
print "Modular node from end: "+str(find_modular_node_fromend(head,3))