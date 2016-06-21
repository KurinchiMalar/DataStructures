# Time Complexity : O(n!)
# Space Complexity : O(n)
'''
""+P(a ->2 | b -> 1)

				"a" + Perm(a->1 | b-->1)							"b" + Perm(a->2 | b ->0)

	"aa"+Perm(a->0 | b --> 1)		"ab"+ Perm(a->1 | b->0)				"ba" + Perm(a->1 | b --> 0)
									 "aba" + Perm(a->0 | b -> 0)
	"aab"  a-->0 b --> 0													"baa" + Perm(a->0 | b --> 0)
'''
def construct_map(countmap,input):
    for ch in input:
        if countmap.__contains__(ch) == False:
            countmap[ch] = 1
        else:
            existing_count = countmap[ch]
            countmap[ch] = existing_count + 1
    return countmap

def printperms(countmap, input, result, passperm):

    if len(passperm) == len(input):
        result.append(passperm)
        return

    print(str(countmap))
    for key in countmap:  # determine the levels

        if countmap[key] != 0:
            if countmap[key] > 0:
                countmap[key] = countmap[key] - 1
            printperms(countmap, input, result, passperm + key)
            countmap[key] = countmap[key] + 1


input = "aba"
countmap = {}
countmap = construct_map(countmap,input)
print(countmap)
result = []
printperms(countmap,input,result,"")
print(str(result))
