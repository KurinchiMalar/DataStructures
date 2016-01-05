
'''
lefthalf:[5, 2, 4]
righthalf:[1, 7, 3, 9]
lefthalf:[5]
righthalf:[2, 4]
lefthalf:[2]
righthalf:[4]
...Ar[0] - 2
...Ar[1] - 4
...Ar[0] - 2
...Ar[1] - 4
...Ar[2] - 5
lefthalf:[1, 7]
righthalf:[3, 9]
lefthalf:[1]
righthalf:[7]
...Ar[0] - 1
...Ar[1] - 7
lefthalf:[3]
righthalf:[9]
...Ar[0] - 3
...Ar[1] - 9
...Ar[0] - 1
...Ar[1] - 3
...Ar[2] - 7
...Ar[3] - 9
...Ar[0] - 1
...Ar[1] - 2
...Ar[2] - 3
...Ar[3] - 4
...Ar[4] - 5
...Ar[5] - 7
...Ar[6] - 9
Array:[1, 2, 3, 4, 5, 7, 9]
'''
def mergesort(Ar):
    if len(Ar) <= 1: # requires atleast two elements to find middle
        return
    middle = len(Ar)//2
    lefthalf = Ar[:middle]
    righthalf = Ar[middle:]
    #print "lefthalf:"+str(lefthalf)
    #print "righthalf:"+str(righthalf)

    mergesort(lefthalf)
    mergesort(righthalf)

    i = j = k = 0
    #j = 0
    #k = 0

    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            Ar[k] = lefthalf[i]
            i = i+1
        else:
            Ar[k] = righthalf[j]
            j = j+1
        #print "...Ar["+str(k)+"] - "+str(Ar[k])
        k = k+1

    while i < len(lefthalf):
        Ar[k] = lefthalf[i]
        #print "...Ar["+str(k)+"] - "+str(Ar[k])
        i=i+1
        k=k+1

    while j < len(righthalf):
        Ar[k] = righthalf[j]
        #print "...Ar["+str(k)+"] - "+str(Ar[k])
        j=j+1
        k=k+1
    return Ar

# = [5,2,4,1,7,3,9]
'''Ar = [6,4,9,2,1,4,3,8,0,12,5]

print "output"+str(mergesort(Ar))'''


