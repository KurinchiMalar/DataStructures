'''
 An array A contains n integers from the range X to Y. Also , there is one number that is not in A from range X to Y.
'''

def find_missing_number_in_given_range(Ar,X,Y):

    n = len(Ar)
    S = [-1] * n

    for i in range(0,n):
        S[Ar[i]-X] = Ar[i]

    print S

    for i in range(0,len(S)):
        if S[i] == -1:
            missing_num = i+X
            break

    return missing_num

Ar = [10,16,14,12,11,10,13,15,17,12,19]
print ""+str(find_missing_number_in_given_range(Ar,10,20))


