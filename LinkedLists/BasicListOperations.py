# Link on shallow and deep copy. - USEFUL
# http://stackoverflow.com/questions/17246693/what-exactly-is-the-difference-between-shallow-copy-deepcopy-and-normal-assignm

import ListNode
import copy

# Time Complexity : O(n)
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
def get_length_of_list(node):
    length = traverse_list(node)
    return length

# insert
# Time Complexity : O(1)
def insert_at_beginning(node,data):
    newnode = ListNode.ListNode(data)
    if node == None:
        return newnode

    newnode.set_next(node)
    return newnode

# Time Complexity : O(n)
def insert_at_end(node,data):
    newnode = ListNode.ListNode(data)
    if node == None:
        return newnode

    current = node
    while current.get_next() != None:
        current = current.get_next()

    current.set_next(newnode)
    return node

# Time Complexity : O(n) worst case
def insert_at_middle(node,data,pos):
    newnode = ListNode.ListNode(data)
    if node == None:
        return newnode

    current = node
    count = 0
    while current.get_next() != None:
        count = count + 1
        current = current.get_next()

        if count == pos:
            newnode.set_next(current.get_next())
            current.set_next(newnode)
            break
    return node

# search
# Time Complexity : O(n) worst case
def search_in_list(node,data):

    if node == None:
        return -1

    while node != None :
        if node.get_data() == data:
            return 1

        node = node.get_next()
    return -1

# Delete
# Time Complexity : O(1)
def delete_at_beginning(node):
    if node == None:
        return None

    node = node.get_next()
    return node

# Time Complexity : O(n) Worst Case
def delete_at_end(node):
    if node == None:
        return None
    current = node
    prev = None
    while current.get_next() != None:
        prev = current
        current = current.get_next()

    prev.set_next(None)
    return node

# Time Complexity : O(n) Worst case
def delete_at_middle(node,pos):
    if node == None:
        return None

    if pos == 1:
        return delete_at_beginning(node)

    count = 1
    prev = None
    current = node

    while current != None:
        prev = current
        count = count + 1
        current = current.get_next()
        if count == pos:
            prev.set_next(current.get_next())
            break
    return node

# Time Complexity : O(n) WorstCase
def delete_given_data(node,data):
    if node == None:
        return None

    if node.get_data() == data:
        return delete_at_beginning(node)
    prev = None
    current = node

    while current != None:
        if current.get_data() == data:
            prev.set_next(current.get_next())
            break

        prev = current
        current = current.get_next()

    return node

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

orig_head = copy.deepcopy(head)

length = get_length_of_list(head)
print "Length of orig list: "+ str(length)
print "----------------------------"
head = insert_at_beginning(head,8)
print"Insert At beginning length of list now: "+str(traverse_list(head))

head = copy.deepcopy(orig_head)
head = insert_at_end(head,8)
print"Insert At End length of list now: "+str(traverse_list(head))


head = copy.deepcopy(orig_head)
head = insert_at_middle(head,8,2)
print"Insert At Middle length of list now: "+str(traverse_list(head))
print "----------------------------"

head = copy.deepcopy(orig_head)

print "Search data isFound = : "+str(search_in_list(head,7))
print "Search data isFound = : "+str(search_in_list(head,8))
print "----------------------------"

head = copy.deepcopy(orig_head)
head = delete_at_beginning(head)
print "Delete at beginning length of list now: "+str(traverse_list(head))

head = copy.deepcopy(orig_head)
head = delete_at_end(head)
print "Delete at end length of list now: "+str(traverse_list(head))

head = copy.deepcopy(orig_head)
head = delete_at_middle(head,3)
print "Delete at middle given pos length of list now: "+str(traverse_list(head))

head = copy.deepcopy(orig_head)
head = delete_given_data(head,5)
print "Delete at given data length of list now: "+str(traverse_list(head))
print "----------------------------"
