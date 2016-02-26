# a+b+c = k
'''This can be done in O(1) space and O(N2) time.
First lets solve a simpler problem:
Given two arrays A and B pick one element from each so that their sum is equal to given number K.

Sort both the arrays which takes O(NlogN).
Take pointers i and j so that i points to the start of the array A and j points to the end of B.
Find the sum A[i] + B[j] and compare it with K

if A[i] + B[j] == K we have found the pair A[i] and B[j]
if A[i] + B[j] < K, we need to increase the sum, so increment i.
if A[i] + B[j] > K, we need to decrease the sum, so decrement j.
This process of finding the pair after sorting takes O(N).

Now lets take the original problem. We've got a third array now call it C.

So the algorithm now is :

foreach element x in C
  find a pair A[i], B[j] from A and B such that A[i] + B[j] = K - x
end for
The outer loop runs N times and for each run we do a O(N) operation making the entire algorithm O(N2).'''


from HeapSort import Heap
from SumExistsTwoLists import is_two_nos_sum_is_k_Exists_method2
ob = Heap()
# n + (nlogn +n)  = nlogn + n
def is_sum_exists_three_lists(A,B,C,ksum):

    for i in range(0,len(C)-1):
        diff = ksum - C[i]
        print diff
        if is_two_nos_sum_is_k_Exists_method2(A,B,diff) == True:
            print C[i]
            return True
    return False



A = [6,3,7,1,2]
B = [5,1,2,4,6]
C = [3,4,2,1,5]
print str(is_sum_exists_three_lists(A,B,C,15))
