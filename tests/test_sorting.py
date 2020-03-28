import pytest

from core.sorting.quicksort import Quicksort
from core.sorting.quickselect import Quickselect, OutOfBoundsError
from core.sorting.mergesort import Mergesort

import random


def test_quicksort():
    random.seed("test quicksort")
    for _ in range(10):
        array = [random.randint(0, 100) for _ in range(100)]

        Quicksort.run(array)

        assert array == sorted(array)


def test_quicksort_empty():
    array = []
    Quicksort.run(array)

    assert array == []


def test_mergesort():
    random.seed("test mergesort")
    for _ in range(10):
        array = [random.randint(0, 100) for _ in range(100)]

        result = Mergesort.run(array)

        assert result == sorted(array)


def test_mergesort_empty():
    array = []
    result = Mergesort.run(array)

    assert result == []


def test_quickselect():
    random.seed("test quickselect")
    for _ in range(10):
        array = [random.randint(0, 100) for _ in range(100)]
        k = random.randint(0, 99)

        result = Quickselect.select(array, k)

        assert result == sorted(array)[k]


def test_quickselect_empty():
    array = []
    with pytest.raises(OutOfBoundsError):
        Quickselect.select(array, 0)
    with pytest.raises(OutOfBoundsError):
        Quickselect.select(array, 1)

    array = [1, 2, 3]
    with pytest.raises(OutOfBoundsError):
        Quickselect.select(array, -1)
    with pytest.raises(OutOfBoundsError):
        Quickselect.select(array, 3)
