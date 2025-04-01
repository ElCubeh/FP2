"""Módulo para ejecutar el ejercicio pedido."""

import random
from doublelinkedlist import DoubleLinkedList


if __name__ == "__main__":
    my_list = DoubleLinkedList()
    data = [random.randint(10, 15) for i in range(10)]

    # Insertamos una secue3ncia de valores aleatorios en una lista

    for value in data:
        my_list.insert_as_first(value)

    # Mostramos los valores que hay en la lista

    for item in my_list:
        print(item)
