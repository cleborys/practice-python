import pytest

from core.tree.arraytree import (
    ArrayTree,
    DoesNotExistError,
    NoParentError,
    ContainerMismatchError,
    InvalidItemError,
)


@pytest.fixture
def tree():
    return ArrayTree()


def test_init(tree):
    tree = ArrayTree()

    assert len(tree) == 0


def test_root(tree):
    root = tree.set_root("root")

    assert root.value == "root"
    assert root is tree.get_root()


def test_get_root_empty(tree):
    assert tree.get_root() is None


def test_reset_root(tree):
    root = tree.set_root("old_value")
    tree.set_root("new_value")

    assert root.value == "new_value"


def test_children(tree):
    root = tree.set_root("root")
    r = tree.set_right(root, "r")
    rl = tree.set_left(r, "rl")

    assert rl.value == "rl"
    assert tree.get_left(tree.get_right(root)) is rl


def test_reassign_child(tree):
    root = tree.set_root("root")
    r = tree.set_right(root, "old_value")
    tree.set_right(root, "new_value")

    assert r.value == "new_value"


def test_nonexistent_children(tree):
    root = tree.set_root("root")

    assert tree.get_right(root) is None
    assert tree.get_left(root) is None


def test_nonexistent_internal_children(tree):
    root = tree.set_root("root")
    r = tree.set_right(root, "r")
    l = tree.set_left(root, "l")
    rr = tree.set_right(r, "rr")

    assert tree.get_right(l) is None
    assert tree.get_left(l) is None


def test_parent(tree):
    root = tree.set_root("root")
    r = tree.set_right(root, "r")
    rl = tree.set_left(r, "rl")
    rlr = tree.set_right(rl, "rlr")

    assert tree.get_parent(rlr) is rl
    assert tree.get_parent(rl) is r
    assert tree.get_parent(r) is root


def test_swap_parent(tree):
    root = tree.set_root("root")
    r = tree.set_right(root, "r")

    tree.swap_with_parent(r)

    assert tree.get_root() is r
    assert tree.get_right(r) is root


def test_swap_right(tree):
    root = tree.set_root("root")
    r = tree.set_right(root, "r")

    tree.swap_with_right(root)

    assert tree.get_root() is r
    assert tree.get_right(r) is root


def test_swap_left(tree):
    root = tree.set_root("root")
    l = tree.set_left(root, "l")

    tree.swap_with_left(root)

    assert tree.get_root() is l
    assert tree.get_left(l) is root


def test_nonexistent_parent(tree):
    root = tree.set_root("root")

    assert tree.get_parent(root) is None


def test_get_last_empty(tree):
    assert tree.get_last() is None


def test_get_last(tree):
    root = tree.set_root("root")
    l = tree.set_left(root, "l")

    assert tree.get_last() is l


def test_add_last_empty(tree):
    new = tree.add_last("new")

    assert tree.get_root() is new
    assert tree.get_root().value == "new"


def test_add_last(tree):
    root = tree.add_last("root")
    l = tree.add_last("l")
    r = tree.add_last("r")
    ll = tree.add_last("ll")
    lr = tree.add_last("lr")
    rl = tree.add_last("rl")
    rr = tree.add_last("rr")

    assert tree.get_root() is root
    assert tree.get_left(root) is l
    assert tree.get_right(root) is r
    assert tree.get_left(l) is ll
    assert tree.get_right(l) is lr
    assert tree.get_left(r) is rl
    assert tree.get_right(r) is rr
    assert tree.get_left(ll) is None


def test_add_last_invalid(tree):
    root = tree.set_root("root")
    r = tree.set_right(root, "r")

    # add_last would now add a node in position ll,
    # which is invalid, since l does not exist
    with pytest.raises(NoParentError):
        tree.add_last("ll")


def test_add_last_length(tree):
    assert len(tree) == 0
    tree.add_last(1)
    assert len(tree) == 1
    tree.add_last(1)
    assert len(tree) == 2
    tree.add_last(1)
    assert len(tree) == 3
    tree.delete_last()
    assert len(tree) == 2
    tree.add_last(1)
    assert len(tree) == 3
    tree.delete_last()
    assert len(tree) == 2
    tree.delete_last()
    assert len(tree) == 1
    tree.delete_last()
    assert len(tree) == 0


def test_delete_last_invalidates(tree):
    root = tree.set_root("root")
    tree.delete_last()

    assert root.is_valid is False


def test_delete_last_empty(tree):
    with pytest.raises(DoesNotExistError):
        tree.delete_last()


def test_delete_last_simple(tree):
    root = tree.set_root("root")
    l = tree.set_left(root, "l")
    r = tree.set_right(root, "r")

    assert len(tree) == 3
    assert tree.delete_last() is r
    assert r.is_valid is False
    assert tree.get_right(root) is None

    assert tree.delete_last() is l
    assert tree.delete_last() is root


def test_delete_last(tree):
    root = tree.set_root("root")
    l = tree.set_left(root, "l")
    ll = tree.set_left(l, "ll")
    r = tree.set_right(root, "r")
    rl = tree.set_left(r, "rl")
    rr = tree.set_right(r, "rr")
    rrl = tree.set_left(rr, "rrl")

    assert len(tree) == 7
    assert tree.delete_last() is rrl
    assert len(tree) == 6
    assert rrl.is_valid is False
    assert tree.get_left(rr) is None

    assert tree.delete_last() is rr
    assert tree.delete_last() is rl
    assert tree.delete_last() is ll
    assert tree.delete_last() is r
    assert tree.delete_last() is l
    assert tree.delete_last() is root

    assert len(tree) == 0


def test_invalid_item_access(tree):
    root = tree.set_root("root")
    r = tree.set_right(root, "r")
    tree.delete_last()

    with pytest.raises(InvalidItemError):
        tree.get_parent(r)


def test_container_mismatch():
    tree = ArrayTree()
    tree_root = tree.set_root("tree")

    other = ArrayTree()
    other_root = other.set_root("other")

    with pytest.raises(ContainerMismatchError):
        tree.set_right(other_root, "bad")
