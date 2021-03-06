
from LinkedLists.ListNode import ListNode
class Queue:
    def __init__(self,head=None):
        self.head = head
        self.size = 0

    # Time Complexity: O(1)
    def enqueue(self,data):
        newnode = ListNode(data)
        self.size = self.size + 1
        if self.head == None:
            self.head = newnode
            return self.head
        else:
            current = self.head
            while current.get_next() != None:
                current = current.get_next()
            current.set_next(newnode)
        return self.head
    # Time Complexity : O(1)
    def dequeue(self):
        if self.head == None:
            return None
        else:
            self.size = self.size - 1
            torem = self.head
            self.head = self.head.get_next()
            return torem.get_data()

    def print_queue(self):
        current = self.head
        while current != None:
            print current.get_data(),
            current = current.get_next()
        print

'''q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()
#q.dequeue()
q.print_queue()
print q.size'''