import pytest

from core.stack import Stack, EmptyStackError


@pytest.fixture
def stack():
    return Stack()


def test_init():
    stack = Stack()

    assert len(stack) == 0


def test_pop_empty(stack):
    with pytest.raises(EmptyStackError):
        stack.pop()


def test_peek_empty(stack):
    with pytest.raises(EmptyStackError):
        stack.peek()


def test_stack(stack):
    stack.push(1)
    stack.push(2)
    stack.push(3)

    assert stack.peek() == 3
    assert stack.pop() == 3

    stack.push(4)
    stack.push(5)

    assert stack.pop() == 5
    assert stack.peek() == 4
    assert stack.pop() == 4
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert len(stack) == 0


def test_len(stack):
    assert len(stack) == 0

    stack.push(1)
    assert len(stack) == 1
    stack.push(2)
    assert len(stack) == 2

    stack.pop()
    assert len(stack) == 1
    stack.push(2)
    assert len(stack) == 2

    stack.pop()
    assert len(stack) == 1
    stack.pop()
    assert len(stack) == 0
