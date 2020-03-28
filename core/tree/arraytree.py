from typing import Any, Optional

ValueType = Any

from .error import TreeError, ContainerMismatchError


class ArrayTreeError(TreeError):
    pass


class InvalidItemError(ArrayTreeError):
    pass


class DoesNotExistError(ArrayTreeError):
    pass


class NoParentError(ArrayTreeError):
    pass


class ArrayTree:
    class Empty:
        def __init__(self):
            pass

        def __repr__(self):  # pragma: no cover
            return "X"

    class Item:
        def __init__(self, container: "ArrayTree", index: int, value: ValueType):
            self._value = value
            self._valid = True
            self._container = container
            self._index = index

        @property
        def container(self) -> "ArrayTree":
            return self._container

        @property
        def value(self) -> ValueType:
            return self._value

        @property
        def is_valid(self) -> bool:
            return self._valid

        def _invalidate(self):
            self._valid = False

        def _reassign(self, value: ValueType):
            self._value = value

        def __repr__(self):  # pragma: no cover
            return f"<Item: {self._value}>"

    def __init__(self):
        self._back = []
        self._marker = self.Empty()
        self._len = 0

    def __len__(self):
        return self._len

    def __str__(self):  # pragma: no cover
        return str(self._back)

    def set_root(self, value: ValueType) -> Item:
        if len(self._back) == 0:
            self._back.append(self.Item(self, 0, value))
            self._len += 1
        else:
            self._back[0]._reassign(value)

        return self._back[0]

    def get_root(self) -> Optional[Item]:
        if len(self._back) == 0:
            return None
        return self._back[0]

    def get_parent(self, item: Item) -> Optional[Item]:
        self._verify_item(item)
        if item._index == 0:
            return None

        parent_index = self._parent_of(item._index)
        return self._back[parent_index]

    def get_right(self, item: Item) -> Optional[Item]:
        return self.get_child(True, item)

    def get_left(self, item: Item) -> Optional[Item]:
        return self.get_child(False, item)

    def get_child(self, right: bool, item: Item) -> Optional[Item]:
        self._verify_item(item)
        if right:
            child_index = self._right_of(item._index)
        else:
            child_index = self._left_of(item._index)

        if not self._verify_index(child_index):
            return None

        child = self._back[child_index]
        if child is self._marker:
            return None

        return child

    def set_right(self, item: Item, value: ValueType) -> Item:
        return self.set_child(item, True, value)

    def set_left(self, item: Item, value: ValueType) -> Item:
        return self.set_child(item, False, value)

    def set_child(self, item: Item, right: bool, value: ValueType) -> Item:
        """
        Sets the child  to value and returns the newly created or modified item.
        Affects right child if `right` is set to True, else the left child.
        """
        self._verify_item(item)
        if right:
            child_index = self._right_of(item._index)
        else:
            child_index = self._left_of(item._index)

        while len(self._back) <= child_index:
            self._back.append(self._marker)

        if self._back[child_index] is self._marker:
            self._back[child_index] = self.Item(self, child_index, value)
            self._len += 1
        else:
            self._back[child_index]._reassign(value)

        return self._back[child_index]

    def get_last(self) -> Optional[Item]:
        if len(self._back) == 0:
            return None

        return self._back[-1]

    def add_last(self, value: ValueType) -> Item:
        """
        Adds a new node at the next place in in-level traversal.
        Raises NoParentError if that node would not have a parent,
        for example because the tree is not complete.
        """
        new_index = len(self._back)
        if new_index == 0:
            return self.set_root(value)

        parent_index = self._parent_of(new_index)
        if (
            not self._verify_index(parent_index)
            or self._back[parent_index] is self._marker
        ):
            raise NoParentError

        self._len += 1
        self._back.append(self.Item(self, new_index, value))
        return self._back[new_index]

    def delete_last(self) -> Item:
        """
        Deletes the last item (with respect to level-order traversal)
        and returns the deleted item.

        Assumes self._back[-1] is a valid item if it exists.
        """
        if len(self._back) == 0:
            raise DoesNotExistError

        deleted_item = self._back.pop()
        self._len -= 1
        deleted_item._invalidate()

        while self._back and self._back[-1] is self._marker:
            self._back.pop()

        return deleted_item

    def swap_with_parent(self, item: Item):
        other = self.get_parent(item)
        if other is not None:
            self.swap_items(item, other)

    def swap_with_right(self, item: Item):
        other = self.get_right(item)
        if other is not None:
            self.swap_items(item, other)

    def swap_with_left(self, item: Item):
        other = self.get_left(item)
        if other is not None:
            self.swap_items(item, other)

    def swap_items(self, item: Item, other: Item):
        self._verify_item(item)
        self._verify_item(other)

        item_index = item._index
        other_index = other._index
        self._back[item_index], self._back[other_index] = other, item

        self._back[item_index]._index = item_index
        self._back[other_index]._index = other_index

    def _verify_item(self, item: Item):
        if item.container != self:
            raise ContainerMismatchError
        if item.is_valid is False:
            raise InvalidItemError

    def _verify_index(self, i: int) -> bool:
        return 0 <= i < len(self._back)

    @staticmethod
    def _right_of(i: int) -> int:
        return 2 * i + 2

    @staticmethod
    def _left_of(i: int) -> int:
        return 2 * i + 1

    @staticmethod
    def _parent_of(i: int) -> int:
        return (i - 1) // 2
