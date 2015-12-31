#Problem: Given an array of elements , each which is at most K positions from it's target position, devise an algorithm that sorts in O(nlogK)

'''
# eg)    Input : 6 9 10 1 2 3 5

    Say k = 3 means every element will be at position+3. Where position is the actual location of it when the array is sorted.

    Above array when sorted = 1 2 3 5 6 9 10

    See element 2 at position 1 , is in position (1+ 3) = 4 in input.

Solution 1: Insertion Sort -> Complexity O(nk)

Solution 2: Using Minheap  --> Complexity O(k) + O((n-k)*logn)

        Insert first k+1 elements into minheap --> O(k)
        for i in ( k+1 to n) : --> (n-k) * O(log n)
            remove minimum from heap and start filling result array from 0
            Insert k+1 into removed element's place in heap. And heapify again if necessary.
        once i reached n
            extract minimum from heap and keep filling result array.(because the most maximum will be retained in heap till last) -->O(1)
'''
class Heap:
    def __init__(self):
        self.kplusone_elemlist = []
        self.heapsize = 0

    def swap(self,x,y):
        temp = self.kplusone_elemlist[x]
        self.kplusone_elemlist[x] = self.kplusone_elemlist[y]
        self.kplusone_elemlist[y] = temp

    def find_min_of_xy(self,x,y):
        if self.kplusone_elemlist[x] < self.kplusone_elemlist[y]:
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

        if self.kplusone_elemlist[i] > self.kplusone_elemlist[smallest]:
            print "swap("+str(i)+","+str(smallest)+")"
            self.swap(i,smallest)
        print ("    min_heapify("+str(smallest)+")")
        self.min_heapify(smallest)


    def build_MinHeap(self):
        for i in range((self.heapsize/2)-1,-1,-1):
            print "-----------------------------------"
            print("min_heapify("+str(i)+")...")
            self.min_heapify(i)

    def replace_min(self,elem):
        min_elem = self.kplusone_elemlist[0]
        self.kplusone_elemlist[0] = elem
        if elem > min_elem: # minheapify necessary
            self.min_heapify(0)
        return min_elem

    def extract_min(self):
        if self.heapsize > 0:
            min_elem = self.kplusone_elemlist[0]
            self.swap(self.heapsize-1,0)
            self.heapsize = self.heapsize-1
            self.min_heapify(0)
            return min_elem
        else:
            print "Cannot extract from empty heap!"
            return -1

    def sort_nearlysorted(self,Ar,k):

        print Ar

        # create array from 0 to k+1
        for b in range(0,k+1):
            self.kplusone_elemlist.append(Ar[b])
        self.heapsize = len(self.kplusone_elemlist)
        print "elem_list"+str(self.kplusone_elemlist)

        self.build_MinHeap()
        print "minheap elem_list"+str(self.kplusone_elemlist)

        j = k+1
        for i in range(0,len(Ar)):

            if j < len(Ar): # take min from minheap, and replace one element from (k+1 to n) range to heap[0]
                print "replacing Ar["+str(i)+"] with "+ str(Ar[j])
                Ar[i] = self.replace_min(Ar[j])
                #print "replacing Ar["+i+"] with "+ str(Ar[j])
                j = j+1
            else:
                Ar[i] = self.extract_min()
        print "sorted :"+str(Ar)


ob = Heap()
A = [6,9,10,1,2,3,5]
Ar = A[:]

ob.sort_nearlysorted(Ar,3)

