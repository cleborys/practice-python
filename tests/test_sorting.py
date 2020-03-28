from core.sorting.quicksort import Quicksort

import random


def test_quicksort():
    random.seed("test quicksort")
    array = [random.randint(0, 100) for _ in range(100)]

    Quicksort.run(array)

    assert array == sorted(array)
