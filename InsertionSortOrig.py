def do_InsertionSort(Ar):
    for i in range(1,len(Ar)):
        temp = Ar[i]
        k = i
        while k > 0 and temp < Ar[k-1]:
            Ar[k] = Ar[k-1]
            k-=1
        Ar[k] = temp
    return Ar

A = [5,7,6,1,4]
A = [4,3,2,1]
print(do_InsertionSort(A))
