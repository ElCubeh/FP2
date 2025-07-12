# ESCRIBA AQUÍ LA CLASE
class Libro:
    # descomente la siguiente línea si quiere usarla
    # __autor_número: dict[str, int] = {}  # diccionario autor: nº libros
class Libro:
    _total_libros = 0
    _libros_por_autor = {}

    def __init__(self, titulo: str, autor: str, fecha: int):
        self._titulo = titulo
        self._autor = autor
        self._fecha = fecha
        self._prestado = False
        
        Libro._total_libros += 1
        Libro._libros_por_autor[autor] = Libro._libros_por_autor.get(autor, 0) + 1

    @property
    def titulo(self) -> str:
        return self._titulo
    
    @property
    def autor(self) -> str:
        return self._autor
    
    @property
    def fecha(self) -> int:
        return self._fecha
    
    @property
    def prestado(self) -> bool:
        return self._prestado
    
    @prestado.setter
    def prestado(self, value: bool):
        if not isinstance(value, bool):
            raise ValueError("El valor debe ser booleano")
        self._prestado = value

    def prestar(self):
        if self._prestado:
            raise ValueError("El libro ya está prestado")
        self._prestado = True

    def devolver(self):
        if not self._prestado:
            raise ValueError("El libro no está prestado")
        self._prestado = False

    @classmethod
    def total_libros(cls) -> int:
        return cls._total_libros

    @classmethod
    def publicados_autor(cls, autor: str) -> int:
        return cls._libros_por_autor.get(autor, 0)

    def __str__(self) -> str:
        estado = "Prestado" if self._prestado else "Disponible"
        return f'"{self._titulo}" por {self._autor} ({self._fecha}) - {estado}'