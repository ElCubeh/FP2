class Guest:
    def __init__(self, name, rsvp_status="pendiente", plus_ones=0):
        self.name = name
        self.rsvp_status = rsvp_status
        self.plus_ones = plus_ones

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class EventBase:
    def __init__(self):
        self.first = None
        self._size = 0

    def add_guest(self, guest):
        new_node = Node(guest)
        if self.first is None: self.first = new_node
        else:
            curr = self.first
            while curr.next:
                curr = curr.next
            curr.next = new_node
        self._size += 1

    def get_size(self):
        return self._size

class Event(EventBase):
    _total_confirmed = 0

    def __init__(self):
        super().__init__()

    def update_rsvp_status(self, name, new_status):
        initial_attendees = self.attendee_count
        curr = self.first
        while curr:
            if curr.value.name == name:
                curr.value.rsvp_status = new_status
                Event._total_confirmed += (self.attendee_count - initial_attendees)
                return True
            curr = curr.next
        return False

    @property
    def attendee_count(self):
        count = 0
        curr = self.first
        while curr:
            if curr.value.rsvp_status == "asistirá":
                count += 1 + curr.value.plus_ones
            curr = curr.next
        return count

    def get_pending_guests(self):
        pending = []
        curr = self.first
        while curr:
            if curr.value.rsvp_status == "pendiente":
                pending.append(curr.value.name)
            curr = curr.next
        return pending

    @classmethod
    def get_total_confirmed_attendees(cls):
        return cls._total_confirmed