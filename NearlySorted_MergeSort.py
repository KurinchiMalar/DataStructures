#Complexity O(n/k * klogk)  = O(nlogk)

# merging k elements using mergesort = klogk
# every n/k elem group is given to mergesort

# Hence totally O(nlogk)
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



