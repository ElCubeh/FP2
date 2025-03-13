from stackexceptions import StackEmptyError


class Stack:
    def __init__(self):
        """Inicializa una pila vacía."""
        self._elements = []

    def push(self, item):
        """Añade un elemento a la pila."""
        self._elements.append(item)

    def pop(self):
        """Extrae y devuelve el elemento más reciente de la pila."""
        if self.is_empty():
            raise StackEmptyError
        return self._elements.pop()

    @property
    def top(self):
        """Devuelve el elemento más reciente sin extraerlo."""
        if self.is_empty():
            raise StackEmptyError
        return self._elements[-1]

    def is_empty(self):
        """Devuelve True si la pila está vacía, False en caso contrario."""
        return len(self._elements) == 0

    def __len__(self):
        """Devuelve la cantidad de elementos en la pila."""
        return len(self._elements)
