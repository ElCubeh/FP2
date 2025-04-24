"""A continuación, te propongo un nuevo ejercicio con una clase LinkedList que:
    Inserción: En lugar de insertar al principio (insert_front), insertará nodos al final de la lista.

    Eliminación: En lugar de eliminar números pares (delete_even_numbers), eliminará nodos cuyos valores sean strings que contengan una vocal 
    (por ejemplo, "hello" contiene vocales, pero "xyz" no).

    Otros métodos: Mantendré un método para mostrar la lista (display) y añadiré un método diferente al count_strings, 
    por ejemplo, uno que calcule la suma de los valores numéricos en la lista.
"""

class LinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next_node = None
    def __init__(self):
        self.__first = None
    
    def insert_front(self, value):
        n_nodo = self.Node(value)
        if not self.__first:
            self.__first = self.__last = n_nodo
        else:
            self.__last.next_node = n_nodo
            self.__last = n_nodo
    
    def delete_nodes_with_vowels(self):
        vocales = set("aeiouAEIOU")

        def contains_vowel(s):
            return isinstance(s, str) and any(char in vocales for char in s)

        while self.__first and contains_vowel(self.__first.value):
            self.__first = self.__first.next_node

        current = self.__first
        while current and current.next_node:
            if contains_vowel(current.next_node.value):
                current.next_node = current.next_node.next_node
            else:
                current = current.next_node
    
    def mostrar(self):
        current = self.__first
        while current:
            print(current.value)
            current = current.next_node

    def sum_num_values(self):
        total = 0
        current = self.__first
        while current:
            if isinstance(current.value, (int, float)):
                total += current.value
            current = current.next_node
        return total
    

if __name__ == "__main__":
    lista = LinkedList()
    
    # Insertamos valores mixtos: algunos con vocales, algunos numéricos y otros sin vocales
    lista.insert_front("hello")
    lista.insert_front("xyz")
    lista.insert_front(42)
    lista.insert_front("aeiou")
    lista.insert_front(3.14)
    lista.insert_front("brrr")
    lista.insert_front(100)

    print("Lista original:")
    lista.mostrar()

    # Eliminamos nodos que contienen vocales
    lista.delete_nodes_with_vowels()

    print("\nLista después de eliminar nodos con vocales:")
    lista.mostrar()

    # Mostramos la suma de los valores numéricos
    suma = lista.sum_num_values()
    print("\nSuma de los valores numéricos:", suma)
