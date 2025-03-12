"""Module with the answer to the problem."""


class Texto():
    """texto."""

    def __init__(self, lista_de_párrafos):
        """Crea copia interna del texto (lista de párrafos)."""
        self.__txt = lista_de_párrafos[:]

    def __str__(self):
        """Representación informal."""
        return '\n'.join([parrafo.get_str() for parrafo in self.__txt])

    @property
    def npalabras(self):
        return sum(len(parrafo.get_palabras()) for parrafo in self.__txt)

    def get_parrafo(self, indice):
        if 0 <= indice < len(self.__txt):
            return self.__txt[indice]

    def set_parrafo(self, indice, parrafo):
        if 0 <= indice < len(self.__txt):
            self.__txt[indice] = parrafo

    @property
    def nparrafos(self):
        return len(self.__txt)

    @nparrafos.setter
    def nparrafos(self, nuevo_num):
        while len(self.__txt) > nuevo_num:
            self.__txt.pop()
        while len(self.__txt) < nuevo_num:
            self.__txt.append(Parrafo(''))

# NO MODIFIQUE EL CODIGO DEBAJO DE ESTA LINEA


class Parrafo:
    """Representa un párrafo."""

    def __init__(self, texto):
        """Se inicializa un párrafo al texto str pasado."""
        if type(texto) is not str:
            raise ValueError
        self.__contenido = texto

    def get_palabras(self):
        """Devuelve una lista con las palabras en el párrafo."""
        import re
        return re.findall(r"\b\w+\b", self.__contenido)

    def get_ncaracteres(self):
        """Devuelve el número de caracteres en las palabras del párrafo."""
        return sum([len(p) for p in self.get_palabras()])

    def get_str(self):
        """Devuelve la representación informal del párrafo."""
        return self.__contenido
