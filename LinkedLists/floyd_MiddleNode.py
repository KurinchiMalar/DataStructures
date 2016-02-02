
import ListNode

# Time Complexity : O(n) + O(n) = O(n)

def find_the_middle_node_naive(node):
    if node == None:
        return -1

    current = node
    count = 0
    while current != None:
        current = current.get_next()
        count = count + 1

    current = node

    for i in range(1,(count // 2) + 1):
        current = current.get_next()
    return current.get_data()


'''
Algorithm:

    The tort will be in middle of beginning of seq and hare, because of the way they move


    Actually for even list.... you can have a prev pointer to tort and return that to get the actual middle

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



'''
# Time Complexity : O(n)
def find_the_middle_node_floyd(node):

    tort = node
    hare = node

    while hare != None and hare.get_next() != None:
        tort = tort.get_next()
        hare = hare.get_next().get_next()
    return tort.get_data()

head = ListNode.ListNode(1)
#print ListNode.ListNode.__str__(head)
n1 = ListNode.ListNode(2)
n2 = ListNode.ListNode(3)
n3 = ListNode.ListNode(4)
n4 = ListNode.ListNode(5)
n5 = ListNode.ListNode(6)
#n6 = ListNode.ListNode(7)

head.set_next(n1)
n1.set_next(n2)
n2.set_next(n3)
n3.set_next(n4)
n4.set_next(n5)
#n5.set_next(n6)

print "Middle Node : "+str(find_the_middle_node_naive(head))
print "Middle Node Floyd : "+str(find_the_middle_node_floyd(head))