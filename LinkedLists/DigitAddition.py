'''
    Given two linked lists, each list node with one integer digit, add these two linked lists. Result should be stored in
    third linked list.

    # Head contains the most significant digit

'''

import ListNode

class Result:
    def __init__(self,newNode,carry):
        self.newNode = newNode
        self.carry = carry

def prepareResult(list1, list2):
    headToCopy = None
    if list1 is None:
        headToCopy = list2
    if list2 is None:
        headToCopy = list1
    if headToCopy is None:
        return Result(None, 0)
    head = ListNode.ListNode(headToCopy.data)
    tmpHead = head
    headToCopy = headToCopy.next
    while headToCopy is not None:
        newNode = ListNode.ListNode(headToCopy.data)
        tmpHead.next = newNode
        tmpHead = newNode
        headToCopy = headToCopy.next
    return Result(head, 0)


def add_equal_lists_withcarry(list1,list2):

    if list1 == None and list2 == None:
        return Result(None, 0)

    if (list1 is not None and list2 is None) or (list2 is not None and list1 is None):
        return prepareResult(list1, list2)

    tempResult = add_equal_lists_withcarry(list1.get_next(), list2.get_next())
    cursum = tempResult.carry + list1.get_data() + list2.get_data()
    carry = cursum / 10
    cursumDigit = cursum % 10
    result = ListNode.ListNode(0)
    result.set_next(tempResult.newNode)
    result.set_data(cursumDigit)

    final = Result(result,carry)
    return final

def get_length_of_list(node):
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
    return count

head1 = ListNode.ListNode(9)
#print ListNode.ListNode.__str__(head)
n1 = ListNode.ListNode(3)
n2 = ListNode.ListNode(5)
#n3 = ListNode.ListNode(7)
#n4 = ListNode.ListNode(9)
#n5 = ListNode.ListNode(10)
#n6 = ListNode.ListNode(12)

head2 = ListNode.ListNode(9)
m1 = ListNode.ListNode(4)
m2 = ListNode.ListNode(6)
m3 = ListNode.ListNode(8)
#m4 = ListNode.ListNode(11)
#m5 = ListNode.ListNode(14)
#m6 = ListNode.ListNode(19)

head1.set_next(n1)
n1.set_next(n2)
#n2.set_next(n3)
#n3.set_next(n4)
#n4.set_next(n5)
#n5.set_next(n6)

head2.set_next(m1)
m1.set_next(m2)
m2.set_next(m3)
#m3.set_next(m4)
#m4.set_next(m5)
#m5.set_next(m6)

traverse_list(head1)
traverse_list(head2)
result = add_equal_lists_withcarry(head1,head2)
node = result.newNode
if result.carry > 0:
    node = ListNode.ListNode(0)
    node.set_next(result.newNode)
    node.set_data(result.carry)
traverse_list(node)