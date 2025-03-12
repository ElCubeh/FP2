"""This module contains the class Time."""


class Time:
    """Represents a time."""

    # Don't forget to add the initializer
    def __init__(self, h, m):
        self.h = h
        self.m = m

    def __repr__(self):
        return f"Time({self.h}, {self.m})"

    def __str__(self):
        return f"{self.h:02}:{self.m:02}"


if __name__ == "__main__":
    # Example of use (not part of the solution)

    t = Time(12, 5)
    print("Formal: {}".format(repr(t)))
    print("Informal: {}".format(t))
