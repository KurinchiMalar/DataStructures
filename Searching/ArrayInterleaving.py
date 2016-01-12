
'''
You'll notice the first and last element are already in place, so we don't need to worry about them.
We will keep a left index variable which represents the first item in the first half of the array that needs changed.
 After that we set a right index variable to the first item in the 2nd half of the array that needs changed.
  Now all we do is swap the item at the right index down one-by-one until it reaches the left index item.
   Increment the left index by 2 and the right index by 1, and repeat until
        the indexes overlap or the left goes past the right index (the right index will always end on the last index of the array).
We increment the left index by two every time because the item at left + 1 has already naturally fallen into place.
'''
# BruteForce

# Time Complexity : O(n*n)

def array_interleaving_bruteforce(Ar):

    left = 1
    right = len(Ar)//2

    while left < right:
        print "----------------------------------------------"


        #for i in range(right,left,-1):
        i = right
        while i > left:
            print "(left,right):"+str(left)+","+str(right)
            print
            print "swapping("+str(Ar[i])+","+str(Ar[i-1])+")"
            Ar[i],Ar[i-1] = Ar[i-1],Ar[i]
            i = i - 1

        left = left + 2
        right = right + 1

'''
['a1', 'a2', 'a3', 'a4', 'b1', 'b2', 'b3', 'b4']
 i = 1
 j = 0
swapping(3,4)
---------------------
 i = 2
 j = 0
swapping(2,3)
 j = 1
swapping(4,5)
---------------------
 i = 3
 j = 0
swapping(1,2)
 j = 1
swapping(3,4)
 j = 2
swapping(5,6)
---------------------
['a1', 'b1', 'a2', 'b2', 'a3', 'b3', 'a4', 'b4']
'''

def interleave_careercup(Ar):
  n = len(Ar)//2;
  for i in range(1,n):
    print " i = "+str(i)
    for j in range(0,i):
        print " j = "+str(j)
        print "swapping("+str(n-i+2*j)+","+str(n-i+2*j+1)+")"
        Ar[n-i+2*j],Ar[n-i+2*j+1] = Ar[n-i+2*j+1],Ar[n-i+2*j]

    print ("---------------------")


# Time Complexity : O(n)
# Space Complexity : O(n)
def interleave_annalogic(Ar):

    m = (len(Ar)//2) - 1

    for i in range(1,m+1): # how many times  -- ideally height of the tree / triangle - 3 here

        k = m

        for j in range(0,i): # At height 1 , swap 1 time...At height 2 swap 2 times, At height 3 swap 3 times... At height i swap i times:).
            Ar[k],Ar[k+1] = Ar[k+1],Ar[k]
            k = k+2
        m = m-1
    print Ar


Ar= ('a1','a2','a3','a4','a5','b1','b2','b3','b4','b5');
Ar = list(Ar)
#print Ar
#array_interleaving_bruteforce(Ar)
#print Ar
#interleave_careercup(Ar)
#print(Ar)
interleave_annalogic(Ar)


