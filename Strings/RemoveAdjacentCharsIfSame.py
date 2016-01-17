'''
    Given a string "ABCCBCBA", give an algorithm for recursively removing the adjacent characters if they are same.

    eg) ABCCBCBA --> ABBCBA --> ACBA
'''

# Time Complexity : O(n)
# Space Complexity : O(1)

'''
Algorithm: ( Similar to Hashing - RemoveDuplicatesInString Sorting solution. Use resultptr and keep accumulating result)

     1) result_ptr will start from -1

        if  not equal adjacents seen--> copy current content to resultptr and move i

        if equals, resultptr = resultptr -1 and input ptr = inputptr + 1
'''

def remove_adjacent_duplicates(inputstring):

    result_ptr = -1
    i = 0

    while i < len(inputstring):

        if result_ptr == -1 or inputstring[result_ptr] != inputstring[i]:

            result_ptr = result_ptr + 1
            inputstring[result_ptr] = inputstring[i]
            i = i + 1
        else:
            while i < len(inputstring) and inputstring[result_ptr] == inputstring[i]:

                result_ptr = result_ptr - 1
                i = i + 1

    return inputstring[0:result_ptr+1]

mystr = "abccdde"
print ""+str(remove_adjacent_duplicates(list(mystr)))