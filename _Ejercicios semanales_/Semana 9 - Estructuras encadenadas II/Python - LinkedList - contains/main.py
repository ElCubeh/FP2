"""Módulo para ejecutar el ejercicio pedido."""

import random

from linkedlist import LinkedList

if __name__ == "__main__":
    my_list = LinkedList()
    data1 = [random.randint(10, 15) for i in range(10)]
    data2 = [random.randint(10, 20) for i in range(10)]
    indexs = [0, 0, 1, 2, 1, 4, 3, 4, 6, 2]

    # Se inserta una secuencia de valores aleatorios en una lista

    for index, value in zip(indexs, data1):
        my_list.insert(index, value)

    # Se buscan elementos aleatorios en la lista

    print(data1)

    for e in data2:
        print(e, my_list.contains(e))
