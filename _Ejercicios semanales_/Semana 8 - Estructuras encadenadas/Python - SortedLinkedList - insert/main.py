"""Módulo para ejecutar el método pedido en el ejercicio."""

import random
from sortedlinkedlist import SortedLinkedList


if __name__ == "__main__":
    my_slist = SortedLinkedList()
    values = []

    # Se llama al metodo insert insertando una secuencia de valores aleatorios.

    for i in range(10):
        num = random.randint(10, 100)
        my_slist.insert(num)
        values.append(num)

    # Se muestra el resultado de la secuencia de inserciones.

    print("Se han insertado los siguientes valores", values)
    print("y la lista contiene:", end="")

    for item in my_slist:
        print(item, end="->")
