class DLLNode:
    def __init__ (self, value):
        self.value = value
        self.prev = None
        self.next = None

class DLinkedList:
    def __init__ (self): 
        self.first = None
        self.last = None
    def as_string(self):
        if self.first == None:
            return "<>"
        else:
            s = "<" + str(self.first.value)
            current = self.first.next
            while current != None:
                s = s + ", " + str(current.value)
                current = current.next
            s = s + ">"
            return s
    def prepend (self, value):
        node = DLLNode(value)
        if self.first == None:
            self.first = node
            self.last = node
            return None
        self.first.prev = node
        node.next = self.first
        self.first = node
        # make it so that if the list is one long, self.first and self.last are the same values
        if self.first.next == None:
            self.last = node

    def append (self, value):
        node = DLLNode(value)
        current = self.first
        if current == None:
            self.first = node
            self.last = node
            return None
        while current.next != None:
            current = current.next
        current.next = node
        node.prev = current
        self.last = node

    def remove(self, value):
        current = self.first
        while current.value != value:
            current = current.next
        if current.next == None:
            current.prev.next = None
            self.last = current.prev
        elif current.prev == None:
            self.first = current.next
        else:
            current.prev.next = current.next

    def insert_at(self, index, value):
        current = self.first
        node = DLLNode(value)
        if self.first == None:
            self.first = node
            self.last = node
            return None
        for x in range(0, index):
            if current.next != None:
                current = current.next
            else:
                self.append(value)
                return None
        if index == 0:
            self.first = node
            node.next = current
            current.prev = node
        else:
            node.prev = current.prev
            current.prev.next = node
            current.prev = node
            node.next = current
            

    def __str__(self):
        return self.as_string()

d = DLinkedList()
d.prepend(3)
d.prepend(2)
d.prepend(1)
d.prepend(0)
d.remove(0)
print(d)
