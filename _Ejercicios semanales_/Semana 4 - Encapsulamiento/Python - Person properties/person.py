"""This module contains the class Person."""


class Person:
    """Represents a person.

    Properties:
    name   : str the name of a person.
    surname: str the surname of a person.

    """
    # complete la clase
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and value.strip():
            self._name = value
        else:
            self._name = "unknown"

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value):
        if isinstance(value, str) and value.strip():
            self._surname = value
        else:
            self._surname = "unknown"


if __name__ == "__main__":
    # Example of use (not part of the solution)

    person1 = Person("John", "Doe")
    print(f"Name   : {person1.name}")
    print(f"surname: {person1.surname}")
