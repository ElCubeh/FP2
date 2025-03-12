"""This module contains the class Person."""


class Person:
    """Represents a person.

    Attributes:
    name   : str the name of a person.
    surname: str the surname of a person.

    """
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f'Person("{self.name}", "{self.surname}")'

    def __str__(self):
        return f"{self.name} {self.surname}"


if __name__ == "__main__":
    # Example of use (not part of the solution)

    person1 = Person("John", "Doe")
    print("Formal: {}".format(repr(person1)))
    print("Informal: {}".format(person1))
