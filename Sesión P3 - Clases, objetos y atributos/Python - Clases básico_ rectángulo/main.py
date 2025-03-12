"""Ejemplo de uso de la funciones requerida."""

from solution import Rectangulo, Punto

tests = [
    (Punto(2, 3), Punto(3, 4)),
    (Punto(0, 0), Punto(1, 2)),
]

for p1, p2 in tests:
    print("Puntos", p1.get_str(), p2.get_str())
    r = Rectangulo(p1, p2)
    print("Perímetro", r.perimetro())
    print("Rectángulo", r.get_str())
    r.reescalar(1.5)
    print("Después de reescalar 1.5")
    print("Perímetro", r.perimetro())
    print("Rectángulo", r.get_str())
    print()
