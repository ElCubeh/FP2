# Clases base (Ticket, Node, TicketQueueBase)

class TicketQueue(TicketQueueBase):
    _total_resolved_tickets = 0

    def __init__(self):
        super().__init__()
        self._resolved_count = 0

    def resolve_ticket(self, index):
        ticket = self.remove_item_at_index(index) # Asumiendo un método auxiliar
        if ticket:
            self._resolved_count += 1
            TicketQueue._total_resolved_tickets += 1
        return ticket
    
    # Método auxiliar para no repetir código de eliminación
    def remove_item_at_index(self, index):
        if index < 0 or index >= self.get_size():
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

    @property
    def pending_tickets(self):
        return self.get_size()

    def get_highest_priority_ticket(self):
        if not self.first:
            return None
        
        highest_priority_ticket = self.first.value
        curr = self.first.next
        while curr:
            if curr.value.priority > highest_priority_ticket.priority:
                highest_priority_ticket = curr.value
            curr = curr.next
        return highest_priority_ticket

    @classmethod
    def get_total_resolved_tickets(cls):
        return cls._total_resolved_tickets