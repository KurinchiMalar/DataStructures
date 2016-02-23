'''
    Given a string, write a python method to check whether is palindrome or not , using doubly ended queue.
'''

# Time Complexity : O(n)
# Space Complexity : O(n)

import DoubleEndedQueue

def isPalindrome(mystring):

    dq = DoubleEndedQueue.DEQ()
    for elem in mystring:
        dq.push_back(elem)

    dq.print_deq()

    isPali = True
    while dq.get_size() > 1:
        first = dq.pop_back().get_data()
        last = dq.pop_front().get_data()
        print "first: "+str(first)

        if first != last:
            isPali = False
            return isPali

    return isPali


mystring = "madam"
mystring = "madamam"
mystring = "aa"

print "isPalindrome: "+str(isPalindrome(mystring))