"""Ejemplo de uso de la clase requerida."""

from solution import Matriz

ms = [(3, 3, 5), (5, 7, -1), (1, 2, 7), ]
for n, m, v in ms:
    print("Datos", n, m, v)
    mat = Matriz(n, m, v)
    print("dimensiones() =>", mat.dimensiones())
    print("valor(1, 1) =>", mat.valor(1, 1))
    mat.cambia_valor(1, 1, -3)
    print("cambio_valor => valor(1, 1) =>", mat.valor(1, 1))
    print("get_str() =>", mat.get_str())
    print()
