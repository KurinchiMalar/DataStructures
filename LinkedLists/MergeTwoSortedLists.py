import ListNode
import copy
def traverse_list(node):
    current = node
    count = 0
    while current != None:
        print current.get_data(),
        count = count + 1
        current = current.get_next()
    print
    return count

# Time Complexity :O(min(m,n)) where m and n are the lengths of the two lists
# Space Complexity :O(1)

'''
FOUR POINTERS -  mainhead,p,q,r
'''
def merge_two_sorted_lists_fourpointers(node1,node2):

    if node1 == None and node2 != None:
        return node2

    if node1 != None and node2 == None:
        return node1

    if node1 == None and node2 == None:
        return None

    # initialze mainhead of result list
    mainhead = None

    if node1.get_data() <= node2.get_data():
        mainhead = node1
        p = node1
        q = node1.get_next()
        r = node2
    else:
        mainhead = node2
        p = node2
        q = node2.get_next()
        r = node1

    while q != None and r != None:

        if q.get_data() <= r.get_data():

            while q.get_data() <= r.get_data():
                p.set_next(q)
                p = p.get_next()
                q = q.get_next()
                if q == None:
                    break
        else:

            while r.get_data() <= q.get_data():
                p.set_next(r)
                p = p.get_next()
                r = r.get_next()
                if r == None:
                    break


    return mainhead

# Time Complexity : O(min(m,n))
# Space Complexity : O(1) ... 1 extra dummy node in the beginnning.

'''
MORE NEAT


Two pointers + One dummy node

Uses only mainhead and a pointer p.
'''
def merge_two_sorted_lists_with_onlytwopointer(node1,node2):

    if node1 == None and node2 != None:
        return node2

    if node1 != None and node2 == None:
        return node1

    if node1 == None and node2 == None:
        return None

    mainhead = ListNode.ListNode(-1)

    p = mainhead

    while node1 != None and node2 != None:

        if node1.get_data() <= node2.get_data():

            p.set_next(node1)
            node1 = node1.get_next()
        else:

            p.set_next(node2)
            node2 = node2.get_next()

        p = p.get_next()


    if node1 == None:
        p.set_next(node2)
    else:
        p.set_next(node1)

    traverse_list(mainhead.get_next())

head1 = ListNode.ListNode(1)
#print ListNode.ListNode.__str__(head)
n1 = ListNode.ListNode(3)
n2 = ListNode.ListNode(5)
n3 = ListNode.ListNode(7)
n4 = ListNode.ListNode(9)
n5 = ListNode.ListNode(10)
n6 = ListNode.ListNode(12)

head2 = ListNode.ListNode(2)
m1 = ListNode.ListNode(4)
m2 = ListNode.ListNode(6)
m3 = ListNode.ListNode(8)
m4 = ListNode.ListNode(11)
m5 = ListNode.ListNode(14)
m6 = ListNode.ListNode(19)

head1.set_next(n1)
n1.set_next(n2)
n2.set_next(n3)
n3.set_next(n4)
n4.set_next(n5)
n5.set_next(n6)

head2.set_next(m1)
m1.set_next(m2)
m2.set_next(m3)
m3.set_next(m4)
m4.set_next(m5)
m5.set_next(m6)

orig_head1 = copy.deepcopy(head1)
orig_head2 = copy.deepcopy(head2)

print "list1: "+str(traverse_list(head1))
print
print "list2: "+str(traverse_list(head2))
print
finallist = merge_two_sorted_lists_fourpointers(head1,head2)

print "WITH FOUR POINTERS:  finallist is above, and length is:"+str(traverse_list(finallist))
print "----------------------------------------------------------------"
traverse_list(orig_head1)
traverse_list(orig_head2)
head1 = orig_head1
head2 = orig_head2
finallist = merge_two_sorted_lists_with_onlytwopointer(head1,head2)
print "WITH TWO POINTERS:  finallist is above, and length is:"+str(traverse_list(finallist))


