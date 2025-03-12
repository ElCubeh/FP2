"""This module contains the class Point."""


class Point:
    """A point in a plane"""
    def __init__(self, x, y):
        """A point is initialized with x and y coordinates"""
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("improper type for x coordinate")
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("improper type for y coordinate")
        self._y = value


if __name__ == "__main__":
    # Example of use (not part of the solution)

    p = Point(3.0, 4.5)
    print(f"(x = {p.x}, y = {p.y})")
    # should raise an exception:
    p = Point("3.0", "4.5")
