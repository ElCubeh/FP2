"""This module contains the class Time."""


class Time:
    """Represents a time"""
    def __init__(self, h, m):
        """Time objects are initialized with hours and minutes"""
        self.hour = h
        self.minute = m

    # Añada aquí el método que se pide.
    def increase(self):
        if self.minute < 59:
            self.minute += 1
        else:
            self.minute = 0
            if self.hour < 23:
                self.hour += 1
            else:
                self.hour = 0


# Practique completar aquí código personal de prueba al ejecutar (cohete).
if __name__ == "__main__":
    for i in range(100):
        pass
