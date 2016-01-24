'''
    Given an array find longest increasing subsequence in this array.
    https://www.youtube.com/watch?v=CE2b_-XfVDk
'''

# Time Complexity : O(n*n)
# Space Complexity : O(n)

def get_length_of_longest_increasing_subsequence(Ar):

    n = len(Ar)

    T = [1]*(n)

    #print T
    for i in range(1,n):
        for j in range(0,i):
            if Ar[j] < Ar[i]:
                T[i] = max(T[i],T[j]+1) # i contributes to 1 and till now how many increasing in T[j] ==> 1+T[j]
                                        # if T[i] has a bigger number, occurence of -1 should not be reducing it, so see a max...

    #print T

    max_subseq_len = T[0]
    for i in range(1,n):
        if T[i] > max_subseq_len:
            max_subseq_len = T[i]

    return max_subseq_len

def do_binary_search(Ar,T,end,elem):

    start = 0

    while start <= end:

        if start == end:
            return start+1

        middle = (start+end)//2

        if middle < end and Ar[T[middle]] <= elem and elem <= Ar[T[middle+1]]:
            return middle + 1   # we are returning the ceil...

        elif Ar[T[middle]] < elem:
            start = middle+1
        else:
            end = middle -1
    return -1


# https://www.youtube.com/watch?v=S9oUiVYEq7E
# Time Complexity : O(nlogn)
# Space Complexity : O(n)
def longest_increasing_subsequence_nlogn(Ar):

    n = len(Ar)
    T = [0] * (n)
    R = [-1] * (n)

    res_length = 0

    # if greater append
    # if less replace

    for i in range(1,len(Ar)):

        if Ar[i] > Ar[T[res_length]]: # append

            R[i] = T[res_length]
            res_length = res_length + 1
            T[res_length] = i

        else: # replace

            if Ar[i] <= Ar[T[0]]:
                T[0] = i
            else:  # should be between 0 and res_len
                ceil_index = do_binary_search(Ar,T,res_length,Ar[i])
                #print "ceil for : "+str(Ar[i])+" is :"+str(ceil_index)
                T[ceil_index] = i # found the place to put i
                R[i] = T[ceil_index-1]  # put the mapping for i in result.

    #print R
    #print T
    #print  res_length  # holds the end index of T list. Hence the actual length will be res_length + 1

    # to print the sequence..
    index = T[res_length]
    result = []
    result.insert(0,Ar[index])
    while index >= 0:
        if R[index] == -1:
            break
        else:
            result.insert(0,Ar[R[index]])
        index = R[index]

    return res_length+1,result


Ar = [3,4,-1,0,6,2,3]
Ar = [3,4,-1,5,8,2,3,12,7,9,10]
print "length of longest incr subseq O(n*n): "+str(get_length_of_longest_increasing_subsequence(Ar))
print
length,result = longest_increasing_subsequence_nlogn(Ar)
print "length of longest increasing subseq O(nlogn) :"+str(length)
print "longest increasing subseq O(nlogn) :"+str(result)