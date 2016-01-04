def swap(Ar,x,y):
    temp = Ar[x]
    Ar[x] = Ar[y]
    Ar[y] = temp
    #return Ar

def do_selectionsort(Ar):
    for i in range(0,len(Ar)):
        least = i
        for k in range(i,len(Ar)):
            if Ar[k] < Ar[least]:
                swap(Ar,least,k)

    return Ar

A = [9,2,6,1,4,8]
print(do_selectionsort(A))