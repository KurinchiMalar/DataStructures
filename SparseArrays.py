
#Time Complextiy : O(n)
# Space Complexity : O(n)
# https://www.hackerrank.com/challenges/sparse-arrays?h_r=next-challenge&h_v=zen
def count_occurences(Ar, queryAr):
    hash_table = {}
    for item in Ar:
        if hash_table.__contains__(item) == False:
            hash_table[item] = 1
        else:
            hash_table[item] = hash_table[item] + 1

    for item in queryAr:
        if hash_table.__contains__(item) == True:
            print hash_table[item]
        else:
            print 0


Ar = []
colln_no = raw_input().strip()

for i in range(int(colln_no)):
    Ar.append(str(raw_input()))

query_no = raw_input().strip()
queryAr = []
for i in range(int(query_no)):
    queryAr.append(str(raw_input()))

#print str(Ar)
#print str(queryAr)
count_occurences(Ar,queryAr)
'''
4
aba
baba
aba
xzxb
3
aba
xzxb
ab

'''