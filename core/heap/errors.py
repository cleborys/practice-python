class HeapError(Exception):
    """
    Common base class for errors raised by heaps.
    """

    pass


class HeapEmptyError(Exception):
    """
    Raised when trying to pop from an empty heap.
    """

    pass
