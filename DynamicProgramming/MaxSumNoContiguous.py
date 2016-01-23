'''
    Given a sequence of numbers A(1)....A(n), give an algorithm for finding a contiguous subsequence A(i)...A(j) for which the sum of elements
    in the subsequence is maximum.

    Here the condition is we should not select two contiguous numbers.
'''

'''
Decide whether to choose i.

   if Ar[i]+M[i-2] > M[i-1] choose Ar[i]
   else:
        M[i] = M[i-1]
'''

# Time Complexity : O(n)
# Space Complexity : O(n)

def max_sum_with_no_two_contiguous_numbers_lefttoright(Ar):

    M = [0]*(len(Ar)+1)

    M[0] = Ar[0]
    M[1] = max(Ar[0],Ar[1])

    for i in range(2,len(Ar)):

        if Ar[i] + M[i-2] > M[i-1]:
            M[i] = Ar[i] + M[i-2]
        else:
            M[i] = M[i-1]

    return M[len(Ar)-1]

# Time Complexity : O(n)
# Space Complexity : O(n)

def max_sum_with_no_two_contiguous_numbers_righttoleft(Ar):

    n = len(Ar)
    M = [0]*(n+1)

    M[n-1] = Ar[n-1]
    M[n-2] = max(Ar[n-1],Ar[n-2])

    for i in range(n-3,-1,-1):

        if Ar[i] + M[i+2] > M[i+1]:
            M[i] = Ar[i] + M[i+2]
        else:
            M[i] = M[i+1]

    return M[0]

# Time Complexity : O(n)
# Space Complexity : O(n)
def max_sum_with_no_three_contiguous_numbers_lefttoright(Ar):

    n = len(Ar)
    M = [0]*(n+1)

    M[0] = Ar[0]
    M[1] = max(Ar[1]+M[0],M[0])
    M[2] = max(Ar[2]+M[0],M[0])

    for i in range(3,len(Ar)):
        if Ar[i] + Ar[i-1] + M[i-3] > Ar[i] + M[i-2]:
            M[i] = Ar[i] + Ar[i-1] + M[i-3]
        else:
            M[i] = Ar[i] + M[i-2]

    return M[len(Ar)-1]

# Time Complexity : O(n)
# Space Complexity : O(n)
def max_sum_with_no_three_contiguous_numbers_righttoleft(Ar):

    n = len(Ar)
    M = [0]*(n+1)

    M[n-1] = Ar[n-1]
    M[n-2] = max(Ar[n-2]+M[n-1],M[n-1])
    M[n-3] = max(Ar[n-3]+M[n-1],M[n-1])

    for i in range(n-4,-1,-1):
        if Ar[i] + Ar[i+1] + M[i+3] > Ar[i] + M[i+2]:
            M[i] = Ar[i] + Ar[i+1] + M[i+3]
        else:
            M[i] = Ar[i] + M[i+2]

    return M[0]






Ar = [5,  5, 10, 40, 50, 35]

print "Max_sum no two contiguous numbers_lefttoright: "+str(max_sum_with_no_two_contiguous_numbers_lefttoright(Ar))
print "Max_sum no two contiguous numbers_righttoleft: "+str(max_sum_with_no_two_contiguous_numbers_righttoleft(Ar))
print "-------------------------------"
print "Max_sum no three contiguous numbers_lefttoright: "+str(max_sum_with_no_three_contiguous_numbers_lefttoright(Ar))
print "Max_sum no three contiguous numbers_righttoleft: "+str(max_sum_with_no_three_contiguous_numbers_righttoleft(Ar))