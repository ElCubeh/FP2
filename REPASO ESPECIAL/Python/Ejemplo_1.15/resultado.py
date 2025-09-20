class Vehicle:
    def __init__(self, license_plate, model, mileage):
        self.license_plate = license_plate
        self.model = model
        self.mileage = mileage

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class FleetBase:
    def __init__(self):
        self.first = None
        self._size = 0

    def add_vehicle(self, vehicle):
        new_node = Node(vehicle)
        if self.first is None: self.first = new_node
        else:
            curr = self.first
            while curr.next:
                curr = curr.next
            curr.next = new_node
        self._size += 1

    def get_size(self):
        return self._size

class Fleet(FleetBase):
    _total_retired_mileage = 0

    def __init__(self):
        super().__init__()

    def retire_vehicle(self, license_plate):
        prev, curr = None, self.first
        while curr:
            if curr.value.license_plate == license_plate:
                if prev is None: self.first = curr.next
                else: prev.next = curr.next
                self._size -= 1
                Fleet._total_retired_mileage += curr.value.mileage
                return curr.value
            prev, curr = curr, curr.next
        return None

    def update_mileage(self, license_plate, new_mileage):
        curr = self.first
        while curr:
            if curr.value.license_plate == license_plate:
                curr.value.mileage = new_mileage
                return True
            curr = curr.next
        return False

    @property
    def average_mileage(self):
        if self.get_size() == 0:
            return 0
        total_mileage = 0
        curr = self.first
        while curr:
            total_mileage += curr.value.mileage
            curr = curr.next
        return total_mileage / self.get_size()

    @classmethod
    def get_total_retired_mileage(cls):
        return cls._total_retired_mileage