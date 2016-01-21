

def partition(Ar,low,high,elem):

    i = low

    while i <= high: # on using for with range, i am not able to modify the iterator i....it goes sequentially range(low,high)

        if Ar[i] < elem:
            Ar[i],Ar[low] = Ar[low],Ar[i]
            low = low + 1

        elif Ar[i] == elem and i < high:   # when elem at high index is equal to elem given...cycle will be formed on i = i-1 and i = i+1
            Ar[i],Ar[high] = Ar[high],Ar[i]
            i = i - 1   # because we dont want i to get incremented after swapping with high.
        i = i + 1


    Ar[low],Ar[high] = Ar[high],Ar[low]
    return low


def match_nuts_with_bolts(nuts,bolts,low,high):

    if low < high:

        # take random element from nut and partition in bolt , say the random is nuts[high]
        pivot = partition(bolts,low,high,nuts[high])
        print "Bolts: "+str(bolts)+"pivot : "+str(bolts[pivot])

        # partition nuts with the picked bolt
        mached_nut = partition(nuts,low,high,bolts[pivot])
        print "Nuts: "+str(nuts)+"pivot : "+str(nuts[mached_nut])


        match_nuts_with_bolts(nuts,bolts,low,pivot-1)
        match_nuts_with_bolts(nuts,bolts,pivot+1,high)

nuts = [5, 1, 9, 4, 14, 10]
bolts = [10, 5, 1, 9, 14, 4]

#nuts = [10,5,1,9,14,4]
#bolts = [1,10,14,5,4,9]
#print ""+str(partition(nuts,0,5,4))

match_nuts_with_bolts(nuts,bolts,0,5)
print "Nuts: "+str(nuts)
print "Bolts: "+str(bolts)


