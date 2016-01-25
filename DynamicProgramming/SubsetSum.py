'''
    Given a sequence of n positive numbers A1, A2, ..., An give an algorithm which checks whether there exists a subset of A
    whose sum of all numbers is T.


    eg) A = [3,2,4,19,3,7,13,10,6,11] , given sum = 17. Is there a subset with the given sum?

        Yes ...[ 4 + 13 ]

'''
# Time Complexity: O(2 pow n)

def check_if_subset_exists_with_given_sum_recusive(Ar,n,sum):

    if sum == 0:
        return 1
    if n == 0 and sum != 0:
        return 0

    if Ar[n-1]> sum: # ignore
        return check_if_subset_exists_with_given_sum_recusive(Ar,n-1,sum)

    # ignore or accept
    return check_if_subset_exists_with_given_sum_recusive(Ar,n-1,sum) or check_if_subset_exists_with_given_sum_recusive(Ar,n-1,sum-Ar[n-1])

#Ar = [1,3,9,2]
#sum = 29
#print "Subset exist? Recursive: "+str(check_if_subset_exists_with_given_sum_recusive(Ar,len(Ar),sum))

# Time Complexity : O(n*S)  Where n is the length of input and S is the given sum
# Space Complexity : O(n*S)
def check_if_subset_exists_with_given_sum(Ar,sum):

    T = [[0]*(sum+1) for x in range(len(Ar)+1)]

    #print T

    T[0][0] = 1

    # For 0 in input... you cannot bring any sum.
    for i in range(1,sum+1):
        T[0][i] = 0

    # Every input will have an empty set (0) as its subset.
    for i in range(1,len(Ar)+1):
        T[i][0] = 1
    #print T

    '''
    Ar = [1,3,9,2]
    sum = 5

            0 1 2 3 4 5 (sum)
      0(0)
      1(1)
      2(3)
      3(9)
(Ar)  4(2)

    '''

    for i in range(1,len(Ar)+1):

        for j in range(1,sum+1):

            '''
            Why do we do this jumping step?

                 Take value 2 and sum 5....

                    1) exclude 2 --> with (0,1,3,9) can i produce sum 5?  False... T[i-1][j] gives this statement
                    2) include 2 -->
                                    if the remaining numbers are able to produce (5-2) sum.... with 2 i can succeed..

                                    so we will have to see in T[3(9)][3].... this will be obtained by jumping 2 steps back.

            '''

            if j >= Ar[i-1]:
                T[i][j] = T[i-1][j] or T[i-1][j-Ar[i-1]]
            else:
                T[i][j] = T[i-1][j]


    # Printing
    result = []
    i = len(Ar)
    j = sum
    print T
    while i >= 0 and j >= 0:
        if i == 0 or j == 0:
            break

        if T[i][j] == 1 and T[i-1][j] == 0:  # since above false , but T[i][j] = true then it has come from jump step. so part of subset definitely

            result.append(Ar[i-1])
            j = j - Ar[i-1]
            i = i - 1

        else:    # T[i][j] = 1 and T[i-1][j] = 1 implies, there is someother value contributing to the subset whose 1 we have copied...so go up to find that value.
            i = i - 1

    return result,T[len(Ar)][sum]



Ar = [1,3,9,2]
sum = 5

Ar = [3,2,4,19,3,7,13,10,6,11]
sum = 17

Ar = [1,5,11,5]
sum = 11
print "Given Ar: "+str(Ar)+" sum : "+str(sum)
result,isExists = check_if_subset_exists_with_given_sum(Ar,sum)
print "Subset exists? : "+str(isExists)
print "Subset is :"+str(result)

