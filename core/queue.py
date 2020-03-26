from .linked_list.singly_linked import SinglyLinkedList
from typing import Any

ValueType = Any


class QueueError(Exception):
    pass


class EmptyQueueError(QueueError):
    pass


class Queue:
    def __init__(self):
        self._back = SinglyLinkedList()

    def __len__(self):
        return len(self._back)

    def enqueue(self, value: ValueType):
        self._back.append(value)

    def dequeue(self) -> ValueType:
        if len(self) == 0:
            raise EmptyQueueError

        return self._back.delete_front().value

    def peek(self):
        if len(self) == 0:
            raise EmptyQueueError

        return self._back.get_head().value
