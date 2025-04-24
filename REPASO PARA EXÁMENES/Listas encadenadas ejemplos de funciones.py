class LinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next_node = None
    
    def __init__(self):
        self.__first = None
        self.__last = None
    
    def append(self, value): #Añadir al final de la lista
        new_node = self.Node(value)
        if not self.__first:
            self.__first = self.__last = new_node
        else:
            self.__last.next_node = new_node
            self.__last = new_node

    def agragar_adelante(self, value): #Añadir al principio de la lista
        new_node = self.Node(value)
        if not self.__first:
            self.__first = self.__last = new_node
        else:
            new_node.next_node = self.__first
            self.__first = new_node

    def insertar_intermedia(self, valor):
        nuevo = Nodo(valor)
        actual = self.cabeza
        while actual:
            if isinstance(actual.valor, int):
                # Insertar después del nodo actual
                nuevo.siguiente = actual. siguiente
                actual.siguiente = nuevo
                return
            actual = actual.siguiente
        # Si no se encontró un entero, insertar al final
        self.insertar_final(valor)
    
    def mostrar(self):  #Enseñar en pantalla
        current = self.__first
        while current:
            print(current.value)
            current = current.next_node

    def eliminar(self, value):  #Método eliminar
        while self.__first and (self.__first.value == value):   #Eliminar Principio
            self.__first = self.__first.next_node

        """while self.__first and (isinstance(self.__first.value, str)):
            self.__first = self.__first.next_node"""            #Ejemplo de como eliminar los valores str de una lista
        """while self.__first and (isinstance(self.__first.value, int)):
            self.__first = self.__first.next_node"""            #Ejemplo de como eliminar los valores entero de una lista
        """while self.__first and (isinstance(self.__first.value, bool)):
            self.__first = self.__first.next_node"""            #Ejemplo de como eliminar los valores boleanos de una lista
        """while self.__first and (isinstance(self.__first.value, float)):
            self.__first = self.__first.next_node"""            #Ejemplo de como eliminar los valores de tipo float de una lista


        current = self.__first                                  #Eliminar el nodo requerido, ya sea entremedia y o al final
        while current != None and current.next_node != None:
            if current.next_node.value == value:
                current.next_node = current.next_node.next_node
            else:
                current = current.next_node

    def actualizar(self, posicion, value): #Actualizar o sustituir valores
        current = self.__first
        indice = 0
        while indice < posicion:
            current = current.next_node
            indice += 1
        current.value = value

    def count_strings(self):    #Contar los valores de tipo str
        count = 0
        current = self.__first
        while current:
            if isinstance(current.value, str):
                count += 1
            current = current.next_node
        return count
    
    def count_int(self):    #Contar los valores de tipo int
        count = 0
        current = self.__first
        while current:
            if isinstance(current.value, int):
                count += 1
            current = current.next_node

    def count_float(self):  #Contar los valores de tipo float
        count = 0
        current = self.__first
        while current:
            if isinstance(current.value, float):
                count += 1
            current = current.next_node

    def count_bool(self):  #Contar los valores de tipo bool
        count = 0
        current = self.__first
        while current:
            if isinstance(current.value, bool):
                count += 1
            current = current.next_node

    def contar(self):  #Contar los valores sin usar el len
        count = 0
        current = self.__first
        while current and current.next_node:
                count += 1
                current = current.next_node
        return count
    
    def __len__(self):      #Muestra la longitud de la lista
        return self.__len
    
    def ordenar(self):
        # comprobamos que la lista está vacía o que solo tiene un nodo
        if not self._first or not self._first.next_node:
            return
        prev = None
        current = self.first
        #aunque invirtamos la lista, , el nodo que era último, seguirá siendo el ultimo ya que no tiene next_node
        old_last = self.last
        #si hay más nodos que examinar, recorremos la lista
        while current:
            #el nodo siguiente al nodo acutal
            next_node = current.next_node
            #cambiamos la dirección del enlace, haciendo que el nido actual apunte hacia atras en vez de hacia adelante.
            current.next_node = prev
            #actualizar prev para que apunte a current. Asi puede ser usado como el nodo anterior en la siguiente iteracion
            prev = current
            #ahora current  avanza al siguiente nodo.
            current = next_node
        #apunta al ultimo nodo procesado, que es el ultimo en el nodo original, sin embargo, al invertir la lista sería el primero.
        self.first = prev
        #en la lista invertida, ese nodo sigue siendo el último porque no tiene un next_node.
        self.last = old_last

    def delete(self, value):   #El método eliminará todos los nodos que tengan un valor igual al pasado como parámetro. 
        if self._SortedLinkedList__first is None:  # Lista vacía
            return

        # Eliminar todas las ocurrencias al principio de la lista
        while self.__first is not None and self.__first.value == value:
            self.__first = self.__first.next_node
            self.__len -= 1

        if self.__first is None:
            return

        # Eliminar ocurrencias en el medio o final de la lista
        prev = self.__first
        current = self.__first.next_node

        while current is not None and current.value <= value:
            if current.value == value:
                prev.next_node = current.next_node
                self.__len -= 1
                current = current.next_node
            else:
                prev = current
                current = current.next_node


lista = LinkedList()
lista.append(1)
lista.append(2)
lista.append(1)
lista.append(3)
lista.append(1)
lista.agragar_adelante("Hola soy el primero")
lista.eliminar(1)
lista.mostrar()