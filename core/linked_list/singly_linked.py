from typing import Any, Optional

from .error import EmptyListError

ValueType = Any


class SinglyLinkedList:
    class Node:
        def __init__(self, value: ValueType):
            self._value = value
            self._next = None

        @property
        def value(self):
            return self._value

        @property
        def next(self):
            return self._next

    def __init__(self):
        self._head = self.Node("Head Node")
        self._last = self._head
        self._len = 0

    def __len__(self):
        return self._len

    def __iter__(self):
        next_node = self._head.next
        while next_node is not None:
            yield next_node
            next_node = next_node.next

    def append(self, value: ValueType) -> Node:
        new_node = self.Node(value)

        self._last._next = new_node
        self._last = self._last._next

        self._len += 1

        return self._last

    def append_front(self, value: ValueType) -> Node:
        new_node = self.Node(value)
        new_second = self._head.next

        new_node._next = new_second
        self._head._next = new_node

        self._len += 1

        return new_node

    def delete_front(self) -> Node:
        if self._head.next is None:
            raise EmptyListError

        deleted = self._head.next
        self._head._next = deleted.next
        self._len -= 1

        return deleted

    def get_head(self) -> Node:
        if len(self) == 0:
            raise EmptyListError

        return self._head.next

    def get_tail(self) -> Node:
        if len(self) == 0:
            raise EmptyListError

        return self._last
