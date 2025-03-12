"""Module with the answer to the problem."""


class Rectangulo():

    def __init__(self, pto_inf_izq, pto_sup_der):
        """Un rectángulo se representa internamente por dos objetos Punto."""
        self.pto_inf_izq = pto_inf_izq
        self.pto_sup_der = pto_sup_der

    def puntos(self):
        """Devuelve tupla con los dos Punto."""
        return self.pto_inf_izq, self.pto_sup_der

    def base(self):
        """Devuelve la longitud de la base."""
        return self.pto_sup_der.x - self.pto_inf_izq.x

    def altura(self):
        """Devuelve la longitud de la altura."""
        return self.pto_sup_der.y - self.pto_inf_izq.y

    def perimetro(self):
        return ((2 * self.base()) + (2 * self.altura()))

    def reescalar(self, factor_num):
        nueva_b = self.base() * factor_num
        nueva_h = self.altura() * factor_num
        self.pto_sup_der.x = self.pto_inf_izq.x + nueva_b
        self.pto_sup_der.y = self.pto_inf_izq.y + nueva_h

    def get_str(self):
        return f"<{self.pto_inf_izq.get_str()}, {self.pto_sup_der.get_str()}>"

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
