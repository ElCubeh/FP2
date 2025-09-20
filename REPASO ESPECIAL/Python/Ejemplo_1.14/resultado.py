class Property:
    def __init__(self, address, market_value, annual_rental_income):
        self.address = address
        self.market_value = market_value
        self.annual_rental_income = annual_rental_income

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class PortfolioBase:
    def __init__(self):
        self.first = None
        self._size = 0

    def acquire_property(self, prop):
        new_node = Node(prop)
        if self.first is None: self.first = new_node
        else:
            curr = self.first
            while curr.next:
                curr = curr.next
            curr.next = new_node
        self._size += 1

    def get_size(self):
        return self._size

class Portfolio(PortfolioBase):
    total_properties_managed = 0

    def acquire_property(self, prop):
        super().acquire_property(prop)
        Portfolio.total_properties_managed += 1

    def sell_property(self, address):
        prev, curr = None, self.first
        while curr:
            if curr.value.address == address:
                if prev is None: self.first = curr.next
                else: prev.next = curr.next
                self._size -= 1
                Portfolio.total_properties_managed -= 1
                return curr.value
            prev, curr = curr, curr.next
        return None

    @property
    def portfolio_value(self):
        total = 0.0
        curr = self.first
        while curr:
            total += curr.value.market_value
            curr = curr.next
        return total

    @property
    def annual_yield(self):
        total_income = 0.0
        curr = self.first
        while curr:
            total_income += curr.value.annual_rental_income
            curr = curr.next
        
        value = self.portfolio_value
        if value == 0:
            return 0
        return total_income / value