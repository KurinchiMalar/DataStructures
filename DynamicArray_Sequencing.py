
'''
N = 5,  # Q = 5
'''
# Time Complexity : O(Q)
# Space Complexity : O(Q)
def dynamicSequencing(Ar):

    N = int(Ar[0][0])
    Q = int(Ar[0][1])
    lastAns = 0

    S = [[] for x in range(N)]

    for query in range(1, Q + 1):

        qtype = Ar[query][0]
        xorval = Ar[query][1]
        value = Ar[query][2]
        seqno = ((xorval) ^ (lastAns)) % N

        #print("qtype: "+str(qtype) + ", xorval: " + str(xorval) + ", value: " + str(value) + ", seqno: " + str(seqno))
        if qtype == 1:  # query1

            S[seqno].append(value)

        else:
            #print "len: " + str(len(S[seqno]))
            if len(S[seqno]) == 0:
                lastAns = 0
            else:
                lastAns = S[seqno][ value % len(S[seqno]) ]
            print lastAns

'''Ar = [[2,5],
      [1,0,5],
      [1,1,7],
      [1,0,3],
      [2,1,0],
      [2,1,1]]
'''
Ar = []
firstline = raw_input().strip().split(' ')
Ar.append(firstline)

for i in range(int(firstline[1])):
    temp = [int(x) for x in raw_input().strip().split(' ')]
    Ar.append(temp)

dynamicSequencing(Ar)
