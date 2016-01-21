'''
Find the median of two sorted arrays in O(logn) --> Divide and Conquer (Binary Search)
'''
'''
Example:

   ar1[] = {1, 5, 7, 10, 13}
   ar2[] = {11, 15, 23, 30, 45}

Middle element of ar1[] is 7. Let us compare 7 with 23 and 30,
    since 7 smaller than both 23 and 30,

    move to right in ar1[].
        Do binary search in {10, 13}, this step will pick 10.
            Now compare 10 with 15 and 23.
    Since 10 is smaller than both 15 and 23,
            again move to right.
            Only 13 is there in right side now.
    Since 13 is greater than 11 and smaller than 15, terminate here. We have got the median as 12 (average of 11 and 13)
'''
# Time Complexity : O(log n)

def get_median_divide_and_conquer(A,B,low,high,n):

    # we have reached the end of A array... median should be in B array :)
    if low > high:
        return get_median_divide_and_conquer(B,A,0,n-1,n) # --> search in B

    i = (low + high) // 2
    j = n-1-i    # find the ith index in B array... n-1 - i

    # Base condition

    if A[i] >= B[j] and A[i] <= B[j+1]:

        return (A[i]+B[j]) // 2

    # current element in A greater than both j and j+1 in B --> go to left half of A
    elif A[i] > B[j] and A[i] > B[j+1]:

        return get_median_divide_and_conquer(A,B,low,i-1,n)

    else:
        return get_median_divide_and_conquer(A,B,i+1,high,n)    # --> go to right half of A

A = [1, 12, 15, 26, 38]
B = [2, 13, 17, 30, 45]

print "Median : "+str(get_median_divide_and_conquer(A,B,0,4,5))

'''
A variation:

The question is how we can find the median of a receiving stream of integer values(e.g. for 12, 14, 252, 243, 15 the median is 15) in O(log N) where N is number of values. Please note that we have a stream of integer values, hence by receiving each value, we have to re-find the median.

Example:

  | Input | median
1 |   12  |   12
2 |   14  |   13 = (12+14)/2
3 |   252 |   14
.
.
.

P.S: An example of using this algorithm could be filtering an image.




Okay, with the update to the question so the intent is clear (not just find the median, but re-find the median each time you receive a new number), I think there's a way.

I'd start with a pair of heaps: a max-heap and a min-heap.

    The min-heap will contain the numbers larger than the median,

    and the max-heap the numbers smaller than the median.


    When you receive the first number, that's your median.

    When you receive the second,
            you insert the smaller of the two into the max-heap,
            and the larger of the two into the min-heap.

    The median is then the average of the smallest on the min-heap, and the largest on the max-heap.



Along with the two heaps,

    you'll want storage for a single integer that will be
        the current median when you've received an odd number of inputs.
        You'll populate that fairly simply: if you receive an input with it currently empty, you basically sort those two items and insert the smaller into the heap for the smaller items, and larger into the heap for larger items. Your new median will then be the mean of the bases of those two heaps (and you'll mark the other storage location as empty).

When you receive a new number with that empty, you'll compare the new number to the median. If it's between the numbers as the bases of the heaps, it's the new median, and you're done. Otherwise, extract the number from the base that must hold the median (larger numbers of the new number is larger, smaller if it's smaller) and put it into the median spot, then insert the new number into heap that came from.

At least if memory serves, the extract/insert into a heap should be O(log N). I believe everything else involved should be constant complexity.


'''
