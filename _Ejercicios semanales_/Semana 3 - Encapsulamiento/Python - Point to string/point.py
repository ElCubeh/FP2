"""This module contains the class Point."""


class Point:
    """A point in a plane."""

    # No olvidar añadir el inicializador
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x = {self.x}, y = {self.y})"

    def __str__(self):
        return f"{self.x}, {self.y}"


if __name__ == "__main__":
    # Example of use (not part of the solution)

    p = Point(3.0, 4.5)
    print("Formal: {}".format(repr(p)))
    print("Informal: {}".format(p))
