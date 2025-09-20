class Entry:
    def __init__(self, title, text, date):
        self.title = title
        self.text = text
        self.date = date

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class JournalBase:
    def __init__(self):
        self.first = None
        self._size = 0
    
    def add_entry(self, entry):
        new_node = Node(entry)
        if self.first is None: self.first = new_node
        else:
            curr = self.first
            while curr.next:
                curr = curr.next
            curr.next = new_node
        self._size += 1

    def get_size(self):
        return self._size

class Journal(JournalBase):
    _total_word_count = 0
    
    def add_entry(self, entry):
        super().add_entry(entry)
        Journal._total_word_count += len(entry.text.split())

    def find_entry_by_title(self, title):
        curr = self.first
        while curr:
            if curr.value.title == title:
                return curr.value
            curr = curr.next
        return None

    @property
    def word_count(self):
        count = 0
        curr = self.first
        while curr:
            count += len(curr.value.text.split())
            curr = curr.next
        return count

    def get_entries_for_date(self, date):
        entries = []
        curr = self.first
        while curr:
            if curr.value.date == date:
                entries.append(curr.value)
            curr = curr.next
        return entries

    @classmethod
    def get_total_journals_word_count(cls):
        return cls._total_word_count