'''
    Given m sets of integers that have n elements in them. Give an algorithm to find an element which appeared in maximum number of sets.

'''
# http://stackoverflow.com/questions/34809390/iterate-individual-elements-in-python-sets/34809464#34809464
from _ast import List
from collections import Counter
from itertools import chain

def find_element_which_appeared_in_maximum_overall_elegant(input_set):

    #print ""+str(Counter(chain.from_iterable(input_set)).most_common(1))
    #return Counter(chain.from_iterable(input_set)).most_common(1)
    return Counter(chain.from_iterable(input_set)).most_common(1)[0][0]

# Time Complexity : O(n)
# Space Complexity : O(n)
def find_element_which_appeared_maximum_overall(input_set):

    hash_table = {}

    # count the frequencies
    for pair in input_set:
        for elem in pair:  # hash_table[elem] = hash_table.get(elem,0) + 1   .....dict.get(key, default=None)
                           # default -- This is the Value to be returned in case key does not exist.
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

'''
 Given m sets of integers that have n elements in them. Give an algorithm to find an element which appeared in maximum number of sets.

 We have to return the element which appeared in maximum number of sets not maximum overall.

 Algorithm:

    For every element ->

    maintain a hashentry like this -->

        elem : [] # this list is used to put a 1 in indices of corresponding set_counter.

                  # Just to indicate this element has occured in which set. If already set in set1(say) we can ignore. This is a duplicate.

        Example:
        ------------------------------------------
set:(4, 6, 1, 6)setcounter:1
element:4
hashtable[elem][0, 1, 0, 0, 0]
element:6
hashtable[elem][0, 1, 0, 0, 0]
element:1
hashtable[elem][0, 1, 0, 0, 0]
element:6
hashtable[elem][0, 1, 0, 0, 0]
------------------------------------------
set:(1, 3, 9, 5)setcounter:2
element:1
hashtable[elem][0, 1, 1, 0, 0]
element:3
hashtable[elem][0, 0, 1, 0, 0]
element:9
hashtable[elem][0, 0, 1, 0, 0]
element:5
hashtable[elem][0, 0, 1, 0, 0]
------------------------------------------
set:(1, 7, 7, 9)setcounter:3
element:1
hashtable[elem][0, 1, 1, 1, 0]
element:7
hashtable[elem][0, 0, 0, 1, 0]
element:7
hashtable[elem][0, 0, 0, 1, 0]
element:9
hashtable[elem][0, 0, 1, 1, 0]
------------------------------------------
set:(4, 4, 4, 2)setcounter:4
element:4
hashtable[elem][0, 1, 0, 0, 1]
element:4
hashtable[elem][0, 1, 0, 0, 1]
element:4
hashtable[elem][0, 1, 0, 0, 1]
element:2
hashtable[elem][0, 0, 0, 0, 1]
{1: [0, 1, 1, 1, 0], 2: [0, 0, 0, 0, 1], 3: [0, 0, 1, 0, 0], 4: [0, 1, 0, 0, 1], 5: [0, 0, 1, 0, 0], 6: [0, 1, 0, 0, 0], 7: [0, 0, 0, 1, 0], 9: [0, 0, 1, 1, 0]}
'''
'''
Space Complexity -

say {(2,3,4,6),(5,5,5,2)}

m = 2
n = 4

Hashtable : O(n)


Then for every n, there is O(m) list

n*O(m) = O(mn) = O(n)

WorstCase: Say all elements are distinct in every set.

    Space Complexity:

    Hashtable : O(mn)
                then for every mn we create a m list

                ==> O(mn *m)
    Time Complexity:

            Iterate through hashtable O(mn)*m (through list)

'''
def create_new_list(set_counter, numberofsets):

    temp = [0] * (numberofsets+1)
    temp[set_counter] = 1
    return temp

def find_element_which_appeared_in_max_sets(input_set):
    set_counter = 0
    hash_table = {}
    for set in input_set:
        print "------------------------------------------"
        set_counter = set_counter + 1
        print "set:"+str(set)+"setcounter:"+str(set_counter)
        for elem in set:
            print "element:"+str(elem)
            if elem not in hash_table:
                hash_table[elem] = create_new_list(set_counter,input_set.__len__()) # if there are 3 sets, we need 0,1,2,3 indices
            else:

                existing_list = hash_table[elem]
                if existing_list[set_counter] != 1:  # already set --> duplicate so ignore, set only if not set already.
                    existing_list[set_counter] = 1
                hash_table[elem] = existing_list
            print "hashtable[elem]"+str(hash_table[elem])
    print hash_table

    max_count = 0
    max_occured_elem = -1
    for elem in hash_table:

        elem_list = hash_table[elem]
        cur_list_sum = 0
        for item in elem_list:
            cur_list_sum += item
        #print "elem:"+str(elem)+"...."+"cur_list_sum:"+str(cur_list_sum)
        if cur_list_sum > max_count:
            max_count = cur_list_sum
            max_occured_elem = elem
        #print "max_elem:"+str(max_occured_elem)+"...."+"max_count:"+str(max_count)

    #print max_count
    return max_occured_elem





#input_set = {(5,4),(3,2),(4,3),(8,3)}

#input_set = {(5,5,5,2),(2,3,4,6)}
input_set = {(1,3,9,5),(4,4,4,2),(4,6,1,6),(1,7,7,9)}

#print ""+str(find_element_which_appeared_in_max_sets(input_set))
#print ""+str(find_element_which_appeared_in_maximum_overall_elegant(input_set))

print ""+str(find_element_which_appeared_in_max_sets(input_set))