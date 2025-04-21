from stackexceptions import StackEmptyError


class Stack:
    class Node:
        def __init__(self, value, next_node=None):
            self.value = value
            self.next_node = next_node

    def __init__(self):
        self.__top = None
        self.__len = 0

    def push(self, value):
        new_node = self.Node(value)
        new_node.next_node= self.__top
        self.__top = new_node
        self.__len += 1

    def pop(self):
        if self.is_empty():
            raise StackEmptyError("No se puede hacer pop en una pila vacía")
        value = self.__top.value
        self.__top = self.__top.next_node
        self.__len -= 1
        return value

    @property
    def top(self):
        if self.is_empty():
            raise StackEmptyError("No se puede acceder al top de una pila vacía.")
        return self.__top.value

    def is_empty(self):
        return self.__top is None

    def __len__(self):
        return self.__len
