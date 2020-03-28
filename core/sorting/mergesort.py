from typing import Any, List

ValueType = Any


class Mergesort:
    @classmethod
    def run(cls, array: List[ValueType]) -> List[ValueType]:
        return cls._sort(array, 0, len(array))

    @classmethod
    def _sort(cls, array: List[ValueType], start: int, end: int) -> List[ValueType]:
        if end == start:
            return []
        if end == start + 1:
            return array[start:end]

        middle = start + (end - start) // 2

        left_part = cls._sort(array, start, middle)
        right_part = cls._sort(array, middle, end)

        return cls._merge(left_part, right_part)

    @staticmethod
    def _merge(left: List[ValueType], right: List[ValueType]) -> List[ValueType]:
        buffer_list = []
        left_index = 0
        right_index = 0

        while left_index < len(left) and right_index < len(right):
            if right[right_index] < left[left_index]:
                buffer_list.append(right[right_index])
                right_index += 1
                continue

            buffer_list.append(left[left_index])
            left_index += 1

        buffer_list.extend(left[i] for i in range(left_index, len(left)))
        buffer_list.extend(right[i] for i in range(right_index, len(right)))

        return buffer_list
