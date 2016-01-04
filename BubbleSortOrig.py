def swap(Ar,x,y):
    temp = Ar[x]
    Ar[x] = Ar[y]
    Ar[y] = temp
    return Ar

def do_bubblesort(Ar):    #O(n*n)
    count = 0;
    for i in range(0,len(Ar)):
        for k in range(len(Ar)-1,i,-1):
            if k == 0: #when k = 0 ; Ar[0] and Ar[-1] will be compared
                break
            elif Ar[k] < Ar[k-1]:
                count = count+1
                print(str(count)+":"+"swap("+str(k)+","+str(k-1)+")")
                Ar = swap(Ar,k,k-1)
    return Ar


# swapped is never made to zero. Buggy here!! Don't see this. O(n)
def do_bubblesort_improved(Ar):
    swapped = 222222
    count = 0
    for i in range(0,len(Ar)):
        if swapped == 0:
            break
        for k in range(len(Ar)-1,i,-1):
            if k == 0:
                break
            elif Ar[k] < Ar[k-1]:
                count += 1
                print(str(count)+":"+"swap("+str(k)+","+str(k-1)+")")
                Ar = swap(Ar,k,k-1)
                swapped = 1
    return Ar


A = [2,1,3,4,5]
print(do_bubblesort(A))

A = [2,1,3,4,5]
print("========================")
print(do_bubblesort_improved(A))