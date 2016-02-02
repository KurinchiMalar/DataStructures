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

    # Let's return middle node, start of next list
    # for odd list tort will be the middle node.
    if hare != None: # odd list.
        return tort,tort.get_next()
    else: # for even list prev_tort will be the middle node.
        return prev_tort,tort

def compare_lists(list1,list2):

    temp1 = list1
    temp2 = list2

    while temp1 != None and temp2 != None:

        if temp1.get_data() != temp2.get_data():
            return 0
        temp1 = temp1.get_next()
        temp2 = temp2.get_next()

    if temp1 == None and temp2 == None:
        return 1
    return 0


# Time Complexity : O(n)
# Space Complexity : O(1)
def chec_pali(node):

    if node == None:
        return

    if node.get_next() == None:
        return True

    prev_tort = node
    tort = node
    hare = node

    while hare != None and hare.get_next() != None:
        prev_tort = tort
        tort = tort.get_next()
        hare = hare.get_next().get_next()


    if hare != None: # for odd list tort will be the middle node. so secondhalf starting will be tort.get_next()
        middle_node = tort
        tort = tort.get_next()
    else: # for even list prev_tort will be the middle node.  so secondhalf starting will be tort.
        middle_node = None

    prev_tort.set_next(None)  # breaking firsthalf

    tort = reverse_recursive(tort) # reversing second half

    print "Comparing .... "
    traverse_list(node)
    traverse_list(tort)

    result = compare_lists(node,tort) # comparing

    if middle_node != None: # resetting odd list.
        prev_tort.set_next(middle_node)
        middle_node.set_next(reverse_recursive(tort))
    else:
        prev_tort.set_next(reverse_recursive(tort))

    #traverse_list(node)
    return result

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
n2 = ListNode.ListNode(7)
n3 = ListNode.ListNode(4)
n4 = ListNode.ListNode(3)
n5 = ListNode.ListNode(2)
n6 = ListNode.ListNode(1)

#orig_head = ListNode.ListNode(1)
#orig_head.set_next(n1)

head.set_next(n1)
n1.set_next(n2)
n2.set_next(n3)
n3.set_next(n4)
n4.set_next(n5)
n5.set_next(n6)

traverse_list(head)
#head1 = reverse_recursive(head)
print "isPalindrome: "+str(chec_pali(head))
