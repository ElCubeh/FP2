# --- CLASES BASE (Proporcionadas por el examen) ---
class Song:
    """Representa una canción con título, artista y duración en segundos."""
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def __str__(self):
        return f"{self.title} by {self.artist} ({self.duration}s)"

class Node:
    """Un nodo en la lista enlazada, contiene una canción."""
    def __init__(self, song):
        self.value = song
        self.next = None

class PlaylistBase:
    """Clase base para la gestión de la lista enlazada de canciones."""
    def __init__(self):
        self.first = None
        self._size = 0

    def add_song(self, song):
        new_node = Node(song)
        if self.first is None:
            self.first = new_node
        else:
            current = self.first
            while current.next:
                current = current.next
            current.next = new_node
        self._size += 1

    def get_song(self, index):
        if index < 0 or index >= self._size:
            return None
        current = self.first
        for _ in range(index):
            current = current.next
        return current.value

    def get_size(self):
        return self._size

    def __str__(self):
        if self.first is None:
            return "Playlist vacía"
        items = []
        current = self.first
        while current:
            items.append(str(current.value))
            current = current.next
        return " -> ".join(items)

# --- CLASE A DESARROLLAR (Nuestra Solución) ---
class Playlist(PlaylistBase):
    """Gestiona una playlist con funcionalidades avanzadas."""
    
    # Atributo de CLASE: compartido por todas las instancias de Playlist
    _total_played_time = 0

    def __init__(self):
        super().__init__()
        # Atributo de INSTANCIA: único para cada objeto Playlist
        self._time_spent = 0

    @property
    def total_duration(self):
        """(Solo lectura) Calcula la duración total de las canciones restantes."""
        total = 0
        current_node = self.first
        while current_node:
            total += current_node.value.duration
            current_node = current_node.next
        return total

    def play_song(self, index):
        """Elimina una canción, la devuelve y actualiza los contadores de tiempo."""
        if index < 0 or index >= self.get_size():
            return None

        song_to_play = None

        if index == 0:
            song_to_play = self.first.value
            self.first = self.first.next
        else:
            previous_node = None
            current_node = self.first
            count = 0
            while count < index:
                previous_node = current_node
                current_node = current_node.next
                count += 1
            song_to_play = current_node.value
            previous_node.next = current_node.next
        
        self._size -= 1 # No olvidar decrementar el tamaño

        if song_to_play:
            self._time_spent += song_to_play.duration
            Playlist._total_played_time += song_to_play.duration
        
        return song_to_play

    @classmethod
    def get_total_played_time(cls):
        """Devuelve el tiempo total reproducido en TODAS las playlists."""
        return cls._total_played_time

    def get_playlist_as_list(self):
        """Devuelve una lista de Python con las canciones de la playlist."""
        python_list = []
        current_node = self.first
        while current_node:
            python_list.append(current_node.value)
            current_node = current_node.next
        return python_list