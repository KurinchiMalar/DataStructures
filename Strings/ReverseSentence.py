'''
   Give an algorithm to reverse a sentence.

   eg) This is a string

      Output: string a is This

'''

# Time Complexity : O(n)
# Space Complexity : O(1) for computation,    for result list. --> O(n)

def reverse_sentence(sentence):

    isWord = False
    result = []
    start = 0

    for i in range(0,len(sentence)):

        if (sentence[i] ==" " or sentence[i] =="\t") and isWord == True: # First space after a word

            isWord = False
            #print "start:"+str(start)+"  i:"+str(i)
            result.insert(0,sentence[start:i])
            result.insert(0," ")

        elif sentence[i] != " " and sentence[i] != "\t" and isWord == False:  # First nonspace and beginning of word encountered
        #elif not (sentence[i] == ' ' or sentence[i] == '\t' or isWord):

            isWord = True
            start = i

        #  every other space after space ignored... only word, first space come under elif and if respectively.

    if isWord:  # For the last word
        result.insert(0,sentence[start:len(sentence)])
        #result.insert(0," ")


    return "".join(result)





sentence = "This                    is a string"
sentence = "I am a good girl always"
print ""+str(reverse_sentence(sentence))