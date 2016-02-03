__author__ = 'kurnagar'

'''
There are n people standing in a circle waiting to be executed. The counting out begins at some point in the circle and proceeds around the circle in a fixed direction.
 In each step, a certain number of people are skipped and the next person is executed. The elimination proceeds around the circle (which is becoming smaller and smaller as the executed people are removed),
 until only the last person remains, who is given freedom.
Given the total number of persons n and a number k which indicates that k-1 persons are skipped and kth person is killed in circle.
The task is to choose the place in the initial circle so that you are the last one remaining and so survive.

For example, if n = 5 and k = 2, then the safe position is 3.
    Firstly, the person at position 2 is killed, then person at position 4 is killed, then person at position 1 is killed. Finally, the person at position 5 is killed. So the person at position 3 survives.

If n = 7 and k = 3, then the safe position is 4. The persons at positions 3, 6, 2, 7, 5, 1 are killed in order, and person at position 4 survives.
'''
import ListNode

def traverse_clist(node):
    current = node
    count = 0
    while current.get_next() != node:
        print current.get_data(),
        count = count + 1
        current = current.get_next()

    print current.get_data(),
    print
    return count+1



# Time Complexity :O(nk)  ~~ O(n)
def find_survior_JosephusCircle(n,m):

    if n == None:
        return 0

    # initialize circular linked list (JosephusCircle)

    head = ListNode.ListNode(1)
    prev = head
    for i in range(2,n+1):
        current = ListNode.ListNode(i)
        prev.set_next(current)
        prev = current

    prev.set_next(head)
    print "len: "+str(traverse_clist(head))

    # chop every kth member

    count = 0

    prev = ListNode.ListNode(-1) # dummy
    current = head
    answer = []
    kill = []
    while current.get_next() != current:
        count = count + 1
        # chop this guy
        if count == m:
            count = 0
            #traverse_clist(head)
            kill.append(current.get_data())
            prev.set_next(current.get_next())

            current = current.get_next()
            #traverse_clist(head)
            # removed current
            #answer.append(current.get_data())
        else:
            prev = current
            current = current.get_next()


    answer.append(current.get_data())
    print "We kill: "+str(kill)
    print "Safe position: "+str(answer)


find_survior_JosephusCircle(5,2)
#find_survior_JosephusCircle(7,3)