class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        next = Node(value)
        if not self.head and not self.tail:
            self.head = next
            self.tail = next
        else:
            next.set_next(self.head)
            self.head = next
    
    def add_to_tail(self, value):
        next = Node(value)
        if self.head is None and self.tail is None:
            self.head = next
            self.tail = next
        else:
            self.tail.set_next(next)
            self.tail = next
    
    def remove_tail(self):
        if self.head is None and self.tail is None:
            return None
        if self.head == self.tail:
            value = self.tail.get_value()
            self.head = None
            self.tail = None
            return value
        else:
            value = self.tail.get_value()
            current_node = self.head
            while current_node.get_next() != self.tail:
                current_node = current_node.get_next()
            self.tail = current_node
            self.tail.set_next(None)
            return value

    def remove_head(self):
        if self.head is None and self.tail is None:
            return None
        if self.head == self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value
        else:
            value = self.head.get_value()
            self.head = self.head.get_next()
            return value

    def print__elements(self):
        current = self.head

        while current is not None:
            print(current.value)
            current = current.get_next()

# a = LinkedList()

# a.add_to_tail(5)
# a.add_to_tail(15)
# a.add_to_tail(25)
# a.add_to_head(35)
# print(a.remove_tail)
# print(a.print__elements())