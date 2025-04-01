"""Módulo para ejecutar el ejercicio pedido."""

import random

from linkedlist import LinkedList

if __name__ == "__main__":
    my_slist = LinkedList()
    data = [random.randint(10, 15) for i in range(10)]
    indexs = [0, 0, 1, 2, 1, 4, 3, 4, 6, 2]

    # Se inserta una secuencia de valores aleatorios en una lista

    for index, value in zip(indexs, data):
        my_slist.insert(index, value)

    # Se muestra el efecto al ir eliminando valores de la lista

    for e in data:
        print("----")
        for item in my_slist:
            print(item, sep="->")

        my_slist.remove(e)
        print("Se extrae:", e)
