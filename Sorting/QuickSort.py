'''quick(0,4)
quick(5,6)
----------------------------------------
quick(0,1)
quick(2,3)
----------------------------------------
quick(2,2)
quick(3,3)
----------------------------------------
quick(5,6)
quick(7,6)
----------------------------------------
[1, 2, 3, 4, 5, 7, 9]
'''
def swap(Ar,x,y):
    temp = Ar[x]
    Ar[x] = Ar[y]
    Ar[y] = temp

def partition(Ar,low,high):
    pivot = low
    swap(Ar,pivot,high)
    for i in range(low,high):
        if Ar[i] <= Ar[high]: # we have swapped pivot and high... so high is the pivot now.
            swap(Ar,low,i)
            low = low + 1

    swap(Ar,low,high) #swap back high (which is pivot) to original and return it. {lesss than pivot |PIVOT| more than pivot}
    return low

def quick_sort(Ar,low,high):
    if low < high:
        pivot = partition(Ar,low,high)
        print ("quick("+str(low)+","+str(pivot-1)+")")
        print ("quick("+str(pivot+1)+","+str(high)+")")
        print("----------------------------------------")
        return quick_sort(Ar,low,pivot-1)
        return quick_sort(Ar,pivot+1,high)
    return Ar

Ar = [5,2,4,1,7,3,9]
quick_sort(Ar,0,len(Ar)-1)
print(str(Ar))
