'''
    Given an array of characters formed with a's and b's. The string marked with special character X which represents the middle of
    the list (for example: ababa....ababXbabab....baaaa). Check whether the string is a palindrome.
'''
import Stack
# Linear Method

# Time Complexity : O(n)
# Space Complexity : O(1)

def isPalindrome_Linear(inp):

    if inp == None:
        return None

    i = 0
    j = len(inp) - 1

    while i != j:
        if inp[i] != inp[j]:
            return -1

        i = i + 1
        j = j - 1

    return 1

# Time Complexity : O(n)
# Space Complexity : O(n)

def isPalindrome_Stacks(inp):

    i = 0
    stack = Stack.Stack()
    while inp[i] != "X":
        stack.push(inp[i])
        i = i + 1

    i = i + 1
    #stack.print_stack()

    while i < len(inp):
        if stack.size == 0 or stack.pop().get_data() != inp[i]:
            return -1
        i = i + 1
    return 1









inp = "abababXbababab"
inp = list(inp)
print "isPalindrome linear: "+str(isPalindrome_Linear(inp))
print "isPalindrome Stacks: "+str(isPalindrome_Stacks(inp))