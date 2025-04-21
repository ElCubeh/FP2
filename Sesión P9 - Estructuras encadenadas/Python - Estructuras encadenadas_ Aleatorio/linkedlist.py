"""Definición de la clase LinkedList para construir listas enlazadas."""

class LinkedList:
    """Lista simplemente encadenada."""

    class Node:
        """Nodos de la lista."""

        def __init__(self, value, next_node = None):
            """Inicializa el valor y el enlace al siguiente nodo."""

            self.value = value
            self.next_node = next_node
            
    def __init__(self):
        """Inicializa el principio y final a None, y el tamaño a 0."""
        
        self.__first = None
        self.__last  = None
        self.__len = 0
        
    def __len__(self):
        """Devuelve el tamaño de la lista."""
        
        return self.__len
    
    # NO MODIFIQUE ESTA LÍNEA ni el código que está por encima
    # (de lo contrario, no serán fiables los tests automáticos).
    # Escriba su solución a partir de la siguiente línea.
    def append(self, value):
        new_node = self.Node(value)
        if not self.__first:
            self.__first = new_node
            self.__last = new_node
        else:
            self.__last.next_node = new_node
            self.__last = new_node
        self.__len += 1

    def filtrar(self):
        nueva_lista = LinkedList()
        current = self.__first
        while current:
            if isinstance(current.value, int):
                nueva_lista.append(current.value)
            current = current.next_node
        return nueva_lista
    
# Código a ejecutar si se pulsa 🚀
if __name__ == "__main__":
    lista_enlazada = LinkedList()
    # Añada más código de prueba si lo desea
