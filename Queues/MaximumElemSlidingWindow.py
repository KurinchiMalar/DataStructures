'''Given an array and an integer k, find the maximum for each and every contiguous subarray of size k.

Examples:

Input :
arr[] = {1, 2, 3, 1, 4, 5, 2, 3, 6}
k = 3
Output :
3 3 4 5 5 5 6

Input :
arr[] = {8, 5, 10, 7, 9, 4, 15, 12, 90, 13}
k = 4
Output :
10 10 10 15 15 90 90'''

# Time Complexity : O(n)
# Space Complexity : O(k)
import DoubleEndedQueue
def get_maximum_elem_sliding_window(Ar,k):

    dq = DoubleEndedQueue.DEQ()
    result = []

    #   /* Process first k (or first window) elements of array */
    i = 0
    while i < k:
         # if current greater, keep popping.
         #  idea: largest of this window should be in front of queue.
        while dq.get_size() > 0 and Ar[i] >= Ar[dq.peek_tail()]:
            dq.pop_back()

        dq.push_back(i)  # append.
        i = i + 1
    dq.print_deq()
    #print dq.peek_head()
    #result.append(Ar[dq.peek_head()])
    #print result
    # start of next window.
    #print i
    #Process rest of the elements, i.e., from arr[k] to arr[n-1]
    while i < len(Ar):
        print "****************************************"

        result.append(Ar[dq.peek_head()])
        print "i: "+str(i)+"  result: "+str(result)

        # remove the indices not belonging to this window.
        #  i - k   --> if i is 5 --> 5-3 = 2.... window [3,4,5]


        dq.print_deq()

        while dq.get_size() > 0 and dq.peek_head() <= i-k:
            ret = dq.pop_front()
            print ret
            if ret == -1:
                break

        dq.print_deq()

        # if current greater, keep popping.
         #  idea: largest of this window should be in front of queue.

        while dq.get_size() > 0 and Ar[i] >= Ar[dq.peek_tail()]:
            ret = dq.pop_back()
            if ret == -1:
                break

        print "now: "+str(dq.get_size())
        dq.print_deq()
        dq.push_back(i)  # append.'''
        i = i + 1

    if dq.get_size() != 0:
        result.append(Ar[dq.peek_head()])
        dq.pop_front()
    print result
#Ar = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
Ar = [4,3,2,1,5,7,6,8,9]
get_maximum_elem_sliding_window(Ar,3)