'''
    Given m sets of integers that have n elements in them. Give an algorithm to find an element which appeared in maximum number of sets.

'''
# http://stackoverflow.com/questions/34809390/iterate-individual-elements-in-python-sets/34809464#34809464
from collections import Counter
from itertools import chain

def find_element_which_appeared_in_max_sets_elegant(input_set):

    #print ""+str(Counter(chain.from_iterable(input_set)).most_common(1))
    #return Counter(chain.from_iterable(input_set)).most_common(1)
    return Counter(chain.from_iterable(input_set)).most_common(1)[0][0]

# Time Complexity : O(n)
# Space Complexity : O(n)
def find_element_which_appeared_in_max_sets(input_set):

    hash_table = {}

    # count the frequencies
    for pair in input_set:
        for elem in pair:
            if elem in hash_table:
                hash_table[elem] = hash_table[elem] + 1
            else:
                hash_table[elem] = 1 # first occurence

    # scan and find the element with highest frequency.
    max_freq = 0
    for elem in hash_table:

        if hash_table[elem] > max_freq:
            max_freq = hash_table[elem]
            max_occured_elem = elem

    return max_occured_elem


input_set = {(5,4),(3,2),(4,3),(8,3)}
#print ""+str(find_element_which_appeared_in_max_sets(input_set))
print ""+str(find_element_which_appeared_in_max_sets_elegant(input_set))