"""Módulo para ejecutar el ejercicio pedido."""

import random

from deletablesll import DeletableSLL

if __name__ == "__main__":
    my_slist = DeletableSLL()
    data = [random.randint(10, 100) for i in range(10)]

    # Se rellena una lista con valores aleatorios

    for e in data:
        my_slist.insert(e)

    # Se muestra la lista a medida que se vabn quitando elementos

    for e in data:
        print("----")
        for item in my_slist:
            print(item)

        my_slist.delete(e)
