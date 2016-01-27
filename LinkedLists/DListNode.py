__author__ = 'kurnagar'

class DListNode:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

    def set_data(self,newdata):
        self.data = newdata

    def get_data(self):
        return self.data

    def set_next(self,node):
        self.next = node

    def get_next(self):
        return self.next

    def has_next(self):
        return self.next != None

    def set_prev(self,node):
        self.prev = node

    def get_prev(self):
        return self.prev

    def has_prev(self):
        return self.prev != None

    # __str__ returns string equivalent of Object
    def __str__(self):
        return "Node[Data = %s]" % (self.data,)
