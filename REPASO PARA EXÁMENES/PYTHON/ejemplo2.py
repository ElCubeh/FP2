"""Inserción intermedia: En lugar de insertar nodos al principio o al final, los nodos se insertarán en una posición intermedia, 
específicamente después del primer nodo cuyo valor sea un entero (como definimos en el ejercicio anterior).
Eliminación diferente: En lugar de eliminar strings con vocales (delete_vowel_strings), implementaremos un nuevo tipo de eliminación. 
Para variar, el nuevo método eliminará nodos cuyos valores sean enteros mayores que un umbral dado (por ejemplo, enteros mayores a 5)."""

class LinkedList:
    class Node:
        def init(self, value):
            self.value = value
            self.next_node = None

    def init(self):
        self.head = None
        self.tail = None

    def insert_middle(self, value):
        new_node = self.Node(value)
        if not self.head:
            # Si la lista está vacía, insertar como cabeza
            self.head = self.tail = new_node
            return

        current = self.head
        prev = None
        while current and not isinstance(current.value, int):
            prev = current
            current = current.next_node

        if current:
            # Insertar después del primer entero
            new_node.next_node = current.next_node
            current.next_node = new_node
            if not new_node.next_node:
                self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.__tail = new_node
    def delete_large_integers(self, threshold):
        while self.head and isinstance(self.head.value, int) and self.head.value > threshold:
            self.head = self.head.next_node
            if not self.head:
                self.tail = None
        current = self.head
        while current and current.next_node:
            if isinstance(current.next_node.value, int) and current.next_node.value > threshold:
                current.next_node = current.next_node.next_node
                if not current.next_node:
                    self.tail = current
            else:
                current = current.next_node

    def display(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next_node

    def sum_numbers(self):
        total = 0
        current = self.__head
        while current:
            if isinstance(current.value, int):
                total += current.value
            current = current.next_node
        return total