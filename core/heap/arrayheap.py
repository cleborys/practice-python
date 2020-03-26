from core.tree.arraytree import ArrayTree
from .errors import HeapEmptyError

from typing import Any

ValueType = Any
Item = ArrayTree.Item


class ArrayHeap:
    def __init__(self):
        self._tree = ArrayTree()

    def __len__(self) -> int:
        return len(self._tree)

    def __str__(self) -> str:  # pragma: no cover
        return str(self._tree)

    def push(self, value: ValueType):
        new_item = self._tree.add_last(value)
        self._bubble(new_item)

    def pop(self) -> ValueType:
        if len(self) == 0:
            raise HeapEmptyError

        to_pop = self._tree.get_root()
        to_swap = self._tree.get_last()

        self._tree.swap_items(to_pop, to_swap)
        self._tree.delete_last()

        if to_swap is not to_pop:
            self._bubble(to_swap)

        return to_pop.value

    def _bubble(self, item: Item):
        self._bubble_up(item)
        self._bubble_down(item)

    def _bubble_up(self, item: Item):
        parent = self._tree.get_parent(item)
        while parent is not None and parent.value > item.value:
            self._tree.swap_items(item, parent)
            parent = self._tree.get_parent(item)

    def _bubble_down(self, item: Item):
        child = self._get_smallest_child(item)
        while child is not None and child.value < item.value:
            self._tree.swap_items(item, child)
            child = self._get_smallest_child(item)

    def _get_smallest_child(self, item: Item):
        left_child = self._tree.get_left(item)
        right_child = self._tree.get_right(item)

        if left_child is None:
            return right_child

        if right_child is None or left_child.value < right_child.value:
            return left_child

        return right_child
