'''
    Given a string, give an algorithm for finding the first repeating letter in a string.

'''

def find_first_repeating_letter(inputstring):

    hash_table = {}

    for i in inputstring:
        hash_table[i] = hash_table.get(i,0) + 1
        if hash_table[i] == 2:
            return i
    return -1

inputstring = "abgzdgdez"
print ""+str(find_first_repeating_letter(inputstring))