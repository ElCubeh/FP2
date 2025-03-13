"""Módulo de prueba de la clase Stack y la excepción StackEmptyError."""

from stack import Stack
# Descomentar la siguiente línea tras definir la excepción StackEmptyError
from stackexceptions import StackEmptyError


if __name__ == "__main__":
    # Creamos una pila vacía
    my_stack = Stack()

    # Insertamos 10 elementos en my_stack
    for i in range(10):
        my_stack.push(i)
        print(my_stack.top)

    print("---")

    # Vaciamos my_stack y mostramos los elementos a medida que los quitamos

    while not my_stack.is_empty():
        print(my_stack.top)
        my_stack.pop()

    # Descomentar la línea de abajo para probar la excepción
    my_stack.pop()
