"""Módulo para hacer puebas con la clase Rectangle."""

from rectangle import Rectangle

r1 = Rectangle(1.0, 2.0)
print("Original:\n\tlength: {}\n\twidth: {}".format(r1.length, r1.width))

r2 = r1 ** 0
print("Nuevo:\n\tlength: {}\n\twidth: {}".format(r2.length, r2.width))
