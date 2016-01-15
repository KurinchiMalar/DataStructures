'''
    Given two sets A and B, and a number K, Give an algorithm for finding whether there exists a pair of elements, one from A and one from B, that add upto K
'''

# Time Complexity : O(n)
# Space Complexity : O(n)

def find_two_elements_whose_sum_is_k(smallerset,largerset,k):

    hash_table = {}
    for elem in smallerset:
        hash_table[elem] = elem
    print hash_table
    for elem in largerset:
        #print "elem:"+str(elem)+"k-elem:"+str(k-elem)
        if k-elem in hash_table:
            print elem
            print k-elem
            yield elem,k-elem
    return


A = (2,4,5)
B = (7,9,8,10)
if len(A) < len(B):
    smallerset = A
    largerset = B
else:
    smallerset = B
    largerset = A

result = find_two_elements_whose_sum_is_k(smallerset,largerset,13)

for i in result:
    print i
