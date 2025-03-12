"""Module with the answer to the problem."""


class Rectangulo:
    def __init__(self, p1, p2):
        if p1.x >= p2.x or p1.y >= p2.y:
            raise BadRectangle("Rectángulo erróneo")
        self.__ini = p1
        self.__fin = p2

    @property
    def ini(self):
        return self.__ini

    @ini.setter
    def ini(self, valor):
        if valor.x >= self.__fin.x or valor.y >= self.__fin.y:
            raise BadRectangle("Rectángulo erróneo")
        self.__ini = valor

    @property
    def fin(self):
        return self.__fin

    @fin.setter
    def fin(self, valor):
        if valor.x <= self.__ini.x or valor.y <= self.__ini.y:
            raise BadRectangle("Rectángulo erróneo")
        self.__fin = valor

    def esta_contenido(self, p):
        return self.__ini.x <= p.x <= self.__fin.x and \
                self.__ini.y <= p.y <= self.__fin.y

    def __str__(self):
        return f"<{self.__ini.get_str()}, {self.__fin.get_str()}>"

# NO MODIFIQUE EL CODIGO DEBAJO DE ESTA LINEA


class Punto:
    """Punto con dos propiedades x e y."""

    def __init__(self, x, y):
        """Inicializa punto."""
        self.x = x
        self.y = y

    def get_str(self):
        """Devuelve punto como str."""
        return f"({self.x}, {self.y})"


class BadRectangle(Exception):
    """Exception for BadRectangle."""

    pass
