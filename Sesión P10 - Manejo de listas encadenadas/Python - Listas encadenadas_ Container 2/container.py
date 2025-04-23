class Container:
    class Node:
        def __init__(self, value, next = None):
            self.value = value  # El valor en el nodo.
            self.next = next    # El enlace al siguiente nodo.


    def __init__(self):
        self.first = None   # El enlace al primer nodo de la lista.
        self.last = None   # El enlace al último nodo de la lista.


    def insert(self, value):
        new_node = Container.Node(value)
        if self.last:
            self.last.next = new_node
        self.last = new_node
        if not self.first:
            self.first = new_node
    
    # ESCRIBA SOLO A PARTIR DE ESTA LÍNEA. NO ELIMINE LAS LÍNEAS ANTERIORES.
    @property
    def size(self):
        current = self.first
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def find_unique(self, value):
        current = self.first
        count = 0
        while current:
            if current.value == value:
                count += 1
            current = current.next
        return count == 1

    def delete_all(self, value):
        current = self.first
        prev = None
        while current:
            if current.value == value:
                if prev is None:
                    self.first = current.next
                else:
                    prev.next = current.next
                if current.next is None:
                    self.last = prev
                current = current.next
                continue
            prev = current
            current = current.next
