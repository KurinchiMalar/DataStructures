

# Time Complexity : O(n)

# Space Complexity : O(256)

def count_occurence_of_characters_in_a_string(Ar):

    n = len(Ar)

    count = [0]*256

    for i in range(n):
        count[ord(Ar[i])] = count[ord(Ar[i])] + 1

    for i in range(n):
        if count[ord(Ar[i])] > 0:

            print "char :"+ Ar[i] +" occured :"+str(count[ord(Ar[i])])
            if count[ord(Ar[i])] > 1: # occured again
                count[ord(Ar[i])] = -count[ord(Ar[i])]


Ar = ['C','a','r','e','e','r','m','o','n','k']

count_occurence_of_characters_in_a_string(Ar)
