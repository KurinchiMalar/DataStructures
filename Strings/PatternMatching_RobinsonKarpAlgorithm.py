'''

Robinson-Karp String Matching Algorithm.

    In this method instead of checking for each possible postion in T, we check only

        if the hashing of P and hashing of m characters of T gives the same result.


    In our case, instead of a hashing function , I am just comparing m characters of input with pattern whose length is m.

    Logic to choose m chars of input at anytime:

        123456
        1) Remove first digit : 123 -100 * 1 = 23
        2) Multiply by 10 to shift it: 23 * 10 = 230
        3) Add last digit : 230 + 4 = 234 :) bingo!!

'''

# Time Complexity : O(mn)    Every n is compared with m

def match_given_pattern(inputstring,pattern):

    n = len(inputstring)
    m = len(pattern)

    subs = inputstring[0:m] # initialize
    print subs
    for i in range(m,n):

        if subs == pattern:
            print "Matched:"+subs
            return i-m # index at which pattern begins
        val = int(subs[0]) * (10 *(m-1))
        val = int(subs) - val

        subs = str(val*10 + int(inputstring[i]))

        print subs
    return -1

inputstring = "8659312"
pattern = "93"

print ""+str(match_given_pattern(inputstring,pattern))