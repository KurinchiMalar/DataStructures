def counting_sort(Ar,k):
    B = [0 for el in Ar]
    C = [0 for el in range(0,k+1)]
    print "Ar :"+str(Ar)
    print "B :"+str(B)
    print "C :"+str(C)

    for j in range(0,len(Ar)): #Build the counting array...how many times current index has occured in original Ar
        C[Ar[j]] = C[Ar[j]] + 1

    print "C now :"+str(C)

    # Build array such that each index says "I have x number of smaller elements in result array less than or equal to x"
    for j in range(1,k+1):
        C[j] = C[j-1] +  C[j]

    print "C new :" + str(C)

    #Put element 5 in input array = C[5] - 1 th position in Result array B.
    # In this eg) 5 in input array = 6th position (C[5] - 1) in B
    # Then subtract 1 since one occurence is captured in result already now.
    for i in range(len(Ar)-1,-1,-1):
        B[C[Ar[i]]-1] = Ar[i]
        C[Ar[i]] = C[Ar[i]] - 1
        #print B[C[Ar[i]]-1]

    print "Result :" + str(B)

if __name__ == '__main__':
    Ar = [5,2,3,1,2,3,0]
    counting_sort(Ar,5)
