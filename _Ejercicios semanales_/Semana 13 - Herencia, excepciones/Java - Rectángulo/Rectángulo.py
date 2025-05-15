class Rectángulo:
    """Un rectángulo es un poligono de 4 lados cuyos ángulos tienen todos 90º.
    
    Métodos
    -------
    get_base: devuelve la base del rectángulo
    get_altura: devuelve la altura del rectángulo
    """

    def __init__(self, base, altura):
        """Inicializa un rectángulo."""
        
        self.__base = base
        self.__altura = altura

    
    def get_base(self):
        """Devuelve la base del rectángulo."""
        return self.__base
        
    def get_altura(self):
        """Devuelve la altúra del rectángulo."""
        return self.__altura

    def __eq__(self, other):
        """Devuelve True si los dos rectángulos son iguales.
        
        dos rectángulos son iguales si lo son sus bases y sus alturas
        """
        if type(other) == Rectángulo:
            return self.get_base() == other.get_base() \
                   and self.get_altura() == other.get_altura()
        else:
            return False

    def __str__(self):
        """Devuelve una representación del rectángulo como string."""

        return "Rectángulo de base: " + str(self.get_base()) + \
               " y altura: " + str(self.get_altura())

if __name__ == "__main__":
    r = Rectángulo(10, 5)
    print(r == r)
