from containerbase import ContainerBase 

class InterestGroup(ContainerBase):

    class Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    def is_member(self, name):
        current = self.first  
        while current:
            if current.value == name:
                return True
            current = current.next
        return False

    def add_member(self, name):
        if self.is_member(name):
            return False
        new_node = self.Node(name)
        if self.first is None:  
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self._size += 1
        return True

    @property
    def size(self):
        return self._size

    def union(self, other_group):
        new_group = InterestGroup()
        current = self.first  
        while current:
            new_group.add_member(current.value)
            current = current.next
        current = other_group.first  
        while current:
            new_group.add_member(current.value)
            current = current.next
        return new_group

    def remove_member(self, name):
        current = self.first  
        prev = None
        while current:
            if current.value == name:
                if prev is None:
                    self.first = current.next  
                    if self.first is None:
                        self.last = None  
                else:
                    prev.next = current.next
                    if current == self.last:  
                        self.last = prev
                self._size -= 1
                return True
            prev = current
            current = current.next
        return False