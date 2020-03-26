from .linked_list.singly_linked import SinglyLinkedList
from collections import deque
from typing import Any

ValueType = Any


class StackError(Exception):
    pass


class EmptyStackError(StackError):
    pass


class Stack:
    def __init__(self):
        self._back = SinglyLinkedList()

    def __len__(self):
        return len(self._back)

    def push(self, value: ValueType):
        self._back.append_front(value)

    def pop(self) -> ValueType:
        if len(self) == 0:
            raise EmptyStackError

        return self._back.delete_front().value

    def peek(self) -> ValueType:
        if len(self) == 0:
            raise EmptyStackError

        return self._back.get_head().value


class ArrayStack:
    def __init__(self):
        self._back = []

    def __len__(self):
        return len(self._back)

    def push(self, value: ValueType):
        self._back.append(value)

    def pop(self) -> ValueType:
        if len(self) == 0:
            raise EmptyStackError

        return self._back.pop()

    def peek(self) -> ValueType:
        if len(self) == 0:
            raise EmptyStackError

        return self._back[-1]


class DequeStack:
    def __init__(self):
        self._back = deque()

    def __len__(self):
        return len(self._back)

    def push(self, value: ValueType):
        self._back.append(value)

    def pop(self) -> ValueType:
        if len(self) == 0:
            raise EmptyStackError

        return self._back.pop()

    def peek(self) -> ValueType:
        if len(self) == 0:
            raise EmptyStackError

        return self._back[-1]
