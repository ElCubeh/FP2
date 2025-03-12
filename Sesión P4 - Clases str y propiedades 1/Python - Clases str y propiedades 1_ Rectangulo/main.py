"""Ejemplo de uso de la funciones requerida."""

from solution import Rectangulo, Punto, BadRectangle
import inspect

tests = [
    (Punto(2, 3), Punto(3, 4)),
    (Punto(-2, -3), Punto(1, 5)),
    (Punto(3, 5), Punto(1, 6)),
    (Punto(1, 3), Punto(3, 2)),
]

for p1, p2 in tests:
    try:
        print("Puntos", p1.get_str(), p2.get_str())
        r = Rectangulo(p1, p2)
        print("Está contenido el Punto(0, 0):", r.esta_contenido(Punto(0, 0)))
        print("Rectángulo", r)
    except BadRectangle as err:
        print(f"Rectángulo erróneo")
    print()
