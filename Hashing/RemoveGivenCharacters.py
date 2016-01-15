'''
 Give an algorithm to remove the specified characters from a given string
'''


def remove_chars(inputstring,charstoremove):

    hash_table = {}
    result = []
    for char in charstoremove:
        hash_table[char] = 1
    #print hash_table
    for char in inputstring:
        if char not in hash_table:
            result.append(char)
        else:
            if hash_table[char] != 1:
                result.append(char)

    result = ''.join(result)
    print result

remove_chars("hello","he")
