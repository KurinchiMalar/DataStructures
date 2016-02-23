'''
A Deque is a doubly ended queue, that allows insertion and deletion at both the ends.
'''
from LinkedLists import DListNode
class DoublyLinkedList:
    def __init__(self,head,tail):
        self.head = head
        self.tail = tail
        self.size = 0
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

    # Time Complexity : O(1)
    def insert_at_beginning(self,data):

        newnode = DListNode.DListNode(data)
        self.size = self.size + 1
        if self.head == None:
            self.head = newnode
            self.tail = newnode

        else:
            if self.head.get_next() == None: # only one node, then set tail appropriately.
                self.tail = self.head
            self.head.set_prev(newnode)
            newnode.set_next(self.head)
            self.head = newnode

        return self.head

    # Time Complexity : O(1)
    def insert_at_end(self,data):

        newnode = DListNode.DListNode(data)
        self.size = self.size + 1
        if self.tail == None:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.set_next(newnode)
            newnode.set_prev(self.tail)
            self.tail = newnode
        return self.head


    def delete_at_beginning(self):
        if self.head == None:
            print "Empty list, cannot be deleted!!!!!!!!!."
            return -1
        if self.head == self.tail:
            torem = self.head
            self.head = None
            self.tail = None
            self.size = 0
            return torem
        torem = self.head
        self.head = self.head.get_next()
        self.head.set_prev(None)
        self.size = self.size - 1
        return torem

    def delete_at_end(self):

        if self.head == None:
            print "Empty list, cannot be deleted."
            return -1
        elif self.head == self.tail: # One node
            torem = self.head
            self.head = None
            self.tail = None
            self.size = 0
            #print "CurTail: "+str(self.tail.get_data())
            return torem
        else:
            torem = self.tail
            previousNode = self.tail.get_prev()
            torem.set_prev(None)
            self.size = self.size - 1
            self.tail = previousNode
            self.tail.set_next(None)
            print "CurTail: "+str(self.tail.get_data())
            return torem

class DEQ:
    def __init__(self,dlist=None):
        self.dlist = dlist

    def get_size(self):
        if self.dlist == None:
            return 0
        return self.dlist.size

    def peek_head(self):
        if self.dlist.head == None:
            print "Peek_head: Dlist empty."
            return -1
        return self.dlist.head.get_data()

    def peek_tail(self):
        if self.dlist.tail == None:
            print "DList empty"
            return -1
        return self.dlist.tail.get_data()

    def push_front(self,data):
        if self.dlist == None:
            self.dlist = DoublyLinkedList(None,None)
        return self.dlist.insert_at_beginning(data)

    def push_back(self,data):
        if self.dlist == None:
            self.dlist = DoublyLinkedList(None,None)
        return self.dlist.insert_at_end(data)

    def pop_front(self):
        if self.dlist == None:
            print "Nothing to pop!. Dq not initialized!"
            return -1
        return self.dlist.delete_at_beginning()

    def pop_back(self):
        if self.dlist == None:
            print "Nothing to pop!. Dq not initialized!"
            return -1
        return self.dlist.delete_at_end()

    def print_deq(self):
        return self.dlist.print_forward()
'''dlist = DoublyLinkedList(None,None)
dq = DEQ(dlist)

dq.push_front(9)
dq.push_front(8)
dq.push_front(7)
dq.push_front(6)
dq.push_front(5)
dq.push_front(4)
dq.push_front(3)

dq.print_deq()
dq.pop_front()
dq.pop_back()
dq.print_deq()
dq.pop_front()
dq.pop_back()
dq.print_deq()
dq.pop_front()
dq.pop_back()
dq.print_deq()
dq.pop_front()
dq.pop_back()
#dq.push_back(4)
#dq.pop_front()

dq.print_deq()
print dq.get_size()'''

