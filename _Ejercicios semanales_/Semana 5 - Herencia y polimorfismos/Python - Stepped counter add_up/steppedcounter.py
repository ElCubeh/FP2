"""Este módulo ofrece la clase SteppedCounter."""

from counter import Counter


class SteppedCounter(Counter):
    """A counter with a custom step."""

    def __init__(self, step):
        """Initialize a Counter and add custom step."""
        super().__init__()
        self.__step = step

    @property
    def step(self):
        """Return step's current value."""
        return self.__step

    # Put your code here
    def add_up(self):
        for _ in range(self.__step):
            super().add_up()


if __name__ == "__main__":
    # Example of use (not part of the solution)

    c = SteppedCounter(3)
    print(c.count)
    c.add_up()
    print(c.count)
