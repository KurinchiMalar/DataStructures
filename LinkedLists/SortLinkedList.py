'''
Write a function to sort linked list - MergeSort
'''

# Time Complexity : O(nlogn)
import ListNode

'''def mergesort_list(head,size):

    if head == None:
        return head

    middle = size // 2

    list2 = head

    for i in range(0,middle):
        list2 = list2.get_next()

    list1 = mergesort_list(head,middle)
    list2 = mergesort_list(list1,size - (middle))
'''
def mergesort(head,size):

    if size <= 1:
        return head

    middle = size//2

    #lefthalf = Ar[:middle]
    #righthalf = Ar[middle:]
    list2 = head

    '''
    say list is 3 5 2 7 6 8 9
                0 1 2 3 4 5 6

            middle = 7/2 = 3

            list2 = 7 6 8 9   # list 2 will start at middle.

    '''
    for i in range(0,middle):
        list2 = list2.get_next()

    list1 = mergesort(head,middle)
    list2 = mergesort(list2,size - middle) # list2 is starting from middle

    print "-----------------------middle: "+str(middle)+"-----------------size: "+str(size)
    traverse_list(list1)
    traverse_list(list2)

    result = merge_two_lists(list1,middle,list2,size-middle)

    traverse_list(result)
    return result


def merge_two_lists(list1,size1,list2,size2):


    if list1 == None:
        return list2

    if list2 == None:
        return list1

    dummy = ListNode.ListNode(-1)

    newlist = dummy
    i = 0
    j = 0

    while i < size1 and j < size2:

        if list1.get_data() < list2.get_data():

            newlist.set_next(list1)
            list1 = list1.get_next()
            i = i + 1

        else:

            newlist.set_next(list2)
            list2 = list2.get_next()
            j = j + 1
        newlist = newlist.get_next()

    while i < size1:
        newlist.set_next(list1)
        list1 = list1.get_next()
        i = i + 1
        newlist = newlist.get_next()

    while j < size2:
        newlist.set_next(list2)
        list2 = list2.get_next()
        j = j + 1
        newlist = newlist.get_next()


    newlist.set_next(None) #### very very importantttttt!!!!!!!!@....other wise yours will be an endless list


    return dummy.get_next()


def get_length_of_list(node):
    current = node
    count = 0
    while current != None:
        count = count + 1
        current = current.get_next()
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

head = ListNode.ListNode(10)
#print ListNode.ListNode.__str__(head)
n1 = ListNode.ListNode(2)
n2 = ListNode.ListNode(13)
n3 = ListNode.ListNode(40)
n4 = ListNode.ListNode(5)
n5 = ListNode.ListNode(19)
n6 = ListNode.ListNode(16)

head.set_next(n1)
n1.set_next(n2)
n2.set_next(n3)
n3.set_next(n4)
n4.set_next(n5)
n5.set_next(n6)
print "Input"
traverse_list(head)

#print ""+str(get_length_of_list(head))
head1 = mergesort(head,get_length_of_list(head))

print "final"
traverse_list(head1)
