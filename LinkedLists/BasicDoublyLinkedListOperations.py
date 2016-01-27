__author__ = 'kurnagar'

import DListNode
import copy

class DoublyLinkedList:
    def __init__(self,head,tail):
        self.head = head
        self.tail = tail
    # Time Complexity : O(n)
    def print_forward(self):
        current = self.head
        if current == None:
            return -1
        count = 0
        while current != None:
            print current.get_data(),
            count = count + 1
            current = current.get_next()
        print
        return count

    # Time Complexity : O(n)
    def print_reverse(self):
        current = self.tail
        if current == None:
            return -1
        count = 0
        while current != None:
            print current.get_data(),
            count = count + 1
            current = current.get_prev()
        print
        return count

    # Time Complexity : O(1)
    def insert_at_beginning(self,data):

        newnode = DListNode.DListNode(data)
        if self.head == None:
            self.head = newnode
            self.tail = newnode
        else:
            self.head.set_prev(newnode)
            newnode.set_next(self.head)
            self.head = newnode

    # Time Complexity : O(1)
    def insert_at_end(self,data):

        newnode = DListNode.DListNode(data)
        if self.tail == None:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.set_next(newnode)
            newnode.set_prev(self.tail)
            self.tail = newnode

    def get_node_at_given_index(self,index):

        if self.head == None:
            return None
        current = self.head
        i = 0
        while i < index and current.get_next() != None:
            i = i + 1
            current = current.get_next()

        if i < index and current == None:
            return None # index invalid
        return current #

    # Time Complexity : O(n) # if position is n worst case.
    def insert_at_given_position(self,pos,data):

        newnode = DListNode.DListNode(data)

        if self.head == None or pos == 0:
            return self.insert_at_beginning(data)

        count = 0
        current = self.get_node_at_given_index(pos)

        if current == None or current.get_next()==None:
            self.insert_at_end(data)
        else:
            print "came here"

            newnode.set_next(current)
            newnode.set_prev(current.get_prev())
            current.get_prev().set_next(newnode)
            current.set_prev(newnode)

    # Time Complexity : O(n) Worst Case
    def search_for_given_data(self,data):

        if self.head == None:
            return False

        current = self.head

        while current != None:
            if current.get_data() == data:
                return True
            current = current.get_next()
        return False

    # Time Complexity : O(n) middle
    #                   O(1) for begin and end
    def delete(self,data):

        if self.head == None:
            return False

        if self.head.get_data() == data:
            self.head = self.head.get_next()
            return True

        elif self.tail.get_data() == data:
            self.tail.get_prev().set_next(None)
            return True

        else: # should be in middle
            current = self.head
            while current != None:
                if current.get_data() == data:
                    current.get_prev().set_next(current.get_next())
                    current.get_next().set_prev(current.get_prev())
                    return True
                current = current.get_next()
            return False


head = DListNode.DListNode(1)

n1 = DListNode.DListNode(2)
n2 = DListNode.DListNode(3)
n3 = DListNode.DListNode(4)
n4 = DListNode.DListNode(5)
n5 = DListNode.DListNode(6)
n6 = DListNode.DListNode(7)

orig_head = DListNode.DListNode(1)
orig_head.set_next(n1)

head.set_next(n1) # no need prev for first node

n1.set_next(n2)
n1.set_prev(head)

n2.set_next(n3)
n2.set_prev(n1)

n3.set_next(n4)
n3.set_prev(n2)

n4.set_next(n5)
n4.set_prev(n3)

n5.set_next(n6)
n5.set_prev(n4)

n6.set_prev(n5) # no need next for last node


dlist = DoublyLinkedList(head,n6)
orig_dlist = copy.deepcopy(dlist)

print "ForwardPrint - length of dlist: "+str(dlist.print_forward())
print "ReversePrint -length of dlist: "+str(dlist.print_reverse())
print "-----------------------------------------------------------"

dlist = copy.deepcopy(orig_dlist)
dlist.insert_at_beginning(8)
print "Insert at beginning: "+str(dlist.print_forward())
dlist = copy.deepcopy(orig_dlist)
dlist.insert_at_end(8)
print "Insert at end: "+str(dlist.print_forward())
dlist = copy.deepcopy(orig_dlist)
index = 3
print "Node at index: "+str(index)+ " is: "+DListNode.DListNode.__str__(dlist.get_node_at_given_index(3))
dlist.insert_at_given_position(3,100)
print "Insert at given position: "+str(index)+" Length is :"+str(dlist.print_forward())
print "-----------------------------------------------------------"
dlist = copy.deepcopy(orig_dlist)
search_data = 44
print "Search for: "+str(search_data)+" result :"+str(dlist.search_for_given_data(search_data))
print "-----------------------------------------------------------"
dlist = copy.deepcopy(orig_dlist)
delete_data = 6
dlist.delete(delete_data)
print "Deleting : "+str(delete_data)+"List len is : "+str(dlist.print_forward())









