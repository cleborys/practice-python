from .error import EmptyListError, ContainerMismatch

from typing import Any, Optional

ValueType = Any


class DoublyLinkedList:
    class Node:
        def __init__(self, container: "DoublyLinkedList", value: ValueType):
            self._value = value
            self._next: Optional["DoublyLinkedList.Node"] = None
            self._previous: Optional["DoublyLinkedList.Node"] = None
            self._container = container

        @property
        def value(self):
            return self._value

    def __init__(self):
        self._head = self.Node(self, "Head Guard")
        self._tail = self.Node(self, "Tail Guard")
        self._head._next = self._tail
        self._tail._previous = self._head
        self._len = 0

    def __iter__(self):
        node = self._head._next
        while node is not self._tail:
            yield node
            node = node._next

    def iter_values(self):
        for node in self:
            yield node.value

    def __len__(self):
        return self._len

    def insert_front(self, value: ValueType) -> Node:
        return self._insert_after(self._head, value)

    def insert_back(self, value: ValueType) -> Node:
        return self._insert_after(self._tail._previous, value)

    def insert_before(self, position: Node, value: ValueType) -> Node:
        self._verify_node(position)
        return self._insert_after(position._previous, value)

    def insert_after(self, position: Node, value: ValueType) -> Node:
        self._verify_node(position)
        return self._insert_after(position, value)

    def _insert_after(self, position: Node, value: ValueType) -> Node:
        """
        Inserts a new value after the given position,
        assumes the position is valid.
        """
        new_node = self.Node(self, value)
        new_node._previous = position
        new_node._next = position._next

        new_node._previous._next = new_node
        new_node._next._previous = new_node

        self._len += 1

        return new_node

    def splice_out(self, node: Node):
        self._verify_node(node)

        node._next._previous = node._previous
        node._previous._next = node._next

        node._next = None
        node._previous = None

        self._len -= 1

    def _verify_node(self, node: Node):
        if node._container is not self:
            raise ContainerMismatch

    def get_head(self) -> Node:
        if len(self) == 0:
            raise EmptyListError
        return self._head._next

    def get_tail(self) -> Node:
        if len(self) == 0:
            raise EmptyListError
        return self._tail._previous
