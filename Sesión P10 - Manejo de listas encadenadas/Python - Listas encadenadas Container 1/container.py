class Container:
    class Node:
        def __init__(self, value, next = None):
            self.value = value
            self.next = next

    # Escriba a partir de esta línea. No modifique esta línea ni las anteriores.
    def __init__(self):
        self.first = None
        self.last = None

    def insert(self, value):
        nuevo_nodo = self.Node(value)

        if self.first is None:
            self.first = nuevo_nodo
            self.last = nuevo_nodo
        else:
            self.last.next = nuevo_nodo
            self.last = nuevo_nodo

    def delete(self):
        current = self.first
        prev = None

        while current:
            if isinstance(current.value, str):
                if prev is None:
                    self.first = current.next
                else:
                    prev.next = current.next
                if current == self.last:
                    self.last = prev
                current = current.next
            else:
                prev = current
                current = current.next