import pytest

from core.stack import Stack, ArrayStack, DequeStack, EmptyStackError


@pytest.mark.parametrize("cls", [Stack, ArrayStack, DequeStack])
def test_init(cls):
    stack = cls()

    assert len(stack) == 0


@pytest.mark.parametrize("stack", [Stack(), ArrayStack(), DequeStack()])
def test_pop_empty(stack):
    with pytest.raises(EmptyStackError):
        stack.pop()


@pytest.mark.parametrize("stack", [Stack(), ArrayStack(), DequeStack()])
def test_peek_empty(stack):
    with pytest.raises(EmptyStackError):
        stack.peek()


@pytest.mark.parametrize("stack", [Stack(), ArrayStack(), DequeStack()])
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


@pytest.mark.parametrize("stack", [Stack(), ArrayStack(), DequeStack()])
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
