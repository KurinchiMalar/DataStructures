'''
    Given two lists

        list1 = [A1,A2,.....,An]
        list2 = [B1,B2,....,Bn]

        merge these two into a third list

        result = [A1 B1 A2 B2 A3 ....]
'''

# Time Complexity : O(n)
# Space Complexity : O(1)
import ListNode
import copy

def merge_zigzag(node1,node2,m,n):

    if node1 == None or node2 == None:
        return node1 or node2

    p = node1
    q = p.get_next()
    r = node2
    s = r.get_next()

    while q != None and s != None:

        p.set_next(r)
        r.set_next(q)

        p = q
        if q != None:
            q = q.get_next()

        r = s
        if s != None:
            s = s.get_next()

    if q == None:
        p.set_next(r)

    if s == None:
        p.set_next(r)
        r.set_next(q)

    return node1


def get_len_of_list(node):
    current = node
    count = 0
    while current != None:
        #print current.get_data(),
        count = count + 1
        current = current.get_next()
    #print
    return count

def traverse_list(node):
    current = node
    count = 0
    while current != None:
        print current.get_data(),
        count = count + 1
        current = current.get_next()
    print

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

traverse_list(head1)
traverse_list(head2)

m = get_len_of_list(head1)
n = get_len_of_list(head2)
result = merge_zigzag(head1,head2,m,n)

print "RESULT:"
traverse_list(result)


