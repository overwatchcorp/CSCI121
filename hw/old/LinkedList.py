
class LLNode:
    def __init__(self,value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.first = None

    def prepend(self, value):
        node = LLNode(value)
        node.next = self.first
        self.first = node

    def contains(self, value):
        current = self.first
        while current != None:
            if current.value == value:
                return True
            current = current.next
        return False

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

    def length(self):
        count = 0
        current = self.first
        while current != None:
            count = count + 1
            current = current.next
        return count
    
    def sum(self):
        sum = 0
        current = self.first
        while current != None:
            sum += current.value
            current = current.next
        return sum

    def is_empty(self):
        return (self.first == None)

    def display(self):
        print(self.as_string())

    def append(self, value):
        if self.first == None:
            self.first = LLNode(value)
        else:
            current = self.first
            while current.next != None:
                current = current.next
            current.next = LLNode(value)

    def remove(self, value):
        previous = None
        current  = self.first
        while current != None and current.value != value:
            previous = current
            current = current.next
        if current != None:
            if previous != None:
                previous.next = current.next
            else:
                self.first = current.next
    def apply (self, f):
        current = self.first
        while current != None:
            current.value = f(current.value)
            current = current.next

    def remove_all(self, value):
        current = self.first
        previous = None
        while current != None:
            if current.value == value:
                if previous == None:
                    self.first = self.first.next
                else:
                    previous.next = current.next
                current = self.first
                previous = None
            else:
                previous = current
                current = current.next


    def __str__(self):
        return self.as_string()

    def __repr__(self):
        return self.as_string()

    def __bool__(self):
        return not self.is_empty() 
    

class Sorted(LinkedList):
   def insert(self, value):
       node = LLNode(value)
       if self.first == None:
           self.first = node
           return None
       elif value < self.first.value:
           self.prepend(value)
       else:
           current = self.first
           prev = None
           while current != None and value > current.value:
               previous = current
               current = current.next
           if current == None:
               self.append(value)
           node.next = current
           if previous != None:
               previous.next = node

