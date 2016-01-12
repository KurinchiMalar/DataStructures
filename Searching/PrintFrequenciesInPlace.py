'''
     Given an array of n elements, how do you print the frequencies of elements without using extra space.

     Assume all elementss are positive, editable and less than n.
'''
# Time Complexity : O(n)
# Space Complexity : O(1)
def print_frequencies_negation(Ar):

    pos = 0
    n = len(Ar)-1

    while pos <= n:

        expected_pos = Ar[pos]-1 # In an array of 0 to n , a value say 5 will be at position 4
        '''print "-------------------------------------------------------"
        print "(pos,expected_pos):"+str(pos)+", "+str(expected_pos)
        print "(Ar[pos],Ar[expected_pos]):"+str(Ar[pos])+", "+str(Ar[expected_pos])'''
        if Ar[pos] > 0 and Ar[expected_pos] > 0:
            Ar[pos],Ar[expected_pos] = Ar[expected_pos],Ar[pos] # Save valuable element at Ar[expected_pos] into Ar[pos]
            Ar[expected_pos] = -1 # marking first occurence of number (expected_pos+1)

            #DONT INCREMENT POS HERE.....ONLY WHEN EXP_POS < 0 or POS < 0 we have to alter pos.

        elif Ar[pos] > 0: # Ar[expected_pos] is negative, means we are encountering repeated version of it. So increment frequency.
            Ar[expected_pos] = Ar[expected_pos] - 1 # -1-1 = -2 means two times occured
            Ar[pos] = 0 # this is to show that this element has not occured at all upto now.
            pos = pos + 1

        else:  # frequency of this index is already taken care.
            pos = pos + 1

    print Ar

    for i in range(0,len(Ar)):
        print "Element "+str(i+1)+"occured "+str(abs(Ar[i]))+"times"

Ar = [10,1,9,4,7,6,5,5,1,2,1]
print_frequencies_negation(Ar)