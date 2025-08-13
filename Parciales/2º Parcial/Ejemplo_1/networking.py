from networking import InterestGroup

class InterestGroup():

    class Node:
        def __init__(self, value:str, next=None)-> None:
            self.value = value
            self.next = next

    def __init__(self)->None:
        self.first = None
        self._size = 0

    def is_member(self, name:str)-> bool:
        current = self.first  
        while current:
            if current.value == name:
                return True
            current = current.next
        return False

    def add_member(self, name:str) -> bool:
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
    def size(self) -> int:
        return self._size
    
    def copy(self)-> InterestGroup:
        new_group = InterestGroup()
        new_group.add_member(self.first.value)
        current = self.first.next
        while current:
            new_group.add_member(current.value)
            current = current.next
        return new_group


    def union(self, other_group:InterestGroup) -> InterestGroup:
        new_group = self.copy()
        current = other_group.first
        while current:
            new_group.add_member(current.value)
            current = current.next
        return new_group

    def remove_member(self, name:str) -> bool:
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
    
    def __str__(self)-> str:
        current = self.first
        result = ""
        while current:
            result += f"{current.value}]->"
            current = current.next
        return result + "None"
