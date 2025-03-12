"""Clase a modificar para el ejercicio."""


class Botella:
    """Representa una botella con una determinada capacidad y contenido."""
    capacidades: dict = {}

    def __init__(self, capacidad, contenido):
        """Inicializa una botella con una capacidad y contenido dados."""
        self.__capacidad = capacidad
        self.__contenido = contenido
        # Actualizar el diccionario de capacidades
        if capacidad in Botella.capacidades:
            Botella.capacidades[capacidad] += 1
        else:
            Botella.capacidades[capacidad] = 1

    @property
    def capacidad(self):
        """Devuelve la capacidad del objeto."""
        return self.__capacidad

    @property
    def contenido(self):
        """Contenido del objeto."""
        return self.__contenido

    @contenido.setter
    def contenido(self, nuevo_contenido):
        """Modifica el contenido de la botella asegurando que no supere su capacidad."""
        if 0 <= nuevo_contenido <= self.__capacidad:
            self.__contenido = nuevo_contenido
        else:
            raise ValueError("El contenido no puede ser negativo ni superar la capacidad de la botella.")

    @classmethod
    def botellas_capacidad(cls, capacidad):
        """Devuelve el número de botellas creadas hasta el momento de la capacidad dada."""
        return cls.capacidades.get(capacidad, 0)
    # NOTA: se recomienda escribir el setter a continuación del getter


if __name__ == "__main__":
    b = Botella(500, 450)
    print(b.capacidad, b.contenido)
    # print(b.botellas_capacidad(500))
    # print(b.botellas_capacidad(600))
    Botella(500, 450)
    Botella(600, 450)
    # print(b.botellas_capacidad(500))
    # print(b.botellas_capacidad(600))
