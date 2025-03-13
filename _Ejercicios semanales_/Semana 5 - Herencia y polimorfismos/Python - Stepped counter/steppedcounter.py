"""This module contains the class SteppedConuter which extents Counter."""

from counter import Counter

# Put your code here


class SteppedCounter(Counter):
    def __init__(self, step):
        super().__init__()
        if not isinstance(step, int) or step <= 0:
            raise ValueError
        self._step = step

    @property
    def step(self):
        return self._step


if __name__ == "__main__":
    # Example of use (not part of the solution)
    c = SteppedCounter(3)
    print(c.count)
    print(c.step)
    c.add_up()
    print(c.count)
