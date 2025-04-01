# Escriba aquí el código requerido.
from sortedlinkedlist import SortedLinkedList


class DeletableSLL(SortedLinkedList):
    def __init__(self):
        """Inicializador de la clase."""
        super().__init__()

    def delete(self, value):
        if self._SortedLinkedList__first is None:  # Lista vacía
            return

        # Eliminar todas las ocurrencias al principio de la lista
        while self._SortedLinkedList__first is not None and \
                self._SortedLinkedList__first.value == value:
            self._SortedLinkedList__first = \
                self._SortedLinkedList__first.next_node
            self._SortedLinkedList__len -= 1

        if self._SortedLinkedList__first is None:
            return

        # Eliminar ocurrencias en el medio o final de la lista
        prev = self._SortedLinkedList__first
        current = self._SortedLinkedList__first.next_node

        while current is not None and current.value <= value:
            if current.value == value:
                prev.next_node = current.next_node
                self._SortedLinkedList__len -= 1
                current = current.next_node
            else:
                prev = current
                current = current.next_node
