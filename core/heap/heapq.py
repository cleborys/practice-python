import heapq
from .errors import HeapEmptyError


class HeapQHeap:
    def __init__(self):
        self._back = []
        self._length = 0

    def __len__(self):
        return self._length

    def push(self, x):
        heapq.heappush(self._back, x)
        self._length += 1

    def pop(self):
        if len(self) == 0:
            raise HeapEmptyError

        result = heapq.heappop(self._back)
        self._length -= 1
        return result
