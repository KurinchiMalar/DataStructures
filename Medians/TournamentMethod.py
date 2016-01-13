'''
Give an algorithm to find the second smallest element
'''

# Number of Comparisons for first minimum : n + log n - 1
# Number of Comparisons for second minimum : n + log n - 1 (leaving the first minimum)

def get_smallest_tournament_method(Ar):

    idx = range(0,len(Ar)) # indices of players.
    knockout = [[]for i in idx] # for every index has a list of knockout items
    comparison_count = 0

    while len(idx) > 1: # number of levels

        print "This Round participants: "+str(idx)
        idxtemp = [] # winners of current round

        # If odd, the last player automatically goes to next round. so iterate only from 0 ,1,2.... len(Ar)-2 .. leave the last elem.
        odd = len(idx) % 2
        #print odd


        for i in range(0,len(idx)-odd,2): # number of games in current round

            first_i = idx[i]
            second_i = idx[i+1]
            print "player1: "+str(Ar[first_i])+"  player2: "+str(Ar[second_i])
            comparison_count += 1

            if Ar[first_i] <= Ar[second_i]: #Ar[first_i] is the winner
               idxtemp.append(first_i)
               knockout[first_i].append(Ar[second_i]) # this will be used in backtracking
            else:
                idxtemp.append(second_i)
                knockout[second_i].append(Ar[first_i])
        print idxtemp
        '''
            [2, 3, 7, 1, 6]
            This Round participants: [0, 1, 2, 3, 4]
            player1: 2  player2: 3
            player1: 7  player2: 1
            [0, 3]
            After this i will be 2.... first =2 second = 3  ... we need to add index 4 which is the last element.
            [0, 3, 4]
        '''
        if odd == 1:
            idxtemp.append(idx[i+2]) # if odd add the last element directly to go to next round.
        print idxtemp

        print "---------------------"
        idx = idxtemp

    print "final idx:"+str(idx)
    print "smallest element:"+str(Ar[idx[0]])
    print "number of comparisons:"+str(comparison_count)
    print "knocked out by smallest:"+str(knockout[idx[0]])

    losers_to_mostminimum_elem = knockout[idx[0]]
    second_min = losers_to_mostminimum_elem[0]
    for i in range(1,len(losers_to_mostminimum_elem)):
        if Ar[i] < second_min:
            second_min = Ar[i]
            comparison_count = comparison_count+1

    print "second minimum:"+str(second_min)
    print "number of comparisons:"+str(comparison_count)
Ar = [2,3,7,1,6]
print Ar

get_smallest_tournament_method(Ar)



