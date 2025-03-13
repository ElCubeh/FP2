class Evens:
    def __init__(self, max_num):
        self._max_num = max_num
        self._current = 2

    def __iter__(self):
        return self

    def __next__(self):
        if self._current > self._max_num:
            raise StopIteration
        num = self._current
        self._current += 2
        return num


for i in Evens(10):
    print(i)

for i in Evens(15):
    print(i)
