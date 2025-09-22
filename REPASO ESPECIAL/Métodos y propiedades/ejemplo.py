# -----------------------------------------------------------------------------
# 1. CLASES BÁSICAS (LOS BLOQUES DE CONSTRUCCIÓN)
# -----------------------------------------------------------------------------

class Item:
    """Un objeto de ejemplo que almacenaremos en nuestra lista."""
    def __init__(self, name, value, category):
        self.name = name
        self.value = value
        self.category = category

    def __str__(self):
        return f"({self.name}, {self.value}, {self.category})"

class Node:
    """Un nodo de la lista enlazada."""
    def __init__(self, value):
        self.value = value
        self.next = None

# -----------------------------------------------------------------------------
# 2. CLASE CONTENEDORA (IMPLEMENTA LOS 5 PATRONES)
# -----------------------------------------------------------------------------

class Container:
    """Una clase que gestiona una lista enlazada de objetos 'Item'."""
    
    def __init__(self):
        self.first = None
        self._size = 0

    def get_size(self):
        return self._size

    def __str__(self):
        if self.first is None:
            return "Container: []"
        items = []
        curr = self.first
        while curr:
            items.append(str(curr.value))
            curr = curr.next
        return "Container: [" + " -> ".join(items) + "]"

    def add_item(self, item):
        new_node = Node(item)
        if self.first is None:
            self.first = new_node
        else:
            curr = self.first
            while curr.next:
                curr = curr.next
            curr.next = new_node
        self._size += 1

    # --- PATRÓN 1: Eliminar un Nodo por Índice ---
    def remove_item_at_index(self, index):
        if not (0 <= index < self._size):
            return None

        item_to_remove = None
        if index == 0:
            item_to_remove = self.first.value
            self.first = self.first.next
        else:
            prev = self.first
            for _ in range(index - 1):
                prev = prev.next
            item_to_remove = prev.next.value
            prev.next = prev.next.next

        self._size -= 1
        return item_to_remove

    # --- PATRÓN 2: Buscar y Eliminar un Nodo por Valor ---
    def remove_item_by_name(self, name):
        prev, curr = None, self.first
        while curr:
            if curr.value.name == name:
                if prev is None:
                    self.first = curr.next
                else:
                    prev.next = curr.next
                self._size -= 1
                return curr.value
            prev, curr = curr, curr.next
        return None

    # --- PATRÓN 3: Buscar y Actualizar un Nodo ---
    def update_item_value(self, name, new_value):
        curr = self.first
        while curr:
            if curr.value.name == name:
                curr.value.value = new_value
                return True
            curr = curr.next
        return False

    # --- PATRÓN 4: Calcular un Valor Agregado (Propiedad) ---
    @property
    def total_value(self):
        total = 0
        curr = self.first
        while curr:
            total += curr.value.value
            curr = curr.next
        return total

    # --- PATRÓN 5: Filtrar la Lista ---
    def filter_by_category(self, category):
        results = []
        curr = self.first
        while curr:
            if curr.value.category == category:
                results.append(curr.value)
            curr = curr.next
        return results

# -----------------------------------------------------------------------------
# 3. BLOQUE DE EJECUCIÓN (PARA PROBAR EL CÓDIGO)
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    
    # Creamos una instancia de nuestro contenedor
    my_container = Container()
    print("Estado inicial:")
    print(my_container)
    print("-" * 30)

    # Añadimos algunos objetos
    my_container.add_item(Item("Manzana", 10, "Fruta"))
    my_container.add_item(Item("Plátano", 20, "Fruta"))
    my_container.add_item(Item("Lechuga", 5, "Verdura"))
    my_container.add_item(Item("Naranja", 15, "Fruta"))
    print("Después de añadir 4 items:")
    print(my_container)
    print("-" * 30)
    
    # 1. Probamos "Eliminar por Índice" (eliminamos 'Lechuga' en índice 2)
    print("1. Probando 'remove_item_at_index(2)'...")
    removed_item = my_container.remove_item_at_index(2)
    print(f"   Item eliminado: {removed_item}")
    print(f"   Estado actual: {my_container}")
    print("-" * 30)

    # 2. Probamos "Eliminar por Valor" (eliminamos 'Naranja')
    print("2. Probando 'remove_item_by_name(\"Naranja\")'...")
    removed_item = my_container.remove_item_by_name("Naranja")
    print(f"   Item eliminado: {removed_item}")
    print(f"   Estado actual: {my_container}")
    print("-" * 30)

    # 3. Probamos "Actualizar un Nodo" (cambiamos el valor de 'Manzana' a 99)
    print("3. Probando 'update_item_value(\"Manzana\", 99)'...")
    success = my_container.update_item_value("Manzana", 99)
    print(f"   Operación exitosa: {success}")
    print(f"   Estado actual: {my_container}")
    print("-" * 30)

    # 4. Probamos la "Propiedad Calculada"
    print("4. Probando la propiedad 'total_value'...")
    total = my_container.total_value
    print(f"   Suma total de valores: {total}") # Debería ser 99 + 20 = 119
    print("-" * 30)
    
    # 5. Probamos "Filtrar la Lista"
    my_container.add_item(Item("Pera", 25, "Fruta"))
    print("Añadido 'Pera' para el filtro.")
    print(f"Estado actual: {my_container}")
    print("5. Probando 'filter_by_category(\"Fruta\")'...")
    frutas = my_container.filter_by_category("Fruta")
    print("   Frutas encontradas:")
    for fruta in frutas:
        print(f"   - {fruta}")
    print("-" * 30)