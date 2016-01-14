'''
     Given an array of characters, give an algorithm for removing the duplicates.
'''


def toMutable(inputstring):
    temp = []
    for x in inputstring:
        temp.append(x)
    return temp

# Time Complexity : O(n * n)
# Space Complexity : O(1)

def remove_duplicates_fromstring_bruteforce(input_str):
    Ar = toMutable(input_str)
    print Ar
    result = []
    result.append(Ar[0])

    for i in range(1, len(Ar)):
        for j in range(0, i):
            occured = 0
            if Ar[i] == Ar[j]:
                occured = 1
                break
        if occured == 0:
            result.append(Ar[i])

    return result

# Sorting Solution
# Time Complexity : O(nlogn)
# Space Complexity : O(1)

def remove_duplicates_fromstring_sorting(input_str):
    Ar = toMutable(input_str)
    Ar.sort()

    print Ar
    result = []
    result_ptr = 1
    ip_ptr = 1

    for ip_ptr in range(1,len(Ar)):

        if Ar[ip_ptr] != Ar[ip_ptr-1]:
            Ar[result_ptr] = Ar[ip_ptr]
            result_ptr = result_ptr + 1


    return Ar[:result_ptr]

# Hashing Solution

# Time Complexity : O(n)
# Space Complexity : O(n)

def remove_duplicates_fromstring_hashing(input_str):

    Ar = toMutable(input_str)

    hash_ar = []
    result = []

    for x in Ar:
        if x not in hash_ar:
            hash_ar.append(x)
            result.append(x)

    return result

input_str = "ge41eks4fo7r1geeks"
#input_str = "bananas"

#print ""+str(remove_duplicates_fromstring_bruteforce(input_str))

#print ""+str(remove_duplicates_fromstring_sorting(input_str))

print ""+str(remove_duplicates_fromstring_hashing(input_str))

