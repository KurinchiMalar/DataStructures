__author__ = 'kurnagar'

# Permutations Complexity : O(n*n!)
# Combinations Complexity : O(2 pow n)

def get_permutations_recursive(Ar,k):

    if k >= len(Ar):

        print "".join(Ar)
        return


    for i in range(k,len(Ar)):

        Ar[i],Ar[k] = Ar[k],Ar[i] # fixing current k.
        get_permutations_recursive(Ar,k+1)   #   current k+1 becomes next i.
        Ar[i],Ar[k] = Ar[k],Ar[i]

def get_permutations_iterative(Ar):

    level =[Ar[0]]
    for i in range(1,len(Ar)):

        nList =[]

        for item in level:
            nList.append(item+Ar[i])
            for j in range(0,len(item)):
                nList.append(item[0:j]+Ar[i]+item[j:])

        level = nList


    print level

def get_combinations_recursive(Ar,tempresult,result,idx):


    for i in range(idx,len(Ar)):

        tempresult += Ar[i]
        result.append(tempresult)
        #print result

        get_combinations_recursive(Ar,tempresult,result,i+1)

        tempresult = tempresult[0:-1]


    return result

def get_combinations_iterative(Ar):

    level = [""]
    for i in range(0,len(Ar)):

        nList = []

        for item in level:

            nList.append(item+Ar[i])

        level += nList

    print level

mystr = "abc"

#get_permutations_recursive(list(mystr),0)
#get_permutations_iterative(list(mystr))

result = get_combinations_recursive(list(mystr),"",[],0)
print result

get_combinations_iterative(list(mystr))




