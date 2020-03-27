from .base import BinarySearchTree
from typing import Any, Tuple, List

ValueType = Any
KeyType = int
Node = BinarySearchTree.Node


class AVLTree(BinarySearchTree):
    def _rebalance_hook(self, path: List[Node]):
        """
        Assumes path to be nonempty.
        """
        while path:
            parent = path.pop()
            parent._update_height()
            if parent._is_balanced():
                continue
            self._rebalance(parent)

    def _rebalance(self, node: Node):
        """
        Find the larger child of the larger child,
        breaking draws as aligned.
        Then rotate the middle node up twice.
        """

        left_height = node._get_child_height(False)
        right_height = node._get_child_height(True)

        choose_right = right_height > left_height
        if choose_right:
            child = node._right
        else:
            child = node._left

        child_left_height = child._get_child_height(False)
        child_right_height = child._get_child_height(True)

        equal_heights = child_left_height == child_right_height
        child_right_higher = child_right_height > child_left_height
        child_choose_right = child_right_higher or (equal_heights and choose_right)

        equal_alignment = choose_right == child_choose_right
        if equal_alignment:
            # rotate middle node up
            self._rotate_child_up(node, choose_right)
        else:
            # rotate grandchild up twice
            self._rotate_child_up(child, child_choose_right)
            self._rotate_child_up(node, choose_right)

    def _rotate_child_up(self, node: Node, right: bool):
        """
        Modifies nodes in-place,
        so they should remain encapsulated.
        """
        if right:
            rotated = node._right
        else:
            rotated = node._left

        node._value, rotated._value = rotated._value, node._value

        if right:
            node._right = rotated._right
            rotated._right = rotated._left
            rotated._left = node._left
            node._left = rotated
        else:
            node._left = rotated._left
            rotated._left = rotated._right
            rotated._right = node._right
            node._right = rotated


class AVLTreeMap:
    def __init__(self):
        self._back = AVLTree()

    def __len__(self):
        return len(self._back)

    def __getitem__(self, key):
        found, path = self._back.search(key)
        if not found:
            raise KeyError

        return path[-1].value

    def __setitem__(self, key, value):
        self._back.insert(key, value)
