class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

    def set_data(self,newdata):
        self.data = newdata

    def get_data(self):
        return self.data

    def set_next(self,newnode):
        self.next = newnode

    def get_next(self):
        return self.next

    def has_next(self):
        return self.next != None


class MyList():
    def __init__(self,head=None):
        self.head = head


    def insert_in_mylist(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.get_next() != None:
                current = current.get_next()
            current.set_next(new_node)


    def size_of_mylist(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def print_mylist(self):
        current = self.head
        while current:
            print ""+str(current.get_data())
            current = current.get_next()


# Time Complexity : O(n)
# Space Complexity : O(n)

def check_loop_in_list(head):
    hash_table = {}
    current = head
    while current:
        if current in hash_table:
            print "Loop found! :"+str(current.get_data())
            return 1
        else:
            hash_table[current] = current.get_data()
            current = current.get_next()
    return -1



#Ar = [3,4,5,6,4,5,6,7]

head = Node(3)
n1 = Node(4)
n2 = Node(5)
n3 = Node(6)
n4 = Node(7)

head.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = None

temp = head

print "printing...."
while temp:
    print ""+str(temp.data)
    temp = temp.next
print temp
print head

#l1.print_mylist()
print ""+str(check_loop_in_list(head))
