"""Este módulo ofrece una clase para manejar listas encadenadas."""


class SortedLinkedList:
    """Representa una lista simplemente encadenada."""

    class Node:
        """Nodo de una lista simplemente encadenada."""

        def __init__(self, value, next_node=None):
            """Cada nodo tiene un valor y un enlace al siguiente nodo."""
            self.value = value
            self.next_node = next_node

    def __init__(self):
        """Incializa una lista vacía."""
        self.__first = None
        self.__len = 0

    def __len__(self):
        """Devuelve el número de elementos de la lista."""
        return self.__len

    def __iter__(self):
        """Generdor para recorrer la lista."""
        current = self.__first

        while current is not None:
            yield current.value
            current = current.next_node

    def insert(self, value):
        """Inserta un elemento en una lista ordenada de menor a mayor."""
        if len(self) == 0 or value <= self.__first.value:
            self.__first = self.Node(value, self.__first)
        else:
            current = self.__first

            while (
                current.next_node is not None and
                current.next_node.value < value
            ):
                current = current.next_node

            current.next_node = self.Node(value, current.next_node)

        self.__len += 1
