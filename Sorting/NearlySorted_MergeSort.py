#Complexity O(n/k * klogk)  = O(nlogk)

# merging k elements using mergesort = klogk
# every n/k elem group is given to mergesort

# Hence totally O(nlogk)
'''
k = 3
4 5 9 | 7 8 3 | 1 2 6

1st merge sort all blocks
4 5 9 | 3 8 9 | 1 2 6

Time Complexity = O(n * (n/k) log k)
i.e to sort k numbers is k * log k
to sort n/k such blocks = (n/k) * k log k = n log k

2nd start merging two blocks at a time
i.e
to merge k + k elements 2k log k
to merge 2k + k elements 3k log k
similarly it has to proceed until qk + k = n, so it becomes n log k
where q = (n/k) - 1
'''
from MergeSort import mergesort

def split_into_groups_of_size_k(Ar,k):
    r = []
    for j in range(0,(len(Ar)/k)+1):
        start = k * j
        end = start + k
        if start >= len(Ar):
            break
        if end >=len(Ar) and start < len(Ar):
            r.append(Ar[start:end])
            break
        #print "start,end = "+str(start)+","+str(end)
        r.append( Ar[start:end])
        #print r[j]
    return r

def merge_two_lists(list1,list2):
    list1.extend(list2)
    return list1

Ar = [6,9,10,1,2,3,5]
print Ar

split_blocks = split_into_groups_of_size_k(Ar,2)

print str(split_blocks)

for i in range(0,len(split_blocks)):
    mergesort(split_blocks[i])

print "Sorted blocks:" +str(split_blocks)


while len(split_blocks) > 1 :
    split_blocks[1] = merge_two_lists(split_blocks[0],split_blocks[1])
    split_blocks.pop(0)
    mergesort(split_blocks[0])
    print str(split_blocks)



