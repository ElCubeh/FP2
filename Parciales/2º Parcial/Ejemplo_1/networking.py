

class InterestGroup():

    class Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    def __init__(self):
        self.first = None
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
        current = self.first
        while current:
            if current.next is None:
                current.next = new_node
                self._size += 1
                return True     
            current = current.next #añadir último
        self.first = new_node
        self._size += 1
        return True     #añadir primero
    @property
    def size(self):
        return self._size
    
    def copy(self):
        new_group = InterestGroup()
        new_group.add_member(self.first.value)
        current = self.first.next
        while current:
            new_group.add_member(current.value)
            current = current.next
        return new_group


    def union(self, other_group):
        new_group = self.copy()
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
                    return True         #eliminar 1º
                elif current.next is None:
                    prev.next = None
                    return True         #eliminar último
                else:
                    prev.next = current.next
                    current.next = None
                self._size -= 1
                return True             #eliminar medio
            prev = current
            current = current.next
        return False
    
    def __str__(self):
        current = self.first
        result = ""
        while current:
            result += f"{current.value}]->"
            current = current.next
        return result + "None"
