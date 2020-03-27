from core.union_find import UnionFind, DuplicateItemError, NotFoundError


import pytest


def test_init():
    partitions = UnionFind()
    assert len(partitions) == 0


def test_add():
    partitions = UnionFind()
    partitions.add_new(1)
    partitions.add_new(2)
    partitions.add_new("banana")

    assert partitions.same_partition(1, 2) is False


def test_add_duplicate():
    partitions = UnionFind()
    partitions.add_new(1)

    with pytest.raises(DuplicateItemError):
        partitions.add_new(1)


def test_union():
    partitions = UnionFind()
    partitions.add_new(1)
    partitions.add_new(2)
    assert partitions.same_partition(1, 2) is False

    partitions.union(1, 2)
    assert partitions.same_partition(1, 2) is True

    partitions.union(1, 2)
    assert partitions.same_partition(1, 2) is True


def test_union_missing():
    partitions = UnionFind()
    partitions.union(1, 2)

    assert partitions.same_partition(1, 2) is True


def test_comparison_missing():
    partitions = UnionFind()
    with pytest.raises(NotFoundError):
        partitions.same_partition(1, 2)
