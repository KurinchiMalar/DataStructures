
#Time Complexity : O(n+ klogn)
# n elements to be put in heap first, then k number of extract min ==> k times minHeapify() = k*logn

class Heap:
    def __init__(self):
        self.heapList = [0]
        self.heapsize = 0

    def swap(self,x,y):
        temp = self.heapList[x]
        self.heapList[x] = self.heapList[y]
        self.heapList[y] = temp

    def find_min_of_xy(self,x,y):
        if self.heapList[x] < self.heapList[y]:
            return x
        else:
            return y

    def find_max_of_xy(self,x,y):
        if self.heapList[x] > self.heapList[y]:
            return x
        else:
            return y

    def min_heapify(self,i):
        left = 2*i+1
        right = 2*i+2
        smallest = -1
        print "(i , left,right)"+"...."+str(i)+","+str(left)+","+str(right)
        if left >= self.heapsize:
            return

        if left < self.heapsize and right < self.heapsize:
            smallest = self.find_min_of_xy(left,right)
        elif left < self.heapsize:
            smallest = left
        if self.heapList[i] > self.heapList[smallest]:
            print "swap("+str(i)+","+str(smallest)+")"
            self.swap(i,smallest)
        print ("    min_heapify("+str(smallest)+")")
        self.min_heapify(smallest)

    def max_heapify(self,i):
        left = 2*i+1
        right = 2*i+2
        largest = -1
        print "(i , left,right)"+"...."+str(i)+","+str(left)+","+str(right)
        if left >= self.heapsize:
            return

        if left < self.heapsize and right < self.heapsize:
            largest = self.find_max_of_xy(left,right)
        elif left < self.heapsize:
            largest = left
        if self.heapList[i] < self.heapList[largest]:
            print "swap("+str(i)+","+str(largest)+")"
            self.swap(i,largest)
        print ("    max_heapify("+str(largest)+")")
        self.max_heapify(largest)

    def extract_min(self):
        print self.heapList

        if self.heapsize > 0:
            #min_elem = self.heapList.pop(0) # pop() removes the element
            min_elem = self.heapList[0]
            self.swap(self.heapsize-1,0)
            self.heapsize = self.heapsize-1
            self.min_heapify(0)
            return min_elem
        else:
            print "Cannot extract from empty heap!"
            return -1

    def extract_max(self):
        print self.heapList

        if self.heapsize > 0:
            #min_elem = self.heapList.pop(0) # pop() removes the element
            max_elem = self.heapList[0]
            self.swap(self.heapsize-1,0)
            self.heapsize = self.heapsize-1
            self.max_heapify(0)
            return max_elem
        else:
            print "Cannot extract from empty heap!"
            return -1

    def build_Minheap(self):
        for i in range((self.heapsize/2)-1,-1,-1):
            print "-----------------------------------"
            print("min_heapify("+str(i)+")...")
            self.min_heapify(i)

    def build_Maxheap(self):
        for i in range((self.heapsize/2)-1,-1,-1):
            print "-----------------------------------"
            print("max_heapify("+str(i)+")...")
            self.max_heapify(i)

    def get_kth_smallest(self,k):
        self.build_Minheap()
        val = 0
        for i in range(1,k+1):
            val = self.extract_min()
        return val

    def get_kth_largest(self,k):
        self.build_Maxheap()
        val = 0
        for i in range(1,k+1):
            val = self.extract_max()
        return val

ob = Heap()
ob.heapList = [4,9,6,7,8,1,2]
ob.heapsize = len(ob.heapList)

#print "kth smallest is :"+str(ob.get_kth_smallest(6))

print "kth largest is :"+str(ob.get_kth_largest(3))
