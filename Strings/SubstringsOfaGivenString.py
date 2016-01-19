'''
Write a program to get all the substrings of a given string.
'''

# Time Complexity : O(n*n)
# Space Complexity : O(1)
def print_substrings(inputstring):

    result = []

    for i in range(0,len(inputstring)):

        for j in range(i,len(inputstring)):

            result.append(inputstring[i:j+1])

    print result

print_substrings("fun")

# An efficient solution will be using suffix tree - Yet to be learnt