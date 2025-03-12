"""Module with the answer to the problem."""


class Matriz:
    """matriz."""

    def __init__(self, nfilas, valor_inicial):
        """Inicializa la matriz al valor indicado."""

        self.__vinicial = valor_inicial
        self.__mat = [
            [self.__vinicial for j in range(nfilas)] for i in range(nfilas)
        ]

    @property
    def dimension(self):
        return self._dimension
    
    @dimension.setter
    def dimension(self, nueva_dimension):
        if nueva_dimension < self._dimension:
            raise ValueError("No se puede reducir la dimensión de la matriz.")
        elif nueva_dimension > self._dimension:
            for fila in self._matriz:
                fila.extend([self._matriz[0][0]] * (nueva_dimension - self._dimension))
            self._matriz.extend([[self._matriz[0][0]] * nueva_dimension for _ in range(nueva_dimension - self._dimension)])
        self._dimension = nueva_dimension
    
    def valor(self, fila, columna):
        if not (0 <= fila < self._dimension and 0 <= columna < self._dimension):
            raise IndexError("Índice fuera de rango.")
        return self._matriz[fila][columna]
    
    def cambia_valor(self, fila, columna, nuevo_valor):
        if not (0 <= fila < self._dimension and 0 <= columna < self._dimension):
            raise IndexError("Índice fuera de rango.")
        self._matriz[fila][columna] = nuevo_valor

    def __str__(self):
        return "\n".join([str(fila) for fila in self.__mat])