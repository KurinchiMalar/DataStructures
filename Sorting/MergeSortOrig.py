
def do_mergeSort(Ar):
    if len(Ar) > 1:
        middle = len(Ar) / 2
        lefthalf = Ar[:middle]
        righthalf = Ar[middle:]
        do_mergeSort(lefthalf)
        do_mergeSort(righthalf)
        i=j=k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                Ar[k] = lefthalf[i]
                i += 1
            else:
                Ar[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            Ar[k] = lefthalf[i]
            k += 1
            i += 1

        while j < len(righthalf):
            Ar[k] = righthalf[j]
            k += 1
            j += 1

Ar = [8,7,6,5,4,3,2,1]
do_mergeSort(Ar)
print(Ar)