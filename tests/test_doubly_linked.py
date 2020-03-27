import pytest

from core.linked_list.error import EmptyListError, ContainerMismatch
from core.linked_list.doubly_linked import DoublyLinkedList


@pytest.fixture
def llist():
    return DoublyLinkedList()


def test_init():
    llist = DoublyLinkedList()

    assert len(llist) == 0


def test_iter_empty(llist):
    assert [x for x in llist] == []


def test_insert_front(llist):
    llist.insert_front(3)
    llist.insert_front(2)
    llist.insert_front(1)

    assert len(llist) == 3
    assert [x.value for x in llist] == [1, 2, 3]


def test_insert_back(llist):
    llist.insert_back(1)
    llist.insert_back(2)
    llist.insert_back(3)

    assert len(llist) == 3
    assert [x.value for x in llist] == [1, 2, 3]


def test_insert_before(llist):
    llist.insert_back(1)
    node = llist.insert_back(2)
    llist.insert_back(3)

    llist.insert_before(node, "new")

    assert len(llist) == 4
    assert [x.value for x in llist] == [1, "new", 2, 3]


def test_insert_after(llist):
    llist.insert_back(1)
    node = llist.insert_back(2)
    llist.insert_back(3)

    llist.insert_after(node, "new")

    assert len(llist) == 4
    assert [x.value for x in llist] == [1, 2, "new", 3]


def test_insert_splice_out(llist):
    llist.insert_back(1)
    node = llist.insert_back(2)
    llist.insert_back(3)

    llist.splice_out(node)

    assert node._previous is None
    assert node._next is None

    assert len(llist) == 2
    assert [x.value for x in llist] == [1, 3]


def test_get_head_tail(llist):
    head = llist.insert_back(1)
    llist.insert_back(2)
    tail = llist.insert_back(3)

    assert llist.get_head() is head
    assert llist.get_tail() is tail


def test_get_head_tail_empty(llist):
    with pytest.raises(EmptyListError):
        llist.get_head()

    with pytest.raises(EmptyListError):
        llist.get_tail()


def test_splice_out_head(llist):
    llist.insert_back(1)
    llist.insert_back(2)
    llist.insert_back(3)

    llist.splice_out(llist.get_head())
    assert len(llist) == 2
    assert [x.value for x in llist] == [2, 3]

    llist.splice_out(llist.get_tail())
    assert len(llist) == 1
    assert [x.value for x in llist] == [2]


def test_container_mismatch():
    list1 = DoublyLinkedList()
    node1 = list1.insert_front(1)

    list2 = DoublyLinkedList()

    with pytest.raises(ContainerMismatch):
        list2.insert_after(node1, "bad")


def test_iter_values(llist):
    llist.insert_back(1)
    llist.insert_back(2)
    llist.insert_back(3)

    values = list(llist.iter_values())
    assert values == [1, 2, 3]
    assert [v for v in llist.iter_values()] == [1, 2, 3]
