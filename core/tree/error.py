class TreeError(Exception):
    pass


class InvalidNodeError(TreeError):
    pass


class ContainerMismatchError(TreeError):
    pass


class CannotDeleteError(TreeError):
    """
    Raised when attempting to delete a node with children.
    """

    pass
