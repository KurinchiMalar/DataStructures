__author__ = 'kurnagar'

import copy
import CircListNode
class CircList:
    def __init__(self,head):
        self.head = head
        #self.head.set_next(self.head)

    # Time Complexity : O(n)
    def insert_at_beginning(self,data):
        newnode = CircListNode.CircListNode(data)

        if self.head == None:
            return None

        newnode.set_next(self.head.get_next())

        current = self.head
        while current.get_next() != self.head: # beginning.
            current = current.get_next()
        current.set_next(newnode)
        self.head = newnode

    # Time Complexity : O(n)
    def insert_at_end(self,data):
        if self.head == None:
            return None

        newnode = CircListNode.CircListNode(data)

        if self.head.get_next() == self.head: # only one node
            newnode.set_next(self.head)
            self.head.set_next(newnode)

        else:
            current = self.head
            while current.get_next() != self.head:  # end
                current = current.get_next()

            current.set_next(newnode)
            newnode.set_next(self.head)

    # Time Complexity : O(n)
    def insert_at_pos(self,pos,data):

        newnode = CircListNode.CircListNode(data)

        if self.head == None:
            return None

        if pos == 0:
            self.insert_at_beginning(data)
        else:
            prev = None
            current = self.head
            count = 0
            while current.get_next() != self.head:
                prev = current
                current = current.get_next()
                count = count + 1

                if count == pos:
                    prev.set_next(newnode)
                    newnode.set_next(current)
                    break

    # Time Complexity : O(n)
    def delete_at_beginning(self):

        if self.head == None:
            return None

        current = self.head
        while current.get_next() != self.head: # beginning.
            current = current.get_next()
        current.set_next(self.head.get_next())
        self.head = self.head.get_next()
        return True

    # Time Complexity : O(n)
    def delete_at_pos(self,pos):

        if self.head == None:
            return False

        if pos == 0:
            self.delete_at_beginning()
        elif pos >= self.get_length_of_list():
            return False
        else:
            prev = self.head
            current = self.head.get_next()
            count = 1
            while current != self.head:
                if count == pos:
                    prev.set_next(current.get_next())
                    break
                prev = current
                current = current.get_next()
                count = count + 1
            return True
    # Time Complexity : O(n) Worst case
    def search_data(self,data):

        if self.head == None:
            return False

        if self.head.get_data() == data:
            return True

        current = self.head.get_next()

        while current != self.head:
            if current.get_data() == data:
                return True
            current = current.get_next()
        return False


    # Time Complexity : O(n)
    def traverse_list(self):
        current = self.head
        count = 0
        while current.get_next() != self.head:
            print current.get_data(),
            count = count + 1
            current = current.get_next()

        print current.get_data(),
        print
        return count+1

    # Time Complexity : O(n)
    def get_length_of_list(self):
        current = self.head
        count = 0
        while current.get_next() != self.head:
            count = count + 1
            current = current.get_next()
        return count+1



head = CircListNode.CircListNode(1)
#print CircListNode.CircListNode.__str__(head)
n1 = CircListNode.CircListNode(2)
n2 = CircListNode.CircListNode(3)
n3 = CircListNode.CircListNode(4)
n4 = CircListNode.CircListNode(5)
n5 = CircListNode.CircListNode(6)
n6 = CircListNode.CircListNode(7)

#orig_head = CircListNode.CircListNode(1)
#orig_head.set_next(n1)

head.set_next(n1)
n1.set_next(n2)
n2.set_next(n3)
n3.set_next(n4)
n4.set_next(n5)
n5.set_next(n6)
n6.set_next(head) # making it circular

clist = CircList(head) # initialize head and tail.
orig_clist = copy.deepcopy(clist)

length = clist.traverse_list()
#print ""+str(clist.get_length_of_list())
print "Length of orig list: "+ str(length)
print "----------------------------"

clist = copy.deepcopy(orig_clist)
clist.insert_at_beginning(9)
print "insert begin done. length: "+str(clist.traverse_list())

clist = copy.deepcopy(orig_clist)
clist.insert_at_end(9)
print "insert end done. length: "+str(clist.traverse_list())

clist = copy.deepcopy(orig_clist)
clist.insert_at_pos(1,77)
print "insert at pos done. length: "+str(clist.traverse_list())
print "----------------------------"
clist = copy.deepcopy(orig_clist)
print "List is . length: "+str(clist.traverse_list())
print "isFound: "+str(clist.search_data(7))
print "----------------------------"

clist = copy.deepcopy(orig_clist)
print "Deletion status:"+str(clist.delete_at_pos(7))
print "Deleted List is . length: "+str(clist.traverse_list())
print "----------------------------"

