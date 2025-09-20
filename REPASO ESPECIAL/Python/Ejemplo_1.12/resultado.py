class Dish:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class OrderBase:
    def __init__(self):
        self.first = None
        self._size = 0
    
    def add_dish(self, dish):
        new_node = Node(dish)
        if self.first is None: self.first = new_node
        else:
            curr = self.first
            while curr.next:
                curr = curr.next
            curr.next = new_node
        self._size += 1
    
    def get_size(self):
        return self._size

class Order(OrderBase):
    total_revenue = 0.0

    def __init__(self):
        super().__init__()

    def remove_dish_by_name(self, name):
        prev, curr = None, self.first
        while curr:
            if curr.value.name == name:
                if prev is None: self.first = curr.next
                else: prev.next = curr.next
                self._size -= 1
                return curr.value
            prev, curr = curr, curr.next
        return None

    @property
    def subtotal(self):
        total = 0.0
        curr = self.first
        while curr:
            total += curr.value.price
            curr = curr.next
        return total

    def get_dishes_by_category(self, category):
        dishes = []
        curr = self.first
        while curr:
            if curr.value.category == category:
                dishes.append(curr.value)
            curr = curr.next
        return dishes
    
    def close_order(self):
        Order.total_revenue += self.subtotal
        self.first = None
        self._size = 0