    def getMaxIndex(self,x,y):
        if self.heapList[x] > self.heapList[y]:
            return x
        else:
            return y

    #heapify
    def max_heapify(self,i,len):
        left = 2*i+1
        right = 2*i+2
        print "left:"+str(left)
        print "right:"+str(right)
        print("leftlen:("+str(left)+","+str(len)+")")
        if left > len:
            return
        if left <=len and right <= len: # largest of left,right
            largest = self.getMaxIndex(left,right)
        else:
            largest = left

        if self.heapList[i] < self.heapList[largest]: # compare largest of left,right with parent
            print("swap:("+str(largest)+","+str(i)+")")
            self.swap(largest,i)
        print self.heapList
        print("SelfHeapify:("+str(largest)+","+str(len)+")")
        self.max_heapify(largest,len)

    #BuildHeap
    #first non-parent from end --> len/2)
    def build_heap(self,start,len):
        for i in range((len//2), -1,-1):
            print("Heapify:("+str(i)+","+str(len)+")")
            self.max_heapify(i,len)

    #HeapSort
    def HeapSort(self,i,len):
        self.size = len
        self.build_heap(i,self.size)
        for i in range(self.size,-1,-1):
            self.swap(0,self.size)
            self.size = self.size-1
            self.max_heapify(0,self.size)

        print self.heapList


if __name__ == '__main__':
    ob = Heap()
    ob.heapList = [4,3,5,6,2,1]
    ob.heapList = [4,3,2,1,8]
    #min_index = ob.find_min()
    print ob.heapList
    ob.HeapSort(0,4)
    print ob.heapList
