import pytest

from core.queue import Queue, EmptyQueueError


@pytest.fixture
def queue():
    return Queue()


def test_init():
    queue = Queue()

    assert len(queue) == 0


def test_dequeue_empty(queue):
    with pytest.raises(EmptyQueueError):
        queue.dequeue()


def test_peek_empty(queue):
    with pytest.raises(EmptyQueueError):
        queue.peek()


def test_queue(queue):
    queue.enqueue(1)
    queue.enqueue(2)

    assert queue.peek() == 1
    assert queue.dequeue() == 1

    queue.enqueue(3)
    queue.enqueue(4)

    assert queue.dequeue() == 2
    assert queue.dequeue() == 3
    assert queue.dequeue() == 4
    assert len(queue) == 0


def test_queue_len(queue):
    queue.enqueue(1)
    assert len(queue) == 1
    queue.enqueue(2)
    assert len(queue) == 2
    queue.peek()
    assert len(queue) == 2
    queue.dequeue()
    assert len(queue) == 1
    queue.enqueue(3)
    assert len(queue) == 2
    queue.enqueue(4)
    assert len(queue) == 3
    queue.dequeue()
    assert len(queue) == 2
    queue.dequeue()
    assert len(queue) == 1
    queue.dequeue()
    assert len(queue) == 0
