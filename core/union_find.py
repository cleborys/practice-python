from typing import Any

ValueType = Any


class UnionFindError(Exception):
    pass


class DuplicateItemError(UnionFindError):
    pass


class NotFoundError(UnionFindError):
    pass


class UnionFind:
    class Item:
        def __init__(self, value: ValueType):
            self._value = value
            self._next = None
            self._size = 1

        def __lt__(self, other: "Item") -> bool:
            return self._size < other._size

    def __init__(self):
        self._items = {}

    def __len__(self):
        return len(self._items)

    def __contains__(self, value: ValueType) -> bool:
        return value in self._items

    def add_new(self, value: ValueType):
        if value in self:
            raise DuplicateItemError

        new_item = self.Item(value)
        self._items[value] = new_item

    def union(self, a: ValueType, b: ValueType) -> bool:
        """
        Returns whether a new union was created.
        """
        if a not in self:
            self.add_new(a)
        if b not in self:
            self.add_new(b)

        a_leader = self._find_leader(a)
        b_leader = self._find_leader(b)

        if a_leader is b_leader:
            return False

        # union by rank
        if a_leader < b_leader:
            a_leader._next = b_leader
            b_leader._size += a_leader._size
        else:
            b_leader._next = a_leader
            a_leader._size += b_leader._size
        return True

    def same_partition(self, a: ValueType, b: ValueType) -> bool:
        return self._find_leader(a) is self._find_leader(b)

    def _find_leader(self, value: ValueType):
        if value not in self:
            raise NotFoundError

        ancestors = [self._items[value]]
        while ancestors[-1]._next is not None:
            ancestors.append(ancestors[-1]._next)

        leader = ancestors.pop()
        # path compression
        for node in ancestors:
            node._next = leader

        return leader
