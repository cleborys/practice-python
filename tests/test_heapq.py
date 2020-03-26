import pytest
from core.heap.errors import HeapEmptyError
from core.heap.heapq import HeapQHeap
from core.heap.arrayheap import ArrayHeap


@pytest.fixture
def heap():
    return HeapQHeap()


@pytest.mark.parametrize("heap", [HeapQHeap(), ArrayHeap()])
def test_push(heap):
    heap.push(1)
    heap.push(2)
    heap.push(3)


@pytest.mark.parametrize("heap", [HeapQHeap(), ArrayHeap()])
def test_pop(heap):
    heap.push(8)
    heap.push(0)
    heap.push(2)
    assert heap.pop() == 0
    assert heap.pop() == 2
    assert heap.pop() == 8


@pytest.mark.parametrize("heap", [HeapQHeap(), ArrayHeap()])
def test_len(heap):
    heap = HeapQHeap()
    assert len(heap) == 0
    heap.push(1)
    assert len(heap) == 1
    heap.push(2)
    assert len(heap) == 2
    heap.push(3)
    assert len(heap) == 3
    heap.pop()
    assert len(heap) == 2
    heap.pop()
    assert len(heap) == 1
    heap.pop()
    assert len(heap) == 0


@pytest.mark.parametrize("heap", [HeapQHeap(), ArrayHeap()])
def test_heap_sort(heap):
    input_list = [3, 5, 2, 5, 2, 4, 6, 6, 3, 2, 4, 6, 3]
    for x in input_list:
        heap.push(x)

    output_list = []
    for _ in range(13):
        output_list.append(heap.pop())

    assert output_list == sorted(input_list)


@pytest.mark.parametrize("heap", [HeapQHeap(), ArrayHeap()])
def test_pop_from_empty(heap):
    with pytest.raises(HeapEmptyError):
        heap.pop()
