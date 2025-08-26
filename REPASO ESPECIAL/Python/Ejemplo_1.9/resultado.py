# Clases base (Contact, Node, ContactListBase)

class ContactList(ContactListBase):
    _total_contacts = 0
    
    def add_contact(self, contact):
        super().add_contact(contact)
        ContactList._total_contacts += 1

    def remove_contact_by_name(self, name):
        prev = None
        curr = self.first
        while curr:
            if curr.value.name == name:
                if prev is None: # Es el primer nodo
                    self.first = curr.next
                else:
                    prev.next = curr.next
                self._size -= 1
                ContactList._total_contacts -= 1
                return curr.value
            prev = curr
            curr = curr.next
        return None

    @property
    def favorite_count(self):
        count = 0
        curr = self.first
        while curr:
            if curr.value.is_favorite:
                count += 1
            curr = curr.next
        return count

    def get_favorites(self):
        favorites = []
        curr = self.first
        while curr:
            if curr.value.is_favorite:
                favorites.append(curr.value)
            curr = curr.next
        return favorites

    @classmethod
    def get_total_contacts(cls):
        return cls._total_contacts