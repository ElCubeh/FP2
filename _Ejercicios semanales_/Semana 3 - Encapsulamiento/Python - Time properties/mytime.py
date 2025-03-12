"""This module contains the class Time."""


# Escriba aquí la definición de la clase pedida.
class Time:
    def __init__(self, hour=0, minute=0):
        self.hour = hour
        self.minute = minute

    @property
    def hour(self):
        return self._hour

    @hour.setter
    def hour(self, value):
        if isinstance(value, int):
            if 0 <= value <= 23:
                self._hour = value
            elif value < 0:
                self._hour = 0
            else:  # value > 23
                self._hour = 23
        else:
            self._hour = 0

    @property
    def minute(self):
        return self._minute

    @minute.setter
    def minute(self, value):
        if isinstance(value, int):
            if 0 <= value <= 59:
                self._minute = value
            elif value < 0:
                self._minute = 0
            else:  # value > 59
                self._minute = 59
        else:
            self._minute = 0

    def __str__(self):
        return f"{self.hour:02}:{self.minute:02}"


if __name__ == "__main__":
    # Example of use (not part of the solution)

    t = Time(12, 5)
    print(f"{t.hour:02}:{t.minute:02}")
