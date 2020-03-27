import pytest

from core.tree.linked import LinkedBinaryTree
from core.tree.error import ContainerMismatchError, InvalidNodeError, CannotDeleteError


@pytest.fixture
def tree():
    return LinkedBinaryTree()


@pytest.fixture
def tree_with_values():
    tree = LinkedBinaryTree()
    root = tree.set_root(3)
    l = tree.add_left(root, 1)
    r = tree.add_right(root, 5)
    lr = tree.add_right(l, 2)
    rl = tree.add_left(r, 4)
    rr = tree.add_right(r, 6)
    return tree


def test_init():
    tree = LinkedBinaryTree()

    assert len(tree) == 0


def test_root(tree):
    assert tree.get_root() is None

    root = tree.set_root("root")
    assert len(tree) == 1
    assert tree.get_root() is root


def test_overwrite_root(tree):
    root = tree.set_root("old")
    tree.set_root("new")

    assert root.value == "new"


def test_add_children(tree):
    root = tree.set_root(3)
    assert len(tree) == 1
    l = tree.add_left(root, 1)
    assert len(tree) == 2
    r = tree.add_right(root, 5)
    assert len(tree) == 3
    lr = tree.add_right(l, 2)
    assert len(tree) == 4
    rl = tree.add_left(r, 4)
    assert len(tree) == 5
    rr = tree.add_right(r, 6)
    assert len(tree) == 6


def test_overwrite_children(tree):
    root = tree.set_root("root")
    l = tree.add_left(root, "old")
    r = tree.add_right(root, "old")

    tree.add_left(root, "new")
    tree.add_right(root, "new")

    assert l.value == "new"
    assert r.value == "new"


def test_container_mismatch():
    tree1 = LinkedBinaryTree()
    tree2 = LinkedBinaryTree()

    root = tree1.set_root("root")

    with pytest.raises(ContainerMismatchError):
        tree2.add_right(root, "bad")


def test_delete_child(tree):
    root = tree.set_root(1)
    r = tree.add_right(root, 2)
    l = tree.add_left(root, 3)

    deleted = tree.delete_child(root, True)
    assert deleted is r
    assert r.is_valid is False

    deleted = tree.delete_child(root, False)
    assert deleted is l
    assert l.is_valid is False


def test_deleted_node_unusable(tree):
    root = tree.set_root(1)
    tree.add_right(root, 2)
    deleted = tree.delete_child(root, True)

    with pytest.raises(InvalidNodeError):
        tree.add_right(deleted, "bad")


def test_delete_nonexistent_child(tree):
    root = tree.set_root(1)
    with pytest.raises(InvalidNodeError):
        tree.delete_child(root, True)


def test_cannot_delete_node_with_children(tree):
    root = tree.set_root(1)
    r = tree.add_right(root, 2)
    rr = tree.add_right(r, 3)

    with pytest.raises(CannotDeleteError):
        tree.delete_child(root, True)


def test_standard_traversal_is_inorder(tree_with_values):
    assert [x.value for x in tree_with_values] == [1, 2, 3, 4, 5, 6]


def test_inorder_traversal(tree_with_values):
    iterator = tree_with_values.inorder_traversal()
    assert [x.value for x in iterator] == [1, 2, 3, 4, 5, 6]


def test_postorder_traversal(tree_with_values):
    iterator = tree_with_values.postorder_traversal()
    assert [x.value for x in iterator] == [2, 1, 4, 6, 5, 3]


def test_preorder_traversal(tree_with_values):
    iterator = tree_with_values.preorder_traversal()
    assert [x.value for x in iterator] == [3, 1, 2, 5, 4, 6]


def test_inorder_traversal_recursive(tree_with_values):
    iterator = tree_with_values.inorder_traversal_recursive()
    assert [x.value for x in iterator] == [1, 2, 3, 4, 5, 6]


def test_postorder_traversal_recursive(tree_with_values):
    iterator = tree_with_values.postorder_traversal_recursive()
    assert [x.value for x in iterator] == [2, 1, 4, 6, 5, 3]


def test_preorder_traversal_recursive(tree_with_values):
    iterator = tree_with_values.preorder_traversal_recursive()
    assert [x.value for x in iterator] == [3, 1, 2, 5, 4, 6]


def test_empty_traversals(tree):
    iterator = tree.preorder_traversal()
    assert [x.value for x in iterator] == []
    iterator = tree.preorder_traversal_recursive()
    assert [x.value for x in iterator] == []

    iterator = tree.postorder_traversal()
    assert [x.value for x in iterator] == []
    iterator = tree.postorder_traversal_recursive()
    assert [x.value for x in iterator] == []

    iterator = tree.inorder_traversal()
    assert [x.value for x in iterator] == []
    iterator = tree.inorder_traversal_recursive()
    assert [x.value for x in iterator] == []
