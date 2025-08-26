# Clases base (Item, Node, ShoppingCartBase)

class ShoppingCart(ShoppingCartBase):
    _all_carts_value = 0

    def __init__(self):
        super().__init__()

    def add_item(self, item): # Sobrescribimos para actualizar el valor total
        super().add_item(item)
        ShoppingCart._all_carts_value += item.unit_price * item.quantity

    def remove_item(self, index, quantity_to_remove):
        if index < 0 or index >= self.get_size() or quantity_to_remove <= 0:
            return None
        
        prev = None
        curr = self.first
        count = 0
        while count < index:
            prev = curr
            curr = curr.next
            count += 1
        
        item_in_cart = curr.value
        removed_value = item_in_cart.unit_price * quantity_to_remove
        
        if quantity_to_remove >= item_in_cart.quantity:
            ShoppingCart._all_carts_value -= item_in_cart.unit_price * item_in_cart.quantity
            if prev is None:
                self.first = curr.next
            else:
                prev.next = curr.next
            self._size -= 1
            return item_in_cart
        else:
            item_in_cart.quantity -= quantity_to_remove
            ShoppingCart._all_carts_value -= removed_value
            return item_in_cart

    @property
    def subtotal(self):
        total = 0
        curr = self.first
        while curr:
            total += curr.value.unit_price * curr.value.quantity
            curr = curr.next
        return total

    @property
    def total_items(self):
        total = 0
        curr = self.first
        while curr:
            total += curr.value.quantity
            curr = curr.next
        return total

    @classmethod
    def get_all_carts_value(cls):
        # Esta es una implementación simplificada. Una real requeriría recalcular.
        # Por simplicidad, asumimos que el valor se gestiona en add/remove.
        return cls._all_carts_value