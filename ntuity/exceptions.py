"""Ntuity exceptions."""

class NtuityError(Exception):
    """Base class for Ntuity errors."""
    
    def __init__(self, status: str) -> None:
        """Initialize."""
        super().__init__(status)
        self.status = status

class ApiError(NtuityError):
    """Raised when the API returns an error."""

class InvalidApiTokenError(NtuityError):
    """Raised when the API token is invalid."""
