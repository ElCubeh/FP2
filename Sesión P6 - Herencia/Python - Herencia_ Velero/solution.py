# Escriba aquí el código requerido.
from clases import Barco
from functools import total_ordering


@total_ordering
class Velero(Barco):
    def __init__(self, manga, eslora, palos):
        super().__init__(manga, eslora)
        self.palos = palos

    @property
    def palos(self):
        return self.__palos

    @palos.setter
    def palos(self, palos):
        self.__palos = palos

    def __lt__(self, other):
        if isinstance(other, Velero):
            return (self.manga * self.eslora) < (other.manga * other.eslora)
        return False

    def __eq__(self, other):
        if isinstance(other, Velero):
            return (self.manga * self.eslora) == (other.manga * other.eslora)
        return NotImplemented


if __name__ == "__main__":
    a = Velero(6, 10, 1)
    b = Velero(3, 20, 2)
    print(a >= b, a != b)
    pass
