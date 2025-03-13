"""Module to test the class REctangle."""

from rectangle import Rectangle

r1 = Rectangle(1.0, 2.0)
print("length: {}\nwidth: {}\n".format(r1.length, r1.width))

r2 = r1 * 2
print("length: {}\nwidth: {}\n".format(r2.length, r2.width))

r2 = 2 * r1
print("length: {}\nwidth: {}\n".format(r2.length, r2.width))
