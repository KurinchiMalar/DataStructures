
def swap(A,x,y):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp

def partition(A,low,high):
    pivot = low
    swap(A,pivot,high)
    for i in range(low,high):
        if A[i] <= A[high]:
            swap(A,low,i)
            low += 1
    swap(A,low,high)
    return low

def quickSort_impl(A,low,high):
    if low < high:
        pivot = partition(A,low,high)
        quickSort_impl(A,low,pivot)
        quickSort_impl(A,pivot+1,high)

def do_quickSort(A):
    quickSort_impl(A,0,len(A)-1)

A = [3,1,5,7,2,9,8]
A = [8,7,6,5,4,3,2,1]
A = [5]
do_quickSort(A)
print(A)
