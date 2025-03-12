"""Ejemplo de uso de la clase requerida."""

from solution import Matriz

# Lista de casos de prueba (dimensión, valor_inicial)
casos = [(3, 2), (2, 4), (1, 6), (0, 8)]
for n, valor_inicial in casos:
    try:
        print(f"Matriz", n, valor_inicial)
        mat = Matriz(n, valor_inicial)
        print(mat)
        print("dimension:", mat.dimension)
        print("valor(1, 1): ", end="")
        print(mat.valor(1, 1))
        print("cambia_valor(1, 1, -3)")
        mat.cambia_valor(1, 1, -3)
        print("dimension += 2")
        mat.dimension += 2
        print(mat)
        print("dimension:", mat.dimension)
        print()
    except Exception as err:
        print("Error en matriz", type(err))
        print()