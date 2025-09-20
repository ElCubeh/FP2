class Photo:
    def __init__(self, filename, date_taken, size_mb):
        self.filename = filename
        self.date_taken = date_taken
        self.size_mb = size_mb

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class AlbumBase:
    def __init__(self):
        self.first = None
        self._size = 0

    def add_photo(self, photo):
        new_node = Node(photo)
        if self.first is None: self.first = new_node
        else:
            curr = self.first
            while curr.next:
                curr = curr.next
            curr.next = new_node
        self._size += 1

    def get_size(self):
        return self._size

class Album(AlbumBase):
    _total_photos_stored = 0
    
    def add_photo(self, photo):
        super().add_photo(photo)
        Album._total_photos_stored += 1

    def delete_photo(self, filename):
        prev, curr = None, self.first
        while curr:
            if curr.value.filename == filename:
                if prev is None: self.first = curr.next
                else: prev.next = curr.next
                self._size -= 1
                Album._total_photos_stored -= 1
                return curr.value
            prev, curr = curr, curr.next
        return None

    @property
    def total_size_mb(self):
        total = 0.0
        curr = self.first
        while curr:
            total += curr.value.size_mb
            curr = curr.next
        return total

    def find_photos_by_date(self, date):
        photos = []
        curr = self.first
        while curr:
            if curr.value.date_taken == date:
                photos.append(curr.value)
            curr = curr.next
        return photos

    @classmethod
    def get_total_photos_stored(cls):
        return cls._total_photos_stored