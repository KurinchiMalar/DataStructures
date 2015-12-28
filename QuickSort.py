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
        quick_sort(Ar,low,pivot-1)
        quick_sort(Ar,pivot+1,high)

Ar = [5,2,4,1,7,3,9]
quick_sort(Ar,0,len(Ar)-1)
print(str(Ar))
