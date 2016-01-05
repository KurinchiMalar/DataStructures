#https://ideone.com/daLlg9
#Time Complexity = O(n) (Building hash_ar and finding max of negatives)
#Space Complexity = O(k) ---- k is the range of numbers in the input array. Here 0 to 5. Hence k = 5
'''
Solution:

1) Store the position of occurence in input array in hash_ar

2) On second occurence negate

3) If already negated just skip

4) Index of the largest negative value is the first repeating element
'''
def first_repeating_element_hashing_withpositions(Ar,n):
    hash_ar = [0] * (n+1)

    for i in range(0,len(Ar)):
        position = hash_ar[Ar[i]]
        if position == 0: # first occurence
            hash_ar[Ar[i]] = i+1  #Array index starts from zero. hence index 0 == position 1

        elif position > 0: # repeating for the first time
            hash_ar[Ar[i]] = -(hash_ar[Ar[i]])

        # if position is negative .... just skip and move to next element. we have already registered it's repetition.
    print hash_ar

    # Find the largest negative value and return the index of it from hash_ar.
    result_val = 0
    result_index = -1
    for i in range(0,len(hash_ar)):
        if hash_ar[i] < 0: # seeing oly negatives
            if result_val == 0 or hash_ar[i] > result_val:
                result_val = hash_ar[i]
                result_index = i
    print "first repeating element is:"+ str(result_index)
    print "result_val:"+str(result_val)
    return result_index



#YET TO UNDERSTAND THIS IMPLEMENTATION
'''def FirstRepeatedElementAmongRepeatedElementsWithHash(A):
	table = {}  # hash
	max = 0
	for element in A:
		if element in table and table[element] == 1:
			table[element] = -2
		elif element in table and table[element] < 0:
			table[element] -= 1
		elif element != " ":
			table[element] = 1
		else:
			table[element] = 0

	for element in A:
		if table[element] < max:
			max = table[element]
			maxRepeatedElement = element

	print maxRepeatedElement, "repeated for ", abs(max), " times"

'''



#A = [3,2,1,2,3]

#FirstRepeatedElementAmongRepeatedElementsWithHash(A)

#Ar = [3,2,1,2,3]

Ar = [3, 2, 1, 1, 2, 1, 2, 5, 5]
first_repeating_element_hashing_withpositions(Ar,5)
#FirstRepeatedElementAmongRepeatedElementsWithHash(Ar)