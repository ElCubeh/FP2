# Clases base (Product, Node, InventoryBase - similares a las del Examen 1)

class Inventory(InventoryBase):
    total_revenue = 0.0 # Atributo de clase

    def __init__(self):
        super().__init__()

    def sell_product(self, name, amount):
        if amount <= 0:
            return 0
            
        prev = None
        curr = self.first
        while curr:
            if curr.value.name == name:
                product = curr.value
                if product.quantity >= amount:
                    sale_value = product.price * amount
                    product.quantity -= amount
                    Inventory.total_revenue += sale_value
                    
                    if product.quantity == 0:
                        if prev is None:
                            self.first = curr.next
                        else:
                            prev.next = curr.next
                        self._size -= 1
                    return sale_value
                else:
                    return 0 # No hay suficiente stock
            prev = curr
            curr = curr.next
        return 0 # Producto no encontrado

    @property
    def inventory_value(self):
        total_value = 0
        curr = self.first
        while curr:
            total_value += curr.value.price * curr.value.quantity
            curr = curr.next
        return total_value

    def get_low_stock_products(self, threshold):
        low_stock = []
        curr = self.first
        while curr:
            if curr.value.quantity <= threshold:
                low_stock.append(curr.value)
            curr = curr.next
        return low_stock