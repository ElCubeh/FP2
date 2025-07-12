# PROBANDO la clase Libro:
from libro import Libro

# Crear varias instancias de libros
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967)
libro2 = Libro("Crónica de una muerte anunciada",
               "Gabriel García Márquez", 1981)
libro3 = Libro("1984", "George Orwell", 1949)

# Mostrar información básica de cada libro
print(libro1)
print(libro2)
print(libro3)

# Prestar un libro y verificar estado
libro1.prestar()
print(f"Después de prestar: {libro1}")

# Intentar prestar un libro ya prestado (manejo de excepciones)
try:
    libro1.prestar()
except ValueError as e:
    print(f"Error: {e}")

# Devolver el libro y verificar estado nuevamente
libro1.devolver()
print(f"Después de devolver: {libro1}")

# Consultar cantidad total de libros creados
print(f"Total libros creados: {Libro.total_libros()}")

# Consultar cuántos libros publicó un autor específico
nlibros = Libro.publicados_autor('Gabriel García Márquez')
print(f"Libros de Gabriel García Márquez: {nlibros}")
nlibros = Libro.publicados_autor('George Orwell')
print(f"Libros de George Orwell: {nlibros}")
nlibros = Libro.publicados_autor('Autor Desconocido')
print(f"Libros de autor inexistente: {nlibros}")

# Modificar directamente el estado de préstamo usando el setter (propiedad)
libro2.prestado = True
print(f"Estado modificado usando setter: {libro2}")
