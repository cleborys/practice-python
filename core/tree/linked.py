from .error import ContainerMismatchError, InvalidNodeError, CannotDeleteError

from typing import Any, Optional

ValueType = Any


class LinkedBinaryTree:
    class Node:
        def __init__(self, container: "LinkedBinaryTree", value: ValueType):
            self._value = value
            self._container = container
            self._valid = True
            self._right: Optional["LinkedBinaryTree.Node"] = None
            self._left: Optional["LinkedBinaryTree.Node"] = None

        @property
        def value(self) -> ValueType:
            return self._value

        @property
        def is_valid(self) -> bool:
            return self._valid

        def invalidate(self):
            self._valid = False

        def _has_children(self):
            return self._left is not None or self._right is not None

    def __init__(self):
        self._len = 0
        self._root = None

    def __len__(self):
        return self._len

    def get_root(self) -> Optional[Node]:
        return self._root

    def set_root(self, value: ValueType) -> Node:
        if self._root is None:
            self._root = self.Node(self, value)
            self._len = 1
        else:
            self._root._value = value

        return self._root

    def _verify_node(self, node: Node):
        if node._container is not self:
            raise ContainerMismatchError
        if not node.is_valid:
            raise InvalidNodeError

    def add_right(self, node: Node, value: ValueType) -> Node:
        return self.add_child(node, True, value)

    def add_left(self, node: Node, value: ValueType) -> Node:
        return self.add_child(node, False, value)

    def add_child(self, node: Node, right: bool, value: ValueType) -> Node:
        self._verify_node(node)

        if right is True and node._right is not None:
            node._right._value = value
            return node._right
        if right is False and node._left is not None:
            node._left._value = value
            return node._left

        new_node = self.Node(self, value)
        self._len += 1
        if right:
            node._right = new_node
        else:
            node._left = new_node

        return new_node

    def delete_child(self, parent: Node, right: bool):
        self._verify_node(parent)
        if right:
            node = parent._right
        else:
            node = parent._left
        if node is None:
            raise InvalidNodeError
        if node._has_children():
            raise CannotDeleteError

        node.invalidate()
        self._len -= 1
        if right:
            parent._right = None
        else:
            parent._left = None

        return node

    def __iter__(self):
        yield from self.inorder_traversal()

    def inorder_traversal(self):
        stack = [self.get_root()]
        while stack[-1] is not None:
            stack.append(stack[-1]._left)
        stack.pop()  # pop off the last None

        while stack:
            yield stack[-1]
            self._inorder_advance(stack)

    @staticmethod
    def _inorder_advance(stack):
        current_node = stack[-1]

        # if we have a right child, go right and then all the way left
        if current_node._right is not None:
            stack.append(current_node._right)
            while stack[-1]._left is not None:
                stack.append(stack[-1]._left)
            return

        # otherwise, go up until we were the left child or exhaust the stack
        current_node = stack.pop()
        while stack and stack[-1]._left is not current_node:
            current_node = stack.pop()

    def postorder_traversal(self):
        stack = [self.get_root()]
        self._postorder_first_in_subtree(stack)

        while stack:
            yield stack[-1]
            self._postorder_advance(stack)

    @staticmethod
    def _postorder_first_in_subtree(stack):
        while stack[-1] is not None:
            if stack[-1]._left is not None:
                stack.append(stack[-1]._left)
            else:
                stack.append(stack[-1]._right)
        stack.pop()  # pop off the last None

    @classmethod
    def _postorder_advance(cls, stack):
        current_node = stack.pop()

        # if we were the right child, return
        if not stack or (stack and stack[-1]._right is current_node):
            return

        # otherwise, if there is a right child, recur there
        stack.append(stack[-1]._right)
        cls._postorder_first_in_subtree(stack)

    def preorder_traversal(self):
        stack = [self.get_root()]
        if stack[0] is None:
            return

        while stack:
            yield stack[-1]
            self._preorder_advance(stack)

    @staticmethod
    def _preorder_advance(stack):
        # if we have a child, go there:
        current_node = stack[-1]
        if current_node._left is not None:
            stack.append(current_node._left)
            return
        elif current_node._right is not None:
            stack.append(current_node._right)
            return

        # otherwise have to go up
        # until we were the left child and have a right sibling
        # and then go to the right child
        curent_node = stack.pop()
        while stack and not (
            stack[-1]._left is current_node and stack[-1]._right is not None
        ):
            current_node = stack.pop()
        if stack:
            stack.append(stack[-1]._right)

    def inorder_traversal_recursive(self):
        if not self._root:
            return
        yield from self._inorder_traversal_recursive(self._root)

    def _inorder_traversal_recursive(self, node: Node):
        if node._left is not None:
            yield from self._inorder_traversal_recursive(node._left)

        yield node

        if node._right is not None:
            yield from self._inorder_traversal_recursive(node._right)

    def preorder_traversal_recursive(self):
        if not self._root:
            return
        yield from self._preorder_traversal_recursive(self._root)

    def _preorder_traversal_recursive(self, node: Node):
        yield node

        if node._left is not None:
            yield from self._preorder_traversal_recursive(node._left)

        if node._right is not None:
            yield from self._preorder_traversal_recursive(node._right)

    def postorder_traversal_recursive(self):
        if not self._root:
            return

        yield from self._postorder_traversal_recursive(self._root)

    def _postorder_traversal_recursive(self, node: Node):
        if node._left is not None:
            yield from self._postorder_traversal_recursive(node._left)

        if node._right is not None:
            yield from self._postorder_traversal_recursive(node._right)

        yield node
