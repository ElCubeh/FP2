"""This module contains the class Rectangle."""


class Rectangle:
    """A quadrilateral with four right angles."""

    def __init__(self, length, width):
        """Initialize a rectangle with length and width."""
        self.__length = length
        self.__width = width

    @property
    def length(self):
        """Return the length of the rectangle."""
        return self.__length

    @property
    def width(self):
        """Return the width of the rectangle."""
        return self.__width

    # Put your code here
    def __str__(self):
        return f"Rectangle(length={self.__length}, width={self.__width}"

    def __mul__(self, other):
        if isinstance(other, int):
            return Rectangle(self.__length * other, self.__width)
        else:
            return Rectangle(self.__length, self.__width)

    def __rmul__(self, other):
        return self.__mul__(other)
