class Heap:
    def __init__(self):
        self.heapList = [0]
        self.size = 0

    def swap(self,x,y):
        temp = self.heapList[x]
        self.heapList[x] = self.heapList[y]
        self.heapList[y] = temp

    # send a parent index.
    # Parent can have just one left child
    # Parent can have both left and right child
    def find_min(self,i):
        if(2*i+2 >= self.size ):  # no right child but has left child
            return 2*i + 1

        if(self.heapList[2*i+1] < self.heapList[2*i+2]):
            return 2*i+1
        else:
            return 2*i+2

     #base condition --> go till parent == root
    def percolate_up(self,i):
        while i//2 > 0:
            if self.heapList[i] < self.heapList[i//2]:
                self.swap(i,i//2)
            i = i//2

    #base_condition --> if leaf stop ie) continue until non-leaf.
    def percolate_down(self,i):
        while 2*i+1 < self.size: # must be a parent with left child atleast ie) non leaf
            minChild = self.find_min(i)
            if self.heapList[i] < self.heapList[minChild]:
                self.swap(i,minChild)
            i = minChild

    def isLeaf(self,index,len):
        if 2*index+1 >= len and 2*index+2 >= len:
            return True
        return False

    def getMaxIndex(self,x,y):
        if self.heapList[x] > self.heapList[y]:
            return x
        else:
            return y

    def getMinIndex(self,x,y):
        if self.heapList[x] < self.heapList[y]:
            return x
        else:
            return y

    #min_heapify
    def min_heapify(self,i,len):

        left = 2*i+1
        right = 2*i+2
        '''print "left:"+str(left)
        print "right:"+str(right)
        print("leftlen:("+str(left)+","+str(len)+")")'''
        if left > len:
            return
        if left <= len and right <= len:
            smallest = self.getMinIndex(left,right)
        else:
            smallest = left

        if self.heapList[i] > self.heapList[smallest]:
            #print("swap:("+str(smallest)+","+str(i)+")")
            self.swap(i,smallest)
        #print("SelfHeapify:("+str(smallest)+","+str(len)+")")
        self.min_heapify(smallest,len)

    #max_heapify
    def max_heapify(self,i,len):
        left = 2*i+1
        right = 2*i+2
        '''print "left:"+str(left)
        print "right:"+str(right)
        print("leftlen:("+str(left)+","+str(len)+")")'''
        if left > len:
            return
        if left <=len and right <= len: # largest of left,right
            largest = self.getMaxIndex(left,right)
        else:
            largest = left

        if self.heapList[i] < self.heapList[largest]: # compare largest of left,right with parent
            #print("swap:("+str(largest)+","+str(i)+")")
            self.swap(largest,i)
        #print self.heapList
        #print("SelfHeapify:("+str(largest)+","+str(len)+")")
        self.max_heapify(largest,len)

    #BuildMaxHeap
    #first non-parent from end --> len/2)
    def build_Maxheap(self,start,len):
        for i in range((len//2), -1,-1):
            #print("Heapify:("+str(i)+","+str(len)+")")
            self.max_heapify(i,len)

    #BuildMinHeap
    def build_MinHeap(self,start,len):
        for i in range((len//2),-1,-1):
            #print("Heapify:("+str(i)+","+str(len)+")")
            self.min_heapify(i,len)

    #HeapSort Descending
    def heapSort_desc(self,i,len):
        self.build_MinHeap(i,len)
        self.size = len
        for i in range(self.size,-1,-1):
            self.swap(0,self.size)
            self.size = self.size-1
            self.min_heapify(0,self.size)
        #print self.heapList

    #HeapSort
    def HeapSort(self,i,len):
        self.size = len
        self.build_Maxheap(i,self.size)
        for i in range(self.size,-1,-1):
            self.swap(0,self.size)
            self.size = self.size-1
            self.max_heapify(0,self.size)

        #print self.heapList


if __name__ == '__main__':
    ob = Heap()
    #ob.heapList = [4,3,5,6,2,1]
    ob.heapList = [4,3,2,1,8]
    ob.heapList = [8,1,6,12,9]
    #min_index = ob.find_min()
    #print ob.heapList
    ob.heapSort_desc(0,4)
    #print ob.heapList
