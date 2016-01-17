
'''
    Combinations of a string:

        Unlike permutations, two combinations are considered to be the same if they contain the same characters, but may be in diff order.
        Give an algorithm that prints all possible combinations of the cahars in a string.

        ab and ac are different combinations. but ab is same as ba. For inputstring abc.

'''

'''
Trace for combinations of string: (Iteration)

/usr/bin/python2.7 /home/ubuntu/gitrepo/DataStructures/Strings/Combinations.py
---------------------------------------------------
i....0
level:[''] nList: []
item: elems[i]: a
---------------------------------------------------
i....1
level:['', 'a'] nList: []
item: elems[i]: b
item:a elems[i]: b
---------------------------------------------------
i....2
level:['', 'a', 'b', 'ab'] nList: []
item: elems[i]: c
item:a elems[i]: c
item:b elems[i]: c
item:ab elems[i]: c
['a', 'b', 'ab', 'c', 'ac', 'bc', 'abc']

Process finished with exit code 0
'''
# Time Complexity : O(n*n)

def get_combinations_iterative(inputstring):

    level = [" "]

    for i in range(0,len(inputstring)):

        nList = []

        for item in level:

            nList.append(item+inputstring[i])

        level += nList

    return level[1:]


#mystr = "abc"

#print ""+str(get_combinations_iterative(mystr))

def get_combinations_recursive(inputstring,nList,idx,level):

    for i in range(idx,len(inputstring)):   # i tracking pointer, idx loop pointer.

        nList += inputstring[i]
        level.append(nList)

        get_combinations_recursive(inputstring,nList,i+1,level)

        nList = nList[0:-1] # on return chuck out last element.... abc returned --> now nlist will have ab. For abc+ combi finished, we ll do for abd...

inputstring = "abc"
level = []
get_combinations_recursive(inputstring,'',0,level)
print level


def get_combinations_geeks_given_r(inputstring,result,start,end,index,r):

    if index == r:
        print result
        return

    for i in range(start,end):

        result[index] = inputstring[i]

        get_combinations_geeks_given_r(inputstring,result,i+1,end,index+1,r)


mystr = "abc"
r = 2
result = [None]*r
get_combinations_geeks_given_r(mystr,result,0,len(mystr),0,r)





'''
Trace for combinations of string: (Recursion)

abcd

a
ab
abc
abcd
abd
ac
acd
ad

tptr = b
""
b
bc
bcd
bd
""

tptr = c

""
c
cd
""

tptr = d
""

d
""


elems = abc

Level 1:
idx = 0
loop i in 0 to 2
   'a'
   recursive('abc', 'a', 1) -> Level 2
   From Level 2
   s = ''
loop i in 1 to 2
   s = 'b'
   recursive('abc', 'b', 2) -> Level 6
   reyirn from level 6
   s = ''
loop i in 2 to 2
	s = 'c'
	recursive('abc', 'c', 3) -> Level 7
	return from level 7

Level 6:
idx = 2
loop i in 2 to 2
	s = 'bc'
	recursive('abc', 'bc, 3 -> Level 7
	retrun from Level 7
	s = 'b'
loop i in 3 to 2
return 1
Level 2:
idx = 1
loop i in 1 to 2
   'ab'
   recursive('abc', 'ab', 2) -> Leve; 3
   From Level 3
   s = 'a'
loop i in 2 to 2
	s = 'ac'
	recursive('abc', 'ac', 3) -> Level 5;
    From Level 5:
	s = 'a'
loop i in 3 to 2
retrun to  Level 1

Level 3:
idx = 2
loop i in 2 to 2
   'abc'
   recursive('abc', 'abc', 3) -> Leve; 4
   From Level 4:
   s = 'ab'
loop i in 3 to 2
return to Level 2

Level 4:
idx = 3
loop i in 3 to 2

return -> Level 3
'''