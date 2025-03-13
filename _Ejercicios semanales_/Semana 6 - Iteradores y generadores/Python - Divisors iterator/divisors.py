"""This module contains the class Divisors which is an Iterator."""


class Divisors:
    """iterator: Returns, one at a time, the divisors os a positive integer."""

    def __init__(self, number):
        """Set number to get its Divisors.

        raise ValueError is number is not a positive integer.
        """
        if type(number) == int and number > 0:
            self.__number = number
        else:
            raise ValueError(
                "Initalization parameter must be a positive integer"
                )

    # Put your code here
    def __iter__(self):
        self.__current = 1
        return self

    def __next__(self):
        while self.__current <= self.__number:
            if self.__number % self.__current == 0:
                result = self.__current
                self.__current += 1
                return result
            self.__current += 1

        raise StopIteration


for i in Divisors(5):
    print(i)

for i in Divisors(12):
    print(i)
