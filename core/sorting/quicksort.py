import random

from typing import Any, List


class Quicksort:
    @classmethod
    def run(cls, array: List[Any]):
        cls._sort(array, 0, len(array))

    @classmethod
    def _sort(cls, array: List[Any], start: int, end: int):
        if end - start < 10:
            cls._insertion_sort(array, start, end)
            return

        pivot = cls._choose_pivot(array, start, end)

        # array[start:left] before pivot
        # array[left:mid] equal to pivot
        # array[right:end] after pivot
        left = start
        mid = start
        right = end

        while mid < right:
            if array[mid] < pivot:
                array[mid], array[left] = array[left], array[mid]
                left += 1
                mid += 1
            elif array[mid] > pivot:
                array[mid], array[right - 1] = array[right - 1], array[mid]
                right -= 1
            else:
                mid += 1

        if left - start < end - right:
            cls._sort(array, start, left)
            cls._sort(array, right, end)
        else:
            cls._sort(array, right, end)
            cls._sort(array, start, left)

    @staticmethod
    def _insertion_sort(array: List[Any], start: int, end: int):
        for current in range(start, end):
            runner = current
            while start < runner:
                swap = runner - 1
                if array[runner] < array[swap]:
                    array[runner], array[swap] = array[swap], array[runner]
                    runner = swap
                else:
                    break

    @classmethod
    def _choose_pivot(cls, array, start, end):
        a = random.randint(start, end - 1)
        b = random.randint(start, end - 1)
        c = random.randint(start, end - 1)
        candidates = [array[a], array[b], array[c]]
        cls._insertion_sort(candidates, 0, 3)
        return candidates[1]
