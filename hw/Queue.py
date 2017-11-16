class LLNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:

    def __init__(self):
        self.first = None
        self.last = None
        
    def enqueue(self, value):
        node = LLNode(value)
        if self.first == None:
            self.first = node
            self.last = node
        else:
            current = self.first
            while current.next != None:
                current = current.next
            current.next = node
            self.last = node

    def head(self):
        if self.first == None:
            return None
        else:
            return self.first.value
    
    def dequeue(self):
        previousFirst = self.first
        self.first = self.first.next
        if self.first == None:
            self.last = None
        return previousFirst.value


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()
q.enqueue(4)
q.dequeue()
q.dequeue()
q.dequeue()
