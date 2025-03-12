"""Module with the answer to the problem."""


def is_upper_triangular_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i):
            if not len(matrix[j]) == len(matrix[i]):
                raise BadMatrix("Matriz no cuadrada")
            if type(matrix[i][j]) is not int:
                try:
                    matrix[i][j] = int(matrix[i][j])
                except ValueError:
                    raise BadMatrix("Dato no convertirle a entero")
    for i in range(n):
        for j in range(i):
            if matrix[i][j] != 0:
                return False
    return True
# NO MODIFIQUE EL CODIGO DEBAJO DE ESTA LINEA


class BadMatrix(Exception):
    """Exception for BadMatrix."""

    pass
