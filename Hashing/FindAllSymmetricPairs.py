'''
     Given a list of number pairs.
     If pair(i,j) exist, and pair(j,i) exist report all such pairs.
'''
#http://stackoverflow.com/questions/34795434/find-symmetric-pairs-in-python/34795741#34795741
# Time Complexity : O(n)
# Space Complexity : O(n)

def find_all_symmetric_pairs(inp_dic):

    for key in inp_dic.iterkeys():
        val = inp_dic.get(key)

        if inp_dic.get(val) == key:
            yield key,val
    return

def find_all_symmetric_pairs_elegant(inp_dic):

    #pairs = [(key,value) for key,value in inp_dic.items()]

    # can be made faster by changing to set instead of list
    pairs = {(key,value) for key,value in inp_dic.items()}
    print pairs
    answer = [pair for pair in pairs if (pair[1], pair[0]) in pairs]
    print(answer)



#inp_dic = [(1,3),(2,6),(3,5),(7,4),(5,3),(8,7),(6,2)]

#inp_dic = dict(inp_dic)

#for key, val in find_all_symmetric_pairs(inp_dic):
#    print "key: " + str(key)
#    print "value: " + str(val)


input_dic = {'1':'3','2':'6','3':'5','7':'4','5':'3','8':'7','4':'7'}
find_all_symmetric_pairs_elegant(input_dic)
