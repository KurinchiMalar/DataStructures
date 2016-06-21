'''
hop = 1
start = orig_start + hop
hop = 2 * hop
'''
def getElementAtIndex(Ar,i):

    return Ar[i]

# Time Complexity : O(log n)
def find_element_arraysize_unknown(Ar,start,k):

    orig_start = start
    hop = 1

    while(1):

        elemAtIndex = getElementAtIndex(Ar,start)

        if elemAtIndex == k:
            return start


        if elemAtIndex == -1 or elemAtIndex > k:
            #print "start " + str(start) + " hop " + str(hop)
            if hop == 1:
                return -1
            return find_element_arraysize_unknown(Ar,start-(hop/4),k)


        start = orig_start + hop
        hop = 2 * hop

Ar = [-20, -10, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]

for item in Ar[0:25]:
    print " "+str(find_element_arraysize_unknown(Ar,0,item))

print " "+str(find_element_arraysize_unknown(Ar,0,-30))