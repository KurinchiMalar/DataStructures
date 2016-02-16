'''
    Given a singly linked list L : L1 -> L2 -> L3 -> ......-> Ln-1 -> Ln

    reoder it to: L1 -> Ln -> L2 -> Ln-1 .....
'''

from LinkedLists import ListNode
import Stack

# Time Complexity : O(n + n/2) = O(n)
# Space Complexity : O(n)

def reorder_list_using_stack(node):

    if node.get_next() == None: # only one node
        return node

    if node.get_next().get_next() == None: # only two nodes
        return node

    hare = node
    tort = node
    # find middle node
    while hare != None and hare.get_next() != None:
        tort = tort.get_next()
        hare = hare.get_next().get_next()

    #print ListNode.ListNode.__str__(tort)
    temp = tort
    stack = Stack.Stack()
    while temp != None:
        stack.push(temp.get_data())
        temp = temp.get_next()
    #stack.print_stack()
    p = node
    q = p.get_next()

    while stack.size > 0:
        #print stack.peek()
        if p == tort:
            p.set_next(None)
            break
        if q == tort:
            q.set_next(None)
            break
        p.set_next(stack.pop())
        p.get_next().set_next(q)
        p = q
        q = p.get_next()

    return node

# Time Complexity: O(n)
# Space Complexity : O(1)

def reorder_list_without_stack_ReverseAndMerge(node):

    if node.get_next() == None: # only one node
        return node

    if node.get_next().get_next() == None: # only two nodes
        return node

    hare = node
    tort = node
    prev = None
    odd_middle_node = None
    later_half = None

    # find middle node
    while hare != None and hare.get_next() != None:
        prev = tort
        tort = tort.get_next()
        hare = hare.get_next().get_next()

    #print ListNode.ListNode.__str__(tort)

    if hare == None: # even
        print "Even"
        prev.set_next(None)
        list2 = tort
        later_half = rev_list(list2)
    elif hare.get_next() == None: # odd
        print "odd"
        odd_middle_node = tort
        prev.set_next(None)
        list2 = tort.get_next()
        later_half = rev_list(list2)

    traverse_list(node)
    traverse_list(later_half)
    result = merge_zigzag_lists(node,later_half,odd_middle_node)
    traverse_list(result)

def merge_zigzag_lists(list1,list2,odd_middle_node):
    if list1 == None and list2 == None:
        return None

    if list1 == None or list2 == None:
        return list1 or list2

    p = list1
    q = p.get_next()

    r = list2
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

    if s == None:
        p.set_next(r)
        if odd_middle_node != None:
            odd_middle_node.set_next(None)
            r.set_next(odd_middle_node)
    elif q == None:
        if odd_middle_node != None:
            odd_middle_node.set_next(None)
            r.set_next(odd_middle_node)
        #r.set_next(q)

    #if odd_middle_node != None:
    return list1



def rev_list(current):
    if current == None:
        return
    if current.get_next() == None:
        head = current
        return head


    head = rev_list(current.get_next())
    current.get_next().set_next(current)
    current.set_next(None)
    return head


def traverse_list(node):
    current = node
    count = 0
    while current != None:
        print current.get_data(),
        count = count + 1
        current = current.get_next()
    print
    #return count

head = ListNode.ListNode(1)
#print ListNode.ListNode.__str__(head)
n1 = ListNode.ListNode(2)
n2 = ListNode.ListNode(3)
n3 = ListNode.ListNode(4)
n4 = ListNode.ListNode(5)
n5 = ListNode.ListNode(6)
n6 = ListNode.ListNode(7)

head.set_next(n1)
n1.set_next(n2)
n2.set_next(n3)
n3.set_next(n4)
n4.set_next(n5)
n5.set_next(n6)

traverse_list(head)
#result = reorder_list_using_stack(head)
#traverse_list(result)

#reversed = rev_list(head)
#traverse_list(reversed)

reorder_list_without_stack_ReverseAndMerge(head)