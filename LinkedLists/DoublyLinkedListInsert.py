class Node(object):
    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node


def SortedInsert(head, data):
    if head == None:
        head = Node(data)
        return head

    p = head

    newNode = Node(data)

    if p.data > data:  # insert in beginning
        newNode.next = p
        p.prev = newNode
        head = newNode
        return head

    while p.next != None:

        if p.data > data:  # insert in middle

            p.prev.next = newNode
            newNode.prev = p.prev
            newNode.next = p
            p.prev = newNode
            return head

        p = p.next

    if p.data < data:
        p.next = newNode  # insert at last
        newNode.prev = p
        return head

    p.prev.next = newNode
    newNode.prev = p.prev
    newNode.next = p
    p.prev = newNode
    return head


def print_dlist(head):
    current = head

    while current != None:
        print current.data,
        current = current.next
    print

def swap(current):

    temp = current.next
    current.next = current.prev
    current.prev = temp


def Reverse(head):
    if head == None:
        return head

    current = head

    while current != None:
        swap(current)
        #current.next,current.prev = swap(current.next,current.prev)
        #current.next,current.prev = current.prev,current.next
        if current.prev == None:
            head = current
            return current
        current = current.prev

    return head


one = Node(1)
head = one
two = Node(2)
three = Node(3)
four = Node(4)
six = Node(6)

one.next = two
two.prev = one

three.prev = two
two.next = three

four.prev = three
three.next = four

six.prev = four
four.next = six

print_dlist(head)
# head = SortedInsert(head,5)

# print_dlist(head)
head = Reverse(head)
print_dlist(head)
