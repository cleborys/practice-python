from typing import Any, List

ValueType = Any


class QuickSelectError(Exception):
    pass


class OutOfBoundsError(QuickSelectError):
    pass


class Quickselect:
    @classmethod
    def select(cls, array: List[ValueType], k: int) -> ValueType:
        """
        Returns the k-th order statistic.
        Mutates the array in-place.
        """
        if not (0 <= k < len(array)):
            raise OutOfBoundsError
        return cls._select(array, k, 0, len(array))

    @classmethod
    def _select(cls, array: List[ValueType], k: int, start: int, end: int) -> ValueType:
        pivot = cls._choose_pivot(array, start, end)
        left, middle, right = cls._partition(array, start, end, pivot)

        # array[start:left] is less than pivot
        # it contains left - start elements
        # array[left:middle] is equal to pivot
        # it contains middle - left elements
        # array[middle:end] is more than pivot
        # it contains end - middle elements
        if k < left:
            return cls._select(array, k, start, left)
        elif k < middle:
            return pivot

        return cls._select(array, k, middle, end)

    @staticmethod
    def _choose_pivot(array, start, end):
        return array[start]

    @staticmethod
    def _partition(array, start, end, pivot):
        left = start
        middle = start
        right = end

        # next low insertion at start
        # next pivot insertion at middle
        # next high insertion at right-1
        # next element to consider is at middle
        while middle < right:
            if array[middle] < pivot:
                array[left], array[middle] = array[middle], array[left]
                left += 1
                middle += 1
            elif array[middle] == pivot:
                middle += 1
            else:
                right -= 1
                array[middle], array[right] = array[right], array[middle]

        return left, middle, right
