"""Este módulo ofrece la clase MobilePoint."""

from point import Point

# Put your code here


class MobilePoint(Point):
    def move(self, dx, dy):
        self.x += dx
        self.y += dy


if __name__ == "__main__":
    # Example of use (not part of the solution)
    p = MobilePoint(3.0, 4.5)
    print("(x = {}, y = {})".format(p.x, p.y))
    p.move(1.0, -1.0)
    print("(x = {}, y = {})".format(p.x, p.y))
