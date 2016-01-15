'''
Given a string , Design an algorithm to find the first non-repeated character
'''

# Time Complexity : O(n*n)
# Space Complexity ; O(1)

def find_first_nonrepeated_character_bruteforce(inputstring):

    input_list = list(inputstring)

    for i in range(0,len(inputstring)):
        print "-----------------------------"
        print ""+ str(i)
        repeated = 0
        for j in range(0,len(inputstring)):
            print "comparing:"+str(inputstring[i]) +" , "+str(inputstring[j])
            # i ! = j is important. Everytime j should should start from 0, because any previous occurences should also be taken into account and eliminated.
            # abgzdabgdez   ... for this on second occurence of a, if we traverse just after a it is not enough. see before also and consider it a repeating element and discard.
            if i != j and inputstring[i] == inputstring[j]:
                repeated = 1
                break
        if repeated == 0:
            return inputstring[i]

    return -1

# Time Complexity : O(n)
# Space Complexity : O(1)

def find_first_nonrepeated_character_hashing(inputstring):
    hash_table = {}

    for i in inputstring:
        hash_table[i] = hash_table.get(i,0)+1

    print hash_table
    for elem in hash_table:
        if hash_table[elem] == 1:
            return elem
    return -1
inputstring = "abgzdabgdez"
#print ""+str(find_first_nonrepeated_character_bruteforce(inputstring))

print ""+str(find_first_nonrepeated_character_hashing(inputstring))

