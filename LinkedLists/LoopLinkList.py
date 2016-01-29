__author__ = 'kurnagar'



import ListNode

# Time Complexity : O(n)
# Space Complexity : O(n)  for hashtable

def check_if_loop_exits_hashtable_method(node):

    if node == None:
        return -1
    hash_table = {}

    current = node

    while current not in hash_table:
        hash_table[current] = current.get_data()
        current = current.get_next()

    #print hash_table
    if current in hash_table:
        print "Loop at: "+ListNode.ListNode.__str__(current)
        return 1



'''
Floyd's Cycle Finding Algorithm
'''
# Time Complexity : O(n)
# Space Complexity : O(1)
def check_if_loop_exits_and_return_loopnode_and_lengthofloop(node):

    if node == None:
        return -1,None,-1

    tort = node
    hare = node

    while tort and hare and hare.get_next():
        tort = tort.get_next()
        hare = hare.get_next().get_next()

        if tort == hare:
            print "tort and hare met at: "+str(ListNode.ListNode.__str__(tort))
            #return 1
            break

    if tort != hare:
        return -1,None # noloop

    meeting_point = tort # will be useed for length of loop and remove loop

    # To find the loop node
    # Bring tort to beginning
    tort = node
    print "tort:"+str(tort.get_data())
    print "hare:"+str(hare.get_data())
    while tort != hare:
        tort = tort.get_next()
        hare = hare.get_next()

    loopnode = tort

    # To find length of loop

    length_of_the_loop = 1 # current meeting point is 1.
    tort = meeting_point
    hare = tort.get_next()

    while tort != hare:
        length_of_the_loop = length_of_the_loop + 1
        hare = hare.get_next()


    return 1,loopnode,length_of_the_loop,meeting_point

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
# Space Complexity : O(1)
def remove_loop(node,loopnode,meeting_point):

    current = meeting_point

    while current.get_next() != loopnode:
        current = current.get_next()

    if current.get_next() == loopnode:
        current.set_next(None)

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
n6.set_next(n2) # loop set here

print "HashTable method : is loop exists: "+str(check_if_loop_exits_hashtable_method(head))
isloop_exists,loopnode,length_of_loop,meeting_point = check_if_loop_exits_and_return_loopnode_and_lengthofloop(head)
print "Check if loop exists: "+str(isloop_exists)
print "Meeting point: "+str(meeting_point)
print "Loop node :"+str(ListNode.ListNode.__str__(loopnode))
print "Length of loop: "+str(length_of_loop)

head = remove_loop(head,loopnode,meeting_point)
print "Removed loop:"+str(traverse_list(head))






















