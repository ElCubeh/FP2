"""Módulo con la respuesta del estudiante."""


class Matriz():
    """Implementación de matriz bidimensional y operaciones asociadas."""

    def __init__(self, n, m, v):
        """Crea atributo: matriz n x m rellena con v."""
        self._mat = [[v]*m for i in range(n)]

    def dimensiones(self):
        return len(self._mat), len(self._mat[0])

    def test(self, fila, columna):
        len1 = len(self._mat)
        len2 = len(self._mat[0])
        if fila < 0 or fila >= len1 or columna < 0 or columna >= len2:
            raise IndexError("Índice fuera de rango")
        else:
            return True

    def valor(self, fila, columna):
        if self.test(fila, columna):
            return self._mat[fila][columna]

    def cambia_valor(self, fila, columna, valor):
        if self.test(fila, columna):
            self._mat[fila][columna] = valor

    def get_str(self):
        return str(self._mat)
