class LinkedListError(Exception):
    pass


class EmptyListError(LinkedListError):
    pass


class ContainerMismatch(LinkedListError):
    pass
