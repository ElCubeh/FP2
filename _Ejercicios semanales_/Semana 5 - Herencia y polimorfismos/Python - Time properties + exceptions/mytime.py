"""
This module offers the class Time.
"""
from timeexceptions import HourError, MinuteError


class Time:
    """Represent a time."""

    def __init__(self, h, m):
        """Initialize Time objects with hours and minutes."""
        self.hour = h
        self.minute = m

    @property
    def hour(self):
        """Return the hour."""
        return self.__hour

    @hour.setter
    def hour(self, value):
        if not type(value) is int or value < 0:
            self.__hour = 0
        elif value > 23:
            self.__hour = 23
            raise HourError(value, "invalid hour")
        else:
            self.__hour = value

    @property
    def minute(self):
        """Return the minute."""
        return self.__minute

    @minute.setter
    def minute(self, value):
        if not type(value) is int or value < 0:
            self.__minute = 0
        elif value > 59:
            self.__minute = 59
            raise MinuteError(value, "invalid minute")
        else:
            self.__minute = value


if __name__ == "__main__":
    # Example of use (not part of the solution)
    try:
        t = Time(120, 5)
        print(f"{t.hour:02}:{t.minute:02}")
    except (HourError, MinuteError) as e:
        print(type(e), e.args[0], e.value_error)
