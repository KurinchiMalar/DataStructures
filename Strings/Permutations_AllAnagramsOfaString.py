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

mystr = "ABC"
print_permutations(list(mystr),0,3)

'''
Understanding Permutations:

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

'''