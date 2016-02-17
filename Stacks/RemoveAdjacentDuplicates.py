'''
    Recursively remove all adjacent duplicates. Given a string of characters, recursively remove adjacent duplicate characters
     from string. The output string should not have any adjacent duplicates.
'''


# Time Complexity : O(n)
# Space Complexity : O(1)  ... inplace, no stack.
def remove_adj_duplicates(mystring):


    result = []
    res_idx = 0
    mystring[res_idx] = mystring[0]
    i = 1

    while i < len(mystring):
        if mystring[i] != mystring[res_idx]:
            res_idx = res_idx + 1
            mystring[res_idx] = mystring[i]
            i = i + 1
        else:
            while i < len(mystring) and mystring[i] == mystring[res_idx]:  # recursively remove all equals.
                res_idx = res_idx - 1
                i = i + 1

    print "mystring:"+str(mystring[0:res_idx+1]) # our desired chars are only upto res_idx.



mystring = "azxxzy"
mystring = "geeksforgeeks"
mystring = "careermonk"
mystring = "mississippi"
mystring = list(mystring)
remove_adj_duplicates(mystring)