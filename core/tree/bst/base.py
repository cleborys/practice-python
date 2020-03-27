from ..linked import LinkedBinaryTree
from typing import Any, Tuple, List

ValueType = Any
KeyType = int


class BinarySearchTree(LinkedBinaryTree):
    class Node(LinkedBinaryTree.Node):
        def __init__(self, container: "BinarySearchTree", value: ValueType):
            super().__init__(container, value)
            self._height = 0

        def _get_child_height(self, right: bool) -> int:
            if right:
                return self._right._height if self._right is not None else -1
            return self._left._height if self._left is not None else -1

        def _update_height(self):
            self._height = 1 + max(
                self._get_child_height(False), self._get_child_height(True)
            )

        @property
        def key(self) -> KeyType:
            return self._value._key

        @property
        def value(self) -> ValueType:
            return self._value._value

        def _is_balanced(self) -> bool:
            height_diff = self._get_child_height(False) - self._get_child_height(True)
            return height_diff * height_diff <= 1

        def __repr__(self) -> str:  # pragma: no cover
            return f"<{self._value}>"

    class Item:
        def __init__(self, key: KeyType, value: ValueType):
            self._key = key
            self._value = value

        def __repr__(self) -> str:  # pragma: no cover
            return f"<Item {self._key}: {self._value}>"

    def search(self, key: KeyType) -> Tuple[bool, List[Node]]:
        """
        Searches for an item with matching key,
        returns True and list of ancestors if found,
        otherwise returns False and list of ancestors for successor or predecessork leaf.
        """
        success = False
        stack = [self._root]
        while stack[-1] is not None:
            current_key = stack[-1].key
            if current_key == key:
                success = True
                break
            if current_key < key:
                stack.append(stack[-1]._right)
            else:
                stack.append(stack[-1]._left)

        if stack[-1] is None:
            stack.pop()

        return success, stack

    def insert(self, key: KeyType, value: ValueType):
        added_item = self.Item(key, value)
        if not self._root:
            self.set_root(added_item)

        found, path = self.search(key)

        if found:
            path[-1]._value = added_item
            return path[-1]

        leaf = path[-1]
        add_right = key > leaf.key
        added_node = self.add_child(leaf, add_right, added_item)
        path.append(added_node)

        self._rebalance_hook(path)

        return added_node

    def _rebalance_hook(self, path: List[Node]):
        pass  # pragma: no cover
