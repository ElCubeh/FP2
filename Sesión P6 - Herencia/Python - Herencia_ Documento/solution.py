# Escriba aquí el código requerido.
from clases import Documento
from functools import total_ordering


@total_ordering
class Libro(Documento):
    def __init__(self, titulo, autor, isbn):
        super().__init__(titulo, autor)
        self.isbn = isbn

    def __isbn_getter(self):
        return self.__isbn

    def __isbn_setter(self, isbn):
        self.__isbn = isbn

    isbn = property(__isbn_getter, __isbn_setter)

    def _val(self):
        return self.título, self.autor

    def __eq__(self, other):
        if isinstance(other, Libro):
            return self._val() == other._val()
        return False

    def __lt__(self, other):
        if isinstance(other, Libro):
            return self._val() < other._val()
        return NotImplemented


if __name__ == "__main__":
    """
    a = Libro(
        "El lenguaje de programación Java", "Arnold, Ken", "84-7829-045-1")
    b = Libro(
        "El gran Documento de Python", "Buttu, Marco", "9788426722904")
    print(a >= b, a != b)
    """
    pass
