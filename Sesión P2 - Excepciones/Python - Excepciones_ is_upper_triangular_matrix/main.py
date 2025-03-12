"""Ejemplo de uso de la función requerida."""

from solution import BadMatrix
from solution import is_upper_triangular_matrix
# triangular superior
m1 = [[1, -1, 2, 3], [0, 4, 0, 0], [0, 0, -2, 0], [0, 0, 0, -1]]
# no triangular superior
m2 = [[1, 0, 0, 0], [0, 4, 0, 0], [0, 0, -2, 0], [0, 0, 999, -1]]
# no cuadrada
m3 = [[1, 0, 0, 0], [0, 4, 0, 9], [0, 0, -2, 0], [0, 0, 0, -1], [0]]
# no cuadrada (convertible)
m4 = [[1, 0, 0, 0], [0, 4, 0, 0], [0, 0, "-2", 0], [0, 0, 0]]
# no cuadrada (no convertible)
m5 = [[2, "x", 0], [0, 44, 1], [-0, 341]]
# triangular superior (convertible)
m6 = [["1", 0, 0], ["0", "44", 1], [0, "-0", "341"]]
# no convertible (str)
m7 = [[4, 0, 0], [0, 44, 1], [0, -0, "hola"]]
# no convertible (list)
m8 = [[[], 0, 0], [0, 44, 1], [0, -0, 1]]
for m in [m1, m2, m3, m4, m5, m6, m7, m8]:
    try:
        print(is_upper_triangular_matrix(m))
    except BadMatrix as err:
        print("Error en matriz", err)
        print(m)
    finally:
        print()
