
# Stack of Boxes

# Time Complexity : O( 2 pow(n))
# Space Complexity : O(n)
import sys
class Box:

    def __init__(self ,length=None ,breadth=None ,height=None):
        self.length = length
        self.breadth = breadth
        self.height = height

def createBoxList():

    boxlist = []
    boxlist.extend((Box(6,6,4),
                   Box(3,3,5),
                   Box(5,5,6),
                   Box(8,8,7),
                   Box(7,7,8),
                   Box(4,4,9),
                   Box(5,5,10)))
    boxlist = []
    boxlist.extend((
        Box(5, 5, 10),
        Box(20, 20, 7),
        Box(4, 4, 6),
        Box(10, 10, 5)
    ))
    return boxlist

def print_boxlist(boxlist):

    for box in boxlist:
        print("( "+str(box.length)+" , "+str(box.breadth)+" , "+str(box.height)+" ) "),

    print

def print_box(box):
    print("Box: ( " + str(box.length) + " , " + str(box.breadth) + " , " + str(box.height) + " ) ")

def getHeight(box):
    return box.height

def sort_boxes_heightdesc(boxesList):

    return sorted(boxesList ,key=getHeight ,reverse=True)

# can place box2 over box1 ?
def can_place_above(box1,box2):

    if box2.length <= box1.length and box2.breadth <= box1.breadth:
        return True
    return False

# boxlist, None, 0 , []
def get_max_height_of_MaxHeightStack(boxlist,prevbottom,offset,result):

    if offset >= len(boxlist):
        return 0

    newbottom = boxlist[offset]

    # considering newbottom
    height_with_newbottom = 0
    if prevbottom == None or can_place_above(prevbottom,newbottom):

        if result[offset] == 0 :
            result[offset] = get_max_height_of_MaxHeightStack(boxlist,newbottom,offset+1,result)
            result[offset] = result[offset] + newbottom.height

        height_with_newbottom = result[offset]

    # without consisdering newbottom

    height_without_newbottom = get_max_height_of_MaxHeightStack(boxlist,prevbottom,offset+1,result)


    return max(height_with_newbottom,height_without_newbottom)

def get_boxbottom_withMaxHeightStack(result,boxlistdesc):
    max = -sys.maxint - 1
    bottombox = None
    for i in range(len(result)):

        if result[i] > max:
            max = result[i]
            bottombox = boxlistdesc[i]

    return max,bottombox

boxlist = createBoxList()
print_boxlist(boxlist)

boxlist_desc= sort_boxes_heightdesc(boxlist)
print_boxlist(boxlist_desc)

result = [0]*len(boxlist_desc)
get_max_height_of_MaxHeightStack(boxlist_desc,None,0,result)

max,bottombox = get_boxbottom_withMaxHeightStack(result,boxlist_desc)

print "Max height possible : "+str(max)
print_box(bottombox)