class StackEmptyError(Exception):
    def __init__(self, message="La pila está vacía, no se puede realizar la operación."):
        self.message = message
        super().__init__(self.message)
