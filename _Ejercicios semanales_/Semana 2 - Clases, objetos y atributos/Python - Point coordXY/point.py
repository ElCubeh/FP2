"""This file contains the class Point."""


class Point:
    """A point in a plane."""
    def __init__(self, x, y):
        """A point is initialized with x and y coordinates"""
        self.x = x
        self.y = y

    # Put your code here
    def coordXY(self):
        return (self.x, self.y)


if __name__ == "__main__":
    # Example of use (not part of the solution)

    p = Point(3.0, 4.5)
    print("x = {}, y = {}".format(p.x, p.y))
    print(p.coordXY())
