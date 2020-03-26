import pytest

from core.linked_list.singly_linked import SinglyLinkedList, EmptyListError


def test_init():
    llist = SinglyLinkedList()

    assert len(llist) == 0


def test_append():
    llist = SinglyLinkedList()

    llist.append(1)
    assert len(llist) == 1

    llist.append(2)
    assert len(llist) == 2

    assert llist.get_tail().value == 2
    assert llist.get_head().value == 1


def test_head_empty():
    llist = SinglyLinkedList()
    with pytest.raises(EmptyListError):
        llist.get_head()


def test_tail_empty():
    llist = SinglyLinkedList()
    with pytest.raises(EmptyListError):
        llist.get_tail()


def test_iter_empty():
    llist = SinglyLinkedList()

    values = [x for x in llist]

    assert values == []


def test_iter():
    llist = SinglyLinkedList()
    llist.append(1)
    llist.append(2)
    llist.append(3)

    values = [x.value for x in llist]

    assert values == [1, 2, 3]


def test_append_front():
    llist = SinglyLinkedList()
    llist.append("middle")
    llist.append("back")
    llist.append_front("front")

    values = [x.value for x in llist]

    assert values == ["front", "middle", "back"]


def test_append_front_len():
    llist = SinglyLinkedList()
    llist.append_front(1)
    llist.append_front(2)

    assert len(llist) == 2


def test_delete_front_empty():
    llist = SinglyLinkedList()
    with pytest.raises(EmptyListError):
        llist.delete_front()


def test_delete_front():
    llist = SinglyLinkedList()
    llist.append(1)
    llist.append(2)
    llist.append(3)

    deleted = llist.delete_front()
    assert deleted.value == 1
    assert len(llist) == 2
    assert [x.value for x in llist] == [2, 3]

    deleted = llist.delete_front()
    assert deleted.value == 2
    assert len(llist) == 1
    assert [x.value for x in llist] == [3]
