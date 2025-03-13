class PowersOfTwo:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.n:
            result = 2 ** self.current
            self.current += 1
            return result
        else:
            raise StopIteration


for i in PowersOfTwo(5):
    print(i)

print()

for i in PowersOfTwo(7):
    print(i)
