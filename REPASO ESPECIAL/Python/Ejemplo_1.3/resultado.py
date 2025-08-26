# Clases base (Book, Node, LibraryBase)

class Library(LibraryBase):
    _total_books_borrowed = 0

    def __init__(self):
        super().__init__()
        self._borrowed_pages = 0

    def checkout_book(self, index):
        if index < 0 or index >= self.get_size():
            return None
        
        book_to_checkout = None
        if index == 0:
            book_to_checkout = self.first.value
            self.first = self.first.next
        else:
            prev = None
            curr = self.first
            count = 0
            while count < index:
                prev = curr
                curr = curr.next
                count += 1
            book_to_checkout = curr.value
            prev.next = curr.next
        
        self._size -= 1
        if book_to_checkout:
            self._borrowed_pages += book_to_checkout.pages
            Library._total_books_borrowed += 1

        return book_to_checkout

    @property
    def total_pages_available(self):
        total = 0
        curr = self.first
        while curr:
            total += curr.value.pages
            curr = curr.next
        return total

    @property
    def borrowed_pages(self):
        return self._borrowed_pages
    
    @borrowed_pages.setter
    def borrowed_pages(self, value):
        if value == 0:
            self._borrowed_pages = 0

    @classmethod
    def get_total_books_borrowed(cls):
        return cls._total_books_borrowed