__author__ = 'kurnagar'

import ListNode
import Stack

def get_length(node):

    if node == None:
        return -1

    current = node
    count = 0
    while current != None:
        current = current.get_next()
        count = count + 1
    return count

# Time Complexity : O(n)
# Space Complexity : O(1)
def find_node_at_intersection(head1,head2):

    list1_len = get_length(head1)
    list2_len = get_length(head2)

    #print "list1 len: "+str(list1_len)+"and list2_len:"+str(list2_len)

    start1 = head1
    start2 = head2

    if list1_len > list2_len: # move diff times in list1
        diff = list1_len - list2_len
        for i in range(diff):
            start1 = start1.get_next()
    elif list2_len > list1_len:
        diff = list2_len - list1_len
        for i in range(diff):
            start2 = start2.get_next()

    print "start1: "+str(start1)+"and start2: "+str(start2)
    while start1 != None and start2 != None:

        if start1 == start2:
            return start1
        start1 = start1.get_next()
        start2 = start2.get_next()

    return None

# Time Complexity : O(m + n) for scanning two lists. m and n are the sizes of two lists.
# Space Complexity : O(m + n) for two stacks.
def find_node_at_intersection_stacks_method(head1,head2):

    stack1 = Stack.Stack()
    stack2 = Stack.Stack()

    while head1 != None:
        stack1.push(head1.get_data())
        head1 = head1.get_next()

    while head2 != None:
        stack2.push(head2.get_data())
        head2 = head2.get_next()

    stack1.print_stack()
    stack2.print_stack()

    while stack1.size > 0 and stack2.size > 0:
        if stack1.peek() != stack2.peek():
            return pop_elem
        pop_elem = stack1.pop()
        stack2.pop()

head1 = ListNode.ListNode(1)
#print ListNode.ListNode.__str__(head)
n1 = ListNode.ListNode(2)
n2 = ListNode.ListNode(3)
n3 = ListNode.ListNode(4)
n4 = ListNode.ListNode(5)
n5 = ListNode.ListNode(6)
n6 = ListNode.ListNode(7)

head2 = ListNode.ListNode(11)
m2 = ListNode.ListNode(10)
m3 = ListNode.ListNode(12)
m4 = ListNode.ListNode(15)
m5 = ListNode.ListNode(16)
m6 = ListNode.ListNode(17)
m7 = ListNode.ListNode(20)
m8 = ListNode.ListNode(21)

#orig_head = ListNode.ListNode(1)
#orig_head.set_next(n1)

head1.set_next(n1)
n1.set_next(n2)
n2.set_next(n3)
n3.set_next(n4)
n4.set_next(n5)
n5.set_next(n6)

head2.set_next(m2)
m2.set_next(m3)
m3.set_next(m4)
m4.set_next(m5)
m5.set_next(m6)
m6.set_next(m7)
m7.set_next(m8)
m8.set_next(n4)

print "Node at intersection: "+str(find_node_at_intersection(head1,head2))

print "Node at intersection using stack method: "+str(find_node_at_intersection_stacks_method(head1,head2))