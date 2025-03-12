"""This file contains the class Point."""


class Point:
    """A point in a plane."""
    def __init__(self, x, y):
        """A point is initialized with x and y coordinates"""
        self.x = x
        self.y = y

    # Put your code here
    def move(self, dx, dy):
        self.x += dx
        self.y += dy


if __name__ == "__main__":
    # Example of use (not part of the solution)

    p = Point(3.0, 4.5)
    print("x = {}, y = {}".format(p.x, p.y))
    p.move(1.0, -1.0)
    print("x = {}, y = {}".format(p.x, p.y))
