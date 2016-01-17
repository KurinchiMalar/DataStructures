'''

Permutations of a String: [ ANAGRAMS ]

    Give an algorithm to print all possible permutations of a given string.
'''

# Algorithm Paradigm: Backtracking

# Time Complexity: O(n*n!)
# Space Complexity : O(1)

def print_permutations(Ar,k,n):
    print "--------------------------------"

    #print "permute( "+str(k)+" , "+str(n)+" )"
    if k == n:
        print "".join(Ar)
        return


    for i in range(k,n):
        #print "swap( "+str(i)+","+str(k)+" )"
        Ar[i],Ar[k] = Ar[k],Ar[i]
        #print "         permute( "+str(k+1)+" , "+str(n)+" )"
        print_permutations(Ar,k+1,n)
        #print "swapback( "+str(i)+","+str(k)+" )"
        Ar[i],Ar[k] = Ar[k],Ar[i]


def print_permutations_Iterative(Ar):

    level = [Ar[0]]

    # 0th element already we have taken, from next character keep inputing one by one to our function
    for i in range(1,len(Ar)):
        nList = []   # This is a temp list to hold
                        # nList.append(item+Ar[i])    placing inputchar  at last position.
        for item in level:
            # take every item and append the character from input at the last
            # this will be one permutation, so remaining you have to do for len(item) -1 times.
            # Say level = [AB , BA] and incoming char is C
            '''
            AB
                nList = ABC

                    Then start adding C from 0 to len(AB) -1 ---> 0 = CAB 1 = ACB stop.
                    now you have ABC CAB ACB !!! BINGO
            '''

            nList.append(item+Ar[i])

            for j in range(0,len(item)):
                nList.append(item[0:j] + Ar[i] +item[j:])
        level = nList

    print nList


#def permutations(elems):
#	for perm in permutationByIteration(elems):
#		print perm

mystr = "ABC"
#print_permutations(list(mystr),0,3)
print_permutations_Iterative(list(mystr))
#permutations(list(mystr))
'''
Understanding Permutations Recursive:

perm (0,3)

for i in range (0,3)
--------------------------------

i = 0 , k = 0 , n = 3

				swap( 0,0 )
						 permute( 1 , 3 )
				--------------------------------
				swap( 1,1 )
						 permute( 2 , 3 )
				--------------------------------
				swap( 2,2 )
						 permute( 3 , 3 )
				--------------------------------
				ABC
				swapback( 2,2 )
				swapback( 1,1 )
				swap( 2,1 )
						 permute( 2 , 3 )
				--------------------------------
				swap( 2,2 )
						 permute( 3 , 3 )
				--------------------------------
				ACB
				swapback( 2,2 )
				swapback( 2,1 )
				swapback( 0,0 )

-------------------------------------------------------

i = 1 k = 0, n = 3

				swap( 1,0 )
						 permute( 1 , 3 )
				--------------------------------
				swap( 1,1 )
						 permute( 2 , 3 )
				--------------------------------
				swap( 2,2 )
						 permute( 3 , 3 )
				--------------------------------
				BAC
				swapback( 2,2 )
				swapback( 1,1 )
				swap( 2,1 )
						 permute( 2 , 3 )
				--------------------------------
				swap( 2,2 )
						 permute( 3 , 3 )
				--------------------------------
				BCA
				swapback( 2,2 )
				swapback( 2,1 )
				swapback( 1,0 )

-----------------------------------------------------------

i = 2 k = 0, n = 3
				swap( 2,0 )
						 permute( 1 , 3 )
				--------------------------------
				swap( 1,1 )
						 permute( 2 , 3 )
				--------------------------------
				swap( 2,2 )
						 permute( 3 , 3 )
				--------------------------------
				CBA
				swapback( 2,2 )
				swapback( 1,1 )
				swap( 2,1 )
						 permute( 2 , 3 )
				--------------------------------
				swap( 2,2 )
						 permute( 3 , 3 )
				--------------------------------
				CAB
				swapback( 2,2 )
				swapback( 2,1 )
				swapback( 2,0 )

========================================================================================================================

Understanding Permutations Iterative:

elems = [ABC]


level:['A']
-------------------------------  i: 1
level:['A']
          item:A elems[i]:B
                      nListBefore:[]
                      nListAfter:['AB']
                      j:0 item:A
                      **************nListBefore:['AB']
                      **************nListAfter:['AB', 'BA']
--------------------------------------
-------------------------------  i: 2
level:['AB', 'BA']
          item:AB elems[i]:C
                      nListBefore:[]
                      nListAfter:['ABC']
                      j:0 item:AB
                      **************nListBefore:['ABC']
                      **************nListAfter:['ABC', 'CAB']
                      j:1 item:AB
                      **************nListBefore:['ABC', 'CAB']
                      **************nListAfter:['ABC', 'CAB', 'ACB']
          item:BA elems[i]:C
                      nListBefore:['ABC', 'CAB', 'ACB']
                      nListAfter:['ABC', 'CAB', 'ACB', 'BAC']
                      j:0 item:BA
                      **************nListBefore:['ABC', 'CAB', 'ACB', 'BAC']
                      **************nListAfter:['ABC', 'CAB', 'ACB', 'BAC', 'CBA']
                      j:1 item:BA
                      **************nListBefore:['ABC', 'CAB', 'ACB', 'BAC', 'CBA']
                      **************nListAfter:['ABC', 'CAB', 'ACB', 'BAC', 'CBA', 'BCA']
--------------------------------------



'''
