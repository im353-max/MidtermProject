class OperationError(Exception):
    """Raised when an invalid operation is performed."""
    pass


class ValidationError(Exception):
    """Raised when invalid input is provided."""
    pass