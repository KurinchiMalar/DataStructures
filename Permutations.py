
'''
k = level (0,1,2) for ABC
i = iterate at a node. At k =0 , i = 0,1,2
                          k = 1, i = 1,2
                            k = 2 ==> print Ar
'''
# Time Complexity : O(n!)
def permute(Ar,k,n):

    if k >= n:
        print "".join(Ar),
        return

    for i in range(k,n):

        Ar[i],Ar[k] = Ar[k],Ar[i]
        permute(Ar,k+1,n)
        Ar[i], Ar[k] = Ar[k],Ar[i]

def combinations(input):

    level = [""]
    for elem in input:
        print "Elem: "+str(elem)
        next_level = []
        for item in level:
            next_level.append(item+elem)

        print "Next_level: "+str(next_level)
        level.extend(next_level)
        print "level: "+str(level)
    print level[1:]

Ar = "ABC"
#print Ar.split()
print list(Ar)
permute(list(Ar),0,3)
combinations(list(Ar))
