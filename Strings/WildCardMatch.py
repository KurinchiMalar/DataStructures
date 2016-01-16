'''

    Given a text and a pattern, give an algorithm for matching pattern in text. Assume ?(single character matcher) and

    *(multi character matcher) are the wild card characters.
'''

# Time Complexity : O(n*m) where m is the length of the pattern and n is the length of the input string.
# Space Complexity : O(1)

def wildcard_match(inputstring,pattern):

    if len(pattern) == 0:
        # if both len of pattern and len of inputstring is 0, then BINGO! It means the input string has fully matched with pattern
        return len(inputstring) == 0

    if pattern[0] == "?":
        # chuck out input_string[0] and pattern[0] --> ? means one and only char
        return len(inputstring) > 0 and wildcard_match(inputstring[1:],pattern[1:])

    elif pattern[0] == "*":

        return wildcard_match(inputstring,pattern[1:]) or \
               (len(inputstring) > 0 and wildcard_match(inputstring[1:],pattern))

    else:

        return len(inputstring) > 0 and inputstring[0] == pattern[0] and wildcard_match(inputstring[1:],pattern[1:]) # successful match move next

    return 0


print ""+str(wildcard_match("cc","c"))
print ""+str(wildcard_match("cc","c*"))
print ""+str(wildcard_match("cc","*"))
print ""+str(wildcard_match("cc","?"))
print ""+str(wildcard_match("cacbade","ca*c*"))
print ""+str(wildcard_match("cacbade","ca*cb*ad*"))
'''
   elif pattern[0] == "*":
        return wildcard_match(inputstring,pattern[1:]) or len(inputstring) > 0 and wildcard_match(inputstring[1:],pattern)

        1) For a * in pattern, chuck out * and send all others in input one by one.
            wildcard_match(inputstring,pattern[1:])

                after  * if there are patterns it should match...
                eg) cacbade   ca*cb*ad* --> cbade *cb*ad*
                                            cbade  cb*ad*  chuck out *
                                            ade      *ad*
                                            ade       ad*  chuck out *
                                            e          *
                                                e          ""  chuck out * (FALSE) will be returned and (or) condition below will get executed.

                eg) cacbade   ca*c*  --> cbade   *c*
                                         cbade    c*
                                         bade     *
                                                bade     ""   (FALSE) will be returned and (or) condition below will get executed.
        or

        2) When pattern is empty, chuck out input one by one and see if it is corresponding

                    continuing above example..

                                                ade     *
                                                de      *
                                                e       *
                                                ""      ""
                                                BINGO!  Matches
'''








