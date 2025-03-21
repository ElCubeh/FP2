"""Module with the answer to the problem."""


class Matriz:
    """matriz."""

    def __init__(self, nfilas, valor_inicial):
        """Inicializa la matriz al valor indicado."""
        if nfilas < 1:
            raise ValueError("La nueva dimensión debe ser mayor o igual a 1")
        self.__vinicial = valor_inicial
        self.__mat = [
            [self.__vinicial for j in range(nfilas)] for i in range(nfilas)
        ]

    def __str__(self):
        return str(self.__mat)

    @property
    def dimension(self):
        return self.__dimension
    
    @dimension.setter
    def dimension(self, nueva_dimension):
        if nueva_dimension < 1:
            raise ValueError("La nueva dimensión debe ser mayor o igual a 1")
        if nueva_dimension < self.__dimension:
            raise ValueError("No se puede reducir la dimensión de la matriz.")
        for i in range(self.__dimension):
            self.__mat[i] = self.__mat[i] + [self.__vinicial] * (nueva_dimension - self.__dimension)
        for i in range(self.__dimension, nueva_dimension):
            self.__mat.append([self.__vinicial] * nueva_dimension)
            self.__dimension = nueva_dimension
    
    def valor(self, fila, columna):
        if fila < 0 or fila >= self.__dimension or columna < 0 or columna >= self.__dimension:
            raise IndexError("Índice fuera de rango.")
        return self.__mat[fila][columna]
    
    def cambia_valor(self, fila, columna, nuevo_valor):
        if fila < 0 or fila >= self.__dimension or columna < 0 or columna >= self.__dimension:
            raise IndexError("Índice fuera de rango.")
        return self.__mat[fila][columna] = nuevo_valor


